#!/usr/bin/env python3
"""Build and refresh the UNICAGD programming systems catalog.

The script is intentionally stdlib-only. It reads the master JSON seed, expands
it with registry-derived records where possible, enriches release metadata, and
renders a linked Markdown corpus for browsing in a repository.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import gzip
import hashlib
import html
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import textwrap
import threading
import time
import tomllib
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.robotparser import RobotFileParser


ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "data" / "source" / "UNICAGD_programming_catalog_MASTER_FULL.json"
LOCAL_EXTENSION = ROOT / "data" / "extensions" / "additional_languages.json"
ORIGINAL_SOURCE = Path("/Users/peter/Intercom •refract/UNICAGD_programming_catalog_MASTER_FULL.json")
CATALOG_DIR = ROOT / "catalog"
ENRICHED_JSON = CATALOG_DIR / "enriched_records.json"
REPORT_MD = CATALOG_DIR / "enrichment_report.md"
LICENSE_INDEX_MD = CATALOG_DIR / "license-index.md"
HTTP_CACHE_DIR = ROOT / ".cache" / "catalog_http"

USER_AGENT = "catarepo-programming-catalog/1.0 (+https://github.com/DRG-INT/UNICAGD-programming-systems-catalog)"
CRAWLER_USER_AGENT = "catarepo-programming-catalog"
ROBOTS_CACHE_DIR = ROOT / ".cache" / "catalog_robots"
DEFAULT_TIMEOUT = 12
DEFAULT_TARGET_RECORDS = 24000
DEFAULT_WORKERS = 12
LICENSE_VALUES_CACHE: dict[int, list[str]] = {}

TAXONOMY = [
    "language_specification",
    "standard_library",
    "compiler",
    "interpreter_runtime",
    "jit_vm",
    "build_system",
    "package_manager",
    "dependency_manager",
    "project_scaffolding",
    "linter",
    "lint_plugin",
    "lint_rule_pack",
    "static_analyzer",
    "type_checker",
    "formatter",
    "security_sast",
    "sanitizer",
    "undefined_behavior_analyzer",
    "memory_analyzer",
    "compiler_diagnostics",
    "language_server",
    "ide_editor_integration",
    "debugger",
    "profiler",
    "benchmarking",
    "testing_framework",
    "assertion_mocking",
    "coverage",
    "fuzzer",
    "documentation",
    "api_doc_generator",
    "parser_lexer_ast",
    "serialization",
    "ffi_bindings",
    "concurrency_parallelism",
    "async_runtime",
    "networking_http",
    "web_framework",
    "cli",
    "database_datastore",
    "message_broker",
    "logging_observability",
    "configuration",
    "cryptography",
    "compression",
    "filesystem_os",
    "datetime",
    "math_numeric_scientific",
    "data_science",
    "machine_learning",
    "visualization_gui",
    "game_engine_game_dev",
    "embedded_hardware",
    "image_audio_dsp",
    "templating",
    "codegen_codemod_refactoring",
    "dead_code_dependency_analysis",
    "api_abi_checker",
    "precommit_ci_quality",
    "container_deployment",
    "interop_bindings",
    "utility_library",
    "framework",
    "library",
    "community_reference",
    "tutorial_book_styleguide",
    "registry_repository",
    "other",
]

BRANCH_ALIASES = {
    "c": "C99",
    "c99": "C99",
    "c23": "C23",
    "c_cpp": "C++23",
    "c++": "C++23",
    "c++23": "C++23",
    "cpp": "C++23",
    "julia": "Julia",
    "rust": "Rust",
    "python": "Python",
    "javascript": "Node.js/JavaScript",
    "node.js/javascript": "Node.js/JavaScript",
    "node/javascript": "Node.js/JavaScript",
    "js": "Node.js/JavaScript",
    "javascript_typescript": "Node.js/TypeScript",
    "typescript_javascript": "Node.js/TypeScript",
    "typescript": "Node.js/TypeScript",
    "node.js/typescript": "Node.js/TypeScript",
    "node/typescript": "Node.js/TypeScript",
    "ts": "Node.js/TypeScript",
    "lua family": "Lua family",
    "lua_family": "Lua family",
    "lua": "Lua family",
    "r": "R",
    "haskell": "Haskell",
    "ghc": "Haskell",
    "matlab": "Matlab",
    "octave": "Octave",
    "gnu octave": "Octave",
    "c-sharp": "C-Sharp",
    "c_sharp": "C-Sharp",
    "csharp": "C-Sharp",
    "c#": "C-Sharp",
    "cs": "C-Sharp",
    "bc": "bc",
    "gnu bc": "bc",
    "dart": "Dart",
    "go": "Go",
    "golang": "Go",
    "starlark": "Starlark",
    "skylark": "Starlark",
    "bzl": "Starlark",
    "basilisk": "Basilisk",
    "basilisk c": "Basilisk",
    "basilisk_c": "Basilisk",
    "ai": "\"aim's\"",
    "a.i.": "\"aim's\"",
    "artificial intelligence": "\"aim's\"",
    "artificial_intelligence": "\"aim's\"",
    "aim": "\"aim's\"",
    "aims": "\"aim's\"",
    "aim's": "\"aim's\"",
    "\"aim's\"": "\"aim's\"",
    "llm": "\"aim's\"",
    "llms": "\"aim's\"",
    "machine intelligence": "\"aim's\"",
    "machine_intelligence": "\"aim's\"",
    "nix": "nix",
    "nix language": "nix",
    "nix_language": "nix",
    "nixos": "nix",
    "nixpkgs": "nix",
    "doctrine": "Doctrines",
    "doctrines": "Doctrines",
    "engineering doctrine": "Doctrines",
    "engineering_doctrine": "Doctrines",
    "architecture doctrine": "Doctrines",
    "architecture_doctrine": "Doctrines",
    "api": "APIs",
    "apis": "APIs",
    "openapi": "APIs",
    "rapidapi": "APIs",
    "asyncapi": "APIs",
    "graphql": "APIs",
    "grpc": "APIs",
    "transmission protocols": "Transmission Protocols",
    "transmission_protocols": "Transmission Protocols",
    "protocols": "Transmission Protocols",
    "network protocols": "Transmission Protocols",
    "network_protocols": "Transmission Protocols",
    "transport protocols": "Transmission Protocols",
    "transport_protocols": "Transmission Protocols",
    "renderer": "Renderers",
    "renderers": "Renderers",
    "rendering": "Renderers",
    "rendering engines": "Renderers",
    "rendering_engines": "Renderers",
    "graphics renderers": "Renderers",
    "graphics_renderers": "Renderers",
    "computer graphics": "Computer Graphics Software",
    "computer_graphics": "Computer Graphics Software",
    "computer graphics software": "Computer Graphics Software",
    "computer_graphics_software": "Computer Graphics Software",
    "graphics software": "Computer Graphics Software",
    "graphics_software": "Computer Graphics Software",
    "engines": "Engines",
    "engine": "Engines",
    "software engines": "Engines",
    "software_engines": "Engines",
    "physics engine": "Physics Engines",
    "physics engines": "Physics Engines",
    "physics_engine": "Physics Engines",
    "physics_engines": "Physics Engines",
    "game engine": "Game Engines",
    "game engines": "Game Engines",
    "game_engine": "Game Engines",
    "game_engines": "Game Engines",
    "icons": "Icons and Logos",
    "logos": "Icons and Logos",
    "icons and logos": "Icons and Logos",
    "icons_and_logos": "Icons and Logos",
    "icon libraries": "Icons and Logos",
    "icon_libraries": "Icons and Logos",
    "brand assets": "Icons and Logos",
    "brand_assets": "Icons and Logos",
    "font briefcase": "Font Briefcase",
    "font_briefcase": "Font Briefcase",
    "font suitcase": "Font Briefcase",
    "font_suitcase": "Font Briefcase",
    "font book": "Font Briefcase",
    "font_book": "Font Briefcase",
    "font manager": "Font Briefcase",
    "font_manager": "Font Briefcase",
    "asset": "Assets",
    "assets": "Assets",
    "asset pipeline": "Assets",
    "asset_pipeline": "Assets",
    "digital assets": "Assets",
    "digital_assets": "Assets",
    "media assets": "Assets",
    "media_assets": "Assets",
    "map": "Maps",
    "maps": "Maps",
    "mapping": "Maps",
    "geospatial": "Maps",
    "gis": "Maps",
    "space engine": "Space Engines",
    "space engines": "Space Engines",
    "space_engine": "Space Engines",
    "space_engines": "Space Engines",
    "rocket engine": "Space Engines",
    "rocket engines": "Space Engines",
    "rocket_engine": "Space Engines",
    "space shuttle": "Space Shuttles",
    "space shuttles": "Space Shuttles",
    "space_shuttle": "Space Shuttles",
    "space_shuttles": "Space Shuttles",
    "orbiter": "Space Shuttles",
    "space map": "Space Maps",
    "space maps": "Space Maps",
    "space_map": "Space Maps",
    "space_maps": "Space Maps",
    "astronomy maps": "Space Maps",
    "astronomy_maps": "Space Maps",
    "effect": "Effects",
    "effects": "Effects",
    "vfx": "Effects",
    "visual effects": "Effects",
    "visual_effects": "Effects",
    "audio effects": "Effects",
    "audio_effects": "Effects",
    "shader effects": "Effects",
    "shader_effects": "Effects",
    "audio": "Audio",
    "sound": "Audio",
    "audio software": "Audio",
    "audio_software": "Audio",
    "dsp audio": "Audio",
    "dsp_audio": "Audio",
    "video": "Video",
    "video software": "Video",
    "video_software": "Video",
    "streaming video": "Video",
    "streaming_video": "Video",
    "photography": "Photography",
    "photo": "Photography",
    "photos": "Photography",
    "camera": "Photography",
    "cameras": "Photography",
    "raw photo": "Photography",
    "raw_photo": "Photography",
    "microscopy": "Microscopy",
    "microscope": "Microscopy",
    "microscopes": "Microscopy",
    "bioimaging": "Microscopy",
    "bio imaging": "Microscopy",
    "telescope": "Telescopes",
    "telescopes": "Telescopes",
    "astronomical telescope": "Telescopes",
    "astronomical telescopes": "Telescopes",
    "observatory": "Telescopes",
    "observatories": "Telescopes",
    "radar": "Radars",
    "radars": "Radars",
    "sar": "Radars",
    "synthetic aperture radar": "Radars",
    "synthetic_aperture_radar": "Radars",
    "satcom": "SatCom Satellites",
    "satcom satellites": "SatCom Satellites",
    "satcom_satellites": "SatCom Satellites",
    "satellite communications": "SatCom Satellites",
    "satellite_communications": "SatCom Satellites",
    "communications satellites": "SatCom Satellites",
    "communications_satellites": "SatCom Satellites",
    "ncis satcom satellites": "SatCom Satellites",
    "ncis_satcom_satellites": "SatCom Satellites",
    "electromagnetoscope": "Electromagnetoscopes",
    "electromagnetoscopes": "Electromagnetoscopes",
    "electromagnetic scopes": "Electromagnetoscopes",
    "electromagnetic_scopes": "Electromagnetoscopes",
    "em scopes": "Electromagnetoscopes",
    "em_scopes": "Electromagnetoscopes",
    "electromagnetic sensing": "Electromagnetoscopes",
    "electromagnetic_sensing": "Electromagnetoscopes",
    "radiogarden": "Radio Garden Speciality",
    "radio garden": "Radio Garden Speciality",
    "radio_garden": "Radio Garden Speciality",
    "radio.garden": "Radio Garden Speciality",
    "radio garden speciality": "Radio Garden Speciality",
    "radio_garden_speciality": "Radio Garden Speciality",
    "internet radio garden": "Radio Garden Speciality",
    "internet_radio_garden": "Radio Garden Speciality",
    "repertoare catalogs": "Repertoare Catalogs",
    "repertoare_catalogs": "Repertoare Catalogs",
    "repertuare catalogs": "Repertoare Catalogs",
    "repertuare_catalogs": "Repertoare Catalogs",
    "repertoire catalogs": "Repertoare Catalogs",
    "repertoire_catalogs": "Repertoare Catalogs",
    "repertory catalogs": "Repertoare Catalogs",
    "repertory_catalogs": "Repertoare Catalogs",
    "catalog": "Catalogs",
    "catalogs": "Catalogs",
    "registry catalogs": "Catalogs",
    "registry_catalogs": "Catalogs",
    "index catalogs": "Catalogs",
    "index_catalogs": "Catalogs",
    "magazine": "Magazines",
    "magazines": "Magazines",
    "periodical": "Magazines",
    "periodicals": "Magazines",
    "journal": "Magazines",
    "journals": "Magazines",
    "zine": "Magazines",
    "zines": "Magazines",
    "hub": "Hubs",
    "hubs": "Hubs",
    "software hub": "Hubs",
    "software_hub": "Hubs",
    "developer hub": "Hubs",
    "developer_hub": "Hubs",
    "package hub": "Hubs",
    "package_hub": "Hubs",
    "model hub": "Hubs",
    "model_hub": "Hubs",
    "data hub": "Hubs",
    "data_hub": "Hubs",
    "brace": "Braces",
    "braces": "Braces",
    "curly braces": "Braces",
    "curly_braces": "Braces",
    "brace syntax": "Braces",
    "brace_syntax": "Braces",
    "bracket matching": "Braces",
    "bracket_matching": "Braces",
    "assembly": "Assembly",
    "asm": "Assembly",
    "assembler": "Assembly",
    "pattern language": "Pattern language",
    "pattern_language": "Pattern language",
    "patterns": "Pattern language",
    "php": "PHP",
    "webassembly": "WebAssembly",
    "wasm": "WebAssembly",
    "sapjava": "SAPJava",
    "sap java": "SAPJava",
    "sap_java": "SAPJava",
    "swift": "Swift",
    "cocoa": "Cocoa",
    "cocoapods": "Cocoa",
    "database": "Databases",
    "databases": "Databases",
    "db": "Databases",
    "storage": "Databases",
    "repository workplaces": "Repository Workplaces",
    "repository_workplaces": "Repository Workplaces",
    "workplaces": "Repository Workplaces",
    "source control": "Repository Workplaces",
    "source_control": "Repository Workplaces",
    "version control": "Repository Workplaces",
    "version_control": "Repository Workplaces",
    "vcs": "Repository Workplaces",
    "gitlab": "Repository Workplaces",
    "gitea": "Repository Workplaces",
    "gittea": "Repository Workplaces",
    "forgejo": "Repository Workplaces",
    "mercurial": "Repository Workplaces",
    "hg": "Repository Workplaces",
    "subversion": "Repository Workplaces",
    "svn": "Repository Workplaces",
}

LANGUAGE_ORDER = [
    "C99",
    "C23",
    "C++23",
    "Julia",
    "Rust",
    "Python",
    "Node.js/JavaScript",
    "Node.js/TypeScript",
    "Lua family",
    "R",
    "Haskell",
    "Matlab",
    "Octave",
    "C-Sharp",
    "bc",
    "Dart",
    "Go",
    "Starlark",
    "Basilisk",
    "\"aim's\"",
    "nix",
    "Doctrines",
    "APIs",
    "Transmission Protocols",
    "Renderers",
    "Computer Graphics Software",
    "Engines",
    "Physics Engines",
    "Game Engines",
    "Icons and Logos",
    "Font Briefcase",
    "Assets",
    "Maps",
    "Space Engines",
    "Space Shuttles",
    "Space Maps",
    "Effects",
    "Audio",
    "Video",
    "Photography",
    "Microscopy",
    "Telescopes",
    "Radars",
    "SatCom Satellites",
    "Electromagnetoscopes",
    "Radio Garden Speciality",
    "Repertoare Catalogs",
    "Catalogs",
    "Magazines",
    "Hubs",
    "Braces",
    "Assembly",
    "Pattern language",
    "PHP",
    "WebAssembly",
    "SAPJava",
    "Swift",
    "Cocoa",
    "Databases",
    "Repository Workplaces",
]

CATEGORY_KEYWORDS = {
    "language_specification": [
        "specification",
        "standard",
        "proposal",
        "working draft",
        "language",
    ],
    "standard_library": ["stdlib", "standard library", "core library"],
    "compiler": ["compiler", "gcc", "clang", "llvm", "transpile"],
    "interpreter_runtime": ["runtime", "interpreter", "vm", "virtual machine"],
    "jit_vm": ["jit", "just-in-time"],
    "build_system": ["build", "make", "cmake", "bazel", "meson", "ninja", "rake"],
    "package_manager": [
        "package manager",
        "registry",
        "installer",
        "npm",
        "pip",
        "cargo",
        "luarocks",
        "pkg",
    ],
    "dependency_manager": ["dependency", "lockfile", "dependencies"],
    "project_scaffolding": ["scaffold", "template", "starter", "boilerplate"],
    "linter": ["lint", "linter"],
    "lint_plugin": ["lint plugin", "eslint plugin", "ruff plugin"],
    "lint_rule_pack": ["rules", "rule pack", "style rules"],
    "static_analyzer": ["static analysis", "analyzer", "analysis", "scan"],
    "type_checker": ["type check", "typing", "typescript", "mypy", "pyright"],
    "formatter": ["format", "formatter", "prettier", "black", "rustfmt"],
    "security_sast": ["sast", "security", "vulnerability", "audit"],
    "sanitizer": ["sanitizer", "asan", "tsan", "ubsan"],
    "undefined_behavior_analyzer": ["undefined behavior", "ub"],
    "memory_analyzer": ["memory", "leak", "valgrind", "heap"],
    "compiler_diagnostics": ["diagnostic", "warnings", "warning"],
    "language_server": ["language server", "lsp", "intellisense"],
    "ide_editor_integration": ["editor", "ide", "vscode", "vim", "neovim", "emacs"],
    "debugger": ["debug", "debugger", "breakpoint"],
    "profiler": ["profile", "profiler", "trace", "tracing"],
    "benchmarking": ["benchmark", "performance"],
    "testing_framework": ["test", "testing", "unit test", "pytest", "jest"],
    "assertion_mocking": ["mock", "assert", "fixture"],
    "coverage": ["coverage"],
    "fuzzer": ["fuzz", "fuzzer", "afl"],
    "documentation": ["documentation", "docs", "manual"],
    "api_doc_generator": ["api docs", "doc generator", "doxygen", "sphinx"],
    "parser_lexer_ast": ["parser", "lexer", "ast", "syntax", "grammar"],
    "serialization": ["json", "yaml", "toml", "xml", "protobuf", "msgpack", "serialize"],
    "ffi_bindings": ["ffi", "binding", "bindings", "foreign function"],
    "concurrency_parallelism": [
        "concurrency",
        "parallel",
        "thread",
        "threading",
        "multiprocessing",
    ],
    "async_runtime": ["async", "event loop", "non-blocking", "tokio"],
    "networking_http": ["http", "network", "socket", "websocket", "tcp", "udp", "client"],
    "web_framework": ["web framework", "server", "router", "django", "express", "fastapi"],
    "cli": ["cli", "command-line", "terminal", "shell"],
    "database_datastore": ["database", "datastore", "redis", "sql", "postgres", "sqlite"],
    "message_broker": ["message broker", "queue", "kafka", "rabbitmq", "mqtt"],
    "logging_observability": ["log", "logging", "observability", "metrics", "telemetry"],
    "configuration": ["configuration", "config", "settings", "env"],
    "cryptography": ["crypto", "cryptography", "encrypt", "tls", "ssl", "hash"],
    "compression": ["compress", "gzip", "zip", "zstd", "brotli"],
    "filesystem_os": ["filesystem", "file system", "os", "path", "directory"],
    "datetime": ["date", "time", "datetime", "calendar"],
    "math_numeric_scientific": ["math", "numeric", "scientific", "linear algebra"],
    "data_science": ["dataframe", "data science", "analytics", "pandas"],
    "machine_learning": ["machine learning", "ml", "ai", "neural", "llm"],
    "visualization_gui": ["visualization", "gui", "plot", "chart", "ui"],
    "game_engine_game_dev": ["game", "engine", "love2d", "vr"],
    "embedded_hardware": ["embedded", "hardware", "iot", "microcontroller", "sensor"],
    "image_audio_dsp": ["image", "audio", "dsp", "video", "signal"],
    "templating": ["template", "templating"],
    "codegen_codemod_refactoring": ["codegen", "codemod", "refactor", "rewrite"],
    "dead_code_dependency_analysis": ["dead code", "unused", "dependency analysis"],
    "api_abi_checker": ["api", "abi", "compatibility"],
    "precommit_ci_quality": ["ci", "pre-commit", "precommit", "quality", "automation"],
    "container_deployment": ["container", "docker", "deployment", "kubernetes"],
    "interop_bindings": ["interop", "bridge", "wrapper"],
    "utility_library": ["utility", "helpers", "toolkit", "belt"],
    "framework": ["framework"],
    "community_reference": ["awesome", "community", "reference", "curated list"],
    "tutorial_book_styleguide": ["tutorial", "book", "style guide", "guide"],
    "registry_repository": ["repository", "registry", "index"],
}

NPM_QUERY_TERMS = [
    "cli",
    "http",
    "server",
    "database",
    "testing",
    "typescript",
    "eslint",
    "prettier",
    "build",
    "security",
    "logging",
    "parser",
    "serialization",
    "react",
    "node",
    "webpack",
    "vite",
    "express",
    "graphql",
    "orm",
    "queue",
    "crypto",
]

PYPI_QUERY_TERMS = [
    "cli",
    "http",
    "server",
    "database",
    "testing",
    "lint",
    "format",
    "parser",
    "serialization",
    "async",
    "security",
    "logging",
    "data",
    "machine",
    "django",
    "fastapi",
    "pytest",
    "sphinx",
]

LUAROCKS_QUERY_TERMS = [
    "json",
    "http",
    "lua",
    "resty",
    "kong",
    "test",
    "cli",
    "parser",
    "redis",
    "sql",
    "crypto",
    "neovim",
]

NUGET_QUERY_TERMS = [
    "json",
    "http",
    "aspnetcore",
    "webapi",
    "entityframework",
    "database",
    "testing",
    "xunit",
    "nunit",
    "logging",
    "serilog",
    "roslyn",
    "analyzer",
    "source generator",
    "cli",
    "configuration",
    "dependency injection",
    "security",
    "grpc",
    "serialization",
    "csharp",
    ".net",
]

MATLAB_GITHUB_QUERIES = [
    "language:MATLAB stars:>100",
    "language:MATLAB topic:matlab",
    "language:MATLAB topic:machine-learning",
    "language:MATLAB topic:signal-processing",
    "language:MATLAB topic:image-processing",
    "language:MATLAB topic:control-systems",
]

ASSEMBLY_GITHUB_QUERIES = [
    "language:Assembly stars:>500",
    "topic:assembly stars:>300",
    "topic:x86 topic:assembly",
    "topic:arm topic:assembly",
    "topic:riscv topic:assembly",
    "assembler stars:>300",
]

PATTERN_GITHUB_QUERIES = [
    "design patterns stars:>1000",
    "software architecture patterns stars:>100",
    "enterprise integration patterns stars:>50",
    "microservices patterns stars:>100",
]

DART_QUERY_TERMS = [
    "http",
    "json",
    "flutter",
    "database",
    "sqlite",
    "testing",
    "lint",
    "build",
    "codegen",
    "serialization",
    "cli",
    "logging",
    "ffi",
    "grpc",
    "state",
    "riverpod",
    "bloc",
    "security",
]

GO_MODULE_SEEDS = [
    "github.com/gin-gonic/gin",
    "github.com/gorilla/mux",
    "github.com/labstack/echo/v4",
    "github.com/go-chi/chi/v5",
    "github.com/spf13/cobra",
    "github.com/spf13/viper",
    "github.com/stretchr/testify",
    "go.uber.org/zap",
    "go.uber.org/fx",
    "golang.org/x/tools",
    "golang.org/x/text",
    "golang.org/x/crypto",
    "golang.org/x/vuln",
    "google.golang.org/grpc",
    "google.golang.org/protobuf",
    "gorm.io/gorm",
    "github.com/jackc/pgx/v5",
    "github.com/lib/pq",
    "github.com/redis/go-redis/v9",
    "github.com/segmentio/kafka-go",
]

GO_GITHUB_QUERIES = [
    "language:Go stars:>3000",
    "topic:golang stars:>1000",
    "topic:go-library stars:>100",
    "topic:go-framework stars:>100",
    "topic:go-modules stars:>50",
]

STARLARK_GITHUB_QUERIES = [
    "language:Starlark stars:>500",
    "topic:starlark stars:>100",
    "topic:bazel rules stars:>100",
    "bazel starlark rules stars:>100",
]

BASILISK_GITHUB_QUERIES = [
    "basilisk c simulation",
    "AVSLab basilisk",
    "basilisk astrodynamics",
    "Basilisk language compiler",
]

AIMS_GITHUB_QUERIES = [
    "topic:llm stars:>500",
    "topic:generative-ai stars:>500",
    "topic:ai-agent stars:>100",
    "topic:inference-server stars:>50",
    "topic:rag stars:>100",
    "topic:vector-search stars:>100",
    "topic:machine-learning stars:>1000",
    "topic:model-serving stars:>100",
    "topic:onnx stars:>100",
    "topic:openai stars:>100",
]

NIX_GITHUB_QUERIES = [
    "language:Nix stars:>1000",
    "topic:nix stars:>500",
    "topic:nixos stars:>500",
    "topic:nix-flakes stars:>100",
    "topic:nixpkgs stars:>100",
]

RENDERERS_GITHUB_QUERIES = [
    "topic:renderer stars:>100",
    "topic:rendering-engine stars:>50",
    "topic:graphics stars:>1000",
    "topic:vulkan stars:>500",
    "topic:opengl stars:>500",
    "topic:webgpu stars:>200",
    "topic:raytracing stars:>100",
    "topic:browser-engine stars:>100",
]

BRACES_GITHUB_QUERIES = [
    "brace matching parser",
    "curly brace formatter",
    "bracket pair colorization",
    "syntax highlighter braces",
    "tree-sitter braces",
    "grammar braces parser",
]

COMPUTER_GRAPHICS_SOFTWARE_GITHUB_QUERIES = [
    "topic:computer-graphics stars:>100",
    "topic:graphics stars:>1000",
    "topic:3d-graphics stars:>100",
    "topic:visualization stars:>500",
    "topic:cad stars:>100",
    "topic:modeling stars:>100",
    "topic:animation stars:>100",
    "topic:shader stars:>100",
]

ENGINES_GITHUB_QUERIES = [
    "topic:engine stars:>100",
    "topic:workflow-engine stars:>100",
    "topic:rules-engine stars:>100",
    "topic:query-engine stars:>100",
    "topic:storage-engine stars:>100",
    "topic:rendering-engine stars:>50",
    "topic:simulation-engine stars:>20",
]

PHYSICS_ENGINES_GITHUB_QUERIES = [
    "topic:physics-engine stars:>50",
    "topic:physics-simulation stars:>50",
    "topic:rigid-body-dynamics stars:>20",
    "topic:collision-detection stars:>20",
    "topic:soft-body stars:>10",
    "topic:fluid-simulation stars:>20",
]

GAME_ENGINES_GITHUB_QUERIES = [
    "topic:game-engine stars:>100",
    "topic:game-development stars:>500",
    "topic:ecs stars:>100",
    "topic:2d-game-engine stars:>20",
    "topic:3d-game-engine stars:>20",
    "topic:game-framework stars:>100",
]

ICONS_AND_LOGOS_GITHUB_QUERIES = [
    "topic:icons stars:>500",
    "topic:icon-font stars:>100",
    "topic:svg-icons stars:>100",
    "topic:logo stars:>100",
    "topic:brand-assets stars:>20",
    "topic:favicons stars:>50",
    "topic:emoji stars:>100",
    "topic:design-system stars:>500",
]

ASSETS_GITHUB_QUERIES = [
    "topic:asset-pipeline stars:>50",
    "topic:assets stars:>100",
    "topic:asset-management stars:>50",
    "topic:game-assets stars:>20",
    "topic:3d-assets stars:>20",
    "topic:textures stars:>20",
    "topic:fonts stars:>100",
    "topic:media-processing stars:>100",
]

FONT_BRIEFCASE_GITHUB_QUERIES = [
    "topic:fonts stars:>100",
    "topic:font-manager stars:>10",
    "topic:fonttools stars:>10",
    "topic:typeface stars:>50",
    "topic:fontforge stars:>10",
    "topic:woff2 stars:>10",
]

REPERTOARE_CATALOGS_GITHUB_QUERIES = [
    "repertoire catalog",
    "music repertoire catalog",
    "performance repertoire",
    "score catalog",
    "setlist catalog",
    "collection repertoire",
]

CATALOGS_GITHUB_QUERIES = [
    "topic:catalog stars:>50",
    "topic:registry stars:>100",
    "topic:index stars:>100",
    "topic:metadata-catalog stars:>10",
    "topic:data-catalog stars:>50",
    "topic:package-registry stars:>50",
]

MAGAZINES_GITHUB_QUERIES = [
    "topic:magazine stars:>20",
    "topic:journal stars:>20",
    "topic:zine stars:>10",
    "topic:newsletter stars:>50",
    "developer magazine",
    "programming magazine archive",
]

HUBS_GITHUB_QUERIES = [
    "topic:hub stars:>50",
    "topic:developer-portal stars:>50",
    "topic:marketplace stars:>100",
    "topic:package-registry stars:>50",
    "topic:model-hub stars:>5",
    "topic:datahub stars:>20",
    "topic:artifact-registry stars:>20",
]

MAPS_GITHUB_QUERIES = [
    "topic:gis stars:>100",
    "topic:geospatial stars:>100",
    "topic:maps stars:>100",
    "topic:openstreetmap stars:>100",
    "topic:vector-tiles stars:>50",
    "topic:web-mapping stars:>50",
    "topic:geocoding stars:>50",
    "topic:routing stars:>50",
]

SPACE_ENGINES_GITHUB_QUERIES = [
    "topic:spaceflight stars:>20",
    "topic:rocket-engine stars:>5",
    "topic:rocket-simulation stars:>10",
    "topic:orbital-mechanics stars:>20",
    "topic:astrodynamics stars:>20",
    "topic:propulsion stars:>10",
]

SPACE_SHUTTLES_GITHUB_QUERIES = [
    "space shuttle simulation",
    "orbiter space flight simulator",
    "shuttle guidance navigation control",
    "NASA space shuttle data",
    "space shuttle telemetry",
]

SPACE_MAPS_GITHUB_QUERIES = [
    "topic:astronomy stars:>100",
    "topic:planetary-science stars:>20",
    "topic:sky-map stars:>10",
    "topic:star-map stars:>10",
    "topic:spice stars:>10",
    "topic:celestial-mechanics stars:>10",
    "astronomy sky map",
    "planetary maps",
    "space visualization",
    "SPICE kernels",
    "star catalog",
]

EFFECTS_GITHUB_QUERIES = [
    "topic:vfx stars:>50",
    "topic:visual-effects stars:>50",
    "topic:post-processing stars:>50",
    "topic:shader-effects stars:>20",
    "topic:particle-system stars:>20",
    "topic:audio-effects stars:>20",
    "topic:dsp stars:>100",
    "topic:compositor stars:>20",
    "shader effects",
    "visual effects compositor",
    "post processing shader",
    "particle system",
    "audio effects dsp",
]

AUDIO_GITHUB_QUERIES = [
    "topic:audio stars:>500",
    "topic:dsp stars:>100",
    "topic:audio-plugin stars:>20",
    "topic:synthesizer stars:>50",
    "topic:speech-processing stars:>50",
    "topic:webrtc-audio stars:>20",
]

VIDEO_GITHUB_QUERIES = [
    "topic:video stars:>500",
    "topic:video-processing stars:>100",
    "topic:streaming stars:>500",
    "topic:ffmpeg stars:>100",
    "topic:webrtc stars:>500",
    "topic:video-encoding stars:>20",
]

PHOTOGRAPHY_GITHUB_QUERIES = [
    "topic:photography stars:>50",
    "topic:raw-image stars:>20",
    "topic:camera stars:>100",
    "topic:exif stars:>50",
    "topic:image-processing stars:>500",
    "topic:hdr stars:>20",
]

MICROSCOPY_GITHUB_QUERIES = [
    "topic:microscopy stars:>20",
    "topic:bioimaging stars:>20",
    "topic:imagej stars:>20",
    "topic:ome-tiff stars:>5",
    "topic:microscope stars:>10",
    "topic:cell-segmentation stars:>20",
]

TELESCOPES_GITHUB_QUERIES = [
    "topic:telescope stars:>10",
    "topic:astronomy stars:>100",
    "topic:observatory stars:>10",
    "topic:astrophotography stars:>10",
    "topic:indi stars:>10",
    "topic:fits stars:>20",
]

RADARS_GITHUB_QUERIES = [
    "topic:radar stars:>20",
    "topic:synthetic-aperture-radar stars:>10",
    "topic:sar stars:>20",
    "topic:radar-signal-processing stars:>5",
    "topic:gnss stars:>20",
    "topic:remote-sensing stars:>50",
]

SATCOM_SATELLITES_GITHUB_QUERIES = [
    "topic:satellite-communications stars:>5",
    "topic:satcom stars:>5",
    "topic:satellite stars:>50",
    "topic:gnuradio stars:>20",
    "topic:sdr stars:>100",
    "topic:ccsds stars:>5",
]

ELECTROMAGNETOSCOPES_GITHUB_QUERIES = [
    "topic:sdr stars:>100",
    "topic:radio stars:>100",
    "topic:spectrum-analyzer stars:>10",
    "topic:electromagnetics stars:>5",
    "topic:magnetometer stars:>5",
    "topic:rf stars:>50",
    "topic:antenna stars:>10",
]

RADIO_GARDEN_SPECIALITY_GITHUB_QUERIES = [
    "\"Radio Garden\"",
    "\"radio.garden\"",
    "radio-garden",
    "radiogarden",
    "\"Radio Garden\" desktop",
    "\"Radio Garden\" API",
    "\"Radio Garden\" android",
    "\"Radio Garden\" electron",
]

PACKAGIST_QUERY_TERMS = [
    "http",
    "json",
    "database",
    "mysql",
    "postgres",
    "redis",
    "testing",
    "phpunit",
    "static analysis",
    "phpstan",
    "psalm",
    "framework",
    "laravel",
    "symfony",
    "logging",
    "security",
    "queue",
    "cache",
    "serialization",
    "cli",
]

COCOAPODS_NAME_TERMS = [
    "swift",
    "network",
    "http",
    "json",
    "database",
    "sqlite",
    "realm",
    "cache",
    "storage",
    "security",
    "crypto",
    "image",
    "audio",
    "video",
    "test",
    "layout",
    "async",
    "firebase",
    "analytics",
    "map",
]

SWIFT_GITHUB_QUERIES = [
    "language:Swift stars:>1000",
    "topic:swift-package stars:>200",
    "topic:swift-server stars:>100",
    "topic:swiftui stars:>500",
    "topic:ios-library stars:>500",
]

WEBASSEMBLY_GITHUB_QUERIES = [
    "language:WebAssembly stars:>50",
    "topic:webassembly stars:>500",
    "topic:wasm stars:>500",
    "topic:wasi stars:>100",
    "topic:wasm-component-model stars:>20",
]

SAPJAVA_MAVEN_QUERIES = [
    'g:"com.sap.cloud.sdk"',
    'g:"com.sap.cds"',
    'g:"com.sap.cloud"',
    'g:"com.sap.conn.jco"',
    "sap hana java",
    "sap odata java",
    "sap cloud sdk",
]

SAPJAVA_GITHUB_QUERIES = [
    "org:SAP Java",
    "SAP Cloud SDK Java",
    "SAP CAP Java",
    "SAP HANA Java",
]

COCOA_GITHUB_QUERIES = [
    "topic:cocoa stars:>200",
    "topic:cocoapods stars:>200",
    "topic:ios-library stars:>500",
    "language:Objective-C stars:>1000",
]

DATABASE_GITHUB_QUERIES = [
    "topic:database stars:>1000",
    "topic:postgresql stars:>1000",
    "topic:mysql stars:>500",
    "topic:sqlite stars:>500",
    "topic:nosql stars:>500",
    "topic:olap stars:>200",
    "topic:database-driver stars:>50",
    "topic:odbc stars:>50",
    "topic:jdbc stars:>50",
    "topic:vector-database stars:>100",
    "topic:time-series-database stars:>100",
    "topic:object-storage stars:>100",
    "topic:data-lake stars:>50",
    "topic:serverless-database stars:>20",
]

GITLAB_PROJECT_QUERIES = [
    "compiler",
    "language server",
    "database",
    "runtime",
    "package manager",
    "static analysis",
    "ci",
    "devops",
    "kubernetes",
    "security",
]

GITEA_REPOSITORY_QUERIES = [
    "compiler",
    "database",
    "language",
    "runtime",
    "ci",
    "devops",
    "library",
    "server",
    "tooling",
    "documentation",
]

REPOSITORY_WORKPLACE_RECORDS = [
    ("GitHub", "registry_repository", "https://github.com/explore", "GitHub public source-code workplace and repository discovery surface for repositories, issues, pull requests, releases, packages, actions, organizations, and automation APIs."),
    ("GitHub CLI", "cli", "https://cli.github.com/manual/", "Official gh command-line client for repository search, issues, pull requests, releases, workflows, authentication, and developer automation."),
    ("GitHub Repository Search API", "documentation", "https://docs.github.com/rest/search/search#search-repositories", "Official GitHub REST API route for repository search and structured repository metadata."),
    ("GitHub Actions", "precommit_ci_quality", "https://docs.github.com/actions", "GitHub workflow automation system for CI, release, deployment, security scanning, package publication, and scheduled jobs."),
    ("GitHub Packages", "registry_repository", "https://docs.github.com/packages", "GitHub package registry for containers and language package ecosystems."),
    ("GitHub Releases", "registry_repository", "https://docs.github.com/repositories/releasing-projects-on-github", "GitHub release publishing surface for tags, release notes, assets, and prerelease channels."),
    ("GitHub Codespaces", "ide_editor_integration", "https://docs.github.com/codespaces", "Hosted development environment connected to GitHub repositories and developer workflows."),
    ("Alpine Linux Packages", "registry_repository", "https://pkgs.alpinelinux.org/packages", "Official Alpine Linux package index for APK package search, versions, architectures, maintainers, repositories, branches, and source package routes."),
    ("Alpine aports", "registry_repository", "https://gitlab.alpinelinux.org/alpine/aports", "Official Alpine package build recipes repository used to produce Alpine Linux packages."),
    ("apk-tools", "package_manager", "https://gitlab.alpinelinux.org/alpine/apk-tools", "Alpine package manager tooling for package indexes, installation, upgrades, repositories, signatures, and system package operations."),
    ("GitLab", "registry_repository", "https://gitlab.com/explore/projects/trending", "GitLab public project workplace and source hosting surface for repositories, issues, merge requests, releases, CI/CD, registries, and groups."),
    ("GitLab Projects API", "documentation", "https://docs.gitlab.com/api/projects/", "Official GitLab projects API for listing, searching, inspecting, and automating project metadata."),
    ("GitLab CLI", "cli", "https://gitlab.com/gitlab-org/cli", "Official GitLab command-line client for issues, merge requests, pipelines, releases, and repository workflows."),
    ("GitLab CI/CD", "precommit_ci_quality", "https://docs.gitlab.com/ci/", "GitLab pipeline system for build, test, release, deployment, package, security, and environment automation."),
    ("GitLab Package Registry", "registry_repository", "https://docs.gitlab.com/user/packages/package_registry/", "GitLab package registry for package publication, dependency workflows, and project-scoped package metadata."),
    ("Gitea", "registry_repository", "https://about.gitea.com/", "Self-hostable Git forge with repositories, issues, pull requests, packages, actions, and federation-oriented workflows."),
    ("Gitea API", "documentation", "https://docs.gitea.com/api/", "Official Gitea API reference for repository, organization, issue, pull request, package, and automation operations."),
    ("Gitea Actions", "precommit_ci_quality", "https://docs.gitea.com/usage/actions/overview", "Gitea integrated CI/CD workflow engine compatible with common action-style automation patterns."),
    ("Gitea Packages", "registry_repository", "https://docs.gitea.com/usage/packages/overview", "Gitea package registry surface for language package ecosystems and container artifacts."),
    ("Forgejo", "registry_repository", "https://forgejo.org/", "Community-controlled forge derived from Gitea for Git hosting, collaboration, CI, federation, and package workflows."),
    ("Codeberg", "registry_repository", "https://codeberg.org/explore/repos", "Forgejo-powered public software development workplace for open-source repositories and organizations."),
    ("Mercurial SCM", "utility_library", "https://www.mercurial-scm.org/", "Distributed version control system using the hg command, with changesets, branches, bookmarks, phases, and extension workflows."),
    ("Mercurial Repository Hosting", "registry_repository", "https://www.mercurial-scm.org/repo/", "Official Mercurial repository browser for Mercurial project source repositories."),
    ("Heptapod", "registry_repository", "https://foss.heptapod.net/", "Mercurial-oriented forge based on GitLab concepts for repositories, merge requests, issues, and CI workflows."),
    ("Apache Subversion", "utility_library", "https://subversion.apache.org/", "Centralized version control system with working copies, commits, branches, tags, externals, hooks, and repository administration."),
    ("Apache Subversion Repository", "registry_repository", "https://svn.apache.org/repos/asf/", "Apache Software Foundation Subversion repository root and browser for ASF-hosted projects."),
    ("ViewVC", "visualization_gui", "https://www.viewvc.org/", "Repository browser for CVS and Subversion repositories."),
    ("TortoiseSVN", "ide_editor_integration", "https://tortoisesvn.net/", "Windows shell integration client for Apache Subversion repositories and working copies."),
    ("Fossil SCM", "utility_library", "https://fossil-scm.org/", "Distributed version control and project workplace with repository, wiki, tickets, forum, and web UI in one executable."),
    ("sourcehut", "registry_repository", "https://sr.ht/", "Hosted software development workplace built around Git, Mercurial, mailing lists, builds, tickets, and Unix-style tooling."),
    ("sourcehut builds", "precommit_ci_quality", "https://builds.sr.ht/", "sourcehut continuous integration and build automation service."),
    ("Gerrit Code Review", "codegen_codemod_refactoring", "https://www.gerritcodereview.com/", "Code review system for Git repositories, change sets, submit queues, review labels, and large project governance."),
    ("Gerrit API", "documentation", "https://gerrit-review.googlesource.com/Documentation/rest-api.html", "Official Gerrit REST API for changes, accounts, groups, projects, plugins, and review automation."),
    ("Gitiles", "visualization_gui", "https://gerrit.googlesource.com/gitiles/", "Git repository browser used with Gerrit and googlesource-hosted projects."),
    ("Go Source Route", "registry_repository", "https://go.googlesource.com/go", "Official Go source repository route on googlesource/Gerrit."),
    ("Go Review Route", "codegen_codemod_refactoring", "https://go-review.googlesource.com/", "Official Go Gerrit code review route for Go project changes."),
    ("Go Dev Source Guide", "documentation", "https://go.dev/doc/contribute", "Official Go contribution guide and source workflow entry point."),
    ("Python CPython Source", "registry_repository", "https://github.com/python/cpython", "Official CPython source repository route."),
    ("Python Developer Guide", "documentation", "https://devguide.python.org/", "Official Python developer guide for source checkout, build, tests, triage, and contribution workflow."),
    ("Rust Source Route", "registry_repository", "https://github.com/rust-lang/rust", "Official Rust compiler and standard library source repository route."),
    ("Rust Forge", "documentation", "https://forge.rust-lang.org/", "Official Rust project forge documentation for release, infrastructure, CI, team, and repository workflows."),
    ("Node.js Source Route", "registry_repository", "https://github.com/nodejs/node", "Official Node.js runtime source repository route."),
    ("TypeScript Source Route", "registry_repository", "https://github.com/microsoft/TypeScript", "Official TypeScript compiler, language service, and tooling source repository route."),
    ("R Source Repository", "registry_repository", "https://svn.r-project.org/R/", "Official R project Subversion repository route for R source and branches."),
    ("R Development Page", "documentation", "https://developer.r-project.org/", "Official R development route for source, build, patch, bug, and release workflow references."),
    ("Julia Source Route", "registry_repository", "https://github.com/JuliaLang/julia", "Official Julia language source repository route."),
    ("Julia General Registry Route", "registry_repository", "https://github.com/JuliaRegistries/General", "Official Julia General package registry source route."),
    ("GHC GitLab Route", "registry_repository", "https://gitlab.haskell.org/ghc/ghc", "Official GHC source route on GitLab for compiler and runtime development."),
    ("Haskell Language Server Source", "registry_repository", "https://github.com/haskell/haskell-language-server", "Official Haskell Language Server source route."),
    ("PHP Source Route", "registry_repository", "https://github.com/php/php-src", "Official PHP implementation source repository route."),
    ("PHP Git Access", "documentation", "https://www.php.net/git.php", "Official PHP Git source access and workflow entry point."),
    ("Dart SDK Source Route", "registry_repository", "https://github.com/dart-lang/sdk", "Official Dart SDK source repository route."),
    ("Swift Source Route", "registry_repository", "https://github.com/swiftlang/swift", "Official Swift compiler and standard library source repository route."),
    ("Swift Package Manager Source", "registry_repository", "https://github.com/swiftlang/swift-package-manager", "Official Swift Package Manager source repository route."),
    ("WebAssembly Spec Source", "registry_repository", "https://github.com/WebAssembly/spec", "Official WebAssembly core specification source route."),
    ("Cocoa Open Source Route", "registry_repository", "https://opensource.apple.com/", "Apple open source release route for Darwin and Apple-distributed open source components."),
    ("LLVM Source Route", "registry_repository", "https://github.com/llvm/llvm-project", "Official LLVM monorepo route used by Clang, lld, libc++, compiler-rt, MLIR, and related tooling."),
    ("GNU Source Route", "registry_repository", "https://savannah.gnu.org/git/", "GNU Savannah Git repository route for GNU project source hosting."),
    ("Apache Source Repositories", "registry_repository", "https://gitbox.apache.org/repos/asf", "Apache Software Foundation GitBox repository browser and source hosting route."),
]

ADDITIONAL_CURATED_LANGUAGE_RECORDS = [
    ("Starlark", "Starlark Language Specification", "language_specification", "https://starlark-lang.org/spec.html", "Official Starlark language specification for syntax, values, modules, functions, evaluation, determinism, and embedding contracts."),
    ("Starlark", "Starlark Language Site", "documentation", "https://starlark-lang.org/", "Official Starlark language site and overview for the Python-like embedded configuration language."),
    ("Starlark", "bazelbuild/starlark", "registry_repository", "https://github.com/bazelbuild/starlark", "Official Starlark source/spec repository and language coordination route."),
    ("Starlark", "Bazel Starlark Language", "documentation", "https://bazel.build/rules/language", "Official Bazel documentation for using Starlark to write BUILD files, macros, and build rules."),
    ("Starlark", "starlark-go", "interpreter_runtime", "https://github.com/google/starlark-go", "Go implementation of the Starlark language for embedding deterministic configuration and scripting."),
    ("Starlark", "starlark-rust", "interpreter_runtime", "https://github.com/facebookexperimental/starlark-rust", "Rust implementation of Starlark used by Buck2 and embeddable build/configuration tooling."),
    ("Starlark", "Bazel", "build_system", "https://github.com/bazelbuild/bazel", "Build and test system that uses Starlark rules and macros for repository-scale build definitions."),
    ("Starlark", "Bazel Central Registry", "registry_repository", "https://registry.bazel.build/", "Official Bazel module registry for Bzlmod module discovery and version metadata."),
    ("Basilisk", "Basilisk C", "language_specification", "https://basilisk.fr/Basilisk%20C", "Official Basilisk C language extension documentation for C-like constructs used in Cartesian-grid discretisation schemes."),
    ("Basilisk", "Basilisk Tutorial", "tutorial_book_styleguide", "https://basilisk.fr/Tutorial", "Official Basilisk tutorial for setup, compilation, and first simulation programs."),
    ("Basilisk", "Basilisk Source", "registry_repository", "https://basilisk.fr/src/README", "Official Basilisk source-code route for the fluid simulation framework and Basilisk C ecosystem."),
    ("Basilisk", "Basilisk Examples", "documentation", "https://basilisk.fr/src/examples/README", "Official Basilisk example programs for numerical simulation, solvers, grids, and output workflows."),
    ("Basilisk", "AVSLab Basilisk", "framework", "https://github.com/AVSLab/basilisk", "Astrodynamics simulation framework with Python, C/C++, messaging, visualization, and GN&C workflows."),
    ("Basilisk", "AVSLab Basilisk Documentation", "documentation", "https://avslab.github.io/basilisk/", "Official Basilisk astrodynamics framework documentation and examples."),
    ("Basilisk", "Basilisk Browser", "interpreter_runtime", "https://www.basilisk-browser.org/", "Open-source desktop web browser named Basilisk; tracked separately because the project name overlaps language/framework records."),
    ("\"aim's\"", "OpenAI API", "networking_http", "https://platform.openai.com/docs/api-reference", "API reference route for model inference, agents, responses, realtime, files, evals, batch work, and operational integration."),
    ("\"aim's\"", "OpenAI Cookbook", "tutorial_book_styleguide", "https://github.com/openai/openai-cookbook", "Example corpus for model calls, retrieval, evals, tool use, structured outputs, and applied AI engineering workflows."),
    ("\"aim's\"", "Hugging Face Hub", "registry_repository", "https://huggingface.co/docs/hub/index", "Model, dataset, and space registry used for discovery, versioning, hosting, inference, and collaboration."),
    ("\"aim's\"", "Hugging Face Transformers", "machine_learning", "https://github.com/huggingface/transformers", "Model library for transformer architectures, tokenizers, inference, training, fine-tuning, and deployment adapters."),
    ("\"aim's\"", "Hugging Face Datasets", "database_datastore", "https://github.com/huggingface/datasets", "Dataset library and registry integration for machine-learning corpora, processing, streaming, and reproducible data loading."),
    ("\"aim's\"", "PyTorch", "machine_learning", "https://github.com/pytorch/pytorch", "Tensor, autograd, compiler, distributed, and deployment framework used across AI training and inference stacks."),
    ("\"aim's\"", "TensorFlow", "machine_learning", "https://github.com/tensorflow/tensorflow", "Machine-learning framework for training, serving, mobile, graph execution, and production model pipelines."),
    ("\"aim's\"", "JAX", "machine_learning", "https://github.com/jax-ml/jax", "Composable numerical computing and accelerator framework used for AI research, transformations, autodiff, and compilation."),
    ("\"aim's\"", "ONNX", "serialization", "https://onnx.ai/", "Open Neural Network Exchange format for model interchange, graph serialization, runtimes, and toolchain compatibility."),
    ("\"aim's\"", "ONNX Runtime", "interpreter_runtime", "https://github.com/microsoft/onnxruntime", "Inference runtime for ONNX models across CPU, GPU, browser, mobile, and server deployments."),
    ("\"aim's\"", "vLLM", "interpreter_runtime", "https://github.com/vllm-project/vllm", "High-throughput LLM inference and serving engine with batching, GPU execution, and OpenAI-compatible server surfaces."),
    ("\"aim's\"", "llama.cpp", "interpreter_runtime", "https://github.com/ggml-org/llama.cpp", "Local LLM inference runtime and model-conversion ecosystem for GGUF models across CPU/GPU backends."),
    ("\"aim's\"", "Ollama", "cli", "https://github.com/ollama/ollama", "Local model runner and service for packaging, serving, and operating LLMs on developer and server machines."),
    ("\"aim's\"", "KServe", "container_deployment", "https://github.com/kserve/kserve", "Kubernetes model-serving platform for inference services, autoscaling, canary rollouts, explainers, and protocol integrations."),
    ("\"aim's\"", "Ray Serve", "container_deployment", "https://docs.ray.io/en/latest/serve/", "Scalable model serving and Python application serving layer for distributed AI workloads."),
    ("\"aim's\"", "MLflow", "logging_observability", "https://github.com/mlflow/mlflow", "Machine-learning lifecycle platform for experiments, model registry, packaging, deployment, and tracking."),
    ("\"aim's\"", "LangChain", "framework", "https://github.com/langchain-ai/langchain", "LLM application framework for chains, agents, retrieval, tools, memory, and integrations."),
    ("\"aim's\"", "LlamaIndex", "framework", "https://github.com/run-llama/llama_index", "Data and retrieval framework for connecting LLM applications to documents, databases, indexes, and tools."),
    ("\"aim's\"", "DSPy", "framework", "https://github.com/stanfordnlp/dspy", "Programming model for composing and optimizing language-model pipelines and prompts."),
    ("\"aim's\"", "Ragas", "testing_framework", "https://github.com/explodinggradients/ragas", "Evaluation toolkit for retrieval-augmented generation, metrics, testsets, and LLM application quality gates."),
    ("\"aim's\"", "OpenAI Evals", "testing_framework", "https://github.com/openai/evals", "Evaluation framework and registry route for model and application behavior tests."),
    ("\"aim's\"", "Model Context Protocol", "networking_http", "https://modelcontextprotocol.io/", "Protocol route for connecting AI applications to tools, resources, prompts, and external systems."),
    ("\"aim's\"", "OpenTelemetry Semantic Conventions For GenAI", "logging_observability", "https://opentelemetry.io/docs/specs/semconv/gen-ai/", "Telemetry conventions for generative AI operations, spans, attributes, models, prompts, and responses."),
    ("nix", "Nix Language", "language_specification", "https://nix.dev/manual/nix/stable/language/", "Official Nix language manual for expressions, values, functions, derivations, imports, and evaluation semantics."),
    ("nix", "Nix Reference Manual", "documentation", "https://nix.dev/manual/nix/stable/", "Official Nix manual for commands, store operations, profiles, flakes, registries, and configuration."),
    ("nix", "Nix Source Route", "registry_repository", "https://github.com/NixOS/nix", "Official Nix package manager and language implementation source repository."),
    ("nix", "Nixpkgs", "registry_repository", "https://github.com/NixOS/nixpkgs", "Official Nix Packages collection and NixOS module source repository."),
    ("nix", "NixOS", "framework", "https://nixos.org/", "NixOS operating system project built around declarative system configuration and Nix packages."),
    ("nix", "NixOS Packages Search", "registry_repository", "https://search.nixos.org/packages", "Official NixOS package search interface for package names, versions, attributes, platforms, and maintainers."),
    ("nix", "NixOS Options Search", "registry_repository", "https://search.nixos.org/options", "Official NixOS option search interface for declarative system configuration."),
    ("nix", "Nix Flakes", "dependency_manager", "https://nix.dev/concepts/flakes", "Official Nix flake concept documentation for locked inputs, reproducible outputs, and project workflows."),
    ("nix", "Hydra", "precommit_ci_quality", "https://github.com/NixOS/hydra", "Nix-based continuous build system used for package and system build farms."),
    ("nix", "NixOS Wiki", "community_reference", "https://wiki.nixos.org/", "Community documentation route for Nix, NixOS, Nixpkgs, modules, packaging, deployment, and operations."),
    ("Doctrines", "NIST Secure Software Development Framework", "security_sast", "https://csrc.nist.gov/Projects/ssdf", "Secure software development doctrine for organizational controls, practices, supply-chain expectations, and software assurance."),
    ("Doctrines", "NIST Cybersecurity Framework", "security_sast", "https://www.nist.gov/cyberframework", "Cybersecurity risk-management doctrine used for identify, protect, detect, respond, and recover functions."),
    ("Doctrines", "NIST SP 800-53", "security_sast", "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final", "Security and privacy controls doctrine for federal information systems and organizations."),
    ("Doctrines", "NIST SP 800-218", "security_sast", "https://csrc.nist.gov/publications/detail/sp/800-218/final", "Secure software development framework publication for software producers and acquirers."),
    ("Doctrines", "CISA Secure by Design", "security_sast", "https://www.cisa.gov/securebydesign", "Secure-by-design and secure-by-default doctrine for software manufacturers and operators."),
    ("Doctrines", "SLSA", "precommit_ci_quality", "https://slsa.dev/", "Supply-chain Levels for Software Artifacts doctrine for build integrity, provenance, and release process hardening."),
    ("Doctrines", "OpenSSF Scorecard", "security_sast", "https://github.com/ossf/scorecard", "OpenSSF automated repository security posture checks used as supply-chain governance evidence."),
    ("Doctrines", "OpenSSF Best Practices Badge", "security_sast", "https://www.bestpractices.dev/", "OpenSSF best-practices checklist and badge route for project governance, security, and quality practices."),
    ("Doctrines", "OWASP ASVS", "security_sast", "https://owasp.org/www-project-application-security-verification-standard/", "Application Security Verification Standard for web application security requirements and verification levels."),
    ("Doctrines", "OWASP SAMM", "security_sast", "https://owaspsamm.org/", "Software Assurance Maturity Model for organizational application-security program governance."),
    ("Doctrines", "OWASP Top 10", "security_sast", "https://owasp.org/www-project-top-ten/", "Common web application risk doctrine and education route."),
    ("Doctrines", "MITRE ATT&CK", "security_sast", "https://attack.mitre.org/", "Adversary tactics and techniques knowledge base used for defensive engineering, detection, and threat modeling."),
    ("Doctrines", "CNCF Cloud Native Trail Map", "community_reference", "https://github.com/cncf/trailmap", "Cloud-native adoption map for container, orchestration, observability, service, and platform engineering decisions."),
    ("Doctrines", "AWS Well-Architected Framework", "documentation", "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html", "Cloud architecture doctrine for operational excellence, security, reliability, performance efficiency, cost, and sustainability."),
    ("Doctrines", "Azure Well-Architected Framework", "documentation", "https://learn.microsoft.com/azure/well-architected/", "Azure architecture doctrine for reliability, security, cost, operations, and performance tradeoffs."),
    ("Doctrines", "Google Cloud Architecture Framework", "documentation", "https://cloud.google.com/architecture/framework", "Google Cloud architecture doctrine for operational excellence, security, reliability, cost, performance, and system design."),
    ("Doctrines", "The Twelve-Factor App", "tutorial_book_styleguide", "https://12factor.net/", "Application architecture doctrine for cloud-native configuration, dependencies, backing services, logs, processes, and disposability."),
    ("Doctrines", "IETF RFC Index", "language_specification", "https://www.rfc-editor.org/rfc-index.html", "Authoritative route to Internet protocol standards, best current practices, and operational specifications."),
    ("Doctrines", "ISO/IEC/IEEE 42010", "documentation", "https://www.iso.org/standard/74393.html", "Architecture description standard for systems and software engineering views, viewpoints, stakeholders, and concerns."),
    ("APIs", "OpenAPI Specification", "language_specification", "https://spec.openapis.org/oas/latest.html", "Official OpenAPI Specification for describing HTTP APIs, operations, schemas, parameters, responses, security, and documents."),
    ("APIs", "OpenAPI Initiative", "community_reference", "https://www.openapis.org/", "Official OpenAPI Initiative route for specification governance, tooling, community, and releases."),
    ("APIs", "Swagger Editor", "api_doc_generator", "https://github.com/swagger-api/swagger-editor", "OpenAPI editing and validation tool for API design workflows."),
    ("APIs", "Swagger UI", "api_doc_generator", "https://github.com/swagger-api/swagger-ui", "OpenAPI documentation UI and interactive API browser."),
    ("APIs", "Swagger Codegen", "codegen_codemod_refactoring", "https://github.com/swagger-api/swagger-codegen", "OpenAPI-driven client/server code generation tooling."),
    ("APIs", "OpenAPI Generator", "codegen_codemod_refactoring", "https://github.com/OpenAPITools/openapi-generator", "OpenAPI generator ecosystem for clients, servers, documentation, and schemas across languages."),
    ("APIs", "AsyncAPI Specification", "language_specification", "https://www.asyncapi.com/docs/reference/specification/latest", "Official AsyncAPI specification for event-driven APIs, channels, messages, bindings, and schemas."),
    ("APIs", "AsyncAPI Generator", "codegen_codemod_refactoring", "https://github.com/asyncapi/generator", "AsyncAPI generator for event-driven API documentation, clients, and service scaffolding."),
    ("APIs", "JSON Schema", "language_specification", "https://json-schema.org/specification", "Official JSON Schema specification route for JSON data validation, vocabularies, references, and schema documents."),
    ("APIs", "GraphQL Specification", "language_specification", "https://spec.graphql.org/", "Official GraphQL specification for schema, type system, validation, execution, introspection, and response format."),
    ("APIs", "gRPC", "networking_http", "https://grpc.io/docs/", "Official gRPC documentation route for protobuf service APIs, clients, servers, deadlines, streaming, and language implementations."),
    ("APIs", "Protocol Buffers", "serialization", "https://protobuf.dev/", "Official Protocol Buffers route for schemas, encoding, code generation, and API contracts."),
    ("APIs", "RapidAPI Hub", "registry_repository", "https://rapidapi.com/hub", "API marketplace and discovery route for public API providers, subscriptions, testing, and integration metadata."),
    ("APIs", "Postman Public API Network", "registry_repository", "https://www.postman.com/explore", "Public API catalog and workspace route for collections, documentation, examples, and API collaboration."),
    ("APIs", "Stoplight", "api_doc_generator", "https://stoplight.io/open-source", "API design, governance, documentation, mocking, and style-guide ecosystem."),
    ("APIs", "Kong Gateway", "networking_http", "https://github.com/Kong/kong", "API gateway platform for routing, plugins, authentication, rate limiting, observability, and service traffic control."),
    ("APIs", "Tyk Gateway", "networking_http", "https://github.com/TykTechnologies/tyk", "API gateway and management platform for authentication, policies, analytics, developer portals, and traffic control."),
    ("APIs", "Apigee", "networking_http", "https://cloud.google.com/apigee", "API management platform for proxies, policies, analytics, monetization, developer portals, and governance."),
    ("APIs", "AWS API Gateway", "networking_http", "https://aws.amazon.com/api-gateway/", "Managed API gateway for REST, HTTP, WebSocket APIs, authorization, throttling, stages, and serverless integrations."),
    ("Transmission Protocols", "IETF RFC Index", "language_specification", "https://www.rfc-editor.org/rfc-index.html", "Authoritative route to Internet protocol standards, best current practices, and operational specifications."),
    ("Transmission Protocols", "IANA Protocol Registries", "registry_repository", "https://www.iana.org/protocols", "Official protocol parameter registries for ports, numbers, media types, DNS, routing, and transport assignments."),
    ("Transmission Protocols", "TCP", "networking_http", "https://www.rfc-editor.org/rfc/rfc9293.html", "Current Transmission Control Protocol specification for reliable byte streams, state machines, and congestion-aware transport behavior."),
    ("Transmission Protocols", "UDP", "networking_http", "https://www.rfc-editor.org/rfc/rfc768.html", "User Datagram Protocol specification for datagram transport and protocol layering."),
    ("Transmission Protocols", "QUIC", "networking_http", "https://www.rfc-editor.org/rfc/rfc9000.html", "QUIC transport protocol specification for encrypted multiplexed streams over UDP."),
    ("Transmission Protocols", "HTTP Semantics", "networking_http", "https://www.rfc-editor.org/rfc/rfc9110.html", "HTTP semantics specification for methods, status codes, fields, content, caching model boundaries, and intermediaries."),
    ("Transmission Protocols", "HTTP/1.1", "networking_http", "https://www.rfc-editor.org/rfc/rfc9112.html", "HTTP/1.1 messaging specification for wire format, framing, connection management, and parsing."),
    ("Transmission Protocols", "HTTP/2", "networking_http", "https://www.rfc-editor.org/rfc/rfc9113.html", "HTTP/2 specification for multiplexed streams, frames, flow control, and header compression."),
    ("Transmission Protocols", "HTTP/3", "networking_http", "https://www.rfc-editor.org/rfc/rfc9114.html", "HTTP/3 mapping of HTTP semantics over QUIC transport."),
    ("Transmission Protocols", "TLS 1.3", "cryptography", "https://www.rfc-editor.org/rfc/rfc8446.html", "Transport Layer Security 1.3 specification for encrypted authenticated channels."),
    ("Transmission Protocols", "DNS", "networking_http", "https://www.rfc-editor.org/rfc/rfc1035.html", "Domain Name System protocol specification for names, resource records, messages, and resolvers."),
    ("Transmission Protocols", "WebSocket", "networking_http", "https://www.rfc-editor.org/rfc/rfc6455.html", "WebSocket protocol for full-duplex communication over an HTTP-upgraded connection."),
    ("Transmission Protocols", "WebRTC", "networking_http", "https://www.w3.org/TR/webrtc/", "W3C WebRTC API specification for real-time media and data channel communication."),
    ("Transmission Protocols", "SCTP", "networking_http", "https://www.rfc-editor.org/rfc/rfc9260.html", "Stream Control Transmission Protocol specification for message-oriented multistream transport."),
    ("Transmission Protocols", "MQTT", "message_broker", "https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html", "OASIS MQTT 5.0 protocol specification for lightweight publish/subscribe messaging."),
    ("Transmission Protocols", "AMQP 1.0", "message_broker", "https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-complete-v1.0.html", "OASIS AMQP 1.0 specification for interoperable messaging."),
    ("Transmission Protocols", "STOMP", "message_broker", "https://stomp.github.io/stomp-specification-1.2.html", "Streaming Text Oriented Messaging Protocol specification for broker messaging."),
    ("Transmission Protocols", "NATS Protocol", "message_broker", "https://docs.nats.io/reference/reference-protocols/nats-protocol", "NATS protocol reference for client/server messaging, pub/sub, request/reply, and control operations."),
    ("Transmission Protocols", "Kafka Protocol", "message_broker", "https://kafka.apache.org/protocol", "Apache Kafka protocol guide for clients, brokers, requests, responses, versions, and wire compatibility."),
    ("Transmission Protocols", "gRPC over HTTP/2", "networking_http", "https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md", "gRPC HTTP/2 protocol mapping for RPC framing, metadata, status, streaming, and compression."),
    ("Transmission Protocols", "OpenSSH Protocol", "cryptography", "https://www.openssh.com/specs.html", "OpenSSH protocol specification route for SSH transport, authentication, connection, and extensions."),
    ("Transmission Protocols", "OpenSSL", "cryptography", "https://github.com/openssl/openssl", "TLS/cryptography library and protocol implementation used in many transport stacks."),
    ("Transmission Protocols", "ngtcp2", "networking_http", "https://github.com/ngtcp2/ngtcp2", "QUIC protocol implementation and tooling."),
    ("Transmission Protocols", "lsquic", "networking_http", "https://github.com/litespeedtech/lsquic", "QUIC and HTTP/3 library implementation."),
    ("Transmission Protocols", "Eclipse Paho", "message_broker", "https://github.com/eclipse-paho", "MQTT client library family and protocol tooling across languages."),
    ("Renderers", "Khronos Vulkan Registry", "language_specification", "https://registry.khronos.org/vulkan/", "Official Vulkan specification and registry route for graphics, compute, extensions, SPIR-V capabilities, and conformance-facing renderer work."),
    ("Renderers", "Khronos OpenGL Registry", "language_specification", "https://registry.khronos.org/OpenGL/", "Official OpenGL specification, extension, shading-language, and API registry route for renderer compatibility work."),
    ("Renderers", "W3C WebGPU", "language_specification", "https://www.w3.org/TR/webgpu/", "WebGPU specification for modern browser and native GPU rendering and compute APIs."),
    ("Renderers", "WebGPU Native", "visualization_gui", "https://github.com/webgpu-native/webgpu-headers", "Native WebGPU C headers and API route for cross-platform renderer implementations."),
    ("Renderers", "Dawn", "visualization_gui", "https://github.com/google/dawn", "WebGPU implementation used for browser and native graphics stacks."),
    ("Renderers", "wgpu", "visualization_gui", "https://github.com/gfx-rs/wgpu", "Rust WebGPU implementation and cross-platform rendering abstraction used by applications and engines."),
    ("Renderers", "Mesa", "visualization_gui", "https://gitlab.freedesktop.org/mesa/mesa", "Open-source OpenGL, Vulkan, and GPU driver stack used by Linux desktops, browsers, games, and compute workloads."),
    ("Renderers", "ANGLE", "visualization_gui", "https://github.com/google/angle", "Almost Native Graphics Layer Engine translating OpenGL ES to native graphics backends for browsers and applications."),
    ("Renderers", "Skia", "visualization_gui", "https://skia.org/", "2D graphics library used for text, vector, raster, GPU-backed rendering, and browser/application UI surfaces."),
    ("Renderers", "Cairo Graphics", "visualization_gui", "https://www.cairographics.org/", "2D graphics library for vector drawing, raster output, PDF/SVG surfaces, and UI rendering pipelines."),
    ("Renderers", "Pixman", "visualization_gui", "https://www.pixman.org/", "Pixel-manipulation library used under Cairo and related raster rendering paths."),
    ("Renderers", "Filament", "visualization_gui", "https://github.com/google/filament", "Physically based real-time rendering engine for Android, desktop, and WebGL/WebGPU-style pipelines."),
    ("Renderers", "Blender Cycles", "visualization_gui", "https://developer.blender.org/docs/features/cycles/", "Production path-tracing renderer used in Blender for CPU/GPU rendering, shading, sampling, and scene output."),
    ("Renderers", "Godot Rendering", "game_engine_game_dev", "https://docs.godotengine.org/en/stable/tutorials/rendering/index.html", "Official Godot rendering documentation for renderer backends, materials, lighting, shaders, and engine settings."),
    ("Renderers", "SVG Specification", "language_specification", "https://www.w3.org/TR/SVG2/", "Scalable Vector Graphics specification used by browsers, document renderers, tooling, and design pipelines."),
    ("Renderers", "WeasyPrint", "api_doc_generator", "https://github.com/Kozea/WeasyPrint", "HTML and CSS to PDF renderer used for document generation and print-output pipelines."),
    ("Renderers", "Chromium Rendering Architecture", "documentation", "https://www.chromium.org/developers/design-documents/gpu-accelerated-compositing-in-chrome/", "Chromium renderer/compositor architecture route for browser GPU acceleration, compositing, and surfaces."),
    ("Computer Graphics Software", "Blender", "visualization_gui", "https://github.com/blender/blender", "3D creation suite for modeling, animation, rendering, compositing, simulation, scripting, and asset pipelines."),
    ("Computer Graphics Software", "Krita", "visualization_gui", "https://invent.kde.org/graphics/krita", "Digital painting and illustration application with brushes, animation, color management, scripting, and document pipelines."),
    ("Computer Graphics Software", "GIMP", "visualization_gui", "https://gitlab.gnome.org/GNOME/gimp", "Raster image editor and graphics processing application with plug-ins, scripting, color, layers, and export workflows."),
    ("Computer Graphics Software", "Inkscape", "visualization_gui", "https://gitlab.com/inkscape/inkscape", "Vector graphics editor for SVG authoring, illustration, paths, typography, extensions, and export workflows."),
    ("Computer Graphics Software", "FreeCAD", "visualization_gui", "https://github.com/FreeCAD/FreeCAD", "Parametric CAD modeler for mechanical design, assemblies, scripting, workbenches, and engineering workflows."),
    ("Computer Graphics Software", "OpenSCAD", "visualization_gui", "https://github.com/openscad/openscad", "Script-based solid modeling CAD system for constructive solid geometry and reproducible mechanical models."),
    ("Computer Graphics Software", "OpenSceneGraph", "visualization_gui", "https://github.com/openscenegraph/OpenSceneGraph", "Scene graph toolkit for real-time graphics, simulation, visualization, and application rendering."),
    ("Computer Graphics Software", "VTK", "visualization_gui", "https://gitlab.kitware.com/vtk/vtk", "Visualization Toolkit for scientific graphics, imaging, geometry processing, rendering, and data pipelines."),
    ("Computer Graphics Software", "ParaView", "visualization_gui", "https://gitlab.kitware.com/paraview/paraview", "Scientific visualization application for large data analysis, rendering, distributed processing, and dashboards."),
    ("Computer Graphics Software", "three.js", "visualization_gui", "https://github.com/mrdoob/three.js", "JavaScript 3D graphics library for WebGL/WebGPU scenes, assets, materials, animation, and browser rendering."),
    ("Computer Graphics Software", "Processing", "visualization_gui", "https://github.com/processing/processing4", "Creative-coding environment for visual arts, graphics programming, education, sketches, and export workflows."),
    ("Computer Graphics Software", "OpenCV", "image_audio_dsp", "https://github.com/opencv/opencv", "Computer vision and image processing library used in graphics pipelines, camera systems, media tools, and automation."),
    ("Engines", "V8", "jit_vm", "https://github.com/v8/v8", "JavaScript and WebAssembly engine with JIT compilation, garbage collection, embedding APIs, and runtime diagnostics."),
    ("Engines", "SpiderMonkey", "jit_vm", "https://spidermonkey.dev/", "Mozilla JavaScript and WebAssembly engine used for language runtime, embedding, JIT, garbage collection, and shell tooling."),
    ("Engines", "JavaScriptCore", "jit_vm", "https://github.com/WebKit/WebKit/tree/main/Source/JavaScriptCore", "WebKit JavaScript engine with bytecode, JIT, garbage collection, WebAssembly, and embedding surfaces."),
    ("Engines", "LLVM", "compiler", "https://github.com/llvm/llvm-project", "Compiler infrastructure engine for frontends, optimizers, code generation, linkers, runtimes, and tooling."),
    ("Engines", "Wasmtime", "interpreter_runtime", "https://github.com/bytecodealliance/wasmtime", "WebAssembly engine and runtime for component-model workloads, WASI, embedding, and sandboxed execution."),
    ("Engines", "Open Policy Agent", "interpreter_runtime", "https://github.com/open-policy-agent/opa", "Policy engine for authorization, admission control, configuration validation, and decision services."),
    ("Engines", "Drools", "interpreter_runtime", "https://github.com/apache/incubator-kie-drools", "Rules engine and decision automation platform for business rules, DMN, constraints, and runtime evaluation."),
    ("Engines", "Temporal", "async_runtime", "https://github.com/temporalio/temporal", "Durable workflow engine for long-running services, retries, activities, signals, schedules, and distributed execution."),
    ("Engines", "Apache Lucene", "database_datastore", "https://github.com/apache/lucene", "Search engine library for indexing, query execution, analyzers, scoring, and full-text retrieval systems."),
    ("Engines", "RocksDB", "database_datastore", "https://github.com/facebook/rocksdb", "Embeddable LSM storage engine for persistent key-value workloads, databases, caches, and stream processors."),
    ("Physics Engines", "Bullet Physics", "game_engine_game_dev", "https://github.com/bulletphysics/bullet3", "Real-time collision detection and rigid-body physics engine used in games, robotics, simulation, and graphics tools."),
    ("Physics Engines", "Box2D", "game_engine_game_dev", "https://github.com/erincatto/box2d", "2D rigid-body physics engine for games and simulations."),
    ("Physics Engines", "Jolt Physics", "game_engine_game_dev", "https://github.com/jrouwe/JoltPhysics", "C++ physics engine for games and real-time simulation with collision detection and multithreaded solving."),
    ("Physics Engines", "NVIDIA PhysX", "game_engine_game_dev", "https://github.com/NVIDIA-Omniverse/PhysX", "Physics simulation SDK for rigid bodies, collision, vehicles, particles, and real-time simulation workloads."),
    ("Physics Engines", "MuJoCo", "math_numeric_scientific", "https://github.com/google-deepmind/mujoco", "Physics engine for robotics, biomechanics, contacts, articulated bodies, simulation, and control research."),
    ("Physics Engines", "Open Dynamics Engine", "game_engine_game_dev", "https://github.com/thomasmarsh/ODE", "Rigid-body dynamics and collision detection engine for real-time simulation."),
    ("Physics Engines", "Chipmunk2D", "game_engine_game_dev", "https://github.com/slembcke/Chipmunk2D", "Lightweight 2D physics engine for games and interactive simulations."),
    ("Physics Engines", "Rapier", "game_engine_game_dev", "https://github.com/dimforge/rapier", "Rust and JavaScript physics engine for 2D/3D rigid bodies, collision detection, and simulation."),
    ("Physics Engines", "Project Chrono", "math_numeric_scientific", "https://github.com/projectchrono/chrono", "Multiphysics simulation engine for vehicles, robotics, granular materials, fluids, and distributed dynamics."),
    ("Physics Engines", "Drake", "math_numeric_scientific", "https://github.com/RobotLocomotion/drake", "Model-based design and simulation toolbox for robotics dynamics, optimization, control, and planning."),
    ("Game Engines", "Godot Engine", "game_engine_game_dev", "https://github.com/godotengine/godot", "Open-source game engine for 2D/3D games, editor tooling, scripting, rendering, physics, and exports."),
    ("Game Engines", "Unreal Engine", "game_engine_game_dev", "https://www.unrealengine.com/", "Commercial-scale real-time 3D engine for games, simulation, virtual production, rendering, networking, and tools."),
    ("Game Engines", "Unity", "game_engine_game_dev", "https://unity.com/", "Real-time development platform and game engine for 2D/3D projects, editor workflows, assets, physics, and deployment."),
    ("Game Engines", "Bevy", "game_engine_game_dev", "https://github.com/bevyengine/bevy", "Rust ECS game engine with renderer, assets, scenes, input, UI, and plugin architecture."),
    ("Game Engines", "O3DE", "game_engine_game_dev", "https://github.com/o3de/o3de", "Open 3D Engine for games, simulation, editor tooling, rendering, networking, and modular gems."),
    ("Game Engines", "Stride", "game_engine_game_dev", "https://github.com/stride3d/stride", "C# game engine for 2D/3D rendering, editor workflows, assets, and runtime systems."),
    ("Game Engines", "Defold", "game_engine_game_dev", "https://github.com/defold/defold", "Cross-platform game engine with editor, scripting, 2D/3D rendering, physics, and asset pipelines."),
    ("Game Engines", "Cocos2d-x", "game_engine_game_dev", "https://github.com/cocos2d/cocos2d-x", "Cross-platform game engine and framework for 2D games and native runtimes."),
    ("Game Engines", "Phaser", "game_engine_game_dev", "https://github.com/phaserjs/phaser", "HTML5 game framework for Canvas/WebGL 2D games, scenes, physics, input, and asset loading."),
    ("Game Engines", "Love2D", "game_engine_game_dev", "https://github.com/love2d/love", "Lua framework for 2D games with graphics, audio, input, filesystem, and packaging workflows."),
    ("Game Engines", "libGDX", "game_engine_game_dev", "https://github.com/libgdx/libgdx", "Java game development framework for desktop, Android, iOS, and web targets."),
    ("Game Engines", "Ren'Py", "game_engine_game_dev", "https://github.com/renpy/renpy", "Visual novel engine and authoring system with scripting, UI, packaging, and asset workflows."),
    ("Icons and Logos", "Simple Icons", "visualization_gui", "https://github.com/simple-icons/simple-icons", "Brand SVG icon set and metadata corpus for product logos, slugs, colors, aliases, and package distribution."),
    ("Icons and Logos", "Lucide", "visualization_gui", "https://github.com/lucide-icons/lucide", "SVG icon library and package ecosystem for application interfaces and design systems."),
    ("Icons and Logos", "Heroicons", "visualization_gui", "https://github.com/tailwindlabs/heroicons", "SVG icon set used with Tailwind-style application UI systems."),
    ("Icons and Logos", "Font Awesome", "visualization_gui", "https://github.com/FortAwesome/Font-Awesome", "Icon toolkit and font/SVG library for application, web, and documentation interfaces."),
    ("Icons and Logos", "Material Symbols", "visualization_gui", "https://fonts.google.com/icons", "Google Material icon and symbol catalog for UI systems, fonts, variable axes, and design assets."),
    ("Icons and Logos", "Bootstrap Icons", "visualization_gui", "https://github.com/twbs/icons", "SVG icon library for Bootstrap and general interface projects."),
    ("Icons and Logos", "Feather Icons", "visualization_gui", "https://github.com/feathericons/feather", "Open-source SVG icon set for lightweight application interfaces."),
    ("Icons and Logos", "Tabler Icons", "visualization_gui", "https://github.com/tabler/tabler-icons", "Large SVG icon set and package ecosystem for dashboards, apps, and design systems."),
    ("Icons and Logos", "Iconify", "visualization_gui", "https://github.com/iconify/iconify", "Unified icon framework and package ecosystem for many icon sets across web frameworks."),
    ("Icons and Logos", "Noun Project API", "networking_http", "https://api.thenounproject.com/", "Icon search and asset API route for symbol discovery and product integrations."),
    ("Icons and Logos", "OpenMoji", "visualization_gui", "https://github.com/hfg-gmuend/openmoji", "Open emoji and icon set with SVG/PNG assets, metadata, and package distribution."),
    ("Icons and Logos", "Emoji Unicode Charts", "language_specification", "https://unicode.org/emoji/charts/", "Unicode emoji charts and data route for standardized symbols, names, sequences, and rendering behavior."),
    ("Icons and Logos", "SVG Specification", "language_specification", "https://www.w3.org/TR/SVG2/", "Scalable Vector Graphics specification used for icon systems, logos, accessibility metadata, and rendering pipelines."),
    ("Icons and Logos", "W3C Web App Manifest Icons", "language_specification", "https://www.w3.org/TR/appmanifest/#icons-member", "Web app manifest icon member specification for installable web applications and icon asset selection."),
    ("Icons and Logos", "Favicon Cheat Sheet", "documentation", "https://github.com/audreyfeldroy/favicon-cheat-sheet", "Practical favicon asset matrix for browsers, platforms, sizes, manifests, and generated website icon files."),
    ("Font Briefcase", "OpenType Specification", "language_specification", "https://learn.microsoft.com/typography/opentype/spec/", "OpenType font format specification route for glyphs, tables, layout, variable fonts, metadata, and renderer compatibility."),
    ("Font Briefcase", "WOFF2", "compression", "https://www.w3.org/TR/WOFF2/", "Web Open Font Format 2.0 specification for compressed web font delivery and browser font loading."),
    ("Font Briefcase", "FreeType", "visualization_gui", "https://gitlab.freedesktop.org/freetype/freetype", "Font rendering library used to load, rasterize, hint, and operate font assets across platforms."),
    ("Font Briefcase", "HarfBuzz", "visualization_gui", "https://github.com/harfbuzz/harfbuzz", "Text shaping engine for scripts, glyph layout, font features, and renderer integration."),
    ("Font Briefcase", "Fontconfig", "configuration", "https://gitlab.freedesktop.org/fontconfig/fontconfig", "Font discovery, matching, substitution, and configuration library used by Unix-like desktop and server systems."),
    ("Font Briefcase", "fontTools", "utility_library", "https://github.com/fonttools/fonttools", "Python font engineering toolkit for OpenType, TrueType, UFO, variable fonts, subsetting, and inspection."),
    ("Font Briefcase", "FontForge", "visualization_gui", "https://github.com/fontforge/fontforge", "Font editor and scripting environment for designing, converting, inspecting, and repairing font files."),
    ("Font Briefcase", "Google Fonts", "registry_repository", "https://github.com/google/fonts", "Font catalog and source repository for font-family metadata, binaries, licenses, and delivery workflows."),
    ("Font Briefcase", "Fontsource", "registry_repository", "https://github.com/fontsource/fontsource", "Self-hostable font package registry and package generation workflow for web font assets."),
    ("Font Briefcase", "Adobe Source Fonts", "registry_repository", "https://github.com/adobe-fonts", "Adobe open-source font repository route for source fonts, build files, releases, and licensing metadata."),
    ("Font Briefcase", "Unified Font Object", "serialization", "https://unifiedfontobject.org/", "UFO font source format specification used for font design, interchange, and build workflows."),
    ("Font Briefcase", "Apple Font Book", "visualization_gui", "https://support.apple.com/guide/font-book/welcome/mac", "macOS Font Book route for installing, validating, organizing, and disabling fonts on Apple systems."),
    ("Assets", "glTF", "serialization", "https://github.com/KhronosGroup/glTF", "Runtime 3D asset format and ecosystem for scenes, meshes, materials, animations, textures, and engine interchange."),
    ("Assets", "USD", "serialization", "https://github.com/PixarAnimationStudios/OpenUSD", "Universal Scene Description framework for scene composition, assets, layers, variants, materials, and production pipelines."),
    ("Assets", "OpenAssetIO", "interop_bindings", "https://github.com/OpenAssetIO/OpenAssetIO", "Open-source interoperability standard and library for asset management systems and content creation tools."),
    ("Assets", "OpenColorIO", "image_audio_dsp", "https://github.com/AcademySoftwareFoundation/OpenColorIO", "Color-management system for film, animation, visual effects, and asset pipeline rendering consistency."),
    ("Assets", "OpenImageIO", "image_audio_dsp", "https://github.com/AcademySoftwareFoundation/OpenImageIO", "Image I/O library and tools for reading, writing, converting, and inspecting texture/image asset formats."),
    ("Assets", "OpenEXR", "serialization", "https://github.com/AcademySoftwareFoundation/openexr", "High dynamic-range image file format and library for visual effects, rendering, and archival image assets."),
    ("Assets", "KTX-Software", "serialization", "https://github.com/KhronosGroup/KTX-Software", "KTX texture tooling for GPU texture containers, Basis Universal compression, and graphics asset delivery."),
    ("Assets", "Basis Universal", "compression", "https://github.com/BinomialLLC/basis_universal", "Universal GPU texture compression system and transcoder for runtime asset delivery."),
    ("Assets", "FFmpeg", "image_audio_dsp", "https://github.com/FFmpeg/FFmpeg", "Media processing toolkit for audio/video decoding, encoding, conversion, streaming, metadata, and asset pipelines."),
    ("Assets", "ImageMagick", "image_audio_dsp", "https://github.com/ImageMagick/ImageMagick", "Image processing and conversion toolkit for raster assets, automation, thumbnails, and format normalization."),
    ("Assets", "Sharp", "image_audio_dsp", "https://github.com/lovell/sharp", "Node.js image processing library used for resizing, transforming, optimizing, and delivering image assets."),
    ("Assets", "SVGO", "compression", "https://github.com/svg/svgo", "SVG optimizer for icon, logo, illustration, and vector asset pipelines."),
    ("Assets", "TexturePacker", "visualization_gui", "https://www.codeandweb.com/texturepacker", "Atlas packing tool for sprite sheets, textures, game assets, and runtime loaders."),
    ("Assets", "FreeType", "visualization_gui", "https://gitlab.freedesktop.org/freetype/freetype", "Font rendering library used to load, rasterize, hint, and operate font assets."),
    ("Assets", "HarfBuzz", "visualization_gui", "https://github.com/harfbuzz/harfbuzz", "Text shaping engine for font assets, scripts, glyph layout, and rendering pipelines."),
    ("Assets", "Google Fonts", "registry_repository", "https://github.com/google/fonts", "Font catalog and source repository for font-family metadata, binaries, licenses, and delivery workflows."),
    ("Assets", "Fontsource", "registry_repository", "https://github.com/fontsource/fontsource", "Self-hostable font package registry and package generation workflow for web font assets."),
    ("Assets", "OpenGameArt", "registry_repository", "https://opengameart.org/", "Game asset repository for textures, sprites, audio, models, tilesets, and license-aware reuse."),
    ("Assets", "Poly Haven", "registry_repository", "https://polyhaven.com/", "Public-domain HDRIs, textures, and 3D models for rendering and game asset pipelines."),
    ("Assets", "AWS S3", "database_datastore", "https://aws.amazon.com/s3/", "Object storage service used for binary assets, media, data lakes, archives, backups, and static delivery."),
    ("Assets", "Cloudflare R2", "database_datastore", "https://developers.cloudflare.com/r2/", "S3-compatible object storage for asset delivery, static files, media, backups, and serverless workflows."),
    ("Assets", "Unity Addressables", "dependency_manager", "https://docs.unity3d.com/Packages/com.unity.addressables@latest", "Unity asset management system for bundles, catalogs, remote loading, dependency tracking, and runtime delivery."),
    ("Assets", "Godot Import Process", "documentation", "https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html", "Godot asset import pipeline for source assets, imported resources, metadata, and runtime-ready files."),
    ("Maps", "OpenStreetMap", "registry_repository", "https://www.openstreetmap.org/", "Collaborative map database and editing ecosystem for roads, places, routing, tiles, geocoding, and geospatial applications."),
    ("Maps", "OSM Wiki Map Features", "documentation", "https://wiki.openstreetmap.org/wiki/Map_features", "OpenStreetMap tagging reference for map objects, keys, values, conventions, and data modeling."),
    ("Maps", "GDAL", "interop_bindings", "https://github.com/OSGeo/gdal", "Geospatial data abstraction library for raster/vector formats, coordinate systems, reprojection, and map data conversion."),
    ("Maps", "PROJ", "math_numeric_scientific", "https://github.com/OSGeo/PROJ", "Coordinate transformation and cartographic projection library for geospatial systems."),
    ("Maps", "QGIS", "visualization_gui", "https://github.com/qgis/QGIS", "Desktop GIS and geospatial platform for map editing, spatial analysis, plugins, databases, and visualization."),
    ("Maps", "PostGIS", "database_datastore", "https://github.com/postgis/postgis", "Spatial database extension for PostgreSQL with geometry, geography, indexes, and geospatial SQL operations."),
    ("Maps", "MapLibre GL JS", "visualization_gui", "https://github.com/maplibre/maplibre-gl-js", "Open-source web map renderer for vector tiles, styles, interactions, and browser map applications."),
    ("Maps", "Leaflet", "visualization_gui", "https://github.com/Leaflet/Leaflet", "JavaScript map library for interactive web maps, tile layers, markers, controls, and plugins."),
    ("Maps", "OpenLayers", "visualization_gui", "https://github.com/openlayers/openlayers", "Web mapping library for raster/vector layers, projections, controls, formats, and geospatial interactions."),
    ("Maps", "Tippecanoe", "serialization", "https://github.com/felt/tippecanoe", "Vector tile generation tool for large geospatial datasets and map delivery pipelines."),
    ("Maps", "Valhalla", "networking_http", "https://github.com/valhalla/valhalla", "Open-source routing engine for navigation, map matching, multimodal routes, and turn-by-turn data."),
    ("Maps", "Nominatim", "networking_http", "https://github.com/osm-search/Nominatim", "OpenStreetMap geocoder and search engine for address/place lookup and reverse geocoding."),
    ("Space Engines", "NASA General Mission Analysis Tool", "math_numeric_scientific", "https://github.com/ChristopherRabotin/GMAT", "Mission analysis and trajectory design system for spacecraft, orbital mechanics, and astrodynamics workflows."),
    ("Space Engines", "Orekit", "math_numeric_scientific", "https://gitlab.orekit.org/orekit/orekit", "Astrodynamics library for orbit propagation, estimation, frames, time scales, maneuvers, and mission analysis."),
    ("Space Engines", "poliastro", "math_numeric_scientific", "https://github.com/poliastro/poliastro", "Python astrodynamics library for orbital mechanics, maneuvers, propagation, and mission analysis."),
    ("Space Engines", "Tudat", "math_numeric_scientific", "https://github.com/tudat-team/tudat", "Astrodynamics and spaceflight simulation toolkit for trajectory design, estimation, propagation, and mission engineering."),
    ("Space Engines", "Basilisk", "framework", "https://github.com/AVSLab/basilisk", "Astrodynamics simulation framework with spacecraft dynamics, messaging, visualization, and GN&C workflows."),
    ("Space Engines", "OpenRocket", "math_numeric_scientific", "https://github.com/openrocket/openrocket", "Rocket design and flight simulation application for airframes, motors, stability, aerodynamics, and trajectories."),
    ("Space Engines", "RocketCEA", "math_numeric_scientific", "https://github.com/sonofeft/RocketCEA", "Python wrapper around NASA CEA for rocket engine combustion performance calculations."),
    ("Space Engines", "Cantera", "math_numeric_scientific", "https://github.com/Cantera/cantera", "Thermodynamics, chemical kinetics, and transport toolkit used for propulsion, combustion, and reacting-flow analysis."),
    ("Space Engines", "NASA CEA", "math_numeric_scientific", "https://software.nasa.gov/software/LEW-17687-1", "NASA Chemical Equilibrium with Applications software route for rocket performance and combustion calculations."),
    ("Space Engines", "SPICE Toolkit", "math_numeric_scientific", "https://naif.jpl.nasa.gov/naif/toolkit.html", "NASA NAIF toolkit for spacecraft geometry, ephemerides, frames, kernels, and mission analysis."),
    ("Space Shuttles", "NASA Space Shuttle Overview", "documentation", "https://www.nasa.gov/space-shuttle/", "NASA Space Shuttle route for program history, orbiters, missions, systems, and operational references."),
    ("Space Shuttles", "NASA Space Shuttle Mission Archives", "registry_repository", "https://www.nasa.gov/mission/space-shuttle/", "NASA mission archive route for shuttle mission records and program data."),
    ("Space Shuttles", "Space Shuttle Technical Conference", "documentation", "https://ntrs.nasa.gov/", "NASA Technical Reports Server route for shuttle engineering papers, mission documents, and systems references."),
    ("Space Shuttles", "Orbiter Space Flight Simulator", "game_engine_game_dev", "https://www.orbiter-forum.com/", "Space flight simulator ecosystem for orbital mechanics, shuttle-style vehicles, addons, and mission scenarios."),
    ("Space Shuttles", "Space Shuttle Ultra", "game_engine_game_dev", "https://github.com/GLS-SSV/SSV", "Open-source Space Shuttle Vessel addon project for Orbiter-style simulation workflows."),
    ("Space Shuttles", "Shuttle Mission Simulator Records", "documentation", "https://history.nasa.gov/sts1/pages/simulators.html", "NASA history route for shuttle simulator and training context."),
    ("Space Maps", "NASA Solar System Treks", "visualization_gui", "https://trek.nasa.gov/", "NASA planetary mapping portals for Moon, Mars, Vesta, Titan, and other bodies with science layers and tools."),
    ("Space Maps", "NASA WorldWind", "visualization_gui", "https://github.com/NASAWorldWind/WebWorldWind", "NASA virtual globe and geospatial visualization SDK for planetary and Earth map applications."),
    ("Space Maps", "CesiumJS", "visualization_gui", "https://github.com/CesiumGS/cesium", "3D geospatial engine for globes, 3D Tiles, terrain, imagery, time-dynamic data, and space visualization."),
    ("Space Maps", "SPICE Kernels", "database_datastore", "https://naif.jpl.nasa.gov/naif/data.html", "NASA NAIF SPICE kernel data route for ephemerides, spacecraft, instruments, frames, and mission geometry."),
    ("Space Maps", "International Virtual Observatory Alliance", "registry_repository", "https://www.ivoa.net/", "Astronomical data interoperability standards and registry ecosystem for sky catalogs, archives, and tools."),
    ("Space Maps", "Astropy", "math_numeric_scientific", "https://github.com/astropy/astropy", "Astronomy Python library for coordinates, time, units, FITS, WCS, tables, cosmology, and observatory data."),
    ("Space Maps", "Stellarium", "visualization_gui", "https://github.com/Stellarium/stellarium", "Open-source planetarium and sky map software with catalogs, simulations, plugins, and visualization."),
    ("Space Maps", "Skyfield", "math_numeric_scientific", "https://github.com/skyfielders/python-skyfield", "Python astronomy library for positions of stars, planets, satellites, and Earth observers."),
    ("Space Maps", "ESA Sky", "visualization_gui", "https://sky.esa.int/", "ESA astronomy sky exploration portal for missions, surveys, catalogs, and visual data discovery."),
    ("Effects", "OpenFX", "interop_bindings", "https://openeffects.org/", "Open plug-in API for visual effects hosts and image-processing effects."),
    ("Effects", "Natron", "visualization_gui", "https://github.com/NatronGitHub/Natron", "Node-based compositor for visual effects, rotoscoping, keying, color, and OpenFX plug-ins."),
    ("Effects", "Blender Compositor", "visualization_gui", "https://docs.blender.org/manual/en/latest/compositing/index.html", "Blender compositing system for visual effects, nodes, masks, color operations, and render outputs."),
    ("Effects", "G'MIC", "image_audio_dsp", "https://github.com/GreycLab/gmic", "Image-processing framework and filter language for effects, transformations, plug-ins, and pipelines."),
    ("Effects", "Shadertoy", "visualization_gui", "https://www.shadertoy.com/", "Shader effect and procedural graphics sharing platform for GLSL fragment shader experiments."),
    ("Effects", "ISF", "language_specification", "https://isf.video/", "Interactive Shader Format for video generators and effects described with GLSL and JSON metadata."),
    ("Effects", "The Book of Shaders", "tutorial_book_styleguide", "https://thebookofshaders.com/", "Educational shader programming route for procedural visual effects and GLSL concepts."),
    ("Effects", "three.js postprocessing", "visualization_gui", "https://github.com/pmndrs/postprocessing", "Post-processing effect framework for three.js scenes, passes, bloom, anti-aliasing, and screen-space effects."),
    ("Effects", "PixiJS Filters", "visualization_gui", "https://github.com/pixijs/filters", "Filter/effect collection for PixiJS rendering pipelines."),
    ("Effects", "Cinder", "visualization_gui", "https://github.com/cinder/Cinder", "C++ creative-coding library for graphics, audio, input, animation, shaders, and effect applications."),
    ("Effects", "JUCE", "image_audio_dsp", "https://github.com/juce-framework/JUCE", "C++ framework for audio plug-ins, DSP effects, instruments, and cross-platform media applications."),
    ("Effects", "Faust", "image_audio_dsp", "https://github.com/grame-cncm/faust", "Functional DSP language and compiler for audio effects, synthesis, plug-ins, and embedded targets."),
    ("Effects", "SoX", "image_audio_dsp", "https://github.com/chirlu/sox", "Audio processing utility for effects, format conversion, filtering, and batch media workflows."),
    ("Effects", "GStreamer Editing Services", "image_audio_dsp", "https://gitlab.freedesktop.org/gstreamer/gst-editing-services", "Timeline and editing framework for media effects, transitions, clips, and rendering pipelines."),
    ("Audio", "FFmpeg Audio", "image_audio_dsp", "https://github.com/FFmpeg/FFmpeg", "Audio decoding, encoding, filtering, streaming, container, and batch processing toolkit."),
    ("Audio", "GStreamer", "image_audio_dsp", "https://gitlab.freedesktop.org/gstreamer/gstreamer", "Multimedia framework for audio pipelines, plugins, streaming, capture, playback, encoding, and processing."),
    ("Audio", "JUCE", "image_audio_dsp", "https://github.com/juce-framework/JUCE", "C++ framework for audio applications, plug-ins, DSP effects, instruments, and cross-platform media tools."),
    ("Audio", "PortAudio", "image_audio_dsp", "https://github.com/PortAudio/portaudio", "Cross-platform audio I/O library for recording, playback, low-latency streams, and device integration."),
    ("Audio", "libsndfile", "image_audio_dsp", "https://github.com/libsndfile/libsndfile", "Audio file I/O library for reading, writing, and converting PCM and compressed sound formats."),
    ("Audio", "SoX", "image_audio_dsp", "https://github.com/chirlu/sox", "Command-line audio processing utility for effects, format conversion, resampling, and batch workflows."),
    ("Audio", "Faust", "image_audio_dsp", "https://github.com/grame-cncm/faust", "Functional DSP language and compiler for audio effects, synthesis, plug-ins, and embedded audio targets."),
    ("Audio", "PipeWire", "image_audio_dsp", "https://gitlab.freedesktop.org/pipewire/pipewire", "Linux multimedia server for audio/video routing, low-latency graph processing, devices, and session integration."),
    ("Video", "FFmpeg Video", "image_audio_dsp", "https://github.com/FFmpeg/FFmpeg", "Video decoding, encoding, filtering, transcoding, streaming, container, subtitle, and media pipeline toolkit."),
    ("Video", "GStreamer Video", "image_audio_dsp", "https://gitlab.freedesktop.org/gstreamer/gstreamer", "Video pipeline framework for capture, playback, encoding, streaming, filters, hardware acceleration, and plugins."),
    ("Video", "OBS Studio", "visualization_gui", "https://github.com/obsproject/obs-studio", "Live video production and recording software with sources, filters, encoders, plugins, and streaming workflows."),
    ("Video", "WebRTC", "networking_http", "https://webrtc.org/", "Real-time media stack for audio/video capture, encoding, transport, data channels, and browser/native communication."),
    ("Video", "x264", "compression", "https://code.videolan.org/videolan/x264", "H.264/AVC encoder used in video compression and streaming pipelines."),
    ("Video", "SVT-AV1", "compression", "https://gitlab.com/AOMediaCodec/SVT-AV1", "AV1 encoder implementation for high-performance video compression workflows."),
    ("Video", "GPAC", "image_audio_dsp", "https://github.com/gpac/gpac", "Multimedia framework for packaging, streaming, MP4, DASH, HLS, scene formats, and media inspection."),
    ("Photography", "libraw", "image_audio_dsp", "https://github.com/LibRaw/LibRaw", "RAW photo decoding library for camera formats, metadata, demosaicing, and image pipeline integration."),
    ("Photography", "RawTherapee", "visualization_gui", "https://github.com/Beep6581/RawTherapee", "RAW photo processing application for demosaicing, color, exposure, lens corrections, and exports."),
    ("Photography", "darktable", "visualization_gui", "https://github.com/darktable-org/darktable", "Photography workflow and RAW developer with non-destructive editing, color management, tethering, and exports."),
    ("Photography", "ExifTool", "utility_library", "https://exiftool.org/", "Metadata extraction and writing tool for images, camera RAW files, video, geotags, and asset management."),
    ("Photography", "OpenImageIO", "image_audio_dsp", "https://github.com/AcademySoftwareFoundation/OpenImageIO", "Image I/O library and command-line tools for photo/image formats, metadata, conversion, and inspection."),
    ("Photography", "dcraw", "image_audio_dsp", "https://www.dechifro.org/dcraw/", "Classic raw photo decoder and reference route for camera RAW conversion behavior."),
    ("Microscopy", "ImageJ", "image_audio_dsp", "https://imagej.net/software/imagej/", "Scientific image analysis platform for microscopy, plugins, macros, segmentation, measurement, and workflows."),
    ("Microscopy", "Fiji", "image_audio_dsp", "https://imagej.net/software/fiji/", "ImageJ distribution with bundled plugins for biological-image analysis and microscopy workflows."),
    ("Microscopy", "OME Bio-Formats", "interop_bindings", "https://github.com/ome/bioformats", "Microscopy image format library for reading proprietary and open biological imaging data formats."),
    ("Microscopy", "OME-NGFF", "serialization", "https://ngff.openmicroscopy.org/", "Next-generation file format specification for scalable bioimaging data in Zarr-backed layouts."),
    ("Microscopy", "napari", "visualization_gui", "https://github.com/napari/napari", "n-dimensional image viewer and plugin platform for microscopy, annotation, segmentation, and analysis."),
    ("Microscopy", "CellProfiler", "image_audio_dsp", "https://github.com/CellProfiler/CellProfiler", "Image analysis software for quantitative microscopy, segmentation, measurement, and pipeline automation."),
    ("Microscopy", "QuPath", "image_audio_dsp", "https://github.com/qupath/qupath", "Bioimage analysis application for pathology, whole-slide imaging, annotation, detection, and measurement."),
    ("Telescopes", "INDI Library", "interop_bindings", "https://github.com/indilib/indi", "Distributed control protocol and driver ecosystem for astronomical instruments, telescopes, cameras, focusers, and observatories."),
    ("Telescopes", "ASCOM Initiative", "interop_bindings", "https://ascom-standards.org/", "Astronomy device-control standards and driver ecosystem for telescopes, cameras, focusers, domes, and observatory automation."),
    ("Telescopes", "KStars", "visualization_gui", "https://invent.kde.org/education/kstars", "Desktop planetarium and observatory-control application with Ekos astrophotography and telescope automation workflows."),
    ("Telescopes", "Stellarium", "visualization_gui", "https://github.com/Stellarium/stellarium", "Planetarium and sky simulation software with telescope control plugins and astronomical catalogs."),
    ("Telescopes", "Astropy FITS", "serialization", "https://docs.astropy.org/en/stable/io/fits/", "FITS file handling route for astronomical image and table data used by observatory pipelines."),
    ("Telescopes", "SAOImage DS9", "visualization_gui", "https://sites.google.com/cfa.harvard.edu/saoimageds9", "Astronomical imaging and data visualization application for FITS inspection, regions, catalogs, and analysis."),
    ("Radars", "GNU Radio", "image_audio_dsp", "https://github.com/gnuradio/gnuradio", "Signal-processing toolkit for software-defined radio, radar experiments, communications, and RF prototyping."),
    ("Radars", "ESA SNAP", "image_audio_dsp", "https://step.esa.int/main/toolboxes/snap/", "Sentinel Application Platform for SAR, optical remote sensing, radar processing, and geospatial analysis."),
    ("Radars", "ISCE2", "math_numeric_scientific", "https://github.com/isce-framework/isce2", "InSAR Scientific Computing Environment for synthetic-aperture radar processing and geodesy workflows."),
    ("Radars", "Py-ART", "math_numeric_scientific", "https://github.com/ARM-DOE/pyart", "Python ARM Radar Toolkit for weather radar data, gridding, correction, visualization, and analysis."),
    ("Radars", "wradlib", "math_numeric_scientific", "https://github.com/wradlib/wradlib", "Weather radar data processing library for georeferencing, attenuation correction, compositing, and hydrology."),
    ("Radars", "sarpy", "math_numeric_scientific", "https://github.com/ngageoint/sarpy", "Python library for reading, writing, and processing synthetic-aperture radar data formats."),
    ("SatCom Satellites", "CCSDS", "language_specification", "https://public.ccsds.org/default.aspx", "Consultative Committee for Space Data Systems standards route for spacecraft communication, telemetry, telecommand, and data systems."),
    ("SatCom Satellites", "DVB-S2", "language_specification", "https://www.etsi.org/technologies/satellite", "ETSI satellite communication standards route including DVB-S/S2/S2X and related broadcast/data links."),
    ("SatCom Satellites", "GNU Radio Satellite Workflows", "image_audio_dsp", "https://github.com/gnuradio/gnuradio", "Software-defined radio toolkit used for satellite signal processing, demodulation, telemetry, and communication experiments."),
    ("SatCom Satellites", "SatNOGS Network", "registry_repository", "https://network.satnogs.org/", "Open ground-station network for satellite observations, scheduling, telemetry collection, and public dashboards."),
    ("SatCom Satellites", "SatNOGS Client", "networking_http", "https://gitlab.com/librespacefoundation/satnogs/satnogs-client", "Ground-station client software for satellite observation automation and data forwarding."),
    ("SatCom Satellites", "gr-satellites", "image_audio_dsp", "https://github.com/daniestevez/gr-satellites", "GNU Radio satellite decoder collection for telemetry, amateur satellites, and public signal workflows."),
    ("SatCom Satellites", "NASA TDRS", "documentation", "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/tdrs/", "NASA Tracking and Data Relay Satellite system route for public satellite communications context."),
    ("SatCom Satellites", "ESA Estrack", "documentation", "https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations", "ESA ground-station network route for mission communications and tracking support."),
    ("Electromagnetoscopes", "GNU Radio", "image_audio_dsp", "https://github.com/gnuradio/gnuradio", "Signal-processing toolkit for observing, decoding, and experimenting with radio-frequency and electromagnetic signals."),
    ("Electromagnetoscopes", "SoapySDR", "interop_bindings", "https://github.com/pothosware/SoapySDR", "Vendor-neutral SDR support library and module system for radio hardware access."),
    ("Electromagnetoscopes", "rtl-sdr", "embedded_hardware", "https://github.com/osmocom/rtl-sdr", "Software and drivers for RTL2832U-based software-defined radio receivers."),
    ("Electromagnetoscopes", "Gqrx", "visualization_gui", "https://github.com/gqrx-sdr/gqrx", "Software-defined radio receiver application for spectrum visualization, demodulation, recording, and hardware control."),
    ("Electromagnetoscopes", "SigDigger", "visualization_gui", "https://github.com/BatchDrake/SigDigger", "Digital signal analyzer for inspecting, demodulating, and visualizing radio-frequency captures."),
    ("Electromagnetoscopes", "SigMF", "serialization", "https://github.com/gnuradio/SigMF", "Signal Metadata Format for describing recorded signal datasets, captures, annotations, and RF metadata."),
    ("Electromagnetoscopes", "openEMS", "math_numeric_scientific", "https://github.com/thliebig/openEMS", "Electromagnetic field solver using FDTD for RF, microwave, antenna, and field simulation workflows."),
    ("Electromagnetoscopes", "Magpylib", "math_numeric_scientific", "https://github.com/magpylib/magpylib", "Python library for calculating magnetic fields of magnets, currents, and sensor arrangements."),
    ("Radio Garden Speciality", "Radio Garden Web App", "visualization_gui", "https://radio.garden/", "Official Radio Garden web application route for interactive globe-based live radio discovery."),
    ("Radio Garden Speciality", "Radio Garden Android Official App", "registry_repository", "https://play.google.com/store/apps/details?id=com.jonathanpuckey.radiogarden", "Official Android application route; useful as the canonical mobile target for emulator and wrapper testing, but not an open-source client."),
    ("Radio Garden Speciality", "Radio Garden iOS App Store", "registry_repository", "https://apps.apple.com/app/radio-garden-live/id1339670993", "Official iOS application route for Radio Garden mobile releases and store metadata."),
    ("Radio Garden Speciality", "radio-garden/react-native-audio-browser", "library", "https://github.com/radio-garden/react-native-audio-browser", "Official Radio Garden React Native audio module with browsable navigation trees and Android Auto/CarPlay-oriented integration."),
    ("Radio Garden Speciality", "chermenin/radio.G", "visualization_gui", "https://github.com/chermenin/radio.G", "Open MIT Electron desktop client for Radio Garden with a downloadable GitHub release route; candidate for macOS/Linux-style desktop packaging checks."),
    ("Radio Garden Speciality", "jonasrmichel/radio-garden-openapi", "api_doc_generator", "https://github.com/jonasrmichel/radio-garden-openapi", "Unofficial Apache-2.0 OpenAPI specification for the Radio Garden API and client generation workflows."),
    ("Radio Garden Speciality", "jonasrmichel/radio-garden-go", "cli", "https://github.com/jonasrmichel/radio-garden-go", "Apache-2.0 Go client and command-line application for the Radio Garden API; installable with Go tooling."),
    ("Radio Garden Speciality", "antoninadert/Radio-Garden-Client", "visualization_gui", "https://github.com/antoninadert/Radio-Garden-Client", "MIT Android WebView client route for Radio Garden; useful when testing APK-style wrapper paths."),
    ("Radio Garden Speciality", "BttrDrgn/radio.garten", "visualization_gui", "https://github.com/BttrDrgn/radio.garten", "MIT C++ desktop client and overlay route; cataloged as cautionary because its README reports it no longer works after a Radio Garden API update."),
    ("Radio Garden Speciality", "radio-garden-m3u", "serialization", "https://github.com/mcplayer9999/radio-garden-m3u", "M3U playlist generation route for Radio Garden station data; license metadata is missing and should be reviewed before reuse."),
    ("Radio Garden Speciality", "radio.garden-to-m3u", "serialization", "https://github.com/ovosimpatico/radio.garden-to-m3u", "AGPL-3.0 Python route for generating M3U playlists from Radio Garden API data; strong copyleft requires a backup plan for redistribution."),
    ("Radio Garden Speciality", "BlueStacks Radio Garden Route", "container_deployment", "https://www.bluestacks.com/apps/music-audio/radio-garden-on-pc.html", "Commercial Android-emulator route for running the official Radio Garden Android app on Windows/macOS; not open-source and not a FreeBSD solution."),
    ("Radio Garden Speciality", "Android-x86", "interpreter_runtime", "https://www.android-x86.org/", "Open Android port route that can be evaluated with virtualization for running Android applications where native desktop clients are unavailable."),
    ("Radio Garden Speciality", "QEMU", "interpreter_runtime", "https://www.qemu.org/", "Open machine emulator and virtualizer route for Android-x86 or other guest-based compatibility experiments across host operating systems."),
    ("Radio Garden Speciality", "Waydroid", "container_deployment", "https://github.com/waydroid/waydroid", "Container-based Android runtime route for Linux hosts; useful as a comparison point, but not a macOS or FreeBSD runtime by itself."),
    ("Repertoare Catalogs", "IMSLP", "registry_repository", "https://imslp.org/", "Public-domain music score library and repertoire catalog route for works, composers, editions, recordings, and metadata."),
    ("Repertoare Catalogs", "MusicBrainz", "registry_repository", "https://musicbrainz.org/", "Open music encyclopedia and metadata catalog for artists, releases, recordings, works, labels, and identifiers."),
    ("Repertoare Catalogs", "Wikidata", "registry_repository", "https://www.wikidata.org/", "Structured linked-data catalog used for repertoire entities, identifiers, relationships, provenance, and cross-domain references."),
    ("Repertoare Catalogs", "Library of Congress Catalog", "registry_repository", "https://catalog.loc.gov/", "Library catalog route for works, editions, subjects, names, authority data, and archival references."),
    ("Repertoare Catalogs", "WorldCat", "registry_repository", "https://search.worldcat.org/", "Global library catalog route for books, scores, recordings, archival holdings, and institution availability."),
    ("Repertoare Catalogs", "Open Library", "registry_repository", "https://openlibrary.org/", "Open bibliographic catalog for books, authors, editions, subjects, identifiers, and linked records."),
    ("Repertoare Catalogs", "Project Gutenberg", "registry_repository", "https://www.gutenberg.org/", "Public ebook catalog and corpus route for texts, metadata, formats, mirrors, and download workflows."),
    ("Repertoare Catalogs", "OpenAlex", "registry_repository", "https://openalex.org/", "Open scholarly catalog for works, authors, institutions, concepts, funders, venues, and citation graph metadata."),
    ("Catalogs", "Backstage Software Catalog", "registry_repository", "https://backstage.io/docs/features/software-catalog/", "Service and software catalog system for components, APIs, resources, owners, templates, and platform engineering metadata."),
    ("Catalogs", "CKAN", "registry_repository", "https://github.com/ckan/ckan", "Open-source data catalog platform for datasets, organizations, metadata, APIs, extensions, and portals."),
    ("Catalogs", "DataHub", "registry_repository", "https://github.com/datahub-project/datahub", "Metadata catalog and governance platform for datasets, schemas, lineage, ownership, search, and discovery."),
    ("Catalogs", "OpenMetadata", "registry_repository", "https://github.com/open-metadata/OpenMetadata", "Data catalog and metadata management platform for discovery, lineage, quality, governance, and collaboration."),
    ("Catalogs", "Schema.org", "language_specification", "https://schema.org/", "Structured-data vocabulary catalog for entities, properties, schemas, linked metadata, and search/discovery integration."),
    ("Catalogs", "SPDX License List", "registry_repository", "https://spdx.org/licenses/", "Machine-readable license catalog used for package metadata, SBOMs, compliance automation, and dependency review."),
    ("Catalogs", "OpenAPI Directory", "registry_repository", "https://github.com/APIs-guru/openapi-directory", "Public OpenAPI specification catalog for API discovery, examples, validation, and code generation."),
    ("Catalogs", "Libraries.io", "registry_repository", "https://libraries.io/", "Open-source package catalog route for dependency metadata, releases, package managers, repositories, and ecosystem search."),
    ("Catalogs", "Ecosyste.ms", "registry_repository", "https://ecosyste.ms/", "Open package/repository metadata indexes for dependency, license, security, and supply-chain analysis."),
    ("Catalogs", "OpenSSF Scorecard", "security_sast", "https://github.com/ossf/scorecard", "Repository security posture cataloging and scoring tool for supply-chain review."),
    ("Magazines", "ACM Queue", "community_reference", "https://queue.acm.org/", "Systems and software engineering magazine route for operations, infrastructure, programming, and architecture articles."),
    ("Magazines", "Communications of the ACM", "community_reference", "https://cacm.acm.org/", "ACM magazine route for computing research, practice, systems, programming, and technology context."),
    ("Magazines", "IEEE Software", "community_reference", "https://www.computer.org/csdl/magazine/so", "IEEE software engineering magazine route for architecture, process, systems, practice, and research articles."),
    ("Magazines", "USENIX ;login:", "community_reference", "https://www.usenix.org/publications/login", "USENIX magazine route for systems, security, operations, research practice, and engineering columns."),
    ("Magazines", "LWN.net", "community_reference", "https://lwn.net/", "Linux and open-source systems publication route for kernel, distributions, security, languages, and infrastructure coverage."),
    ("Magazines", "Phrack", "security_sast", "http://phrack.org/", "Long-running hacker zine and archive route for security research, systems internals, exploitation history, and underground computing culture."),
    ("Magazines", "2600 Magazine", "community_reference", "https://www.2600.com/", "Hacker quarterly route for security culture, telephony history, computing, privacy, and technical essays."),
    ("Magazines", "Linux Gazette", "community_reference", "https://linuxgazette.net/", "Linux magazine archive route for administration, scripting, programming, and Unix-like systems practice."),
    ("Magazines", "Dr. Dobb's Archive", "community_reference", "https://www.drdobbs.com/", "Historical programming magazine route for language, compiler, systems, algorithms, and software engineering articles."),
    ("Magazines", "Computer History Museum Publications", "community_reference", "https://computerhistory.org/publications/", "Computing history publication route for software, hardware, people, institutions, and archival context."),
    ("Hubs", "GitHub Explore", "registry_repository", "https://github.com/explore", "Developer hub for repository discovery, topics, trending projects, organizations, releases, packages, and open-source collaboration."),
    ("Hubs", "GitLab Explore", "registry_repository", "https://gitlab.com/explore", "Project hub for Git repositories, CI/CD, packages, issues, merge requests, groups, and public software discovery."),
    ("Hubs", "Hugging Face Hub", "registry_repository", "https://huggingface.co/docs/hub/index", "Model, dataset, and application hub for AI artifacts, hosted demos, versioning, inference, and collaboration."),
    ("Hubs", "Docker Hub", "registry_repository", "https://hub.docker.com/", "Container image hub for public/private images, tags, namespaces, automated builds, and deployment artifacts."),
    ("Hubs", "Artifact Hub", "registry_repository", "https://artifacthub.io/", "Cloud-native artifact hub for Helm charts, operators, OPA policies, Tekton tasks, containers, and Kubernetes packages."),
    ("Hubs", "npm", "registry_repository", "https://www.npmjs.com/", "JavaScript package hub for packages, versions, readmes, maintainers, security signals, and distribution metadata."),
    ("Hubs", "PyPI", "registry_repository", "https://pypi.org/", "Python package hub for distributions, releases, project metadata, maintainers, and install artifacts."),
    ("Hubs", "crates.io", "registry_repository", "https://crates.io/", "Rust package hub for crates, versions, owners, dependencies, downloads, and release metadata."),
    ("Hubs", "Maven Central", "registry_repository", "https://central.sonatype.com/", "Java/JVM artifact hub for Maven coordinates, versions, POM metadata, and dependency resolution."),
    ("Hubs", "NuGet", "registry_repository", "https://www.nuget.org/", ".NET package hub for packages, versions, frameworks, dependencies, licenses, and release metadata."),
    ("Hubs", "RapidAPI Hub", "registry_repository", "https://rapidapi.com/hub", "API marketplace and hub for discovering, subscribing to, testing, and integrating public API providers."),
    ("Hubs", "Backstage Developer Portal", "registry_repository", "https://backstage.io/", "Developer portal and software catalog hub for components, APIs, resources, templates, documentation, and ownership."),
    ("Hubs", "DataHub", "registry_repository", "https://github.com/datahub-project/datahub", "Metadata hub for datasets, schemas, lineage, owners, governance, search, and data discovery."),
    ("Hubs", "Open VSX Registry", "registry_repository", "https://open-vsx.org/", "Open extension hub for VS Code-compatible editors and development environments."),
    ("Hubs", "Open Build Service", "registry_repository", "https://openbuildservice.org/", "Package build and distribution hub for Linux distributions, repositories, architectures, and release pipelines."),
    ("Braces", "GNU Bash Brace Expansion", "language_specification", "https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html", "Official Bash brace expansion reference for generating strings before other shell expansions."),
    ("Braces", "POSIX Shell Command Language", "language_specification", "https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html", "POSIX shell language specification covering command syntax, expansions, grouping, and quoting rules."),
    ("Braces", "ECMAScript Language Specification", "language_specification", "https://tc39.es/ecma262/", "Official ECMAScript specification route for block syntax, object literals, lexical grammar, and brace-delimited forms."),
    ("Braces", "tree-sitter", "parser_lexer_ast", "https://tree-sitter.github.io/tree-sitter/", "Incremental parsing system used for brace-aware syntax trees, editor highlighting, navigation, and structural tooling."),
    ("Braces", "ANTLR grammars-v4", "parser_lexer_ast", "https://github.com/antlr/grammars-v4", "Large grammar corpus for language parsers, including brace-delimited programming languages and syntax fixtures."),
    ("Braces", "TextMate Grammars", "parser_lexer_ast", "https://macromates.com/manual/en/language_grammars", "TextMate language grammar format used by editors to tokenize braces, scopes, strings, and embedded languages."),
    ("Braces", "Prettier", "formatter", "https://prettier.io/", "Opinionated formatter that rewrites brace-delimited JavaScript, TypeScript, JSON, CSS, GraphQL, Markdown, and many plugin languages."),
    ("Braces", "clang-format", "formatter", "https://clang.llvm.org/docs/ClangFormat.html", "Formatter for C, C++, Java, JavaScript, Objective-C, Protobuf, and related brace-heavy languages."),
    ("Braces", "rustfmt", "formatter", "https://github.com/rust-lang/rustfmt", "Rust formatter for brace style, blocks, expressions, item layout, imports, and edition-aware formatting."),
    ("Braces", "EditorConfig", "configuration", "https://editorconfig.org/", "Cross-editor configuration format used with formatters and editors to keep indentation and brace-adjacent layout consistent."),
    ("Braces", "VS Code Bracket Pair Colorization", "ide_editor_integration", "https://code.visualstudio.com/blogs/2021/09/29/bracket-pair-colorization", "Visual Studio Code bracket-pair colorization route for brace matching and large-file editor behavior."),
    ("Braces", "CodeMirror Bracket Matching", "ide_editor_integration", "https://codemirror.net/docs/ref/#language.bracketMatching", "CodeMirror bracket matching extension route for editor parsing and brace-pair feedback."),
    ("Braces", "Monaco Editor", "ide_editor_integration", "https://microsoft.github.io/monaco-editor/", "Browser editor engine used by VS Code-derived tools with bracket matching, syntax services, and formatter integration."),
]

DATABASE_SYSTEM_RECORDS = [
    ("PostgreSQL", "database_datastore", "https://github.com/postgres/postgres", "Relational database system with SQL, extensions, replication, logical decoding, and operational tooling."),
    ("MySQL", "database_datastore", "https://github.com/mysql/mysql-server", "Relational database server and storage-engine ecosystem."),
    ("MariaDB", "database_datastore", "https://github.com/MariaDB/server", "Community-developed relational database server derived from MySQL."),
    ("SQLite", "database_datastore", "https://www.sqlite.org/", "Embedded SQL database engine used in applications, devices, browsers, and local-first storage."),
    ("DuckDB", "database_datastore", "https://github.com/duckdb/duckdb", "Embedded analytical SQL database for local OLAP and columnar data processing."),
    ("ClickHouse", "database_datastore", "https://github.com/ClickHouse/ClickHouse", "Column-oriented analytical database management system."),
    ("Apache Cassandra", "database_datastore", "https://github.com/apache/cassandra", "Distributed wide-column database for high-scale availability and partition-tolerant storage."),
    ("MongoDB", "database_datastore", "https://github.com/mongodb/mongo", "Document database and distributed storage platform."),
    ("Redis", "database_datastore", "https://github.com/redis/redis", "In-memory data structure server used for cache, streams, documents, vector search, and coordination."),
    ("Valkey", "database_datastore", "https://github.com/valkey-io/valkey", "Open-source in-memory key/value datastore derived from Redis."),
    ("KeyDB", "database_datastore", "https://github.com/Snapchat/KeyDB", "Multithreaded Redis-compatible database."),
    ("FoundationDB", "database_datastore", "https://github.com/apple/foundationdb", "Distributed transactional key-value store with layered data models."),
    ("CockroachDB", "database_datastore", "https://github.com/cockroachdb/cockroach", "Distributed SQL database with serializable transactions and horizontal scaling."),
    ("YugabyteDB", "database_datastore", "https://github.com/yugabyte/yugabyte-db", "Distributed SQL database with PostgreSQL-compatible API surface."),
    ("TiDB", "database_datastore", "https://github.com/pingcap/tidb", "Distributed SQL database with MySQL compatibility and HTAP design."),
    ("ScyllaDB", "database_datastore", "https://github.com/scylladb/scylladb", "High-performance Cassandra-compatible distributed database."),
    ("Neo4j", "database_datastore", "https://github.com/neo4j/neo4j", "Graph database system and Cypher query ecosystem."),
    ("ArangoDB", "database_datastore", "https://github.com/arangodb/arangodb", "Multi-model database for documents, graphs, and key/value data."),
    ("OrientDB", "database_datastore", "https://github.com/orientechnologies/orientdb", "Multi-model database with graph and document capabilities."),
    ("InfluxDB", "database_datastore", "https://github.com/influxdata/influxdb", "Time-series database and telemetry storage platform."),
    ("TimescaleDB", "database_datastore", "https://github.com/timescale/timescaledb", "PostgreSQL extension for time-series and analytical workloads."),
    ("Prometheus TSDB", "database_datastore", "https://github.com/prometheus/prometheus", "Time-series database embedded in the Prometheus monitoring system."),
    ("Apache Druid", "database_datastore", "https://github.com/apache/druid", "Real-time analytics database for event streams and OLAP workloads."),
    ("Apache Pinot", "database_datastore", "https://github.com/apache/pinot", "Realtime distributed OLAP datastore for user-facing analytics."),
    ("Elasticsearch", "database_datastore", "https://github.com/elastic/elasticsearch", "Distributed search, log, document, and analytics engine."),
    ("OpenSearch", "database_datastore", "https://github.com/opensearch-project/OpenSearch", "Search and analytics engine derived from Elasticsearch."),
    ("Solr", "database_datastore", "https://github.com/apache/solr", "Search platform built on Apache Lucene."),
    ("Meilisearch", "database_datastore", "https://github.com/meilisearch/meilisearch", "Search engine for full-text and hybrid search use cases."),
    ("Typesense", "database_datastore", "https://github.com/typesense/typesense", "Fast search engine for typo-tolerant application search."),
    ("Milvus", "database_datastore", "https://github.com/milvus-io/milvus", "Vector database for similarity search and AI retrieval workloads."),
    ("Qdrant", "database_datastore", "https://github.com/qdrant/qdrant", "Vector database and similarity search engine."),
    ("Weaviate", "database_datastore", "https://github.com/weaviate/weaviate", "Vector database with hybrid search and schema-aware object storage."),
    ("Chroma", "database_datastore", "https://github.com/chroma-core/chroma", "Embedding database for AI application retrieval."),
    ("LanceDB", "database_datastore", "https://github.com/lancedb/lancedb", "Vector database built around Lance columnar data format."),
    ("RocksDB", "database_datastore", "https://github.com/facebook/rocksdb", "Embeddable persistent key-value store and LSM storage engine."),
    ("LevelDB", "database_datastore", "https://github.com/google/leveldb", "Embedded key-value storage library."),
    ("LMDB", "database_datastore", "https://git.openldap.org/openldap/openldap", "Memory-mapped embedded key-value database engine."),
    ("Berkeley DB", "database_datastore", "https://www.oracle.com/database/technologies/related/berkeleydb.html", "Embedded key/value database family."),
    ("Apache HBase", "database_datastore", "https://github.com/apache/hbase", "Distributed wide-column database built on Hadoop storage."),
    ("Apache Accumulo", "database_datastore", "https://github.com/apache/accumulo", "Sorted distributed key/value store with cell-level security labels."),
    ("Bigtable", "database_datastore", "https://cloud.google.com/bigtable", "Managed wide-column database service."),
    ("DynamoDB", "database_datastore", "https://aws.amazon.com/dynamodb/", "Managed key-value and document database service."),
    ("Cosmos DB", "database_datastore", "https://azure.microsoft.com/products/cosmos-db", "Globally distributed multi-model managed database service."),
    ("Firestore", "database_datastore", "https://firebase.google.com/docs/firestore", "Serverless document database for web and mobile applications."),
    ("Supabase", "database_datastore", "https://github.com/supabase/supabase", "Postgres application platform with auth, storage, realtime, edge functions, and APIs."),
    ("Neon", "database_datastore", "https://neon.tech/", "Serverless Postgres platform with branching and scale-to-zero architecture."),
    ("Turso", "database_datastore", "https://turso.tech/", "SQLite-compatible database platform based on libSQL."),
    ("PlanetScale", "database_datastore", "https://planetscale.com/", "Managed Vitess/MySQL-compatible database platform."),
    ("Amazon Aurora", "database_datastore", "https://aws.amazon.com/rds/aurora/", "Managed MySQL/PostgreSQL-compatible relational database service."),
    ("Cloudflare D1", "database_datastore", "https://developers.cloudflare.com/d1/", "Serverless SQLite-compatible database for Cloudflare Workers."),
    ("Cloudflare R2", "database_datastore", "https://developers.cloudflare.com/r2/", "Object storage platform with S3-compatible operations."),
    ("Amazon S3", "database_datastore", "https://aws.amazon.com/s3/", "Object storage service used for binary, audio, video, archives, data lakes, and application assets."),
    ("MinIO", "database_datastore", "https://github.com/minio/minio", "S3-compatible object storage server."),
    ("Ceph", "database_datastore", "https://github.com/ceph/ceph", "Distributed object, block, and file storage platform."),
    ("Apache Arrow", "serialization", "https://github.com/apache/arrow", "Columnar memory format and cross-language data interchange system."),
    ("Apache Parquet", "serialization", "https://github.com/apache/parquet-format", "Columnar storage format for analytics data."),
    ("Apache ORC", "serialization", "https://github.com/apache/orc", "Columnar storage format for Hadoop and analytics systems."),
    ("Apache Avro", "serialization", "https://github.com/apache/avro", "Data serialization system with schemas and binary encoding."),
    ("CSV", "serialization", "https://www.rfc-editor.org/rfc/rfc4180", "Comma-separated values tabular interchange format."),
    ("JSON Lines", "serialization", "https://jsonlines.org/", "Line-delimited JSON records for logs, streaming, and batch interchange."),
    ("Apache Iceberg", "database_datastore", "https://github.com/apache/iceberg", "Open table format for large analytic datasets."),
    ("Delta Lake", "database_datastore", "https://github.com/delta-io/delta", "Open table format and transaction log for lakehouse storage."),
    ("Apache Hudi", "database_datastore", "https://github.com/apache/hudi", "Transactional data lake platform and table format."),
    ("ODBC", "database_datastore", "https://learn.microsoft.com/sql/odbc/reference/odbc-programmer-s-reference", "Open Database Connectivity API for database drivers and clients."),
    ("JDBC", "database_datastore", "https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/", "Java Database Connectivity API and driver contract."),
    ("ADO.NET", "database_datastore", "https://learn.microsoft.com/dotnet/framework/data/adonet/", ".NET data access provider model and database connectivity API."),
    ("libpq", "database_datastore", "https://www.postgresql.org/docs/current/libpq.html", "PostgreSQL C client library."),
    ("psycopg", "database_datastore", "https://github.com/psycopg/psycopg", "PostgreSQL adapter for Python."),
    ("SQLAlchemy", "database_datastore", "https://github.com/sqlalchemy/sqlalchemy", "Python SQL toolkit and ORM."),
    ("Prisma", "database_datastore", "https://github.com/prisma/prisma", "Database toolkit, ORM, schema language, and client generator."),
    ("Hibernate ORM", "database_datastore", "https://github.com/hibernate/hibernate-orm", "Java object/relational mapper and persistence framework."),
    ("Entity Framework Core", "database_datastore", "https://github.com/dotnet/efcore", ".NET object-database mapper and migration framework."),
    ("Diesel", "database_datastore", "https://github.com/diesel-rs/diesel", "Rust ORM and query builder."),
    ("GORM", "database_datastore", "https://github.com/go-gorm/gorm", "Go ORM library."),
    ("Active Record", "database_datastore", "https://github.com/rails/rails/tree/main/activerecord", "Ruby on Rails ORM and database migration layer."),
    ("Hasura", "database_datastore", "https://github.com/hasura/graphql-engine", "GraphQL and data API engine over databases."),
    ("PostgREST", "database_datastore", "https://github.com/PostgREST/postgrest", "REST API server generated from PostgreSQL schemas."),
    ("Debezium", "database_datastore", "https://github.com/debezium/debezium", "Change data capture platform for database logs."),
    ("Flyway", "database_datastore", "https://github.com/flyway/flyway", "Database migration and schema versioning tool."),
    ("Liquibase", "database_datastore", "https://github.com/liquibase/liquibase", "Database schema change and migration management tool."),
    ("pgAdmin", "database_datastore", "https://www.pgadmin.org/", "PostgreSQL administration and dashboard tool."),
    ("DBeaver", "database_datastore", "https://github.com/dbeaver/dbeaver", "Universal database client and SQL IDE."),
    ("Metabase", "database_datastore", "https://github.com/metabase/metabase", "Business intelligence, dashboard, and analytics layer over databases."),
    ("Apache Superset", "database_datastore", "https://github.com/apache/superset", "Data exploration and dashboard platform."),
    ("Grafana", "database_datastore", "https://github.com/grafana/grafana", "Dashboarding and observability UI with database and time-series data sources."),
    ("LibreOffice Base", "database_datastore", "https://www.libreoffice.org/discover/base/", "Desktop database front end and table/form/report manager."),
    ("LibreOffice Writer tables", "documentation", "https://help.libreoffice.org/latest/en-US/text/swriter/guide/table_insert.html", "Document table model and editing surface used for structured data in word-processing documents."),
]


@dataclasses.dataclass
class BuildStats:
    source_records: int = 0
    normalized_identities: int = 0
    expanded_records: int = 0
    release_checked: int = 0
    release_known: int = 0
    release_unknown: int = 0
    fetch_errors: int = 0


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._current_href: str | None = None
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attrs_dict = {k: v or "" for k, v in attrs}
        self._current_href = attrs_dict.get("href")
        self._parts = []

    def handle_data(self, data: str) -> None:
        if self._current_href is not None:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._current_href is not None:
            text = " ".join("".join(self._parts).split())
            self.links.append({"href": self._current_href, "text": text})
            self._current_href = None
            self._parts = []


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today_iso() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(
        f"{path.name}.{os.getpid()}.{threading.get_ident()}.{time.time_ns()}.tmp"
    )
    if path == ENRICHED_JSON:
        payload = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    else:
        payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content.rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        return
    path.write_text(normalized, encoding="utf-8")


def copy_source_if_needed(source: Path) -> None:
    if source.resolve() == LOCAL_SOURCE.resolve():
        return
    LOCAL_SOURCE.parent.mkdir(parents=True, exist_ok=True)
    if not LOCAL_SOURCE.exists() or LOCAL_SOURCE.read_bytes() != source.read_bytes():
        shutil.copyfile(source, LOCAL_SOURCE)


def default_source() -> Path:
    if LOCAL_SOURCE.exists():
        return LOCAL_SOURCE
    if ORIGINAL_SOURCE.exists():
        return ORIGINAL_SOURCE
    raise FileNotFoundError(
        f"No source catalog found. Expected {LOCAL_SOURCE} or {ORIGINAL_SOURCE}"
    )


def read_extension_payload() -> dict[str, Any]:
    if not LOCAL_EXTENSION.exists():
        return {"scope": [], "records": []}
    extension = read_json(LOCAL_EXTENSION)
    if not isinstance(extension.get("scope"), list):
        extension["scope"] = []
    if not isinstance(extension.get("records"), list):
        extension["records"] = []
    return extension


def merged_source_payload(source_path: Path) -> dict[str, Any]:
    source = read_json(source_path)
    extension = read_extension_payload()
    merged = dict(source)
    raw_scope = list(source.get("scope", [])) + list(extension.get("scope", []))
    merged_scope = []
    seen_scope = set()
    for item in raw_scope + LANGUAGE_ORDER:
        branch = normalize_branch(item)
        if branch in LANGUAGE_ORDER and branch not in seen_scope:
            seen_scope.add(branch)
            merged_scope.append(branch)
    merged["scope"] = merged_scope
    merged["records"] = list(source.get("records", [])) + list(extension.get("records", []))
    merged["taxonomy"] = source.get("taxonomy", TAXONOMY)
    statistics = dict(source.get("statistics", {}))
    current_target = int(statistics.get("target_control_unique_entities", 0) or 0)
    statistics["target_control_unique_entities"] = max(DEFAULT_TARGET_RECORDS, current_target)
    statistics["extension_records"] = len(extension.get("records", []))
    statistics["extension_languages"] = len(extension.get("scope", []))
    merged["statistics"] = statistics
    if extension.get("extension_id"):
        merged["extension_catalog"] = str(LOCAL_EXTENSION)
        merged["extension_catalog_id"] = extension.get("extension_id")
    return merged


def slugify(value: str, fallback: str = "record") -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or fallback


def stable_hash(value: str, length: int = 10) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:length]


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def plain_markdown_text(value: Any) -> str:
    text = clean_text(value)
    text = re.sub(r"!\[[^\]]*\]\([^)]*(?:\)|$)", " ", text)
    text = re.sub(r"\[[^\]]*\]\([^)]*(?:\)|$)", " ", text)
    text = re.sub(r"\[[^\]]*(?:https?|ht)[^\]]*$", " ", text)
    text = re.sub(r"\([^)]*(?:https?|ht)[^)]*(?:\)|$)", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = text.replace("[", "").replace("]", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def md_escape(value: Any) -> str:
    text = clean_text(value)
    text = text.replace("|", "\\|")
    return text


def label(value: str) -> str:
    return value.replace("_", " ").replace("/", " / ").title()


def normalize_branch(raw: Any) -> str:
    value = clean_text(raw)
    key = value.lower().replace("-", "_").replace(" ", "_")
    return BRANCH_ALIASES.get(value.lower(), BRANCH_ALIASES.get(key, value or "Unknown"))


def normalize_category(raw_type: str, record: dict[str, Any]) -> str:
    if raw_type in TAXONOMY and raw_type != "source_list_item":
        return raw_type
    return infer_category(record)


def infer_category(record: dict[str, Any]) -> str:
    fields = [
        record.get("record_type"),
        record.get("section"),
        record.get("subsection"),
        record.get("name"),
        record.get("description"),
        record.get("raw"),
        record.get("canonical_url"),
        record.get("url"),
    ]
    haystack = " ".join(clean_text(item).lower() for item in fields if item)
    for category, keywords in CATEGORY_KEYWORDS.items():
        for term in keywords:
            if term in haystack:
                return category
    return "other"


def identity_key(branch: str, name: str, category: str) -> str:
    norm_name = re.sub(r"[^a-z0-9]+", "", name.lower())
    return f"{branch.lower()}::{norm_name or name.lower()}::{category}"


def record_slug(record: dict[str, Any]) -> str:
    base = f"{record['catalog_branch']} {record['name']}"
    digest = stable_hash(record["identity_key"], 8)
    return f"{slugify(base)}-{digest}"


def is_http_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def canonical_url_from_record(record: dict[str, Any]) -> str:
    for key in ("canonical_url", "url"):
        value = clean_text(record.get(key))
        if is_http_url(value):
            return value
    return ""


def provenance_from_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    provenance = record.get("provenance")
    if isinstance(provenance, list) and provenance:
        return [item for item in provenance if isinstance(item, dict)]
    source = record.get("source")
    if isinstance(source, dict):
        return [{"kind": source.get("kind", "source"), "source": source}]
    return [{"kind": "catalog_source", "status": "preserved_seed"}]


def normalize_input_record(record: dict[str, Any]) -> dict[str, Any]:
    raw_type = clean_text(record.get("record_type")) or "other"
    branch = normalize_branch(record.get("catalog_branch"))
    name = clean_text(record.get("name")) or clean_text(record.get("id")) or "Unnamed"
    category = normalize_category(raw_type, record)
    canonical_url = canonical_url_from_record(record)
    source_name = "catalog_extension" if isinstance(record.get("source"), dict) and record["source"].get("kind") == "catalog_extension" else "master_json"
    normalized = {
        "id": clean_text(record.get("id")) or stable_hash(json.dumps(record, sort_keys=True)),
        "source": source_name,
        "source_record_type": raw_type,
        "catalog_branch": branch,
        "raw_catalog_branch": clean_text(record.get("catalog_branch")),
        "category": category,
        "name": name,
        "description": clean_text(record.get("description")),
        "canonical_url": canonical_url,
        "source_url": clean_text(record.get("url")),
        "section": clean_text(record.get("section")),
        "subsection": clean_text(record.get("subsection")),
        "verification_status": clean_text(record.get("verification_status")),
        "preserve": bool(record.get("preserve", True)),
        "provenance": provenance_from_record(record),
        "raw": record,
        "release": unknown_release("not_checked"),
        "nightly": unknown_release("not_checked"),
        "relationships": record.get("relationships") if isinstance(record.get("relationships"), list) else [],
        "capabilities": record.get("capabilities") if isinstance(record.get("capabilities"), list) else [],
    }
    normalized["identity_key"] = identity_key(branch, name, category)
    normalized["slug"] = record_slug(normalized)
    return normalized


def unknown_release(reason: str) -> dict[str, Any]:
    return {
        "status": "unknown",
        "version": "",
        "date": "",
        "channel": "",
        "source": "",
        "checked_at": "",
        "reason": reason,
    }


def known_release(
    *,
    version: str,
    date: str,
    source: str,
    channel: str = "stable",
    checked_at: str | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    status = "known" if (version and date) else "partial" if (version or date) else "unknown"
    payload: dict[str, Any] = {
        "status": status,
        "version": version or "",
        "date": date or "",
        "channel": channel,
        "source": source,
        "checked_at": checked_at or now_iso(),
        "reason": "" if status == "known" else "release_date_missing" if status == "partial" else "source_returned_no_release",
    }
    if extra:
        payload.update(extra)
    return payload


def merge_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for record in records:
        key = record["identity_key"]
        if key not in merged:
            merged[key] = dict(record)
            merged[key]["source_record_ids"] = [record["id"]]
            merged[key]["evidence"] = [record]
            continue
        target = merged[key]
        target["source_record_ids"].append(record["id"])
        target["evidence"].append(record)
        for field in ("description", "canonical_url", "source_url", "section", "subsection"):
            if not target.get(field) and record.get(field):
                target[field] = record[field]
        target["provenance"].extend(record.get("provenance", []))
        if target["release"]["status"] == "unknown" and record["release"]["status"] == "known":
            target["release"] = record["release"]
        if target["nightly"]["status"] == "unknown" and record["nightly"]["status"] == "known":
            target["nightly"] = record["nightly"]
    for record in merged.values():
        seen = set()
        unique_provenance = []
        for item in record.get("provenance", []):
            key = json.dumps(item, sort_keys=True, ensure_ascii=False)
            if key not in seen:
                seen.add(key)
                unique_provenance.append(item)
        record["provenance"] = unique_provenance
        record["slug"] = record_slug(record)
    return sorted(merged.values(), key=lambda item: (LANGUAGE_ORDER.index(item["catalog_branch"]) if item["catalog_branch"] in LANGUAGE_ORDER else 99, item["category"], item["name"].lower()))


def compact_evidence_item(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": clean_text(record.get("id")),
        "source": clean_text(record.get("source")),
        "source_record_type": clean_text(record.get("source_record_type")),
        "catalog_branch": clean_text(record.get("catalog_branch")),
        "category": clean_text(record.get("category")),
        "name": clean_text(record.get("name")),
        "canonical_url": clean_text(record.get("canonical_url")),
    }


def compact_raw_value(value: Any) -> Any:
    if not isinstance(value, dict):
        return value if len(clean_text(value)) <= 500 else clean_text(value)[:500]
    compact: dict[str, Any] = {}
    for key, nested in value.items():
        key_text = clean_text(key)
        if key_text in {
            "name",
            "id",
            "full_name",
            "description",
            "summary",
            "version",
            "date",
            "timestamp",
            "published",
            "published_at",
            "created_at",
            "updated_at",
            "license",
            "licenses",
            "licenseExpression",
            "license_expression",
            "homepage",
            "repository",
            "url",
            "html_url",
            "package_url",
            "Path",
            "Version",
            "Timestamp",
            "g",
            "a",
            "latestVersion",
            "p",
        }:
            if isinstance(nested, (dict, list)):
                compact[key_text] = json.loads(json.dumps(nested, ensure_ascii=False)) if len(clean_text(nested)) <= 1000 else clean_text(nested)[:1000]
            else:
                compact[key_text] = nested
    if compact:
        return compact
    return {"omitted": "raw evidence compacted for repository-size limits"}


def compact_record_for_storage(record: dict[str, Any]) -> dict[str, Any]:
    compact = dict(record)
    compact["license_evidence"] = record_license_values(record)
    compact["evidence"] = [compact_evidence_item(item) for item in record.get("evidence", []) if isinstance(item, dict)]
    compact["raw"] = compact_raw_value(record.get("raw", {}))
    return compact


def compact_payload_for_storage(payload: dict[str, Any]) -> dict[str, Any]:
    stored = dict(payload)
    stored["records"] = [compact_record_for_storage(record) for record in payload.get("records", [])]
    return stored


class HttpCache:
    # In-memory robots.txt cache: domain -> RobotFileParser
    _robots_cache: dict[str, RobotFileParser] = {}

    def __init__(
        self,
        cache_dir: Path,
        *,
        enabled: bool = True,
        ttl_seconds: int = 3600,
        timeout: int = DEFAULT_TIMEOUT,
        respect_robots: bool = True,
    ) -> None:
        self.cache_dir = cache_dir
        self.enabled = enabled
        self.ttl_seconds = ttl_seconds
        self.timeout = timeout
        self.respect_robots = respect_robots
        self.errors: list[str] = []
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        ROBOTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def _key(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def _paths(self, url: str) -> tuple[Path, Path]:
        digest = self._key(url)
        return self.cache_dir / f"{digest}.body", self.cache_dir / f"{digest}.json"

    def _get_robots_parser(self, netloc: str) -> RobotFileParser:
        """Fetch and parse robots.txt for a domain, with file-system caching."""
        if netloc in self._robots_cache:
            return self._robots_cache[netloc]
        rp = RobotFileParser()
        rp.set_url(f"https://{netloc}/robots.txt")
        # Check local cache first
        cache_path = ROBOTS_CACHE_DIR / f"{hashlib.sha256(netloc.encode()).hexdigest()}.txt"
        if cache_path.exists():
            try:
                content = cache_path.read_text(encoding="utf-8", errors="replace")
                rp.parse(content.splitlines())
                self._robots_cache[netloc] = rp
                return rp
            except Exception:
                pass
        # Fetch robots.txt
        try:
            data = urllib.request.urlopen(f"https://{netloc}/robots.txt", timeout=self.timeout)
            content = data.read().decode("utf-8", errors="replace")
            rp.parse(content.splitlines())
            cache_path.write_text(content, encoding="utf-8")
        except Exception as exc:
            # If robots.txt can't be fetched, assume allow all
            self.errors.append(f"robots.txt fetch failed for {netloc}: {exc}")
        self._robots_cache[netloc] = rp
        return rp

    def _is_allowed(self, url: str) -> bool:
        """Check if URL is allowed by robots.txt."""
        if not self.respect_robots:
            return True
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return True
        netloc = parsed.netloc
        rp = self._get_robots_parser(netloc)
        allowed = rp.can_fetch(CRAWLER_USER_AGENT, url)
        if not allowed:
            self.errors.append(f"robots.txt denied: {url}")
        return allowed


    def get_bytes(self, url: str, *, accept: str = "application/json") -> bytes | None:
        body_path, meta_path = self._paths(url)
        if self.enabled and self.ttl_seconds > 0 and body_path.exists() and meta_path.exists():
            try:
                meta = read_json(meta_path)
                fetched_at = float(meta.get("fetched_at", 0))
                if time.time() - fetched_at <= self.ttl_seconds:
                    body = body_path.read_bytes()
                    if body[:2] == b"\x1f\x8b":
                        try:
                            body = gzip.decompress(body)
                        except OSError:
                            pass
                    return body
            except Exception:
                pass
        if not self.enabled:
            self.errors.append(f"network disabled: {url}")
            return None
        if not self._is_allowed(url):
            return None
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": accept,
        }
        token = os.environ.get("GITHUB_TOKEN")
        if token and "api.github.com" in urllib.parse.urlparse(url).netloc:
            headers["Authorization"] = f"Bearer {token}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                body = response.read()
                content_encoding = response.headers.get("Content-Encoding", "")
            if "gzip" in content_encoding.lower() or body[:2] == b"\x1f\x8b":
                try:
                    body = gzip.decompress(body)
                except OSError:
                    pass
            if self.ttl_seconds > 0:
                body_path.write_bytes(body)
                write_json(meta_path, {"url": url, "fetched_at": time.time(), "fetched_at_iso": now_iso()})
            return body
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as exc:
            self.errors.append(f"{type(exc).__name__}: {url}: {exc}")
            return None

    def get_text(self, url: str, *, accept: str = "text/plain, text/html, */*") -> str:
        body = self.get_bytes(url, accept=accept)
        if not body:
            return ""
        try:
            return body.decode("utf-8")
        except UnicodeDecodeError:
            return body.decode("utf-8", errors="replace")

    def get_json(self, url: str) -> Any | None:
        body = self.get_bytes(url, accept="application/json, */*")
        if not body:
            return None
        try:
            return json.loads(body.decode("utf-8"))
        except json.JSONDecodeError as exc:
            self.errors.append(f"JSONDecodeError: {url}: {exc}")
            return None


def packageish_name(name: str, ecosystem: str) -> str:
    name = clean_text(name)
    if not name:
        return ""
    if ecosystem == "julia" and name.endswith(".jl"):
        name = name[:-3]
    if ecosystem in {"pypi", "crates", "cran", "hackage", "pub"}:
        if re.search(r"\s|/|\\|:", name):
            return ""
    if ecosystem == "npm":
        if re.search(r"\s|\\", name):
            return ""
    if ecosystem == "nuget":
        if re.search(r"\s|/|\\|:", name):
            return ""
    if ecosystem == "packagist":
        if re.search(r"\s|\\|:", name) or "/" not in name:
            return ""
        vendor, package = name.split("/", 1)
        if not vendor or not package or "/" in package:
            return ""
    if ecosystem == "cocoapods":
        if re.search(r"\s|/|\\|:", name):
            return ""
    if ecosystem == "go":
        if re.search(r"\s|\\|:", name) or "." not in name:
            return ""
    return name


def maven_coordinate(value: str) -> tuple[str, str]:
    coordinate = clean_text(value)
    if coordinate.count(":") != 1 or re.search(r"\s|/|\\", coordinate):
        return "", ""
    group, artifact = coordinate.split(":", 1)
    if not group or not artifact:
        return "", ""
    return group, artifact


def go_proxy_escape(module_path: str) -> str:
    escaped = []
    for char in module_path:
        if "A" <= char <= "Z":
            escaped.append("!" + char.lower())
        else:
            escaped.append(char)
    return urllib.parse.quote("".join(escaped), safe="/!.-_~")


def parse_github_repo(url: str) -> tuple[str, str] | None:
    if not url:
        return None
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) < 2:
        return None
    owner = parts[0]
    repo = parts[1]
    repo = re.sub(r"\.git$", "", repo)
    if not owner or not repo:
        return None
    return owner, repo


def github_release(fetcher: HttpCache, url: str) -> tuple[dict[str, Any], dict[str, Any]]:
    repo = parse_github_repo(url)
    if not repo:
        return unknown_release("not_a_github_repository"), unknown_release("not_a_github_repository")
    owner, name = repo
    latest_url = f"https://api.github.com/repos/{owner}/{name}/releases/latest"
    latest = fetcher.get_json(latest_url)
    stable = unknown_release("github_latest_release_missing")
    if isinstance(latest, dict) and latest.get("tag_name"):
        stable = known_release(
            version=clean_text(latest.get("tag_name")),
            date=clean_text(latest.get("published_at") or latest.get("created_at")),
            source=latest_url,
            channel="stable",
            extra={"release_url": latest.get("html_url", "")},
        )
    releases_url = f"https://api.github.com/repos/{owner}/{name}/releases?per_page=10"
    releases = fetcher.get_json(releases_url)
    nightly = unknown_release("github_prerelease_missing")
    if isinstance(releases, list):
        for release in releases:
            if release.get("prerelease"):
                nightly = known_release(
                    version=clean_text(release.get("tag_name")),
                    date=clean_text(release.get("published_at") or release.get("created_at")),
                    source=releases_url,
                    channel="preview",
                    extra={"release_url": release.get("html_url", "")},
                )
                break
    return stable, nightly


def pypi_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "pypi")
    if not package:
        return unknown_release("not_a_pypi_package_name"), unknown_release("not_a_pypi_package_name"), {}
    url = f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json"
    data = fetcher.get_json(url)
    if not isinstance(data, dict) or not isinstance(data.get("info"), dict):
        return unknown_release("pypi_metadata_missing"), unknown_release("pypi_metadata_missing"), {}
    info = data["info"]
    version = clean_text(info.get("version"))
    releases = data.get("releases") if isinstance(data.get("releases"), dict) else {}
    files = releases.get(version) or []
    release_date = ""
    if files:
        release_date = clean_text(files[-1].get("upload_time_iso_8601") or files[-1].get("upload_time"))
    nightly = unknown_release("pypi_has_no_standard_nightly_channel")
    for candidate in sorted(releases.keys(), reverse=True):
        lower = candidate.lower()
        if any(mark in lower for mark in ("a", "b", "rc", "dev")) and candidate != version:
            candidate_files = releases.get(candidate) or []
            candidate_date = ""
            if candidate_files:
                candidate_date = clean_text(candidate_files[-1].get("upload_time_iso_8601") or candidate_files[-1].get("upload_time"))
            nightly = known_release(
                version=candidate,
                date=candidate_date,
                source=url,
                channel="preview",
            )
            break
    extra = {
        "normalized_name": clean_text(info.get("name")) or package,
        "summary": clean_text(info.get("summary")),
        "license": clean_text(info.get("license")),
        "classifiers": info.get("classifiers") if isinstance(info.get("classifiers"), list) else [],
        "project_urls": info.get("project_urls") if isinstance(info.get("project_urls"), dict) else {},
        "home_page": clean_text(info.get("home_page")),
        "package_url": info.get("package_url", f"https://pypi.org/project/{package}/"),
    }
    return (
        known_release(version=version, date=release_date, source=url, channel="stable"),
        nightly,
        extra,
    )


def npm_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "npm")
    if not package:
        return unknown_release("not_an_npm_package_name"), unknown_release("not_an_npm_package_name"), {}
    encoded = urllib.parse.quote(package, safe="@")
    url = f"https://registry.npmjs.org/{encoded}"
    data = fetcher.get_json(url)
    if not isinstance(data, dict):
        return unknown_release("npm_metadata_missing"), unknown_release("npm_metadata_missing"), {}
    dist_tags = data.get("dist-tags") if isinstance(data.get("dist-tags"), dict) else {}
    times = data.get("time") if isinstance(data.get("time"), dict) else {}
    version = clean_text(dist_tags.get("latest"))
    stable = known_release(
        version=version,
        date=clean_text(times.get(version)),
        source=url,
        channel="stable",
    )
    nightly = unknown_release("npm_preview_tag_missing")
    for tag in ("nightly", "canary", "next", "beta", "rc", "alpha"):
        candidate = clean_text(dist_tags.get(tag))
        if candidate:
            nightly = known_release(
                version=candidate,
                date=clean_text(times.get(candidate)),
                source=url,
                channel=tag,
            )
            break
    latest_info = {}
    versions = data.get("versions")
    if isinstance(versions, dict) and version in versions and isinstance(versions[version], dict):
        latest_info = versions[version]
    repository = latest_info.get("repository") if isinstance(latest_info.get("repository"), dict) else {}
    links = {
        "npm": f"https://www.npmjs.com/package/{package}",
        "homepage": clean_text(latest_info.get("homepage")),
        "repository": clean_text(repository.get("url")),
    }
    extra = {
        "normalized_name": clean_text(data.get("name")) or package,
        "summary": clean_text(data.get("description")),
        "license": latest_info.get("license"),
        "package_url": links["npm"],
        "project_urls": {k: v for k, v in links.items() if v},
    }
    return stable, nightly, extra


def crates_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    crate = packageish_name(name, "crates")
    if not crate:
        return unknown_release("not_a_crate_name"), unknown_release("not_a_crate_name"), {}
    url = f"https://crates.io/api/v1/crates/{urllib.parse.quote(crate)}"
    data = fetcher.get_json(url)
    if not isinstance(data, dict) or not isinstance(data.get("crate"), dict):
        return unknown_release("crate_metadata_missing"), unknown_release("crate_metadata_missing"), {}
    crate_data = data["crate"]
    version = clean_text(crate_data.get("max_stable_version") or crate_data.get("max_version") or crate_data.get("newest_version"))
    stable = known_release(
        version=version,
        date=clean_text(crate_data.get("updated_at")),
        source=url,
        channel="stable",
    )
    nightly = unknown_release("crates_io_has_no_standard_nightly_channel")
    versions = data.get("versions")
    if isinstance(versions, list):
        for version_data in versions:
            candidate = clean_text(version_data.get("num"))
            lower = candidate.lower()
            if any(mark in lower for mark in ("alpha", "beta", "rc", "nightly", "dev")):
                nightly = known_release(
                    version=candidate,
                    date=clean_text(version_data.get("created_at") or version_data.get("updated_at")),
                    source=url,
                    channel="preview",
                )
                break
    extra = {
        "normalized_name": clean_text(crate_data.get("name")) or crate,
        "summary": clean_text(crate_data.get("description")),
        "license": clean_text(crate_data.get("license")),
        "package_url": f"https://crates.io/crates/{crate}",
        "project_urls": {
            "repository": clean_text(crate_data.get("repository")),
            "homepage": clean_text(crate_data.get("homepage")),
            "documentation": clean_text(crate_data.get("documentation")),
            "crates.io": f"https://crates.io/crates/{crate}",
        },
    }
    return stable, nightly, extra


def parse_julia_registry(fetcher: HttpCache) -> dict[str, dict[str, str]]:
    url = "https://raw.githubusercontent.com/JuliaRegistries/General/master/Registry.toml"
    text = fetcher.get_text(url)
    if not text:
        return {}
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        fetcher.errors.append(f"Julia registry TOML decode failed: {exc}")
        return {}
    packages = data.get("packages")
    if not isinstance(packages, dict):
        return {}
    result = {}
    for uuid, item in packages.items():
        if not isinstance(item, dict):
            continue
        name = clean_text(item.get("name"))
        path = clean_text(item.get("path"))
        if name and path:
            result[name.lower()] = {"uuid": uuid, "name": name, "path": path}
    return result


def julia_release(
    fetcher: HttpCache,
    name: str,
    registry: dict[str, dict[str, str]] | None = None,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "julia")
    if not package:
        return unknown_release("not_a_julia_package_name"), unknown_release("not_a_julia_package_name"), {}
    registry = registry if registry is not None else parse_julia_registry(fetcher)
    package_info = registry.get(package.lower())
    if not package_info:
        return unknown_release("julia_registry_entry_missing"), unknown_release("julia_registry_entry_missing"), {}
    path = package_info["path"]
    versions_url = f"https://raw.githubusercontent.com/JuliaRegistries/General/master/{path}/Versions.toml"
    text = fetcher.get_text(versions_url)
    version = ""
    if text:
        try:
            versions = tomllib.loads(text)
            version = sorted(versions.keys(), key=version_sort_key)[-1] if versions else ""
        except Exception as exc:
            fetcher.errors.append(f"Julia Versions.toml parse failed for {package}: {exc}")
    package_url = f"https://github.com/JuliaRegistries/General/tree/master/{path}"
    repo_url = ""
    package_toml = fetcher.get_text(f"https://raw.githubusercontent.com/JuliaRegistries/General/master/{path}/Package.toml")
    if package_toml:
        try:
            package_meta = tomllib.loads(package_toml)
            repo_url = clean_text(package_meta.get("repo"))
        except Exception:
            repo_url = ""
    stable = known_release(
        version=version,
        date="",
        source=versions_url,
        channel="stable",
        extra={"reason": "julia_registry_versions_do_not_include_release_dates"},
    )
    nightly = unknown_release("julia_registry_has_no_standard_nightly_channel")
    extra = {
        "normalized_name": package_info["name"],
        "summary": "",
        "package_url": package_url,
        "project_urls": {
            "registry": package_url,
            "repository": repo_url,
        },
        "julia_uuid": package_info["uuid"],
        "julia_registry_path": path,
    }
    return stable, nightly, extra


def strip_html(value: str) -> str:
    return clean_text(re.sub(r"<.*?>", " ", value, flags=re.DOTALL))


def parse_control_records(text: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    current: dict[str, str] = {}
    current_key = ""
    for raw_line in text.splitlines():
        if not raw_line.strip():
            if current:
                records.append(current)
            current = {}
            current_key = ""
            continue
        if raw_line[:1].isspace() and current_key:
            current[current_key] = clean_text(f"{current[current_key]} {raw_line.strip()}")
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        current_key = key.strip()
        current[current_key] = clean_text(value)
    if current:
        records.append(current)
    return records


def parse_cran_package_index(fetcher: HttpCache) -> dict[str, dict[str, str]]:
    url = "https://cran.r-project.org/src/contrib/PACKAGES"
    text = fetcher.get_text(url, accept="text/plain, */*")
    packages: dict[str, dict[str, str]] = {}
    for record in parse_control_records(text):
        name = clean_text(record.get("Package"))
        if name:
            packages[name.lower()] = record
    return packages


def parse_cran_available_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(
        r"<tr>\s*<td>\s*(?P<date>[^<]+?)\s*</td>\s*"
        r'<td>\s*<a href="(?P<href>[^"]+)">\s*(?:<span[^>]*>)?(?P<name>.*?)(?:</span>)?\s*</a>\s*</td>\s*'
        r"<td>\s*(?P<title>.*?)\s*</td>\s*</tr>",
        re.DOTALL,
    )
    for match in pattern.finditer(text):
        rows.append(
            {
                "date": clean_text(match.group("date")),
                "href": html.unescape(match.group("href")),
                "name": strip_html(match.group("name")),
                "title": strip_html(match.group("title")),
            }
        )
    return rows


def cran_release(
    fetcher: HttpCache,
    name: str,
    *,
    package_index: dict[str, dict[str, str]] | None = None,
    date_hint: str = "",
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "cran")
    if not package:
        return unknown_release("not_a_cran_package_name"), unknown_release("not_a_cran_package_name"), {}
    package_data = package_index.get(package.lower(), {}) if package_index is not None else {}
    description_url = f"https://cran.r-project.org/web/packages/{urllib.parse.quote(package)}/DESCRIPTION"
    if not package_data:
        text = fetcher.get_text(description_url, accept="text/plain, */*")
        records = parse_control_records(text)
        package_data = records[0] if records else {}
    version = clean_text(package_data.get("Version"))
    release_date = clean_text(package_data.get("Date/Publication") or package_data.get("Published") or date_hint)
    summary = clean_text(package_data.get("Title") or package_data.get("Description"))
    canonical = f"https://cran.r-project.org/web/packages/{urllib.parse.quote(package)}/index.html"
    extra = {
        "normalized_name": clean_text(package_data.get("Package")) or package,
        "summary": summary,
        "license": clean_text(package_data.get("License")),
        "package_url": canonical,
        "project_urls": {
            "CRAN": canonical,
            "DESCRIPTION": description_url,
            "repository": clean_text(package_data.get("URL")),
            "bug_reports": clean_text(package_data.get("BugReports")),
        },
    }
    return (
        known_release(version=version, date=release_date, source=description_url, channel="stable"),
        unknown_release("cran_has_no_standard_nightly_channel"),
        extra,
    )


def hackage_name_version(value: str) -> tuple[str, str]:
    clean = clean_text(value).strip("/")
    clean = clean.rsplit("/", 1)[-1]
    match = re.match(r"^(.+)-([0-9][0-9A-Za-z.+-]*)$", clean)
    if not match:
        return clean, ""
    return match.group(1), match.group(2)


def hackage_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "hackage")
    if not package:
        return unknown_release("not_a_hackage_package_name"), unknown_release("not_a_hackage_package_name"), {}
    url = f"https://hackage.haskell.org/package/{urllib.parse.quote(package)}"
    text = fetcher.get_text(url, accept="text/html, */*")
    if not text:
        return unknown_release("hackage_package_page_missing"), unknown_release("hackage_package_page_missing"), {}
    version = ""
    patterns = [
        rf"/package/{re.escape(package)}-([^/\"<]+?)/docs",
        rf"/package/{re.escape(package)}-([^/\"<]+?)/{re.escape(package)}\.cabal",
        rf"{re.escape(package)}-([^/\"<]+?)\.tar\.gz",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            version = clean_text(match.group(1))
            break
    uploaded = ""
    uploaded_match = re.search(
        r"<th>\s*Uploaded\s*</th>\s*<td>.*?<span title=\"[^\"]*\">\s*([^<]+)\s*</span>",
        text,
        re.DOTALL,
    )
    if uploaded_match:
        uploaded = clean_text(uploaded_match.group(1))
    synopsis = ""
    synopsis_match = re.search(r"<th>\s*Synopsis\s*</th>\s*<td[^>]*>\s*(.*?)\s*</td>", text, re.DOTALL)
    if synopsis_match:
        synopsis = strip_html(synopsis_match.group(1))
    candidate_match = re.search(rf'/package/{re.escape(package)}-([^/"<]+?)/candidate', text)
    nightly = unknown_release("hackage_has_no_standard_nightly_channel")
    if candidate_match:
        nightly = known_release(
            version=clean_text(candidate_match.group(1)),
            date="",
            source=url,
            channel="candidate",
            extra={"reason": "hackage_candidate_date_missing"},
        )
    extra = {
        "normalized_name": package,
        "summary": synopsis,
        "package_url": url,
        "project_urls": {"Hackage": url, "RSS": f"{url}.rss"},
    }
    return known_release(version=version, date=uploaded, source=url, channel="stable"), nightly, extra


def is_prerelease_version(version: str) -> bool:
    lower = version.lower()
    return "-" in version or any(mark in lower for mark in ("alpha", "beta", "rc", "preview", "nightly", "dev"))


def pub_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "pub")
    if not package:
        return unknown_release("not_a_pub_package_name"), unknown_release("not_a_pub_package_name"), {}
    url = f"https://pub.dev/api/packages/{urllib.parse.quote(package, safe='')}"
    data = fetcher.get_json(url)
    if not isinstance(data, dict):
        return unknown_release("pub_dev_metadata_missing"), unknown_release("pub_dev_metadata_missing"), {}
    latest = data.get("latest") if isinstance(data.get("latest"), dict) else {}
    pubspec = latest.get("pubspec") if isinstance(latest.get("pubspec"), dict) else {}
    version = clean_text(latest.get("version") or pubspec.get("version"))
    published = clean_text(latest.get("published"))
    nightly = unknown_release("pub_dev_has_no_standard_nightly_channel")
    versions = data.get("versions") if isinstance(data.get("versions"), list) else []
    preview_candidates = []
    for item in versions:
        candidate = clean_text(item.get("version")) if isinstance(item, dict) else ""
        if is_prerelease_version(candidate):
            preview_candidates.append((candidate, clean_text(item.get("published"))))
    if preview_candidates:
        preview_candidates.sort(key=lambda item: version_sort_key(item[0]))
        candidate, candidate_date = preview_candidates[-1]
        nightly = known_release(version=candidate, date=candidate_date, source=url, channel="preview")
    repository = clean_text(pubspec.get("repository"))
    homepage = clean_text(pubspec.get("homepage"))
    extra = {
        "normalized_name": clean_text(data.get("name")) or package,
        "summary": clean_text(pubspec.get("description")),
        "package_url": f"https://pub.dev/packages/{urllib.parse.quote(package, safe='')}",
        "project_urls": {
            "pub.dev": f"https://pub.dev/packages/{urllib.parse.quote(package, safe='')}",
            "repository": repository,
            "homepage": homepage,
        },
    }
    return known_release(version=version, date=published, source=url, channel="stable"), nightly, extra


def go_module_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    module = packageish_name(name, "go")
    if not module:
        return unknown_release("not_a_go_module_path"), unknown_release("not_a_go_module_path"), {}
    url = f"https://proxy.golang.org/{go_proxy_escape(module)}/@latest"
    data = fetcher.get_json(url)
    if not isinstance(data, dict):
        return unknown_release("go_proxy_latest_missing"), unknown_release("go_proxy_latest_missing"), {}
    version = clean_text(data.get("Version"))
    release_time = clean_text(data.get("Time"))
    project_url = ""
    parts = module.split("/")
    if len(parts) >= 3 and parts[0].lower() == "github.com":
        project_url = f"https://github.com/{parts[1]}/{parts[2]}"
    package_url = f"https://pkg.go.dev/{urllib.parse.quote(module, safe='/')}"
    extra = {
        "normalized_name": module,
        "summary": "Go module published through the public Go module proxy.",
        "package_url": package_url,
        "project_urls": {
            "pkg.go.dev": package_url,
            "repository": project_url,
            "Go proxy": url,
        },
        "go_module": module,
    }
    if is_prerelease_version(version):
        return (
            unknown_release("go_proxy_latest_is_preview_or_pseudoversion"),
            known_release(version=version, date=release_time, source=url, channel="module-preview"),
            extra,
        )
    return (
        known_release(version=version, date=release_time, source=url, channel="stable"),
        unknown_release("go_module_proxy_has_no_standard_nightly_channel"),
        extra,
    )


def nuget_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "nuget")
    if not package:
        return unknown_release("not_a_nuget_package_name"), unknown_release("not_a_nuget_package_name"), {}
    lower = package.lower()
    url = f"https://api.nuget.org/v3/registration5-gz-semver2/{urllib.parse.quote(lower, safe='')}/index.json"
    data = fetcher.get_json(url)
    if not isinstance(data, dict):
        return unknown_release("nuget_registration_missing"), unknown_release("nuget_registration_missing"), {}
    entries = []
    for page in data.get("items", []):
        if not isinstance(page, dict):
            continue
        page_items = page.get("items")
        if not isinstance(page_items, list) and page.get("@id"):
            page_data = fetcher.get_json(clean_text(page.get("@id")))
            page_items = page_data.get("items") if isinstance(page_data, dict) else []
        for item in page_items or []:
            catalog_entry = item.get("catalogEntry") if isinstance(item, dict) else None
            if isinstance(catalog_entry, dict):
                entries.append(catalog_entry)
    if not entries:
        return unknown_release("nuget_registration_has_no_versions"), unknown_release("nuget_registration_has_no_versions"), {}
    def usable(entry: dict[str, Any]) -> bool:
        published = clean_text(entry.get("published"))
        return bool(clean_text(entry.get("version"))) and not published.startswith("1900-01-01") and entry.get("listed", True) is not False

    stable_entries = [entry for entry in entries if usable(entry) and not is_prerelease_version(clean_text(entry.get("version")))]
    preview_entries = [entry for entry in entries if usable(entry) and is_prerelease_version(clean_text(entry.get("version")))]
    stable_entry = sorted(stable_entries, key=lambda entry: version_sort_key(clean_text(entry.get("version"))))[-1] if stable_entries else {}
    preview_entry = sorted(preview_entries, key=lambda entry: clean_text(entry.get("published")))[-1] if preview_entries else {}
    normalized = clean_text(stable_entry.get("id") or (entries[-1].get("id") if entries else "") or package)
    summary = clean_text(stable_entry.get("description") or (entries[-1].get("description") if entries else ""))
    package_url = f"https://www.nuget.org/packages/{urllib.parse.quote(normalized, safe='')}"
    stable = known_release(
        version=clean_text(stable_entry.get("version")),
        date=clean_text(stable_entry.get("published")),
        source=url,
        channel="stable",
    )
    nightly = unknown_release("nuget_preview_version_missing")
    if preview_entry:
        nightly = known_release(
            version=clean_text(preview_entry.get("version")),
            date=clean_text(preview_entry.get("published")),
            source=url,
            channel="preview",
        )
    extra = {
        "normalized_name": normalized,
        "summary": summary,
        "license": clean_text(stable_entry.get("licenseExpression") or (entries[-1].get("licenseExpression") if entries else "")),
        "license_url": clean_text(stable_entry.get("licenseUrl") or (entries[-1].get("licenseUrl") if entries else "")),
        "package_url": package_url,
        "project_urls": {
            "NuGet": package_url,
            "project": clean_text(stable_entry.get("projectUrl") or (entries[-1].get("projectUrl") if entries else "")),
            "repository": clean_text(stable_entry.get("repository") or (entries[-1].get("repository") if entries else "")),
        },
    }
    return stable, nightly, extra


def packagist_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "packagist")
    if not package:
        return unknown_release("not_a_packagist_package_name"), unknown_release("not_a_packagist_package_name"), {}
    url = f"https://repo.packagist.org/p2/{urllib.parse.quote(package, safe='/')}.json"
    data = fetcher.get_json(url)
    packages = data.get("packages") if isinstance(data, dict) else {}
    entries = packages.get(package) if isinstance(packages, dict) else None
    if not isinstance(entries, list):
        lower_lookup = package.lower()
        for key, value in packages.items() if isinstance(packages, dict) else []:
            if clean_text(key).lower() == lower_lookup and isinstance(value, list):
                entries = value
                break
    if not isinstance(entries, list) or not entries:
        return unknown_release("packagist_package_metadata_missing"), unknown_release("packagist_package_metadata_missing"), {}

    def usable(entry: dict[str, Any]) -> bool:
        version = clean_text(entry.get("version"))
        return bool(version) and not version.lower().startswith("dev-")

    def sort_key(entry: dict[str, Any]) -> tuple[Any, ...]:
        return (
            clean_text(entry.get("published-time") or entry.get("time")),
            version_sort_key(clean_text(entry.get("version"))),
        )

    stable_entries = [
        entry
        for entry in entries
        if isinstance(entry, dict) and usable(entry) and not is_prerelease_version(clean_text(entry.get("version")))
    ]
    preview_entries = [
        entry
        for entry in entries
        if isinstance(entry, dict) and usable(entry) and is_prerelease_version(clean_text(entry.get("version")))
    ]
    stable_entry = sorted(stable_entries, key=sort_key)[-1] if stable_entries else {}
    preview_entry = sorted(preview_entries, key=sort_key)[-1] if preview_entries else {}
    metadata_entry = stable_entry or (entries[0] if isinstance(entries[0], dict) else {})
    normalized = clean_text(metadata_entry.get("name")) or package
    package_url = f"https://packagist.org/packages/{urllib.parse.quote(normalized, safe='/')}"
    source_meta = metadata_entry.get("source") if isinstance(metadata_entry.get("source"), dict) else {}
    support = metadata_entry.get("support") if isinstance(metadata_entry.get("support"), dict) else {}
    stable = known_release(
        version=clean_text(stable_entry.get("version")),
        date=clean_text(stable_entry.get("published-time") or stable_entry.get("time")),
        source=url,
        channel="stable",
    )
    nightly = unknown_release("packagist_preview_version_missing")
    if preview_entry:
        nightly = known_release(
            version=clean_text(preview_entry.get("version")),
            date=clean_text(preview_entry.get("published-time") or preview_entry.get("time")),
            source=url,
            channel="preview",
        )
    extra = {
        "normalized_name": normalized,
        "summary": clean_text(metadata_entry.get("description")),
        "license": metadata_entry.get("license") if isinstance(metadata_entry.get("license"), list) else clean_text(metadata_entry.get("license")),
        "package_url": package_url,
        "project_urls": {
            "Packagist": package_url,
            "repository": clean_text(source_meta.get("url")),
            "homepage": clean_text(metadata_entry.get("homepage")),
            "issues": clean_text(support.get("issues")),
            "docs": clean_text(support.get("docs")),
        },
    }
    return stable, nightly, extra


def maven_release(fetcher: HttpCache, coordinate: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    group, artifact = maven_coordinate(coordinate)
    if not group:
        return unknown_release("not_a_maven_coordinate"), unknown_release("not_a_maven_coordinate"), {}
    query = f'g:"{group}" AND a:"{artifact}"'
    url = f"https://search.maven.org/solrsearch/select?q={urllib.parse.quote(query)}&rows=1&wt=json"
    data = fetcher.get_json(url)
    response = data.get("response") if isinstance(data, dict) else {}
    docs = response.get("docs") if isinstance(response, dict) else []
    if not isinstance(docs, list) or not docs:
        return unknown_release("maven_central_metadata_missing"), unknown_release("maven_central_metadata_missing"), {}
    doc = docs[0] if isinstance(docs[0], dict) else {}
    version = clean_text(doc.get("latestVersion"))
    timestamp = doc.get("timestamp")
    date = ""
    if isinstance(timestamp, (int, float)):
        date = datetime.fromtimestamp(timestamp / 1000, timezone.utc).replace(microsecond=0).isoformat()
    canonical = f"https://central.sonatype.com/artifact/{urllib.parse.quote(group, safe='.')}/{urllib.parse.quote(artifact, safe='')}"
    stable = known_release(version=version, date=date, source=url, channel="stable")
    nightly = unknown_release("maven_central_search_has_no_standard_nightly_channel")
    extra = {
        "normalized_name": f"{clean_text(doc.get('g')) or group}:{clean_text(doc.get('a')) or artifact}",
        "summary": f"Maven Central artifact with packaging `{clean_text(doc.get('p')) or 'unknown'}`.",
        "package_url": canonical,
        "project_urls": {"Maven Central": canonical},
        "maven_packaging": clean_text(doc.get("p")),
    }
    return stable, nightly, extra


def cocoapods_release(fetcher: HttpCache, name: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    pod = packageish_name(name, "cocoapods")
    if not pod:
        return unknown_release("not_a_cocoapods_name"), unknown_release("not_a_cocoapods_name"), {}
    url = f"https://trunk.cocoapods.org/api/v1/pods/{urllib.parse.quote(pod, safe='')}"
    data = fetcher.get_json(url)
    if not isinstance(data, dict):
        return unknown_release("cocoapods_metadata_missing"), unknown_release("cocoapods_metadata_missing"), {}
    versions = data.get("versions") if isinstance(data.get("versions"), list) else []

    def version_entry_version(entry: dict[str, Any]) -> str:
        return clean_text(entry.get("name") or entry.get("version"))

    def sort_key(entry: dict[str, Any]) -> tuple[Any, ...]:
        return (clean_text(entry.get("created_at")), version_sort_key(version_entry_version(entry)))

    stable_entries = [
        entry
        for entry in versions
        if isinstance(entry, dict) and version_entry_version(entry) and not is_prerelease_version(version_entry_version(entry))
    ]
    preview_entries = [
        entry
        for entry in versions
        if isinstance(entry, dict) and version_entry_version(entry) and is_prerelease_version(version_entry_version(entry))
    ]
    stable_entry = sorted(stable_entries, key=sort_key)[-1] if stable_entries else {}
    preview_entry = sorted(preview_entries, key=sort_key)[-1] if preview_entries else {}
    source_meta = data.get("source") if isinstance(data.get("source"), dict) else {}
    package_url = f"https://cocoapods.org/pods/{urllib.parse.quote(pod, safe='')}"
    stable = known_release(
        version=version_entry_version(stable_entry),
        date=clean_text(stable_entry.get("created_at")),
        source=url,
        channel="stable",
    )
    nightly = unknown_release("cocoapods_preview_version_missing")
    if preview_entry:
        nightly = known_release(
            version=version_entry_version(preview_entry),
            date=clean_text(preview_entry.get("created_at")),
            source=url,
            channel="preview",
        )
    extra = {
        "normalized_name": clean_text(data.get("name")) or pod,
        "summary": clean_text(data.get("summary") or data.get("description")),
        "license": data.get("license"),
        "package_url": package_url,
        "project_urls": {
            "CocoaPods": package_url,
            "homepage": clean_text(data.get("homepage")),
            "repository": clean_text(source_meta.get("git") or source_meta.get("http")),
            "documentation": clean_text(data.get("documentation_url")),
        },
    }
    return stable, nightly, extra


def octave_release(fetcher: HttpCache, name: str, canonical_url: str = "") -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    package = packageish_name(name, "pub")
    if not package:
        return unknown_release("not_an_octave_package_name"), unknown_release("not_an_octave_package_name"), {}
    url = canonical_url if canonical_url.startswith("https://gnu-octave.github.io/packages/") else f"https://gnu-octave.github.io/packages/{urllib.parse.quote(slugify(package))}/"
    text = fetcher.get_text(url, accept="text/html, */*")
    if not text:
        return unknown_release("octave_package_page_missing"), unknown_release("octave_package_page_missing"), {}
    version = ""
    date = ""
    match = re.search(r"<h3[^>]*>\s*[^<]+?\s*</h3>\s*<b>\s*([^&<]+)&nbsp;\(([^)]+)\)</b>", text, re.DOTALL)
    if match:
        version = clean_text(match.group(1))
        date = clean_text(match.group(2))
    if not version:
        match = re.search(r"Package Version:</td>\s*<td>([^<]+)</td>.*?(\d{4}-\d{2}-\d{2})", text, re.DOTALL)
        if match:
            version = clean_text(match.group(1))
            date = clean_text(match.group(2))
    description = ""
    meta_match = re.search(r'<meta property="og:description" content="([^"]+)"', text)
    if meta_match:
        description = html.unescape(meta_match.group(1))
    extra = {
        "normalized_name": package,
        "summary": clean_text(description),
        "package_url": url,
        "project_urls": {"GNU Octave package": url},
    }
    return (
        known_release(version=version, date=date, source=url, channel="stable"),
        unknown_release("octave_packages_have_no_standard_nightly_channel"),
        extra,
    )


def version_sort_key(value: str) -> tuple[Any, ...]:
    parts: list[Any] = []
    for part in re.split(r"([0-9]+)", value):
        if part.isdigit():
            parts.append(int(part))
        else:
            parts.append(part)
    return tuple(parts)


def enrich_one(
    record: dict[str, Any],
    fetcher: HttpCache,
    *,
    julia_registry: dict[str, dict[str, str]] | None = None,
) -> dict[str, Any]:
    branch = record["catalog_branch"]
    enriched = dict(record)
    stable = unknown_release("no_matching_release_source")
    nightly = unknown_release("no_matching_release_source")
    extra: dict[str, Any] = {}
    url = record.get("canonical_url") or record.get("source_url") or ""
    if parse_github_repo(url) and "github.com/JuliaRegistries/General/tree/master/" not in url:
        stable, nightly = github_release(fetcher, url)
    if stable["status"] == "unknown":
        if branch == "Python":
            stable, nightly, extra = pypi_release(fetcher, record["name"])
        elif branch in {"Node.js/JavaScript", "Node.js/TypeScript"}:
            stable, nightly, extra = npm_release(fetcher, record["name"])
        elif branch == "Rust":
            stable, nightly, extra = crates_release(fetcher, record["name"])
        elif branch == "Julia":
            stable, nightly, extra = julia_release(fetcher, record["name"], julia_registry)
        elif branch == "R":
            stable, nightly, extra = cran_release(fetcher, record["name"])
        elif branch == "Haskell":
            stable, nightly, extra = hackage_release(fetcher, record["name"])
        elif branch == "Dart":
            stable, nightly, extra = pub_release(fetcher, record["name"])
        elif branch == "Go":
            stable, nightly, extra = go_module_release(fetcher, record["name"])
        elif branch == "C-Sharp":
            stable, nightly, extra = nuget_release(fetcher, record["name"])
        elif branch == "PHP":
            stable, nightly, extra = packagist_release(fetcher, record["name"])
        elif branch == "SAPJava":
            stable, nightly, extra = maven_release(fetcher, record["name"])
        elif branch == "Cocoa":
            stable, nightly, extra = cocoapods_release(fetcher, record["name"])
        elif branch == "Octave":
            stable, nightly, extra = octave_release(fetcher, record["name"], url)
    if extra:
        if not enriched.get("description") and extra.get("summary"):
            enriched["description"] = extra["summary"]
        if not enriched.get("canonical_url"):
            enriched["canonical_url"] = extra.get("package_url") or ""
        enriched["release_source_metadata"] = extra
    stable["checked_at"] = stable.get("checked_at") or now_iso()
    nightly["checked_at"] = nightly.get("checked_at") or now_iso()
    enriched["release"] = stable
    enriched["nightly"] = nightly
    return enriched


def expansion_record(
    *,
    source: str,
    branch: str,
    name: str,
    category: str,
    description: str = "",
    canonical_url: str = "",
    source_url: str = "",
    release: dict[str, Any] | None = None,
    nightly: dict[str, Any] | None = None,
    provenance: list[dict[str, Any]] | None = None,
    raw: dict[str, Any] | None = None,
) -> dict[str, Any]:
    base = {
        "id": f"{source}-{stable_hash(branch + name + category, 14)}",
        "source": source,
        "source_record_type": "registry_expansion",
        "catalog_branch": normalize_branch(branch),
        "raw_catalog_branch": branch,
        "category": category if category in TAXONOMY else "other",
        "name": clean_text(name),
        "description": clean_text(description),
        "canonical_url": clean_text(canonical_url),
        "source_url": clean_text(source_url),
        "section": "",
        "subsection": "",
        "verification_status": "registry-derived",
        "preserve": True,
        "provenance": provenance
        or [
            {
                "kind": source,
                "status": "registry-derived",
                "retrieved": today_iso(),
            }
        ],
        "raw": raw or {},
        "release": release or unknown_release("not_checked"),
        "nightly": nightly or unknown_release("not_checked"),
        "relationships": [],
        "capabilities": [],
    }
    base["identity_key"] = identity_key(base["catalog_branch"], base["name"], base["category"])
    base["slug"] = record_slug(base)
    return base


def infer_category_from_text(name: str, description: str, fallback: str = "library") -> str:
    pseudo = {
        "record_type": fallback,
        "name": name,
        "description": description,
        "section": "",
        "subsection": "",
        "raw": "",
    }
    category = infer_category(pseudo)
    return category if category != "other" else fallback


def expand_crates(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    per_page = 100
    pages = max(1, (limit + per_page - 1) // per_page)
    for page in range(1, pages + 1):
        if len(records) >= limit:
            break
        url = f"https://crates.io/api/v1/crates?page={page}&per_page={per_page}&sort=downloads"
        data = fetcher.get_json(url)
        if not isinstance(data, dict) or not isinstance(data.get("crates"), list):
            break
        for crate in data["crates"]:
            if len(records) >= limit:
                break
            name = clean_text(crate.get("name"))
            if not name:
                continue
            description = clean_text(crate.get("description"))
            category_text = " ".join(
                [
                    description,
                    " ".join(crate.get("keywords") or []),
                    " ".join(crate.get("categories") or []),
                ]
            )
            category = infer_category_from_text(name, category_text, "library")
            package_url = f"https://crates.io/crates/{urllib.parse.quote(name)}"
            records.append(
                expansion_record(
                    source="crates_io",
                    branch="Rust",
                    name=name,
                    category=category,
                    description=description,
                    canonical_url=package_url,
                    source_url=url,
                    release=known_release(
                        version=clean_text(crate.get("max_stable_version") or crate.get("max_version") or crate.get("newest_version")),
                        date=clean_text(crate.get("updated_at")),
                        source=url,
                        channel="stable",
                    ),
                    nightly=unknown_release("crates_io_has_no_standard_nightly_channel"),
                    raw=crate,
                )
            )
    return records


def expand_npm(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen = set()
    per_query = 250
    for term in NPM_QUERY_TERMS:
        if len(records) >= limit:
            break
        query = urllib.parse.quote(term)
        url = f"https://registry.npmjs.org/-/v1/search?text={query}&size={per_query}&quality=0.35&popularity=0.45&maintenance=0.20"
        data = fetcher.get_json(url)
        if not isinstance(data, dict) or not isinstance(data.get("objects"), list):
            continue
        for item in data["objects"]:
            if len(records) >= limit:
                break
            package = item.get("package") if isinstance(item, dict) else None
            if not isinstance(package, dict):
                continue
            name = clean_text(package.get("name"))
            if not name or name.lower() in seen:
                continue
            seen.add(name.lower())
            description = clean_text(package.get("description"))
            links = package.get("links") if isinstance(package.get("links"), dict) else {}
            canonical = clean_text(links.get("npm")) or f"https://www.npmjs.com/package/{urllib.parse.quote(name)}"
            repository = clean_text(links.get("repository"))
            branch = "Node.js/TypeScript" if looks_typescript(name, description) else "Node.js/JavaScript"
            category = infer_category_from_text(name, description + " " + term, "library")
            records.append(
                expansion_record(
                    source="npm_registry",
                    branch=branch,
                    name=name,
                    category=category,
                    description=description,
                    canonical_url=canonical,
                    source_url=url,
                    release=known_release(
                        version=clean_text(package.get("version")),
                        date=clean_text(package.get("date")),
                        source=url,
                        channel="stable",
                    ),
                    nightly=unknown_release("npm_search_does_not_include_dist_tags"),
                    raw={"package": package, "score": item.get("score")},
                    provenance=[
                        {
                            "kind": "npm_registry_search",
                            "status": "registry-derived",
                            "retrieved": today_iso(),
                            "query": term,
                        }
                    ],
                )
            )
            if repository and repository != canonical:
                records[-1]["release_source_metadata"] = {"project_urls": {"repository": repository, "npm": canonical}}
    return records


def looks_typescript(name: str, description: str) -> bool:
    haystack = f"{name} {description}".lower()
    return (
        "typescript" in haystack
        or name.startswith("@types/")
        or name.startswith("ts-")
        or name.endswith("-ts")
        or " type definitions" in haystack
    )


def expand_julia(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    registry = parse_julia_registry(fetcher)
    records: list[dict[str, Any]] = []
    for info in sorted(registry.values(), key=lambda item: item["name"].lower()):
        if len(records) >= limit:
            break
        name = info["name"]
        category = infer_category_from_text(name, name, "library")
        package_url = f"https://github.com/JuliaRegistries/General/tree/master/{info['path']}"
        records.append(
            expansion_record(
                source="julia_general",
                branch="Julia",
                name=name,
                category=category,
                description=f"Julia package registered in General at {info['path']}.",
                canonical_url=package_url,
                source_url="https://github.com/JuliaRegistries/General",
                release=unknown_release("julia_expansion_does_not_fetch_versions_by_default"),
                nightly=unknown_release("julia_registry_has_no_standard_nightly_channel"),
                raw=info,
                provenance=[
                    {
                        "kind": "julia_general_registry",
                        "status": "registry-derived",
                        "retrieved": today_iso(),
                        "registry_path": info["path"],
                    }
                ],
            )
        )
    return records


def expand_luarocks(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen = set()
    page = 1
    while len(records) < limit and page <= 140:
        url = f"https://luarocks.org/m/root?page={page}"
        text = fetcher.get_text(url, accept="text/html, */*")
        if not text:
            break
        rows = parse_luarocks_rows(text)
        if not rows:
            break
        for row in rows:
            if len(records) >= limit:
                break
            name = row["name"]
            key = name.lower()
            if not name or key in seen:
                continue
            seen.add(key)
            description = row["summary"]
            category = infer_category_from_text(name, description, "library")
            module_url = urllib.parse.urljoin("https://luarocks.org", row["href"])
            records.append(
                expansion_record(
                    source="luarocks_root_manifest",
                    branch="Lua family",
                    name=name,
                    category=category,
                    description=description,
                    canonical_url=module_url,
                    source_url=url,
                    release=unknown_release("luarocks_manifest_page_does_not_include_version_date"),
                    nightly=unknown_release("luarocks_has_no_standard_nightly_channel"),
                    raw=row,
                    provenance=[
                        {
                            "kind": "luarocks_root_manifest",
                            "status": "registry-derived",
                            "retrieved": today_iso(),
                            "page": page,
                        }
                    ],
                )
            )
        page += 1
    if len(records) < limit:
        records.extend(expand_luarocks_search(fetcher, limit - len(records), seen))
    return records[:limit]


def parse_luarocks_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(
        r'<li class="module_row">.*?<a href="(?P<href>/modules/[^"]+)" class="title">(?P<name>.*?)</a>.*?<div class="summary">(?P<summary>.*?)</div>',
        re.DOTALL,
    )
    for match in pattern.finditer(text):
        rows.append(
            {
                "href": html.unescape(re.sub(r"<.*?>", "", match.group("href"))),
                "name": clean_text(re.sub(r"<.*?>", "", match.group("name"))),
                "summary": clean_text(re.sub(r"<.*?>", "", match.group("summary"))),
            }
        )
    return rows


def expand_luarocks_search(fetcher: HttpCache, limit: int, seen: set[str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for term in LUAROCKS_QUERY_TERMS:
        if len(records) >= limit:
            break
        url = f"https://luarocks.org/search?q={urllib.parse.quote(term)}"
        text = fetcher.get_text(url, accept="text/html, */*")
        if not text:
            continue
        for row in parse_luarocks_rows(text):
            if len(records) >= limit:
                break
            key = row["name"].lower()
            if key in seen:
                continue
            seen.add(key)
            module_url = urllib.parse.urljoin("https://luarocks.org", row["href"])
            records.append(
                expansion_record(
                    source="luarocks_search",
                    branch="Lua family",
                    name=row["name"],
                    category=infer_category_from_text(row["name"], row["summary"], "library"),
                    description=row["summary"],
                    canonical_url=module_url,
                    source_url=url,
                    release=unknown_release("luarocks_search_page_does_not_include_version_date"),
                    nightly=unknown_release("luarocks_has_no_standard_nightly_channel"),
                    raw=row,
                    provenance=[
                        {
                            "kind": "luarocks_search",
                            "status": "registry-derived",
                            "retrieved": today_iso(),
                            "query": term,
                        }
                    ],
                )
            )
    return records


def expand_pypi(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    text = fetcher.get_text("https://pypi.org/simple/", accept="text/html, */*")
    if not text:
        return []
    extractor = LinkExtractor()
    extractor.feed(text)
    candidates = []
    terms = tuple(PYPI_QUERY_TERMS)
    for link in extractor.links:
        name = clean_text(link.get("text"))
        lower = name.lower()
        if len(candidates) >= limit * 5:
            break
        if not name or len(name) > 80:
            continue
        if any(term in lower for term in terms) and re.search(r"[a-z]", lower):
            candidates.append(name)
    def build_record(name: str) -> dict[str, Any] | None:
        stable, nightly, extra = pypi_release(fetcher, name)
        if stable["status"] == "unknown":
            return None
        normalized = extra.get("normalized_name", name)
        description = extra.get("summary", "")
        category = infer_category_from_text(normalized, description, "library")
        return expansion_record(
            source="pypi_simple",
            branch="Python",
            name=normalized,
            category=category,
            description=description,
            canonical_url=extra.get("package_url", f"https://pypi.org/project/{normalized}/"),
            source_url="https://pypi.org/simple/",
            release=stable,
            nightly=nightly,
            raw={"name": name, "metadata": extra},
            provenance=[
                {
                    "kind": "pypi_simple_and_json_api",
                    "status": "registry-derived",
                    "retrieved": today_iso(),
                }
            ],
        )

    records: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        futures = [pool.submit(build_record, name) for name in candidates[:limit]]
        for future in concurrent.futures.as_completed(futures):
            try:
                record = future.result()
            except Exception as exc:
                fetcher.errors.append(f"PyPI expansion failed: {exc}")
                continue
            if record is not None:
                records.append(record)
    return sorted(records, key=lambda record: record["name"].lower())


def expand_awesome_lists(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    sources = [
        ("Python", "https://raw.githubusercontent.com/vinta/awesome-python/master/README.md"),
        ("Rust", "https://raw.githubusercontent.com/rust-unofficial/awesome-rust/main/README.md"),
        ("C++23", "https://raw.githubusercontent.com/fffaraz/awesome-cpp/master/README.md"),
        ("Node.js/JavaScript", "https://raw.githubusercontent.com/sindresorhus/awesome-nodejs/main/readme.md"),
        ("R", "https://raw.githubusercontent.com/qinwf/awesome-R/master/README.md"),
        ("Haskell", "https://raw.githubusercontent.com/krispo/awesome-haskell/master/README.md"),
        ("Matlab", "https://raw.githubusercontent.com/mikecroucher/awesome-MATLAB/master/README.md"),
        ("Matlab", "https://raw.githubusercontent.com/uhub/awesome-matlab/master/README.md"),
        ("C-Sharp", "https://raw.githubusercontent.com/uhub/awesome-c-sharp/master/README.md"),
        ("C-Sharp", "https://raw.githubusercontent.com/quozd/awesome-dotnet/master/README.md"),
        ("Dart", "https://raw.githubusercontent.com/yissachar/awesome-dart/master/README.md"),
        ("Go", "https://raw.githubusercontent.com/avelino/awesome-go/main/README.md"),
        ("Pattern language", "https://raw.githubusercontent.com/DovAmir/awesome-design-patterns/master/README.md"),
        ("Pattern language", "https://raw.githubusercontent.com/faif/python-patterns/master/README.md"),
        ("Pattern language", "https://raw.githubusercontent.com/iluwatar/java-design-patterns/master/README.md"),
        ("PHP", "https://raw.githubusercontent.com/ziadoz/awesome-php/master/README.md"),
        ("WebAssembly", "https://raw.githubusercontent.com/mbasso/awesome-wasm/master/README.md"),
        ("Swift", "https://raw.githubusercontent.com/matteocrippa/awesome-swift/master/README.md"),
        ("Cocoa", "https://raw.githubusercontent.com/vsouza/awesome-ios/master/README.md"),
        ("Databases", "https://raw.githubusercontent.com/dhamaniasad/awesome-postgres/master/README.md"),
        ("Databases", "https://raw.githubusercontent.com/numetriclabz/awesome-db/master/README.md"),
        ("Databases", "https://raw.githubusercontent.com/pingcap/awesome-database-learning/master/README.md"),
    ]
    records: list[dict[str, Any]] = []
    per_source = max(25, (limit + len(sources) - 1) // len(sources)) if sources else limit
    for branch, url in sources:
        text = fetcher.get_text(url, accept="text/markdown, text/plain, */*")
        if not text:
            continue
        records.extend(parse_awesome_markdown(branch, url, text, per_source))
    return balanced_trim_expansions(records, limit)


def parse_awesome_markdown(branch: str, url: str, text: str, limit: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    heading = ""
    link_pattern = re.compile(r"^\s*[-*]\s+\[([^\]]+)\]\(([^)]+)\)\s*-?\s*(.*)$")
    for line in text.splitlines():
        if len(records) >= limit:
            break
        if line.startswith("#"):
            heading = line.strip("# ").strip()
            continue
        match = link_pattern.match(line)
        if not match:
            continue
        name, href, desc = match.groups()
        if href.startswith("#") or href.startswith("mailto:"):
            continue
        absolute = urllib.parse.urljoin(url, href)
        category = infer_category_from_text(name, f"{heading} {desc}", "library")
        records.append(
            expansion_record(
                source="awesome_list",
                branch=branch,
                name=name,
                category=category,
                description=desc,
                canonical_url=absolute,
                source_url=url,
                release=unknown_release("awesome_list_does_not_include_release_date"),
                nightly=unknown_release("awesome_list_does_not_include_nightly_channel"),
                raw={"heading": heading, "line": line},
                provenance=[
                    {
                        "kind": "community_reference_markdown",
                        "status": "curated-list-derived",
                        "retrieved": today_iso(),
                        "source_url": url,
                        "section": heading,
                    }
                ],
            )
        )
    return records


def expand_cran(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    source_url = "https://cran.r-project.org/web/packages/available_packages_by_date.html"
    text = fetcher.get_text(source_url, accept="text/html, */*")
    if not text:
        return []
    package_index = parse_cran_package_index(fetcher)
    records: list[dict[str, Any]] = []
    seen = set()
    for row in parse_cran_available_rows(text):
        if len(records) >= limit:
            break
        name = row["name"]
        key = name.lower()
        if not name or key in seen:
            continue
        seen.add(key)
        stable, nightly, extra = cran_release(
            fetcher,
            name,
            package_index=package_index,
            date_hint=row["date"],
        )
        description = row["title"] or extra.get("summary", "")
        records.append(
            expansion_record(
                source="cran_packages_by_date",
                branch="R",
                name=extra.get("normalized_name", name),
                category=infer_category_from_text(name, description, "library"),
                description=description,
                canonical_url=extra.get("package_url", f"https://cran.r-project.org/web/packages/{urllib.parse.quote(name)}/index.html"),
                source_url=source_url,
                release=stable,
                nightly=nightly,
                raw={"cran_by_date": row, "package_metadata": package_index.get(key, {})},
                provenance=[
                    {
                        "kind": "cran_available_packages_by_date",
                        "status": "registry-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    return records


def parse_hackage_recent_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for block_match in re.finditer(r"<tr\b.*?</tr\s*>", text, re.DOTALL):
        block = block_match.group(0)
        date_match = re.search(r"<span title=\"[^\"]*\"\s*>\s*([^<]+)\s*</span", block, re.DOTALL)
        link_match = re.search(r'<a href="/package/([^"]+)"[^>]*>\s*([^<]+)\s*</a', block, re.DOTALL)
        cells = re.findall(r"<td[^>]*>\s*(.*?)\s*</td", block, re.DOTALL)
        if not date_match or not link_match:
            continue
        date = date_match.group(1)
        href, label_text = link_match.groups()
        uploader = strip_html(cells[1]) if len(cells) > 1 else ""
        package, version = hackage_name_version(href)
        if not version:
            package, version = hackage_name_version(label_text)
        rows.append(
            {
                "date": clean_text(date),
                "uploader": clean_text(uploader),
                "name": package,
                "version": version,
                "href": f"/package/{href}",
            }
        )
    return rows


def parse_hackage_top_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(
        r'<tr class="(?:odd|even)"><td><a href="/package/([^"/]+)">([^<]+)</a></td><td>(\d+)</td></tr>'
    )
    for href, name, downloads in pattern.findall(text):
        rows.append({"name": clean_text(name), "href": f"/package/{href}", "downloads": clean_text(downloads)})
    return rows


def expand_hackage(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    seen = set()
    recent_url = "https://hackage.haskell.org/packages/recent"
    recent_text = fetcher.get_text(recent_url, accept="text/html, */*")
    for row in parse_hackage_recent_rows(recent_text):
        if len(records) >= limit:
            break
        name = row["name"]
        key = name.lower()
        if not name or key in seen:
            continue
        seen.add(key)
        package_url = f"https://hackage.haskell.org/package/{urllib.parse.quote(name)}"
        records.append(
            expansion_record(
                source="hackage_recent",
                branch="Haskell",
                name=name,
                category=infer_category_from_text(name, name, "library"),
                description=f"Hackage package recently uploaded by {row.get('uploader') or 'unknown uploader'}.",
                canonical_url=package_url,
                source_url=recent_url,
                release=known_release(version=row["version"], date=row["date"], source=recent_url, channel="stable"),
                nightly=unknown_release("hackage_has_no_standard_nightly_channel"),
                raw=row,
                provenance=[
                    {
                        "kind": "hackage_recent_uploads",
                        "status": "registry-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    top_url = "https://hackage.haskell.org/packages/top"
    top_text = fetcher.get_text(top_url, accept="text/html, */*")
    for row in parse_hackage_top_rows(top_text):
        if len(records) >= limit:
            break
        name = row["name"]
        key = name.lower()
        if not name or key in seen:
            continue
        seen.add(key)
        package_url = f"https://hackage.haskell.org/package/{urllib.parse.quote(name)}"
        records.append(
            expansion_record(
                source="hackage_top_downloads",
                branch="Haskell",
                name=name,
                category=infer_category_from_text(name, name, "library"),
                description=f"Hackage package with {row.get('downloads', 'unknown')} recent downloads in the Hackage top-downloads listing.",
                canonical_url=package_url,
                source_url=top_url,
                release=unknown_release("hackage_top_downloads_page_does_not_include_release_date"),
                nightly=unknown_release("hackage_has_no_standard_nightly_channel"),
                raw=row,
                provenance=[
                    {
                        "kind": "hackage_top_downloads",
                        "status": "registry-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    return records


def expand_pub_dev(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    seen = set()
    candidates: list[tuple[str, str, str]] = []
    completion_url = "https://pub.dev/api/package-name-completion-data"
    data = fetcher.get_json(completion_url)
    names = data.get("packages", []) if isinstance(data, dict) and isinstance(data.get("packages"), list) else []
    for name in names:
        if len(candidates) >= limit:
            break
        package = clean_text(name)
        if not package or package.lower() in seen:
            continue
        seen.add(package.lower())
        candidates.append((package, completion_url, "completion"))
    for term in DART_QUERY_TERMS:
        if len(candidates) >= limit:
            break
        page = 1
        while len(candidates) < limit and page <= 10:
            url = f"https://pub.dev/api/search?q={urllib.parse.quote(term)}&page={page}"
            result = fetcher.get_json(url)
            if not isinstance(result, dict) or not isinstance(result.get("packages"), list):
                break
            page_packages = result["packages"]
            if not page_packages:
                break
            for item in page_packages:
                package = clean_text(item.get("package") if isinstance(item, dict) else item)
                if not package or package.lower() in seen:
                    continue
                seen.add(package.lower())
                candidates.append((package, url, term))
                if len(candidates) >= limit:
                    break
            if not result.get("next"):
                break
            page += 1

    def build_record(candidate: tuple[str, str, str]) -> dict[str, Any] | None:
        package, source_url, term = candidate
        stable, nightly, extra = pub_release(fetcher, package)
        if stable["status"] == "unknown":
            return None
        description = extra.get("summary", "")
        provenance = {
            "kind": "pub_dev_completion_and_package_api" if term == "completion" else "pub_dev_search_and_package_api",
            "status": "registry-derived",
            "retrieved": today_iso(),
        }
        if term != "completion":
            provenance["query"] = term
        return expansion_record(
            source="pub_dev",
            branch="Dart",
            name=extra.get("normalized_name", package),
            category=infer_category_from_text(package, f"{description} {term}", "library"),
            description=description,
            canonical_url=extra.get("package_url", f"https://pub.dev/packages/{urllib.parse.quote(package, safe='')}"),
            source_url=source_url,
            release=stable,
            nightly=nightly,
            raw={"name": package, "metadata": extra},
            provenance=[provenance],
        )

    records: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        futures = [pool.submit(build_record, candidate) for candidate in candidates[:limit]]
        for future in concurrent.futures.as_completed(futures):
            try:
                record = future.result()
            except Exception as exc:
                fetcher.errors.append(f"pub.dev expansion failed: {exc}")
                continue
            if record is not None:
                records.append(record)
    return sorted(records, key=lambda record: record["name"].lower())


def go_module_repository_url(module: str) -> str:
    parts = module.split("/")
    if len(parts) >= 3 and parts[0].lower() == "github.com":
        return f"https://github.com/{parts[1]}/{parts[2]}"
    if len(parts) >= 3 and parts[0].lower() == "gitlab.com":
        return f"https://gitlab.com/{parts[1]}/{parts[2]}"
    if len(parts) >= 3 and parts[0].lower() == "bitbucket.org":
        return f"https://bitbucket.org/{parts[1]}/{parts[2]}"
    return ""


def go_module_expansion_record(
    *,
    module: str,
    version: str,
    timestamp: str,
    source_url: str,
    raw: dict[str, Any],
) -> dict[str, Any]:
    package_url = f"https://pkg.go.dev/{urllib.parse.quote(module, safe='/')}"
    repository = go_module_repository_url(module)
    release = known_release(version=version, date=timestamp, source=source_url, channel="stable")
    nightly = unknown_release("go_module_index_has_no_standard_nightly_channel")
    if is_prerelease_version(version):
        release = unknown_release("go_module_index_event_is_preview_or_pseudoversion")
        nightly = known_release(version=version, date=timestamp, source=source_url, channel="module-preview")
    metadata = {
        "project_urls": {
            "pkg.go.dev": package_url,
            "repository": repository,
            "Go module index": source_url,
        },
        "go_module": module,
    }
    return expansion_record(
        source="go_module_index",
        branch="Go",
        name=module,
        category=infer_category_from_text(module, module, "library"),
        description="Go module observed in the public Go module index with timestamped version metadata.",
        canonical_url=package_url,
        source_url=source_url,
        release=release,
        nightly=nightly,
        raw={"module_index": raw, "metadata": metadata},
        provenance=[
            {
                "kind": "go_module_index",
                "status": "registry-derived",
                "retrieved": today_iso(),
            }
        ],
    )


def expand_go_modules(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    latest_by_module: dict[str, dict[str, Any]] = {}
    for module in GO_MODULE_SEEDS:
        stable, nightly, extra = go_module_release(fetcher, module)
        if stable["status"] == "unknown" and nightly["status"] == "unknown":
            continue
        version = stable.get("version") or nightly.get("version") or ""
        timestamp = stable.get("date") or nightly.get("date") or ""
        latest_by_module[module.lower()] = {
            "Path": module,
            "Version": version,
            "Timestamp": timestamp,
            "SourceURL": extra.get("project_urls", {}).get("Go proxy", ""),
        }

    since = (datetime.now(timezone.utc) - timedelta(days=2)).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    page_limit = 2000
    for _ in range(5):
        if len(latest_by_module) >= limit * 2:
            break
        url = f"https://index.golang.org/index?since={urllib.parse.quote(since)}&limit={page_limit}"
        text = fetcher.get_text(url, accept="application/json, text/plain, */*")
        if not text:
            break
        rows: list[dict[str, Any]] = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(item, dict):
                continue
            module = clean_text(item.get("Path"))
            version = clean_text(item.get("Version"))
            timestamp = clean_text(item.get("Timestamp"))
            if not packageish_name(module, "go") or not version:
                continue
            item["SourceURL"] = url
            rows.append(item)
            key = module.lower()
            old = latest_by_module.get(key)
            if not old or clean_text(old.get("Timestamp")) <= timestamp:
                latest_by_module[key] = item
        if not rows:
            break
        last_timestamp = clean_text(rows[-1].get("Timestamp"))
        if not last_timestamp or last_timestamp == since:
            break
        since = last_timestamp

    records = []
    for item in sorted(latest_by_module.values(), key=lambda row: clean_text(row.get("Timestamp")), reverse=True):
        if len(records) >= limit:
            break
        module = clean_text(item.get("Path"))
        records.append(
            go_module_expansion_record(
                module=module,
                version=clean_text(item.get("Version")),
                timestamp=clean_text(item.get("Timestamp")),
                source_url=clean_text(item.get("SourceURL")) or "https://index.golang.org/index",
                raw=item,
            )
        )
    return records


def expand_nuget(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    seen = set()
    per_query = 100
    for term in NUGET_QUERY_TERMS:
        if len(records) >= limit:
            break
        url = f"https://azuresearch-usnc.nuget.org/query?q={urllib.parse.quote(term)}&take={per_query}&prerelease=true"
        data = fetcher.get_json(url)
        if not isinstance(data, dict) or not isinstance(data.get("data"), list):
            continue
        for package in data["data"]:
            if len(records) >= limit:
                break
            if not isinstance(package, dict):
                continue
            name = clean_text(package.get("id"))
            if not name or name.lower() in seen:
                continue
            seen.add(name.lower())
            versions = package.get("versions") if isinstance(package.get("versions"), list) else []
            stable_versions = [
                clean_text(item.get("version"))
                for item in versions
                if isinstance(item, dict) and not is_prerelease_version(clean_text(item.get("version")))
            ]
            preview_versions = [
                clean_text(item.get("version"))
                for item in versions
                if isinstance(item, dict) and is_prerelease_version(clean_text(item.get("version")))
            ]
            stable_version = sorted(stable_versions, key=version_sort_key)[-1] if stable_versions else clean_text(package.get("version"))
            preview_version = sorted(preview_versions, key=version_sort_key)[-1] if preview_versions else ""
            stable = known_release(
                version=stable_version,
                date="",
                source=url,
                channel="stable",
                extra={"reason": "nuget_search_result_does_not_include_release_date"},
            )
            nightly = (
                known_release(
                    version=preview_version,
                    date="",
                    source=url,
                    channel="preview",
                    extra={"reason": "nuget_search_result_does_not_include_release_date"},
                )
                if preview_version
                else unknown_release("nuget_search_preview_version_missing")
            )
            description = clean_text(package.get("description"))
            normalized = clean_text(package.get("id")) or name
            package_url = f"https://www.nuget.org/packages/{urllib.parse.quote(normalized, safe='')}"
            records.append(
                expansion_record(
                    source="nuget_search",
                    branch="C-Sharp",
                    name=normalized,
                    category=infer_category_from_text(name, f"{description} {' '.join(package.get('tags') or [])} {term}", "library"),
                    description=description,
                    canonical_url=package_url,
                    source_url=url,
                    release=stable,
                    nightly=nightly,
                    raw={"search_result": package},
                    provenance=[
                        {
                                "kind": "nuget_search_api",
                            "status": "registry-derived",
                            "retrieved": today_iso(),
                            "query": term,
                        }
                    ],
                )
            )
    return records


def expand_packagist(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    seen = set()
    candidates: list[tuple[str, str, str, dict[str, Any]]] = []
    per_query = 100
    for term in PACKAGIST_QUERY_TERMS:
        if len(candidates) >= limit * 2:
            break
        url = f"https://packagist.org/search.json?q={urllib.parse.quote(term)}&per_page={per_query}"
        data = fetcher.get_json(url)
        results = data.get("results") if isinstance(data, dict) else []
        if not isinstance(results, list):
            continue
        for item in results:
            if not isinstance(item, dict):
                continue
            name = clean_text(item.get("name"))
            key = name.lower()
            if not packageish_name(name, "packagist") or key in seen:
                continue
            seen.add(key)
            candidates.append((name, url, term, item))
            if len(candidates) >= limit * 2:
                break

    def build_record(candidate: tuple[str, str, str, dict[str, Any]]) -> dict[str, Any] | None:
        name, source_url, term, search_result = candidate
        stable, nightly, extra = packagist_release(fetcher, name)
        description = extra.get("summary") or clean_text(search_result.get("description"))
        normalized = extra.get("normalized_name", name)
        if stable["status"] == "unknown" and nightly["status"] == "unknown" and not description:
            return None
        return expansion_record(
            source="packagist_search",
            branch="PHP",
            name=normalized,
            category=infer_category_from_text(normalized, f"{description} {term}", "library"),
            description=description,
            canonical_url=extra.get("package_url", f"https://packagist.org/packages/{urllib.parse.quote(normalized, safe='/')}"),
            source_url=source_url,
            release=stable,
            nightly=nightly,
            raw={"search_result": search_result, "metadata": extra},
            provenance=[
                {
                    "kind": "packagist_search_and_p2_api",
                    "status": "registry-derived",
                    "retrieved": today_iso(),
                    "query": term,
                }
            ],
        )

    records: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        futures = [pool.submit(build_record, candidate) for candidate in candidates[:limit]]
        for future in concurrent.futures.as_completed(futures):
            if len(records) >= limit:
                break
            try:
                record = future.result()
            except Exception as exc:
                fetcher.errors.append(f"Packagist expansion failed: {exc}")
                continue
            if record is not None:
                records.append(record)
    return sorted(records, key=lambda record: record["name"].lower())


def expand_sapjava_maven(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    seen = set()
    for query in SAPJAVA_MAVEN_QUERIES:
        if len(records) >= limit:
            break
        url = f"https://search.maven.org/solrsearch/select?q={urllib.parse.quote(query)}&rows=100&wt=json"
        data = fetcher.get_json(url)
        response = data.get("response") if isinstance(data, dict) else {}
        docs = response.get("docs") if isinstance(response, dict) else []
        if not isinstance(docs, list):
            continue
        for doc in docs:
            if len(records) >= limit:
                break
            if not isinstance(doc, dict):
                continue
            group = clean_text(doc.get("g"))
            artifact = clean_text(doc.get("a"))
            if not group or not artifact:
                continue
            coordinate = f"{group}:{artifact}"
            if coordinate.lower() in seen:
                continue
            seen.add(coordinate.lower())
            timestamp = doc.get("timestamp")
            date = ""
            if isinstance(timestamp, (int, float)):
                date = datetime.fromtimestamp(timestamp / 1000, timezone.utc).replace(microsecond=0).isoformat()
            version = clean_text(doc.get("latestVersion"))
            canonical = f"https://central.sonatype.com/artifact/{urllib.parse.quote(group, safe='.')}/{urllib.parse.quote(artifact, safe='')}"
            records.append(
                expansion_record(
                    source="maven_central_search",
                    branch="SAPJava",
                    name=coordinate,
                    category=infer_category_from_text(coordinate, f"{query} {clean_text(doc.get('p'))}", "library"),
                    description=f"Maven Central artifact for SAP/Java ecosystem work with packaging `{clean_text(doc.get('p')) or 'unknown'}`.",
                    canonical_url=canonical,
                    source_url=url,
                    release=known_release(version=version, date=date, source=url, channel="stable"),
                    nightly=unknown_release("maven_central_search_has_no_standard_nightly_channel"),
                    raw=doc,
                    provenance=[
                        {
                            "kind": "maven_central_search",
                            "status": "registry-derived",
                            "retrieved": today_iso(),
                            "query": query,
                        }
                    ],
                )
            )
    return records


def expand_cocoapods(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    source_url = "https://cdn.cocoapods.org/all_pods.txt"
    text = fetcher.get_text(source_url, accept="text/plain, */*")
    seed_names = [
        "AFNetworking",
        "Alamofire",
        "SDWebImage",
        "SnapKit",
        "Masonry",
        "RxSwift",
        "RealmSwift",
        "FMDB",
        "CocoaLumberjack",
        "Charts",
        "Firebase",
        "MBProgressHUD",
        "Kingfisher",
        "PromiseKit",
        "Swinject",
        "Starscream",
        "Quick",
        "Nimble",
        "Texture",
        "IGListKit",
    ]
    seen = set()
    candidates: list[str] = []
    for name in seed_names:
        if packageish_name(name, "cocoapods") and name.lower() not in seen:
            seen.add(name.lower())
            candidates.append(name)
    terms = tuple(term.lower() for term in COCOAPODS_NAME_TERMS)
    for line in text.splitlines():
        if len(candidates) >= limit * 3:
            break
        name = clean_text(line)
        lower = name.lower()
        if not packageish_name(name, "cocoapods") or lower in seen:
            continue
        if any(term in lower for term in terms):
            seen.add(lower)
            candidates.append(name)

    def build_record(name: str) -> dict[str, Any] | None:
        stable, nightly, extra = cocoapods_release(fetcher, name)
        description = extra.get("summary") or "CocoaPods package for Cocoa, Cocoa Touch, Swift, or Objective-C projects."
        normalized = extra.get("normalized_name", name)
        if stable["status"] == "unknown" and nightly["status"] == "unknown":
            return None
        return expansion_record(
            source="cocoapods_cdn",
            branch="Cocoa",
            name=normalized,
            category=infer_category_from_text(normalized, description, "library"),
            description=description,
            canonical_url=extra.get("package_url", f"https://cocoapods.org/pods/{urllib.parse.quote(normalized, safe='')}"),
            source_url=source_url,
            release=stable,
            nightly=nightly,
            raw={"name": name, "metadata": extra},
            provenance=[
                {
                    "kind": "cocoapods_cdn_and_trunk_api",
                    "status": "registry-derived",
                    "retrieved": today_iso(),
                }
            ],
        )

    records: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        futures = [pool.submit(build_record, name) for name in candidates[:limit]]
        for future in concurrent.futures.as_completed(futures):
            try:
                record = future.result()
            except Exception as exc:
                fetcher.errors.append(f"CocoaPods expansion failed: {exc}")
                continue
            if record is not None:
                records.append(record)
    return sorted(records, key=lambda record: record["name"].lower())[:limit]


def expand_database_systems(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    del fetcher
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    for name, category, url, description in DATABASE_SYSTEM_RECORDS[:limit]:
        records.append(
            expansion_record(
                source="curated_database_systems",
                branch="Databases",
                name=name,
                category=category,
                description=description,
                canonical_url=url,
                source_url="data/extensions/additional_languages.json",
                release=unknown_release("curated_database_record_requires_source_specific_release_lookup"),
                nightly=unknown_release("curated_database_record_requires_source_specific_preview_lookup"),
                raw={
                    "name": name,
                    "category": category,
                    "url": url,
                    "description": description,
                },
                provenance=[
                    {
                        "kind": "curated_database_systems",
                        "status": "curated-extension-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    return records


def expand_repository_workplace_routes(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    del fetcher
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    for name, category, url, description in REPOSITORY_WORKPLACE_RECORDS[:limit]:
        records.append(
            expansion_record(
                source="curated_repository_workplace_routes",
                branch="Repository Workplaces",
                name=name,
                category=category,
                description=description,
                canonical_url=url,
                source_url="data/extensions/additional_languages.json",
                release=unknown_release("official_workplace_route_requires_source_specific_release_lookup"),
                nightly=unknown_release("official_workplace_route_requires_source_specific_preview_lookup"),
                raw={
                    "name": name,
                    "category": category,
                    "url": url,
                    "description": description,
                },
                provenance=[
                    {
                        "kind": "official_repository_workplace_route",
                        "status": "curated-extension-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    return records


def expand_curated_language_routes(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    del fetcher
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = []
    for branch, name, category, url, description in ADDITIONAL_CURATED_LANGUAGE_RECORDS[:limit]:
        records.append(
            expansion_record(
                source="curated_language_routes",
                branch=branch,
                name=name,
                category=category,
                description=description,
                canonical_url=url,
                source_url="data/extensions/additional_languages.json",
                release=unknown_release("curated_language_route_requires_source_specific_release_lookup"),
                nightly=unknown_release("curated_language_route_requires_source_specific_preview_lookup"),
                raw={
                    "branch": branch,
                    "name": name,
                    "category": category,
                    "url": url,
                    "description": description,
                },
                provenance=[
                    {
                        "kind": "official_language_route",
                        "status": "curated-extension-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
    return records


def expand_gitlab_projects(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []

    def fetch_query(query: str) -> list[dict[str, Any]]:
        url = (
            "https://gitlab.com/api/v4/projects?"
            f"search={urllib.parse.quote(query)}&order_by=star_count&sort=desc&simple=true&per_page=100"
        )
        data = fetcher.get_json(url)
        if not isinstance(data, list):
            return []
        rows = []
        for item in data:
            if isinstance(item, dict):
                item = dict(item)
                item["_source_url"] = url
                item["_query"] = query
                rows.append(item)
        return rows

    items: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, len(GITLAB_PROJECT_QUERIES))) as pool:
        futures = [pool.submit(fetch_query, query) for query in GITLAB_PROJECT_QUERIES]
        for future in concurrent.futures.as_completed(futures):
            try:
                items.extend(future.result())
            except Exception as exc:
                fetcher.errors.append(f"GitLab expansion failed: {exc}")

    records: list[dict[str, Any]] = []
    seen = set()
    for item in sorted(items, key=lambda row: int(row.get("star_count") or 0), reverse=True):
        if len(records) >= limit:
            break
        path = clean_text(item.get("path_with_namespace") or item.get("name_with_namespace") or item.get("name"))
        if not path or path.lower() in seen:
            continue
        seen.add(path.lower())
        description = clean_text(item.get("description"))
        canonical = clean_text(item.get("web_url"))
        last_activity = clean_text(item.get("last_activity_at"))
        release = known_release(
            version="",
            date=last_activity,
            source=clean_text(item.get("_source_url")),
            channel="repository-activity",
            extra={"reason": "gitlab_projects_api_reports_activity_not_release_version"},
        )
        records.append(
            expansion_record(
                source="gitlab_projects_api",
                branch="Repository Workplaces",
                name=path,
                category=infer_category_from_text(path, f"{description} {item.get('_query')}", "library"),
                description=description or "GitLab project discovered from the official GitLab projects API.",
                canonical_url=canonical,
                source_url=clean_text(item.get("_source_url")),
                release=release,
                nightly=unknown_release("gitlab_projects_api_has_no_standard_nightly_channel"),
                raw={
                    "id": item.get("id"),
                    "path_with_namespace": path,
                    "description": description,
                    "web_url": canonical,
                    "star_count": item.get("star_count"),
                    "forks_count": item.get("forks_count"),
                    "last_activity_at": last_activity,
                    "query": item.get("_query"),
                },
                provenance=[
                    {
                        "kind": "gitlab_projects_api",
                        "status": "forge-api-derived",
                        "retrieved": today_iso(),
                        "query": item.get("_query"),
                    }
                ],
            )
        )
    return records


def expand_gitea_repositories(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    endpoints = [
        ("Gitea", "https://gitea.com/api/v1/repos/search"),
        ("Codeberg", "https://codeberg.org/api/v1/repos/search"),
    ]

    def fetch_query(endpoint_name: str, base_url: str, query: str) -> list[dict[str, Any]]:
        url = f"{base_url}?q={urllib.parse.quote(query)}&limit=50"
        data = fetcher.get_json(url)
        items = data.get("data") if isinstance(data, dict) else []
        if not isinstance(items, list):
            return []
        rows = []
        for item in items:
            if isinstance(item, dict):
                item = dict(item)
                item["_endpoint_name"] = endpoint_name
                item["_source_url"] = url
                item["_query"] = query
                rows.append(item)
        return rows

    items: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = [
            pool.submit(fetch_query, endpoint_name, base_url, query)
            for endpoint_name, base_url in endpoints
            for query in GITEA_REPOSITORY_QUERIES
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                items.extend(future.result())
            except Exception as exc:
                fetcher.errors.append(f"Gitea/Codeberg expansion failed: {exc}")

    records: list[dict[str, Any]] = []
    seen = set()
    for item in sorted(items, key=lambda row: int(row.get("stars_count") or 0), reverse=True):
        if len(records) >= limit:
            break
        owner = item.get("owner") if isinstance(item.get("owner"), dict) else {}
        owner_name = clean_text(owner.get("login") or owner.get("username") or owner.get("full_name"))
        repo_name = clean_text(item.get("name") or item.get("full_name"))
        full_name = clean_text(item.get("full_name")) or f"{owner_name}/{repo_name}".strip("/")
        key = f"{item.get('_endpoint_name')}::{full_name}".lower()
        if not full_name or key in seen:
            continue
        seen.add(key)
        description = clean_text(item.get("description"))
        canonical = clean_text(item.get("html_url") or item.get("website"))
        updated = clean_text(item.get("updated_at"))
        release = known_release(
            version="",
            date=updated,
            source=clean_text(item.get("_source_url")),
            channel="repository-activity",
            extra={"reason": "gitea_search_api_reports_activity_not_release_version"},
        )
        records.append(
            expansion_record(
                source="gitea_repositories_api",
                branch="Repository Workplaces",
                name=f"{item.get('_endpoint_name')}: {full_name}",
                category=infer_category_from_text(full_name, f"{description} {item.get('_query')}", "library"),
                description=description or f"{item.get('_endpoint_name')} repository discovered from the official Gitea-compatible search API.",
                canonical_url=canonical,
                source_url=clean_text(item.get("_source_url")),
                release=release,
                nightly=unknown_release("gitea_search_api_has_no_standard_nightly_channel"),
                raw={
                    "full_name": full_name,
                    "description": description,
                    "html_url": canonical,
                    "stars_count": item.get("stars_count"),
                    "forks_count": item.get("forks_count"),
                    "updated_at": updated,
                    "endpoint": item.get("_endpoint_name"),
                    "query": item.get("_query"),
                },
                provenance=[
                    {
                        "kind": "gitea_compatible_repository_search_api",
                        "status": "forge-api-derived",
                        "retrieved": today_iso(),
                        "endpoint": item.get("_endpoint_name"),
                        "query": item.get("_query"),
                    }
                ],
            )
        )
    return records


def expand_github_cli_repositories(
    fetcher: HttpCache,
    *,
    branch: str,
    queries: list[str],
    limit: int,
    source: str,
) -> list[dict[str, Any]]:
    if limit <= 0 or shutil.which("gh") is None or not fetcher.enabled:
        return []
    env = os.environ.copy()
    if env.get("GITHUB_TOKEN") and not env.get("GH_TOKEN"):
        env["GH_TOKEN"] = env["GITHUB_TOKEN"]
    records: list[dict[str, Any]] = []
    seen = set()
    json_fields = "fullName,description,url,language,license,stargazersCount,forksCount,pushedAt,updatedAt"
    for query in queries:
        if len(records) >= limit:
            break
        remaining = min(100, limit - len(records))
        cmd = [
            "gh",
            "search",
            "repos",
            *shlex.split(query),
            "--limit",
            str(remaining),
            "--sort",
            "stars",
            "--order",
            "desc",
            "--json",
            json_fields,
        ]
        try:
            completed = subprocess.run(
                cmd,
                check=False,
                capture_output=True,
                text=True,
                timeout=35,
                env=env,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            fetcher.errors.append(f"gh search failed for {query}: {exc}")
            return records
        if completed.returncode != 0:
            stderr = clean_text(completed.stderr)
            fetcher.errors.append(f"gh search failed for {query}: {stderr}")
            continue
        try:
            items = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            fetcher.errors.append(f"gh search JSON decode failed for {query}: {exc}")
            continue
        if not isinstance(items, list):
            continue
        for item in items:
            if len(records) >= limit:
                break
            if not isinstance(item, dict):
                continue
            full_name = clean_text(item.get("fullName"))
            if not full_name or full_name.lower() in seen:
                continue
            seen.add(full_name.lower())
            description = clean_text(item.get("description"))
            license_data = item.get("license") if isinstance(item.get("license"), dict) else {}
            pushed_at = clean_text(item.get("pushedAt") or item.get("updatedAt"))
            records.append(
                expansion_record(
                    source=source,
                    branch=branch,
                    name=full_name,
                    category=infer_category_from_text(full_name, f"{description} {query}", "library"),
                    description=description,
                    canonical_url=clean_text(item.get("url")),
                    source_url=f"gh search repos {query}",
                    release=known_release(
                        version="",
                        date=pushed_at,
                        source=f"gh search repos {query}",
                        channel="repository-activity",
                        extra={"reason": "gh_search_reports_activity_not_release_version"},
                    ),
                    nightly=unknown_release("gh_search_has_no_standard_nightly_channel"),
                    raw={
                        "full_name": full_name,
                        "description": description,
                        "language": item.get("language"),
                        "license": license_data,
                        "stars": item.get("stargazersCount"),
                        "forks": item.get("forksCount"),
                        "pushed_at": item.get("pushedAt"),
                        "updated_at": item.get("updatedAt"),
                    },
                    provenance=[
                        {
                            "kind": "github_cli_search",
                            "status": "forge-cli-derived",
                            "retrieved": today_iso(),
                            "query": query,
                            "command": "gh search repos",
                        }
                    ],
                )
            )
    return records


def parse_octave_index_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    pattern = re.compile(
        r"<tr>\s*<td>.*?</td>\s*"
        r'<td><a href="(?P<href>[^"]+)">(?P<name>.*?)</a></td>\s*'
        r'<td><div class="description">(?P<description>.*?)</div></td>\s*'
        r"<td>(?P<repository>.*?)</td>\s*"
        r"<td>(?P<version>.*?)</td>\s*"
        r"<td>(?P<date>.*?)</td>\s*</tr>",
        re.DOTALL,
    )
    for match in pattern.finditer(text):
        repository_html = match.group("repository")
        repo_match = re.search(r'href="([^"]+)"', repository_html)
        rows.append(
            {
                "href": html.unescape(match.group("href")),
                "name": strip_html(match.group("name")),
                "description": strip_html(match.group("description")),
                "repository": html.unescape(repo_match.group(1)) if repo_match else "",
                "version": strip_html(match.group("version")),
                "date": strip_html(match.group("date")),
            }
        )
    return rows


def expand_octave(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    source_url = "https://gnu-octave.github.io/packages/"
    text = fetcher.get_text(source_url, accept="text/html, */*")
    records: list[dict[str, Any]] = []
    for row in parse_octave_index_rows(text):
        if len(records) >= limit:
            break
        name = row["name"]
        if not name:
            continue
        canonical = urllib.parse.urljoin(source_url, row["href"])
        records.append(
            expansion_record(
                source="octave_packages_index",
                branch="Octave",
                name=name,
                category=infer_category_from_text(name, row["description"], "library"),
                description=row["description"],
                canonical_url=canonical,
                source_url=source_url,
                release=known_release(version=row["version"], date=row["date"], source=source_url, channel="stable"),
                nightly=unknown_release("octave_packages_have_no_standard_nightly_channel"),
                raw=row,
                provenance=[
                    {
                        "kind": "gnu_octave_packages_index",
                        "status": "registry-derived",
                        "retrieved": today_iso(),
                    }
                ],
            )
        )
        if row.get("repository"):
            records[-1]["release_source_metadata"] = {"project_urls": {"repository": row["repository"], "GNU Octave package": canonical}}
    return records


def expand_github_repositories(
    fetcher: HttpCache,
    *,
    branch: str,
    queries: list[str],
    limit: int,
    source: str,
) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    records: list[dict[str, Any]] = expand_github_cli_repositories(
        fetcher,
        branch=branch,
        queries=queries,
        limit=limit,
        source=source,
    )
    seen = {record["name"].lower() for record in records}
    if len(records) >= limit:
        return records[:limit]
    per_page = 50
    for query in queries:
        page = 1
        while len(records) < limit and page <= 5:
            url = (
                "https://api.github.com/search/repositories?"
                f"q={urllib.parse.quote(query)}&sort=stars&order=desc&per_page={per_page}&page={page}"
            )
            data = fetcher.get_json(url)
            if not isinstance(data, dict) or not isinstance(data.get("items"), list):
                if fetcher.errors and "api.github.com/search/repositories" in fetcher.errors[-1] and "HTTP Error 403" in fetcher.errors[-1]:
                    return records
                break
            items = data["items"]
            if not items:
                break
            for item in items:
                if len(records) >= limit:
                    break
                if not isinstance(item, dict):
                    continue
                full_name = clean_text(item.get("full_name"))
                if not full_name or full_name.lower() in seen:
                    continue
                seen.add(full_name.lower())
                description = clean_text(item.get("description"))
                topics = " ".join(item.get("topics") or [])
                records.append(
                    expansion_record(
                        source=source,
                        branch=branch,
                        name=full_name,
                        category=infer_category_from_text(full_name, f"{description} {topics}", "library"),
                        description=description,
                        canonical_url=clean_text(item.get("html_url")),
                        source_url=url,
                        release=unknown_release("github_search_does_not_include_release_date"),
                        nightly=unknown_release("github_search_does_not_include_nightly_channel"),
                        raw={
                            "full_name": full_name,
                            "description": description,
                            "language": item.get("language"),
                            "stars": item.get("stargazers_count"),
                            "forks": item.get("forks_count"),
                            "topics": item.get("topics"),
                            "pushed_at": item.get("pushed_at"),
                        },
                        provenance=[
                            {
                                "kind": "github_repository_search",
                                "status": "registry-derived",
                                "retrieved": today_iso(),
                                "query": query,
                            }
                        ],
                    )
                )
            page += 1
    return records


def balanced_trim_expansions(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    if len(records) <= limit:
        return records
    by_branch: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_branch[record["catalog_branch"]].append(record)
    active_branches = [branch for branch in LANGUAGE_ORDER if by_branch.get(branch)]
    if not active_branches:
        return records[:limit]
    result: list[dict[str, Any]] = []
    used = set()
    base_quota = max(1, limit // len(active_branches))
    for branch in active_branches:
        for record in by_branch[branch][:base_quota]:
            if len(result) >= limit:
                return result
            used.add(record["id"])
            result.append(record)
    for record in records:
        if len(result) >= limit:
            break
        if record["id"] in used:
            continue
        used.add(record["id"])
        result.append(record)
    return result


def expand_records(
    existing: list[dict[str, Any]],
    fetcher: HttpCache,
    target_records: int,
) -> list[dict[str, Any]]:
    if len(existing) >= target_records:
        return []
    needed = target_records - len(existing)
    expansion_goal = needed + min(1200, max(300, needed // 14))
    budgets = {
        "crates": min(2400, max(0, expansion_goal // 7)),
        "npm": min(2600, max(0, expansion_goal // 6)),
        "julia": min(2400, max(0, expansion_goal // 7)),
        "luarocks": min(1800, max(0, expansion_goal // 10)),
        "pypi": min(900, max(0, expansion_goal // 16)),
        "cran": min(2600, max(0, expansion_goal // 6)),
        "hackage": min(2200, max(0, expansion_goal // 7)),
        "nuget": min(1800, max(0, expansion_goal // 8)),
        "pub_dev": min(1400, max(0, expansion_goal // 12)),
        "go_modules": min(4200, max(0, expansion_goal // 5)),
        "go_github": min(500, max(0, expansion_goal // 35)),
        "packagist": min(700, max(0, expansion_goal // 18)),
        "swift_github": min(700, max(0, expansion_goal // 28)),
        "webassembly_github": min(700, max(0, expansion_goal // 28)),
        "sapjava_maven": min(900, max(0, expansion_goal // 18)),
        "sapjava_github": min(300, max(0, expansion_goal // 55)),
        "cocoapods": min(80, max(0, expansion_goal // 300)),
        "cocoa_github": min(500, max(0, expansion_goal // 35)),
        "database_static": len(DATABASE_SYSTEM_RECORDS),
        "database_github": min(1200, max(0, expansion_goal // 12)),
        "curated_language_routes": len(ADDITIONAL_CURATED_LANGUAGE_RECORDS),
        "starlark_github": min(350, max(0, expansion_goal // 45)),
        "basilisk_github": min(80, max(0, expansion_goal // 200)),
        "nix_github": min(600, max(0, expansion_goal // 25)),
        "renderers_github": min(700, max(0, expansion_goal // 25)),
        "braces_github": min(350, max(0, expansion_goal // 40)),
        "computer_graphics_software_github": min(700, max(0, expansion_goal // 24)),
        "engines_github": min(700, max(0, expansion_goal // 24)),
        "physics_engines_github": min(350, max(0, expansion_goal // 40)),
        "game_engines_github": min(500, max(0, expansion_goal // 32)),
        "icons_and_logos_github": min(500, max(0, expansion_goal // 30)),
        "font_briefcase_github": min(350, max(0, expansion_goal // 45)),
        "assets_github": min(500, max(0, expansion_goal // 30)),
        "maps_github": min(600, max(0, expansion_goal // 28)),
        "space_engines_github": min(250, max(0, expansion_goal // 55)),
        "space_shuttles_github": min(150, max(0, expansion_goal // 90)),
        "space_maps_github": min(250, max(0, expansion_goal // 55)),
        "effects_github": min(500, max(0, expansion_goal // 32)),
        "audio_github": min(500, max(0, expansion_goal // 32)),
        "video_github": min(500, max(0, expansion_goal // 32)),
        "photography_github": min(350, max(0, expansion_goal // 45)),
        "microscopy_github": min(350, max(0, expansion_goal // 45)),
        "telescopes_github": min(250, max(0, expansion_goal // 60)),
        "radars_github": min(250, max(0, expansion_goal // 60)),
        "satcom_satellites_github": min(250, max(0, expansion_goal // 60)),
        "electromagnetoscopes_github": min(250, max(0, expansion_goal // 60)),
        "radio_garden_speciality_github": min(160, max(0, expansion_goal // 85)),
        "repertoare_catalogs_github": min(220, max(0, expansion_goal // 70)),
        "catalogs_github": min(500, max(0, expansion_goal // 32)),
        "magazines_github": min(220, max(0, expansion_goal // 70)),
        "workplace_routes": len(REPOSITORY_WORKPLACE_RECORDS),
        "gitlab_projects": min(300, max(0, expansion_goal // 45)),
        "gitea_repositories": min(200, max(0, expansion_goal // 60)),
        "aims_github": min(900, max(0, expansion_goal // 18)),
        "octave": min(350, max(0, expansion_goal // 35)),
        "matlab_github": min(500, max(0, expansion_goal // 30)),
        "assembly_github": min(650, max(0, expansion_goal // 28)),
        "pattern_github": min(500, max(0, expansion_goal // 35)),
        "awesome": min(2800, max(0, expansion_goal // 7)),
    }
    expansions: list[dict[str, Any]] = []
    source_calls = [
        ("crates.io", lambda: expand_crates(fetcher, budgets["crates"])),
        ("npm", lambda: expand_npm(fetcher, budgets["npm"])),
        ("Julia General", lambda: expand_julia(fetcher, budgets["julia"])),
        ("LuaRocks", lambda: expand_luarocks(fetcher, budgets["luarocks"])),
        ("PyPI", lambda: expand_pypi(fetcher, budgets["pypi"])),
        ("CRAN", lambda: expand_cran(fetcher, budgets["cran"])),
        ("Hackage", lambda: expand_hackage(fetcher, budgets["hackage"])),
        ("NuGet", lambda: expand_nuget(fetcher, budgets["nuget"])),
        ("pub.dev", lambda: expand_pub_dev(fetcher, budgets["pub_dev"])),
        ("Go module index", lambda: expand_go_modules(fetcher, budgets["go_modules"])),
        ("Packagist", lambda: expand_packagist(fetcher, budgets["packagist"])),
        ("SAPJava Maven Central", lambda: expand_sapjava_maven(fetcher, budgets["sapjava_maven"])),
        ("CocoaPods", lambda: expand_cocoapods(fetcher, budgets["cocoapods"])),
        ("curated language routes", lambda: expand_curated_language_routes(fetcher, budgets["curated_language_routes"])),
        ("curated database systems", lambda: expand_database_systems(fetcher, budgets["database_static"])),
        ("official repository workplace routes", lambda: expand_repository_workplace_routes(fetcher, budgets["workplace_routes"])),
        ("GitLab projects API", lambda: expand_gitlab_projects(fetcher, budgets["gitlab_projects"])),
        ("Gitea-compatible repository APIs", lambda: expand_gitea_repositories(fetcher, budgets["gitea_repositories"])),
        ("GNU Octave packages", lambda: expand_octave(fetcher, budgets["octave"])),
        ("Go GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Go",
            queries=GO_GITHUB_QUERIES,
            limit=budgets["go_github"],
            source="github_search_go",
        )),
        ("MATLAB GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Matlab",
            queries=MATLAB_GITHUB_QUERIES,
            limit=budgets["matlab_github"],
            source="github_search_matlab",
        )),
        ("Assembly GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Assembly",
            queries=ASSEMBLY_GITHUB_QUERIES,
            limit=budgets["assembly_github"],
            source="github_search_assembly",
        )),
        ("Pattern language GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Pattern language",
            queries=PATTERN_GITHUB_QUERIES,
            limit=budgets["pattern_github"],
            source="github_search_pattern_language",
        )),
        ("Starlark GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Starlark",
            queries=STARLARK_GITHUB_QUERIES,
            limit=budgets["starlark_github"],
            source="github_search_starlark",
        )),
        ("Basilisk GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Basilisk",
            queries=BASILISK_GITHUB_QUERIES,
            limit=budgets["basilisk_github"],
            source="github_search_basilisk",
        )),
        ("\"aim's\" GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="\"aim's\"",
            queries=AIMS_GITHUB_QUERIES,
            limit=budgets["aims_github"],
            source="github_search_aims",
        )),
        ("nix GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="nix",
            queries=NIX_GITHUB_QUERIES,
            limit=budgets["nix_github"],
            source="github_search_nix",
        )),
        ("Renderers GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Renderers",
            queries=RENDERERS_GITHUB_QUERIES,
            limit=budgets["renderers_github"],
            source="github_search_renderers",
        )),
        ("Braces GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Braces",
            queries=BRACES_GITHUB_QUERIES,
            limit=budgets["braces_github"],
            source="github_search_braces",
        )),
        ("Computer Graphics Software GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Computer Graphics Software",
            queries=COMPUTER_GRAPHICS_SOFTWARE_GITHUB_QUERIES,
            limit=budgets["computer_graphics_software_github"],
            source="github_search_computer_graphics_software",
        )),
        ("Engines GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Engines",
            queries=ENGINES_GITHUB_QUERIES,
            limit=budgets["engines_github"],
            source="github_search_engines",
        )),
        ("Physics Engines GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Physics Engines",
            queries=PHYSICS_ENGINES_GITHUB_QUERIES,
            limit=budgets["physics_engines_github"],
            source="github_search_physics_engines",
        )),
        ("Game Engines GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Game Engines",
            queries=GAME_ENGINES_GITHUB_QUERIES,
            limit=budgets["game_engines_github"],
            source="github_search_game_engines",
        )),
        ("Icons and Logos GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Icons and Logos",
            queries=ICONS_AND_LOGOS_GITHUB_QUERIES,
            limit=budgets["icons_and_logos_github"],
            source="github_search_icons_and_logos",
        )),
        ("Font Briefcase GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Font Briefcase",
            queries=FONT_BRIEFCASE_GITHUB_QUERIES,
            limit=budgets["font_briefcase_github"],
            source="github_search_font_briefcase",
        )),
        ("Assets GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Assets",
            queries=ASSETS_GITHUB_QUERIES,
            limit=budgets["assets_github"],
            source="github_search_assets",
        )),
        ("Maps GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Maps",
            queries=MAPS_GITHUB_QUERIES,
            limit=budgets["maps_github"],
            source="github_search_maps",
        )),
        ("Space Engines GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Space Engines",
            queries=SPACE_ENGINES_GITHUB_QUERIES,
            limit=budgets["space_engines_github"],
            source="github_search_space_engines",
        )),
        ("Space Shuttles GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Space Shuttles",
            queries=SPACE_SHUTTLES_GITHUB_QUERIES,
            limit=budgets["space_shuttles_github"],
            source="github_search_space_shuttles",
        )),
        ("Space Maps GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Space Maps",
            queries=SPACE_MAPS_GITHUB_QUERIES,
            limit=budgets["space_maps_github"],
            source="github_search_space_maps",
        )),
        ("Effects GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Effects",
            queries=EFFECTS_GITHUB_QUERIES,
            limit=budgets["effects_github"],
            source="github_search_effects",
        )),
        ("Audio GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Audio",
            queries=AUDIO_GITHUB_QUERIES,
            limit=budgets["audio_github"],
            source="github_search_audio",
        )),
        ("Video GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Video",
            queries=VIDEO_GITHUB_QUERIES,
            limit=budgets["video_github"],
            source="github_search_video",
        )),
        ("Photography GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Photography",
            queries=PHOTOGRAPHY_GITHUB_QUERIES,
            limit=budgets["photography_github"],
            source="github_search_photography",
        )),
        ("Microscopy GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Microscopy",
            queries=MICROSCOPY_GITHUB_QUERIES,
            limit=budgets["microscopy_github"],
            source="github_search_microscopy",
        )),
        ("Telescopes GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Telescopes",
            queries=TELESCOPES_GITHUB_QUERIES,
            limit=budgets["telescopes_github"],
            source="github_search_telescopes",
        )),
        ("Radars GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Radars",
            queries=RADARS_GITHUB_QUERIES,
            limit=budgets["radars_github"],
            source="github_search_radars",
        )),
        ("SatCom Satellites GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="SatCom Satellites",
            queries=SATCOM_SATELLITES_GITHUB_QUERIES,
            limit=budgets["satcom_satellites_github"],
            source="github_search_satcom_satellites",
        )),
        ("Electromagnetoscopes GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Electromagnetoscopes",
            queries=ELECTROMAGNETOSCOPES_GITHUB_QUERIES,
            limit=budgets["electromagnetoscopes_github"],
            source="github_search_electromagnetoscopes",
        )),
        ("Radio Garden Speciality GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Radio Garden Speciality",
            queries=RADIO_GARDEN_SPECIALITY_GITHUB_QUERIES,
            limit=budgets["radio_garden_speciality_github"],
            source="github_search_radio_garden_speciality",
        )),
        ("Repertoare Catalogs GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Repertoare Catalogs",
            queries=REPERTOARE_CATALOGS_GITHUB_QUERIES,
            limit=budgets["repertoare_catalogs_github"],
            source="github_search_repertoare_catalogs",
        )),
        ("Catalogs GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Catalogs",
            queries=CATALOGS_GITHUB_QUERIES,
            limit=budgets["catalogs_github"],
            source="github_search_catalogs",
        )),
        ("Magazines GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Magazines",
            queries=MAGAZINES_GITHUB_QUERIES,
            limit=budgets["magazines_github"],
            source="github_search_magazines",
        )),
        ("Swift GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Swift",
            queries=SWIFT_GITHUB_QUERIES,
            limit=budgets["swift_github"],
            source="github_search_swift",
        )),
        ("WebAssembly GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="WebAssembly",
            queries=WEBASSEMBLY_GITHUB_QUERIES,
            limit=budgets["webassembly_github"],
            source="github_search_webassembly",
        )),
        ("SAPJava GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="SAPJava",
            queries=SAPJAVA_GITHUB_QUERIES,
            limit=budgets["sapjava_github"],
            source="github_search_sapjava",
        )),
        ("Cocoa GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Cocoa",
            queries=COCOA_GITHUB_QUERIES,
            limit=budgets["cocoa_github"],
            source="github_search_cocoa",
        )),
        ("Databases GitHub search", lambda: expand_github_repositories(
            fetcher,
            branch="Databases",
            queries=DATABASE_GITHUB_QUERIES,
            limit=budgets["database_github"],
            source="github_search_databases",
        )),
        ("awesome lists", lambda: expand_awesome_lists(fetcher, budgets["awesome"])),
    ]
    for source_name, call in source_calls:
        try:
            records = call()
        except Exception as exc:
            fetcher.errors.append(f"Expansion failed for {source_name}: {exc}")
            continue
        expansions.extend(records)
    return balanced_trim_expansions(expansions, expansion_goal)


def enrichment_priority(record: dict[str, Any]) -> tuple[Any, ...]:
    branch = record["catalog_branch"]
    source = record.get("source", "")
    new_branch_rank = {
        "Haskell": 0,
        "C-Sharp": 0,
        "PHP": 0,
        "Go": 0,
        "SAPJava": 0,
        "Cocoa": 0,
        "Swift": 1,
        "WebAssembly": 1,
        "Databases": 1,
        "Repository Workplaces": 1,
        "Starlark": 1,
        "Basilisk": 1,
        "\"aim's\"": 1,
        "nix": 1,
        "Renderers": 1,
        "Braces": 1,
        "Computer Graphics Software": 1,
        "Engines": 1,
        "Physics Engines": 1,
        "Game Engines": 1,
        "Icons and Logos": 1,
        "Font Briefcase": 1,
        "Assets": 1,
        "Maps": 1,
        "Space Engines": 1,
        "Space Shuttles": 1,
        "Space Maps": 1,
        "Effects": 1,
        "Audio": 1,
        "Video": 1,
        "Photography": 1,
        "Microscopy": 1,
        "Telescopes": 1,
        "Radars": 1,
        "SatCom Satellites": 1,
        "Electromagnetoscopes": 1,
        "Radio Garden Speciality": 1,
        "Repertoare Catalogs": 1,
        "Catalogs": 1,
        "Magazines": 1,
        "Matlab": 1,
        "Assembly": 1,
        "Pattern language": 1,
        "bc": 1,
        "R": 2,
        "Dart": 2,
        "Octave": 2,
    }.get(branch, 3)
    source_rank = {
        "hackage_top_downloads": 0,
        "nuget_search": 0,
        "packagist_search": 0,
        "maven_central_search": 0,
        "cocoapods_cdn": 0,
        "go_module_index": 0,
        "curated_database_systems": 1,
        "github_search_go": 1,
        "github_search_matlab": 1,
        "github_search_assembly": 1,
        "github_search_pattern_language": 1,
        "github_search_swift": 1,
        "github_search_webassembly": 1,
        "github_search_sapjava": 1,
        "github_search_cocoa": 1,
        "github_search_databases": 1,
        "curated_language_routes": 1,
        "github_search_starlark": 1,
        "github_search_basilisk": 1,
        "github_search_aims": 1,
        "github_search_nix": 1,
        "github_search_renderers": 1,
        "github_search_braces": 1,
        "github_search_computer_graphics_software": 1,
        "github_search_engines": 1,
        "github_search_physics_engines": 1,
        "github_search_game_engines": 1,
        "github_search_icons_and_logos": 1,
        "github_search_font_briefcase": 1,
        "github_search_assets": 1,
        "github_search_maps": 1,
        "github_search_space_engines": 1,
        "github_search_space_shuttles": 1,
        "github_search_space_maps": 1,
        "github_search_effects": 1,
        "github_search_audio": 1,
        "github_search_video": 1,
        "github_search_photography": 1,
        "github_search_microscopy": 1,
        "github_search_telescopes": 1,
        "github_search_radars": 1,
        "github_search_satcom_satellites": 1,
        "github_search_electromagnetoscopes": 1,
        "github_search_radio_garden_speciality": 1,
        "github_search_repertoare_catalogs": 1,
        "github_search_catalogs": 1,
        "github_search_magazines": 1,
        "curated_repository_workplace_routes": 1,
        "gitlab_projects_api": 1,
        "gitea_repositories_api": 1,
        "catalog_extension": 2,
        "master_json": 2,
    }.get(source, 3)
    status_rank = {"partial": 0, "unknown": 1, "known": 2}.get(record.get("release", {}).get("status"), 3)
    branch_order = LANGUAGE_ORDER.index(branch) if branch in LANGUAGE_ORDER else 99
    return (new_branch_rank, source_rank, status_rank, branch_order, record["name"].lower())


def enrich_records(
    source_path: Path,
    *,
    network: bool,
    target_records: int,
    workers: int,
    cache_ttl: int,
    max_enrich_records: int,
) -> dict[str, Any]:
    source = merged_source_payload(source_path)
    source_records = [normalize_input_record(item) for item in source.get("records", [])]
    fetcher = HttpCache(HTTP_CACHE_DIR, enabled=network, ttl_seconds=cache_ttl)
    expansions = expand_records(source_records, fetcher, target_records)
    combined = source_records + expansions
    merged = merge_records(combined)

    julia_registry: dict[str, dict[str, str]] | None = None
    if network and any(item["catalog_branch"] == "Julia" for item in merged):
        julia_registry = parse_julia_registry(fetcher)

    to_enrich = sorted((record for record in merged if should_enrich(record)), key=enrichment_priority)
    if max_enrich_records > 0:
        to_enrich = to_enrich[:max_enrich_records]
    enriched_by_key: dict[str, dict[str, Any]] = {}
    if network and to_enrich:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futures = {
                pool.submit(enrich_one, record, fetcher, julia_registry=julia_registry): record["identity_key"]
                for record in to_enrich
            }
            for future in concurrent.futures.as_completed(futures):
                key = futures[future]
                try:
                    enriched_by_key[key] = future.result()
                except Exception as exc:
                    fetcher.errors.append(f"Enrichment failed for {key}: {exc}")
    final_records = []
    for record in merged:
        updated = enriched_by_key.get(record["identity_key"], record)
        updated["slug"] = record_slug(updated)
        final_records.append(updated)
    final_records = preserve_prior_observation_times(final_records)
    final_records = merge_with_prior_records(final_records)
    fetch_errors = sorted(dict.fromkeys(fetcher.errors))

    stats = BuildStats(
        source_records=len(source_records),
        normalized_identities=len(final_records),
        expanded_records=len(expansions),
        release_checked=len(to_enrich) if network else 0,
        release_known=sum(1 for item in final_records if item["release"]["status"] == "known"),
        release_unknown=sum(1 for item in final_records if item["release"]["status"] != "known"),
        fetch_errors=len(fetch_errors),
    )
    payload = {
        "generated_at": now_iso(),
        "source_catalog": str(source_path),
        "source_catalog_id": source.get("catalog_id", ""),
        "source_catalog_version": source.get("catalog_version", ""),
        "extension_catalog": source.get("extension_catalog", ""),
        "extension_catalog_id": source.get("extension_catalog_id", ""),
        "scope": source.get("scope", LANGUAGE_ORDER),
        "taxonomy": source.get("taxonomy", TAXONOMY),
        "target_records": target_records,
        "statistics": dataclasses.asdict(stats),
        "fetch_errors": fetch_errors[:500],
        "records": final_records,
    }
    payload = compact_payload_for_storage(payload)
    payload = preserve_generated_at_if_semantically_same(payload)
    write_json(ENRICHED_JSON, payload)
    export_to_sqlite(payload)
    write_text(REPORT_MD, render_enrichment_report(payload))
    return payload


def release_without_checked_at(release: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in release.items() if key != "checked_at"}


def preserve_prior_observation_times(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not ENRICHED_JSON.exists():
        return records
    try:
        previous = read_json(ENRICHED_JSON)
    except Exception:
        return records
    old_by_key = {
        record.get("identity_key"): record
        for record in previous.get("records", [])
        if isinstance(record, dict) and record.get("identity_key")
    }
    for record in records:
        old = old_by_key.get(record.get("identity_key"))
        if not old:
            continue
        for field in ("release", "nightly"):
            current_release = record.get(field)
            old_release = old.get(field)
            if not isinstance(current_release, dict) or not isinstance(old_release, dict):
                continue
            if release_without_checked_at(current_release) == release_without_checked_at(old_release):
                current_release["checked_at"] = old_release.get("checked_at", current_release.get("checked_at", ""))
    return records


def merge_with_prior_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """DeltaLake-style merge: never lose previously collected records.

    Loads the existing enriched_records.json and re-introduces any records
    that were present in the prior run but are not in the current run. This
    ensures the catalog only grows across runs (incremental upsert pattern)
    rather than potentially shrinking when registry results vary between runs.
    """
    if not ENRICHED_JSON.exists():
        return records
    try:
        previous = read_json(ENRICHED_JSON)
    except Exception:
        return records
    prior_records = previous.get("records", [])
    if not prior_records:
        return records
    current_keys = {record.get("identity_key") for record in records}
    carried: list[dict[str, Any]] = []
    for prior in prior_records:
        if isinstance(prior, dict) and prior.get("identity_key") and prior.get("identity_key") not in current_keys:
            carried.append(prior)
    if not carried:
        return records
    return records + carried


SQLITE_DB = CATALOG_DIR / "catalog.sqlite"


def export_to_sqlite(payload: dict[str, Any]) -> int:
    """Export enriched records into a SQLite database for database-backed ingestion.

    Uses an UPSERT (INSERT ... ON CONFLICT) pattern so incremental runs
    update existing rows by identity_key rather than duplicating them.
    Returns the number of rows in the records table.
    """
    import sqlite3

    conn = sqlite3.connect(str(SQLITE_DB))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS records (
            identity_key TEXT PRIMARY KEY,
            catalog_branch TEXT,
            category TEXT,
            name TEXT,
            slug TEXT,
            canonical_url TEXT,
            description TEXT,
            section TEXT,
            subsection TEXT,
            source TEXT,
            source_url TEXT,
            raw_json TEXT,
            release_json TEXT,
            nightly_json TEXT,
            license_text TEXT,
            license_family TEXT,
            generated_at TEXT,
            observed_at TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS record_sources (
            identity_key TEXT,
            source_id TEXT,
            PRIMARY KEY (identity_key, source_id)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS provenance (
            identity_key TEXT,
            kind TEXT,
            status TEXT,
            retrieved TEXT,
            extra TEXT
        )
        """
    )
    now = now_iso()
    inserted = 0
    for record in payload.get("records", []):
        key = record.get("identity_key", "")
        release = record.get("release", {})
        nightly = record.get("nightly", {})
        license_text = ", ".join(record_license_values(record))
        license_fam = license_family(record)
        conn.execute(
            """
            INSERT INTO records (
                identity_key, catalog_branch, category, name, slug,
                canonical_url, description, section, subsection,
                source, source_url, raw_json,
                release_json, nightly_json,
                license_text, license_family,
                generated_at, observed_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(identity_key) DO UPDATE SET
                catalog_branch=excluded.catalog_branch,
                category=excluded.category,
                name=excluded.name,
                slug=excluded.slug,
                canonical_url=excluded.canonical_url,
                description=excluded.description,
                section=excluded.section,
                subsection=excluded.subsection,
                source=excluded.source,
                source_url=excluded.source_url,
                raw_json=excluded.raw_json,
                release_json=excluded.release_json,
                nightly_json=excluded.nightly_json,
                license_text=excluded.license_text,
                license_family=excluded.license_family,
                generated_at=excluded.generated_at,
                observed_at=excluded.observed_at
            """,
            (
                key,
                record.get("catalog_branch", ""),
                record.get("category", ""),
                record.get("name", ""),
                record.get("slug", ""),
                record.get("canonical_url", ""),
                record.get("description", ""),
                record.get("section", ""),
                record.get("subsection", "") or "",
                record.get("source", ""),
                record.get("source_url", ""),
                json.dumps(record.get("raw", {}), sort_keys=True) if isinstance(record.get("raw"), dict) else "",
                json.dumps(release, sort_keys=True),
                json.dumps(nightly, sort_keys=True),
                license_text,
                license_fam,
                now,
                record.get("observed_at", now),
            ),
        )
        for source_id in record.get("source_record_ids", [record.get("id", key)]):
            conn.execute(
                "INSERT OR IGNORE INTO record_sources (identity_key, source_id) VALUES (?, ?)",
                (key, source_id),
            )
        for prov in record.get("provenance", []):
            conn.execute(
                """
                INSERT INTO provenance (identity_key, kind, status, retrieved, extra)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    key,
                    prov.get("kind", ""),
                    prov.get("status", ""),
                    prov.get("retrieved", ""),
                    json.dumps(prov, sort_keys=True),
                ),
            )
        inserted += 1
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM records").fetchone()[0]
    conn.close()
    return count


def stream_records_from_sqlite() -> list[dict[str, Any]]:
    """Read all records from the SQLite database (streaming, no full JSON load needed).

    Returns records in the same shape as enriched_records.json records.
    Useful for recovery when the JSON file is lost but the SQLite DB persists.
    """
    import sqlite3

    if not SQLITE_DB.exists():
        return []
    conn = sqlite3.connect(str(SQLITE_DB))
    conn.row_factory = sqlite3.Row
    cursor = conn.execute(
        """
        SELECT identity_key, catalog_branch, category, name, slug,
               canonical_url, description, section, subsection,
               source, source_url, raw_json,
               release_json, nightly_json,
               license_text, license_family,
               generated_at, observed_at
        FROM records
        ORDER BY catalog_branch, category, name
        """
    )
    records: list[dict[str, Any]] = []
    for row in cursor:
        raw = json.loads(row["raw_json"]) if row["raw_json"] else {}
        record = {
            "identity_key": row["identity_key"],
            "catalog_branch": row["catalog_branch"],
            "category": row["category"],
            "name": row["name"],
            "slug": row["slug"],
            "canonical_url": row["canonical_url"],
            "description": row["description"],
            "section": row["section"],
            "subsection": row["subsection"] if row["subsection"] else None,
            "source": row["source"],
            "source_url": row["source_url"],
            "raw": raw,
            "release": json.loads(row["release_json"]) if row["release_json"] else {},
            "nightly": json.loads(row["nightly_json"]) if row["nightly_json"] else {},
            "license_text": row["license_text"],
            "license_family": row["license_family"],
            "observed_at": row["observed_at"],
        }
        source_ids = [r[0] for r in conn.execute("SELECT source_id FROM record_sources WHERE identity_key = ?", (row["identity_key"],)).fetchall()]
        record["source_record_ids"] = source_ids if source_ids else [row["identity_key"]]
        records.append(record)
    conn.close()
    return records


def recover_from_sqlite(source_path: Path) -> bool:
    """Recover enriched records from the SQLite DB if the JSON file is missing or smaller.

    Returns True if recovery was performed, False otherwise.
    """
    if not SQLITE_DB.exists():
        return False
    if not ENRICHED_JSON.exists():
        sqlite_records = stream_records_from_sqlite()
        if not sqlite_records:
            return False
        payload = {
            "generated_at": now_iso(),
            "source_catalog": str(source_path),
            "scope": LANGUAGE_ORDER,
            "taxonomy": TAXONOMY,
            "records": sqlite_records,
        }
        write_json(ENRICHED_JSON, compact_payload_for_storage(payload))
        return True
    return False


def semantic_payload(payload: dict[str, Any]) -> dict[str, Any]:
    scrubbed = json.loads(json.dumps(payload, ensure_ascii=False))
    scrubbed.pop("generated_at", None)
    for record in scrubbed.get("records", []):
        for field in ("release", "nightly"):
            if isinstance(record.get(field), dict):
                record[field].pop("checked_at", None)
    return scrubbed


def preserve_generated_at_if_semantically_same(payload: dict[str, Any]) -> dict[str, Any]:
    if not ENRICHED_JSON.exists():
        return payload
    try:
        previous = read_json(ENRICHED_JSON)
    except Exception:
        return payload
    if semantic_payload(previous) == semantic_payload(payload):
        payload["generated_at"] = previous.get("generated_at", payload["generated_at"])
    return payload


def sort_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        records,
        key=lambda item: (
            LANGUAGE_ORDER.index(item["catalog_branch"]) if item["catalog_branch"] in LANGUAGE_ORDER else 99,
            item["category"],
            item["name"].lower(),
        ),
    )


def merge_catalog_records_into_payload(payload: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    by_key = {record["identity_key"]: dict(record) for record in payload.get("records", [])}
    for record in records:
        key = record["identity_key"]
        target = by_key.get(key)
        if target is None:
            new_record = compact_record_for_storage(record)
            new_record["source_record_ids"] = list(record.get("source_record_ids", [record["id"]]))
            new_record["evidence"] = [compact_evidence_item(item) for item in record.get("evidence", [record]) if isinstance(item, dict)]
            by_key[key] = new_record
            continue
        source_ids = target.setdefault("source_record_ids", [])
        for source_id in record.get("source_record_ids", [record["id"]]):
            if source_id not in source_ids:
                source_ids.append(source_id)
        evidence = target.setdefault("evidence", [])
        if isinstance(evidence, list):
            existing_ids = {item.get("id") for item in evidence if isinstance(item, dict)}
            for item in record.get("evidence", [record]):
                if isinstance(item, dict) and item.get("id") not in existing_ids:
                    evidence.append(compact_evidence_item(item))
                    existing_ids.add(item.get("id"))
        for field in ("description", "canonical_url", "source_url", "section", "subsection"):
            if not target.get(field) and record.get(field):
                target[field] = record[field]
        if target.get("release", {}).get("status") == "unknown" and record.get("release", {}).get("status") != "unknown":
            target["release"] = record["release"]
        if target.get("nightly", {}).get("status") == "unknown" and record.get("nightly", {}).get("status") != "unknown":
            target["nightly"] = record["nightly"]
        target.setdefault("provenance", [])
        target["provenance"].extend(record.get("provenance", []))
        seen = set()
        unique_provenance = []
        for item in target.get("provenance", []):
            provenance_key = json.dumps(item, sort_keys=True, ensure_ascii=False)
            if provenance_key not in seen:
                seen.add(provenance_key)
                unique_provenance.append(item)
        target["provenance"] = unique_provenance
        target["license_evidence"] = record_license_values(target)
        target["slug"] = record_slug(target)
    updated = dict(payload)
    updated["records"] = sort_records(list(by_key.values()))
    stats = dict(updated.get("statistics", {}))
    stats["normalized_identities"] = len(updated["records"])
    stats["release_known"] = sum(1 for item in updated["records"] if item.get("release", {}).get("status") == "known")
    stats["release_unknown"] = sum(1 for item in updated["records"] if item.get("release", {}).get("status") != "known")
    updated["statistics"] = stats
    return updated


def merge_source_records_into_payload(payload: dict[str, Any], source_path: Path) -> dict[str, Any]:
    source = merged_source_payload(source_path)
    source_records = [normalize_input_record(item) for item in source.get("records", [])]
    updated = merge_catalog_records_into_payload(payload, source_records)
    updated["scope"] = source.get("scope", LANGUAGE_ORDER)
    updated["taxonomy"] = source.get("taxonomy", TAXONOMY)
    updated["source_catalog"] = str(source_path)
    updated["source_catalog_id"] = source.get("catalog_id", updated.get("source_catalog_id", ""))
    updated["source_catalog_version"] = source.get("catalog_version", updated.get("source_catalog_version", ""))
    updated["extension_catalog"] = source.get("extension_catalog", updated.get("extension_catalog", ""))
    updated["extension_catalog_id"] = source.get("extension_catalog_id", updated.get("extension_catalog_id", ""))
    updated["target_records"] = max(int(updated.get("target_records", 0) or 0), int(source.get("statistics", {}).get("target_control_unique_entities", DEFAULT_TARGET_RECORDS)))
    stats = dict(updated.get("statistics", {}))
    stats["source_records"] = len(source_records)
    stats["normalized_identities"] = len(updated["records"])
    stats["release_known"] = sum(1 for item in updated["records"] if item.get("release", {}).get("status") == "known")
    stats["release_unknown"] = sum(1 for item in updated["records"] if item.get("release", {}).get("status") != "known")
    updated["statistics"] = stats
    return updated


def should_enrich(record: dict[str, Any]) -> bool:
    if record.get("source") in {
        "crates_io",
        "npm_registry",
        "pypi_simple",
        "cran_packages_by_date",
        "nuget_search",
        "pub_dev",
        "go_module_index",
        "packagist_search",
        "maven_central_search",
        "cocoapods_cdn",
        "octave_packages_index",
    } and (
        record["release"]["status"] == "known"
        or record.get("nightly", {}).get("status") == "known"
    ):
        return False
    if record.get("source") == "julia_general":
        return False
    if record["catalog_branch"] in {
        "Python",
        "Rust",
        "Julia",
        "Node.js/JavaScript",
        "Node.js/TypeScript",
        "R",
        "Haskell",
        "Dart",
        "Go",
        "C-Sharp",
        "PHP",
        "SAPJava",
        "Cocoa",
        "Octave",
    }:
        return True
    url = record.get("canonical_url") or record.get("source_url") or ""
    return bool(parse_github_repo(url))


def load_enriched_or_source(source_path: Path) -> dict[str, Any]:
    if ENRICHED_JSON.exists():
        return merge_source_records_into_payload(read_json(ENRICHED_JSON), source_path)
    source = merged_source_payload(source_path)
    records = merge_records([normalize_input_record(item) for item in source.get("records", [])])
    return {
        "generated_at": now_iso(),
        "source_catalog": str(source_path),
        "source_catalog_id": source.get("catalog_id", ""),
        "source_catalog_version": source.get("catalog_version", ""),
        "extension_catalog": source.get("extension_catalog", ""),
        "extension_catalog_id": source.get("extension_catalog_id", ""),
        "scope": source.get("scope", LANGUAGE_ORDER),
        "taxonomy": source.get("taxonomy", TAXONOMY),
        "target_records": source.get("statistics", {}).get("target_control_unique_entities", DEFAULT_TARGET_RECORDS),
        "statistics": {
            "source_records": len(source.get("records", [])),
            "normalized_identities": len(records),
            "expanded_records": 0,
            "release_checked": 0,
            "release_known": 0,
            "release_unknown": len(records),
            "fetch_errors": 0,
        },
        "fetch_errors": [],
        "records": records,
    }


def render(source_path: Path) -> dict[str, Any]:
    payload = compact_payload_for_storage(load_enriched_or_source(source_path))
    export_to_sqlite(payload)
    write_json(ENRICHED_JSON, payload)
    records = payload["records"]
    clean_generated_catalog()
    write_text(ROOT / "README.md", render_root_readme(payload))
    write_text(CATALOG_DIR / "index.md", render_catalog_index(payload))
    write_text(CATALOG_DIR / "release-watch.md", render_release_watch(payload))
    write_text(LICENSE_INDEX_MD, render_license_index(payload))
    write_text(CATALOG_DIR / "provenance.md", render_provenance(payload))
    write_text(CATALOG_DIR / "source-map.md", render_source_map(payload))
    write_text(REPORT_MD, render_enrichment_report(payload))
    render_language_pages(records)
    render_category_pages(records)
    render_record_pages(records)
    return payload


def clean_generated_catalog() -> None:
    for relative in ("by-language", "by-category", "records"):
        path = CATALOG_DIR / relative
        if path.exists():
            shutil.rmtree(path)


def render_root_readme(payload: dict[str, Any]) -> str:
    stats = payload.get("statistics", {})
    generated = payload.get("generated_at", "")
    scope = [normalize_branch(item) for item in payload.get("scope", LANGUAGE_ORDER)]
    scope = [item for item in LANGUAGE_ORDER if item in set(scope)]
    counts = count_categories(payload.get("records", []))
    return f"""# UNICAGD Programming Systems Discovery Catalog

Generated: `{generated}`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

{category_index_block(counts, "catalog/by-category/")}

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | {stats.get("source_records", 0)} |
| Canonical identity pages | {stats.get("normalized_identities", len(payload.get("records", [])))} |
| Expansion records added | {stats.get("expanded_records", 0)} |
| Release checks attempted | {stats.get("release_checked", 0)} |
| Known stable release fields | {stats.get("release_known", 0)} |
| Unknown stable release fields | {stats.get("release_unknown", 0)} |
| Fetch errors recorded | {stats.get("fetch_errors", 0)} |
| Target identity count | {payload.get("target_records", DEFAULT_TARGET_RECORDS)} |

## Language Scope

{bullet_list(scope)}

## Update Commands

```bash
python3 tools/build_catalog.py all
python3 tools/build_catalog.py enrich
python3 tools/build_catalog.py render
python3 tools/build_catalog.py check
```

The generated pages are intentionally explicit about uncertainty. Unknown release dates are kept visible with a reason, because the corpus is for operational decisions, not optimistic summaries.
"""


def render_catalog_index(payload: dict[str, Any]) -> str:
    records = payload["records"]
    by_language = defaultdict(list)
    by_category = defaultdict(list)
    for record in records:
        by_language[record["catalog_branch"]].append(record)
        by_category[record["category"]].append(record)
    counts = count_categories(records)
    lines = [
        "# Catalog Index",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
        "",
        "[Release watch](release-watch.md) · [Apache/MIT license index](license-index.md) · [Provenance](provenance.md) · [Source map](source-map.md)",
        "",
        category_index_block(counts, "by-category/"),
        "",
        "## Languages",
        "",
        "| Language | Records | Known stable releases | Page |",
        "| --- | ---: | ---: | --- |",
    ]
    for branch in LANGUAGE_ORDER:
        items = by_language.get(branch, [])
        if not items:
            continue
        known = sum(1 for item in items if item["release"]["status"] == "known")
        path = f"by-language/{slugify(branch)}.md"
        lines.append(f"| {md_escape(branch)} | {len(items)} | {known} | [{md_escape(branch)}]({path}) |")
    lines.extend(["", "## Category Details", "", "| Category | Records | Page |", "| --- | ---: | --- |"])
    for category in sorted(by_category):
        items = by_category[category]
        path = f"by-category/{slugify(category)}.md"
        lines.append(f"| {md_escape(label(category))} | {len(items)} | [{md_escape(category)}]({path}) |")
    lines.extend(
        [
            "",
            "## High-Signal Release Coverage",
            "",
            "| Language | Known | Unknown |",
            "| --- | ---: | ---: |",
        ]
    )
    for branch in LANGUAGE_ORDER:
        items = by_language.get(branch, [])
        if not items:
            continue
        known = sum(1 for item in items if item["release"]["status"] == "known")
        lines.append(f"| {md_escape(branch)} | {known} | {len(items) - known} |")
    return "\n".join(lines)


def render_language_pages(records: list[dict[str, Any]]) -> None:
    by_language = defaultdict(list)
    counts = count_categories(records)
    for record in records:
        by_language[record["catalog_branch"]].append(record)
    for branch, items in by_language.items():
        by_category = defaultdict(list)
        for record in items:
            by_category[record["category"]].append(record)
        lines = [
            f"# {branch}",
            "",
            f"Records: `{len(items)}`",
            "",
            "## Navigation",
            "",
            f"[Catalog index](../index.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)",
            "",
            category_index_block(counts, "../by-category/"),
            "",
            "## Categories",
            "",
        ]
        for category in sorted(by_category):
            category_items = by_category[category]
            lines.append(f"### {label(category)}")
            lines.append("")
            lines.append("| Name | Release | Date | Source |")
            lines.append("| --- | --- | --- | --- |")
            for record in sorted(category_items, key=lambda item: item["name"].lower()):
                rel = record["release"]
                release = rel.get("version") or rel.get("status") or "unknown"
                date = rel.get("date") or rel.get("reason") or "unknown"
                link = f"../records/{record['slug']}.md"
                source = source_label(record)
                lines.append(f"| [{md_escape(record['name'])}]({link}) | {md_escape(release)} | {md_escape(date)} | {md_escape(source)} |")
            lines.append("")
        write_text(CATALOG_DIR / "by-language" / f"{slugify(branch)}.md", "\n".join(lines))


def render_category_pages(records: list[dict[str, Any]]) -> None:
    by_category = defaultdict(list)
    counts = count_categories(records)
    for record in records:
        by_category[record["category"]].append(record)
    for category, items in by_category.items():
        by_language = defaultdict(list)
        for record in items:
            by_language[record["catalog_branch"]].append(record)
        lines = [
            f"# {label(category)}",
            "",
            f"Records: `{len(items)}`",
            "",
            "## Navigation",
            "",
            f"[Catalog index](../index.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)",
            "",
            category_index_block(counts, "", current_category=category),
            "",
        ]
        for branch in LANGUAGE_ORDER:
            branch_items = by_language.get(branch)
            if not branch_items:
                continue
            lines.append(f"## {branch}")
            lines.append("")
            lines.append("| Name | Release | Date | Page |")
            lines.append("| --- | --- | --- | --- |")
            for record in sorted(branch_items, key=lambda item: item["name"].lower()):
                rel = record["release"]
                release = rel.get("version") or rel.get("status") or "unknown"
                date = rel.get("date") or rel.get("reason") or "unknown"
                link = f"../records/{record['slug']}.md"
                lines.append(f"| {md_escape(record['name'])} | {md_escape(release)} | {md_escape(date)} | [open]({link}) |")
            lines.append("")
        write_text(CATALOG_DIR / "by-category" / f"{slugify(category)}.md", "\n".join(lines))


def render_record_pages(records: list[dict[str, Any]]) -> None:
    related_by_branch_category = defaultdict(list)
    counts = count_categories(records)
    for record in records:
        related_by_branch_category[(record["catalog_branch"], record["category"])].append(record)
    for record in records:
        related = [
            item
            for item in related_by_branch_category[(record["catalog_branch"], record["category"])]
            if item["identity_key"] != record["identity_key"]
        ][:8]
        write_text(CATALOG_DIR / "records" / f"{record['slug']}.md", render_record_page(record, related, counts))


def render_record_page(
    record: dict[str, Any],
    related: list[dict[str, Any]],
    counts: Counter[str],
) -> str:
    rel = record.get("release", unknown_release("not_checked"))
    nightly = record.get("nightly", unknown_release("not_checked"))
    description = plain_markdown_text(record.get("description"))
    if len(description) < 24:
        description = generated_description(record)
    canonical = record.get("canonical_url") or ""
    source_ids = record.get("source_record_ids", [record.get("id", "")])
    lines = [
        f"# {record['name']}",
        "",
        "## Navigation",
        "",
        record_navigation(record),
        "",
        "## Identity",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Language branch | {md_escape(record['catalog_branch'])} |",
        f"| Category | {md_escape(label(record['category']))} |",
        f"| Source type | {md_escape(record.get('source_record_type', ''))} |",
        f"| Verification | {md_escape(record.get('verification_status') or source_label(record))} |",
        f"| Canonical URL | {markdown_link(canonical)} |",
        f"| Source record ids | {md_escape(', '.join(source_ids))} |",
        "",
        "## System Engineer Summary",
        "",
        wrap_md(description),
        "",
        "## Operational Role",
        "",
        wrap_md(operational_role(record)),
        "",
        "## Release Intelligence",
        "",
        "| Channel | Status | Version | Date | Source | Reason |",
        "| --- | --- | --- | --- | --- | --- |",
        release_row("stable", rel),
        release_row(nightly.get("channel") or "preview/nightly", nightly),
        "",
        "## License And Use Alert",
        "",
        license_summary(record),
        "",
        "## Engineering Notes",
        "",
        bullet_list(engineering_notes(record)),
        "",
        "## Provenance",
        "",
        provenance_table(record.get("provenance", [])),
        "",
        "## Evidence",
        "",
        evidence_summary(record),
    ]
    if related:
        lines.extend(["", "## Related Records", "", "| Name | Category | Page |", "| --- | --- | --- |"])
        for item in related:
            lines.append(
                f"| {md_escape(item['name'])} | {md_escape(label(item['category']))} | [open]({item['slug']}.md) |"
            )
    lines.extend(["", category_index_block(counts, "../by-category/", current_category=record["category"])])
    return "\n".join(lines)


def generated_description(record: dict[str, Any]) -> str:
    return (
        f"{record['name']} is tracked as {indefinite(label(record['category']).lower())} "
        f"record in the {record['catalog_branch']} branch. The source did not provide a "
        "long description, so this page keeps the identity, release state, provenance, "
        "and operational classification explicit for later enrichment."
    )


def indefinite(phrase: str) -> str:
    return ("an " if phrase[:1].lower() in "aeiou" else "a ") + phrase


def operational_role(record: dict[str, Any]) -> str:
    category = record["category"]
    branch = record["catalog_branch"]
    name = record["name"]
    role = {
        "compiler": "compiler selection, diagnostics behavior, target support, ABI expectations, and build reproducibility",
        "interpreter_runtime": "runtime behavior, deployment packaging, embedding, upgrade cadence, and compatibility validation",
        "build_system": "build graph control, artifact reproducibility, cross-platform build policy, and CI integration",
        "package_manager": "dependency acquisition, lockfile policy, provenance control, and supply-chain monitoring",
        "linter": "static feedback, style policy, defect prevention, and local/CI quality gates",
        "static_analyzer": "defect discovery, security review, undefined-state detection, and regression prevention",
        "type_checker": "interface contracts, migration safety, editor feedback, and large-codebase maintainability",
        "formatter": "low-noise code review, style consistency, and automation-friendly editing",
        "security_sast": "supply-chain review, vulnerability detection, and release gate enforcement",
        "language_server": "editor intelligence, refactoring assistance, diagnostics, and navigation",
        "debugger": "fault isolation, live inspection, breakpoints, and production-adjacent diagnosis",
        "profiler": "hot-path discovery, allocation analysis, latency control, and capacity planning",
        "testing_framework": "unit/integration validation, regression protection, and release confidence",
        "fuzzer": "input-space exploration, parser hardening, and unsafe edge-case discovery",
        "documentation": "operator onboarding, API understanding, and upgrade review",
        "parser_lexer_ast": "language tooling, code generation, static analysis, and source transformation",
        "serialization": "wire formats, persistence, interoperability, and compatibility boundaries",
        "ffi_bindings": "cross-language integration, ABI ownership, memory safety, and runtime embedding",
        "async_runtime": "concurrency scheduling, I/O throughput, cancellation, and latency management",
        "networking_http": "service communication, clients/servers, protocol handling, and edge integration",
        "web_framework": "request routing, middleware policy, service structure, and deployment surface",
        "database_datastore": "state persistence, migrations, performance, and operational recovery",
        "logging_observability": "diagnostics, metrics, auditability, tracing, and incident response",
        "cryptography": "confidentiality, integrity, authentication, and key-management risk",
        "machine_learning": "model pipelines, numerical runtime constraints, and data/deployment interfaces",
        "embedded_hardware": "device constraints, cross-compilation, driver behavior, and field upgrades",
    }.get(category, "ecosystem capability mapping, dependency review, release awareness, and operational fit assessment")
    return f"For a systems engineer, {name} belongs in the {branch} inventory as part of {role}."


def engineering_notes(record: dict[str, Any]) -> list[str]:
    release = record.get("release", {})
    notes = [
        f"Treat category as `{record['category']}` unless a later verified source gives a better classification.",
        "Keep provenance attached when merging duplicate identities; source evidence is not disposable.",
    ]
    if release.get("status") == "known":
        notes.append(
            f"Latest stable metadata was observed from `{release.get('source')}` at `{release.get('checked_at')}`."
        )
    else:
        notes.append(
            f"Stable release is unknown because `{release.get('reason', 'no reason recorded')}`."
        )
    nightly = record.get("nightly", {})
    if nightly.get("status") == "known":
        notes.append(
            f"Preview/nightly metadata is present through channel `{nightly.get('channel')}`."
        )
    else:
        notes.append(
            f"Preview/nightly metadata is unknown because `{nightly.get('reason', 'no reason recorded')}`."
        )
    if not record.get("canonical_url"):
        notes.append("No canonical URL is verified yet; resolve before using this as an authoritative dependency identity.")
    return notes


def markdown_link(url: str) -> str:
    if not url:
        return "unknown"
    if not is_http_url(url):
        return md_escape(url)
    escaped = md_escape(url)
    return f"[{escaped}]({url})"


def release_row(label_text: str, release: dict[str, Any]) -> str:
    return (
        f"| {md_escape(label_text)} | {md_escape(release.get('status', 'unknown'))} | "
        f"{md_escape(release.get('version', ''))} | {md_escape(release.get('date', ''))} | "
        f"{markdown_link(clean_text(release.get('source')))} | {md_escape(release.get('reason', ''))} |"
    )


def provenance_table(provenance: list[dict[str, Any]]) -> str:
    if not provenance:
        return "No provenance entries recorded."
    lines = ["| Kind | Status | Date | Detail |", "| --- | --- | --- | --- |"]
    for item in provenance:
        kind = clean_text(item.get("kind"))
        status = clean_text(item.get("status"))
        date = clean_text(item.get("retrieved") or item.get("as_of"))
        detail = json.dumps(item, ensure_ascii=False, sort_keys=True)
        lines.append(f"| {md_escape(kind)} | {md_escape(status)} | {md_escape(date)} | `{md_escape(detail)}` |")
    return "\n".join(lines)


def evidence_summary(record: dict[str, Any]) -> str:
    evidence = record.get("evidence", [])
    if not evidence:
        raw = record.get("raw", {})
        if raw:
            return f"Raw evidence is compacted in `{ENRICHED_JSON.relative_to(ROOT)}` for repository-size control."
        return "No additional raw evidence recorded."
    lines = [f"Evidence records merged into this identity: `{len(evidence)}`.", ""]
    for item in evidence[:10]:
        lines.append(f"- `{item.get('id')}` from `{item.get('source')}` as `{item.get('source_record_type')}`")
    if len(evidence) > 10:
        lines.append(f"- {len(evidence) - 10} more evidence records omitted from this summary.")
    return "\n".join(lines)


def source_label(record: dict[str, Any]) -> str:
    if record.get("verification_status"):
        return record["verification_status"]
    source = record.get("source")
    if source and source != "master_json":
        return source
    provenance = record.get("provenance") or []
    if provenance:
        return clean_text(provenance[0].get("status") or provenance[0].get("kind"))
    return "preserved"


def flatten_license_value(value: Any) -> list[str]:
    values: list[str] = []
    if value is None:
        return values
    if isinstance(value, str):
        cleaned = clean_text(value)
        if cleaned:
            values.append(cleaned)
        return values
    if isinstance(value, list):
        for item in value:
            values.extend(flatten_license_value(item))
        return values
    if isinstance(value, dict):
        for key in ("type", "name", "identifier", "expression", "license", "url", "file"):
            if key in value:
                values.extend(flatten_license_value(value.get(key)))
        if not values:
            cleaned = clean_text(json.dumps(value, ensure_ascii=False, sort_keys=True))
            if cleaned:
                values.append(cleaned)
    return values


def record_license_values(record: dict[str, Any]) -> list[str]:
    cache_key = id(record)
    if cache_key in LICENSE_VALUES_CACHE:
        return list(LICENSE_VALUES_CACHE[cache_key])
    values: list[str] = []

    def collect(value: Any, parent_key: str = "") -> None:
        lower_key = parent_key.lower()
        if lower_key in {"license", "licenses", "licenseexpression", "license_expression", "licenseurl", "license_url"}:
            values.extend(flatten_license_value(value))
            return
        if isinstance(value, dict):
            for key, nested in value.items():
                collect(nested, clean_text(key))
        elif isinstance(value, list):
            for item in value:
                collect(item, parent_key)
        elif parent_key.lower() == "classifiers":
            text = clean_text(value)
            if "license" in text.lower():
                values.append(text)

    for field in ("license", "licenses", "license_expression", "license_url"):
        values.extend(flatten_license_value(record.get(field)))
    values.extend(flatten_license_value(record.get("license_evidence")))
    collect(record.get("release_source_metadata", {}))
    collect(record.get("raw", {}))
    for evidence in record.get("evidence", [])[:8]:
        if isinstance(evidence, dict):
            collect(evidence.get("raw", {}))
            collect(evidence.get("release_source_metadata", {}))
    unique = []
    seen = set()
    for value in values:
        cleaned = clean_text(value)
        if not cleaned or cleaned.lower() in seen:
            continue
        seen.add(cleaned.lower())
        unique.append(cleaned)
    LICENSE_VALUES_CACHE[cache_key] = list(unique)
    return unique


def license_family(record: dict[str, Any]) -> str:
    values = record_license_values(record)
    if not values:
        return "unknown"
    haystack = " | ".join(values).lower()
    has_apache = bool(re.search(r"\bapache(?: license)?(?:[- ]?2(?:\.0)?)?\b|apache-2\.0", haystack))
    has_mit = bool(re.search(r"\bmit\b|mit license", haystack))
    has_other_permissive = any(
        term in haystack
        for term in (
            "bsd",
            "isc",
            "zlib",
            "0bsd",
            "unlicense",
            "public domain",
            "cc0",
            "postgresql license",
            "python software foundation",
        )
    )
    has_review = any(
        term in haystack
        for term in (
            "gpl",
            "agpl",
            "lgpl",
            "mpl",
            "epl",
            "cddl",
            "sspl",
            "server side public",
            "business source",
            "busl",
            "bsl",
            "commons clause",
            "elastic license",
            "polyform",
            "proprietary",
            "commercial",
            "oracle",
        )
    )
    if has_review and (has_apache or has_mit or has_other_permissive):
        return "mixed_review"
    if has_review:
        return "restricted_review"
    if has_apache:
        return "apache-2.0"
    if has_mit:
        return "mit"
    if has_other_permissive:
        return "permissive_other"
    return "unknown"


def license_family_label(family: str) -> str:
    return {
        "apache-2.0": "Apache-2.0",
        "mit": "MIT",
        "permissive_other": "Other permissive",
        "mixed_review": "Mixed license review",
        "restricted_review": "Backup plan required",
        "unknown": "Unknown license",
    }.get(family, family)


def license_alert(record: dict[str, Any]) -> str:
    family = license_family(record)
    if family == "apache-2.0":
        return "Showcase candidate: permissive Apache-2.0 family; keep notices and patent/license obligations visible."
    if family == "mit":
        return "Showcase candidate: permissive MIT family; keep copyright and permission notices attached."
    if family == "permissive_other":
        return "Permissive but not Apache/MIT; acceptable in many stacks, but do a policy check before presenting it as Apache/MIT."
    if family == "mixed_review":
        return "Backup plan: mixed expression or dual license detected; choose the permissive option only when the exact terms allow it."
    if family == "restricted_review":
        return "Backup plan required before embedding, redistributing, or modifying architecture around this dependency."
    return "Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility."


def license_summary(record: dict[str, Any]) -> str:
    values = record_license_values(record)
    family = license_family(record)
    lines = [
        "| Field | Value |",
        "| --- | --- |",
        f"| Detected family | {md_escape(license_family_label(family))} |",
        f"| Evidence | {md_escape('; '.join(values) if values else 'unknown')} |",
        f"| Alert | {md_escape(license_alert(record))} |",
    ]
    return "\n".join(lines)


def license_row(record: dict[str, Any], release_field: str = "release") -> str:
    release = record.get(release_field, {})
    release_text = release.get("version") or release.get("status") or "unknown"
    date = release.get("date") or release.get("reason") or "unknown"
    link = f"records/{record['slug']}.md"
    return (
        f"| [{md_escape(record['name'])}]({link}) | {md_escape(record['catalog_branch'])} | "
        f"{md_escape(label(record['category']))} | {md_escape(release_text)} | {md_escape(date)} | "
        f"{md_escape('; '.join(record_license_values(record)) or 'unknown')} |"
    )


def sorted_release_records(records: list[dict[str, Any]], release_field: str) -> list[dict[str, Any]]:
    return sorted(
        records,
        key=lambda item: (
            item.get(release_field, {}).get("status") == "known",
            item.get(release_field, {}).get("date") or "",
            item.get("name", "").lower(),
        ),
        reverse=True,
    )


def render_license_table(records: list[dict[str, Any]], release_field: str, limit: int = 250) -> list[str]:
    lines = ["| Name | Language | Category | Version | Date | License Evidence |", "| --- | --- | --- | --- | --- | --- |"]
    if not records:
        lines.append("| None verified |  |  |  |  |  |")
        return lines
    for record in sorted_release_records(records, release_field)[:limit]:
        lines.append(license_row(record, release_field))
    return lines


def render_backup_license_table(records: list[dict[str, Any]], limit: int = 300) -> list[str]:
    lines = ["| Name | Language | Category | Family | Alert | Page |", "| --- | --- | --- | --- | --- | --- |"]
    for record in records[:limit]:
        lines.append(
            f"| {md_escape(record['name'])} | {md_escape(record['catalog_branch'])} | "
            f"{md_escape(label(record['category']))} | {md_escape(license_family_label(license_family(record)))} | "
            f"{md_escape(license_alert(record))} | [open](records/{record['slug']}.md) |"
        )
    if not records:
        lines.append("| None flagged |  |  |  |  |  |")
    return lines


def render_license_index(payload: dict[str, Any]) -> str:
    records = payload.get("records", [])
    families = Counter(license_family(record) for record in records)
    apache = [record for record in records if license_family(record) == "apache-2.0"]
    mit = [record for record in records if license_family(record) == "mit"]
    apache_preview = [record for record in apache if record.get("nightly", {}).get("status") in {"known", "partial"}]
    mit_preview = [record for record in mit if record.get("nightly", {}).get("status") in {"known", "partial"}]
    backup = [
        record
        for record in records
        if license_family(record) in {"mixed_review", "restricted_review", "unknown"}
    ]
    backup.sort(key=lambda record: (license_family(record), record["catalog_branch"], record["name"].lower()))
    lines = [
        "# License Index",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
        "",
        "This page is a license-oriented discovery view. It highlights Apache-2.0 and MIT candidates, keeps preview/nightly signals visible, and raises a backup-plan alert when the catalog cannot prove that a component fits those two license families.",
        "",
        category_index_block(count_categories(records), "by-category/"),
        "",
        "## License Family Counts",
        "",
        "| Family | Records |",
        "| --- | ---: |",
    ]
    for family, count in families.most_common():
        lines.append(f"| {md_escape(license_family_label(family))} | {count} |")
    lines.extend(
        [
            "",
        "## Apache-2.0 Showcase",
        "",
        "Apache-2.0 is useful for projects that want permissive reuse plus an explicit patent grant and NOTICE discipline. It is common in foundations, infrastructure vendors, cloud projects, language/runtime teams, enterprise platform teams, government-funded open systems, and maintainers who expect broad redistribution. Primary references: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) and [SPDX Apache-2.0](https://spdx.org/licenses/Apache-2.0.html).",
            "",
            "### Apache Stable Releases",
            "",
            *render_license_table([record for record in apache if record.get("release", {}).get("status") in {"known", "partial"}], "release"),
            "",
            "### Apache Preview And Nightly Signals",
            "",
            *render_license_table(apache_preview, "nightly"),
            "",
        "## MIT Showcase",
        "",
        "MIT is useful for compact permissive reuse where the main operational requirement is preserving copyright and permission notices. It is common with individual maintainers, small libraries, startups, web tooling, language packages, prototypes, education, research code, and components meant to be embedded with minimal license machinery. Primary reference: [SPDX MIT](https://spdx.org/licenses/MIT.html).",
            "",
            "### MIT Stable Releases",
            "",
            *render_license_table([record for record in mit if record.get("release", {}).get("status") in {"known", "partial"}], "release"),
            "",
            "### MIT Preview And Nightly Signals",
            "",
            *render_license_table(mit_preview, "nightly"),
            "",
            "## Backup Plan Alerts",
            "",
            "Use this section before architecture decisions. If a dependency is restricted, mixed, commercial, or unknown, prefer one of these plans: replace it with an Apache-2.0/MIT alternative; isolate it behind a service boundary; keep it out of distributable client code; negotiate a commercial license; or require SBOM/legal review before adoption.",
            "",
            *render_backup_license_table(backup),
            "",
            "## Practical Selection Checklist",
            "",
            "- For an Apache-2.0-first architecture, keep NOTICE files and patent-grant expectations visible in dependency review.",
            "- For an MIT-first architecture, preserve copyright and permission notices in redistributed source and binary bundles.",
            "- For unknown licenses, treat the component as blocked until a primary package, repository, or vendor source proves the license.",
            "- For copyleft, source-available, commercial, or mixed expressions, design a replace-or-isolate path before implementation depends on it.",
        ]
    )
    return "\n".join(lines)


def wrap_md(text: str, width: int = 100) -> str:
    text = plain_markdown_text(text)
    return "\n".join(textwrap.wrap(text, width=width)) if text else ""


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None"


def count_categories(records: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for record in records:
        category = clean_text(record.get("category"))
        if category:
            counts[category] += 1
    return counts


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def category_index_block(
    counts: Counter[str],
    link_prefix: str,
    *,
    current_category: str = "",
) -> str:
    lines = ["## Category Index", ""]
    if not counts:
        lines.append("No category records available.")
        return "\n".join(lines)
    links = []
    for category in sorted(counts):
        text = f"{label(category)} ({counts[category]})"
        href = f"{link_prefix}{slugify(category)}.md"
        link_text = f"[{md_escape(text)}]({href})"
        links.append(f"**{link_text}**" if category == current_category else link_text)
    for group in chunked(links, 4):
        lines.append(" · ".join(group))
    return "\n".join(lines)


def record_navigation(record: dict[str, Any]) -> str:
    branch = record["catalog_branch"]
    category = record["category"]
    return (
        f"[Catalog index](../index.md) · "
        f"[Language: {md_escape(branch)}](../by-language/{slugify(branch)}.md) · "
        f"[Category: {md_escape(label(category))}](../by-category/{slugify(category)}.md) · "
        "[Release watch](../release-watch.md) · "
        "[Apache/MIT license index](../license-index.md)"
    )


def render_release_watch(payload: dict[str, Any]) -> str:
    records = payload["records"]
    known = [item for item in records if item["release"]["status"] == "known"]
    unknown = [item for item in records if item["release"]["status"] != "known"]
    known.sort(key=lambda item: item["release"].get("date") or "", reverse=True)
    reason_counts = Counter(item["release"].get("reason", "unknown") for item in unknown)
    lines = [
        "# Release Watch",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
        "",
        "[Catalog index](index.md) · [Apache/MIT license index](license-index.md) · [Provenance](provenance.md)",
        "",
        category_index_block(count_categories(records), "by-category/"),
        "",
        "## Coverage",
        "",
        "| State | Count |",
        "| --- | ---: |",
        f"| Known stable release | {len(known)} |",
        f"| Unknown stable release | {len(unknown)} |",
        "",
        "## Newest Known Stable Metadata",
        "",
        "| Name | Language | Category | Version | Date | Page |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in known[:250]:
        release = record["release"]
        lines.append(
            f"| {md_escape(record['name'])} | {md_escape(record['catalog_branch'])} | {md_escape(label(record['category']))} | "
            f"{md_escape(release.get('version'))} | {md_escape(release.get('date'))} | [open](records/{record['slug']}.md) |"
        )
    lines.extend(["", "## Unknown Reasons", "", "| Reason | Count |", "| --- | ---: |"])
    for reason, count in reason_counts.most_common():
        lines.append(f"| {md_escape(reason)} | {count} |")
    lines.extend(["", "## Preview And Nightly Signals", "", "| Name | Language | Channel | Version | Date | Page |", "| --- | --- | --- | --- | --- | --- |"])
    preview_records = [item for item in records if item.get("nightly", {}).get("status") == "known"]
    preview_records.sort(key=lambda item: item["nightly"].get("date") or "", reverse=True)
    if not preview_records:
        lines.append("| None verified |  |  |  |  |  |")
    for record in preview_records[:250]:
        nightly = record["nightly"]
        lines.append(
            f"| {md_escape(record['name'])} | {md_escape(record['catalog_branch'])} | {md_escape(nightly.get('channel'))} | "
            f"{md_escape(nightly.get('version'))} | {md_escape(nightly.get('date'))} | [open](records/{record['slug']}.md) |"
        )
    return "\n".join(lines)


def render_provenance(payload: dict[str, Any]) -> str:
    records = payload["records"]
    provenance_counts = Counter()
    source_counts = Counter()
    for record in records:
        source_counts[source_label(record)] += 1
        for item in record.get("provenance", []):
            provenance_counts[(clean_text(item.get("kind")), clean_text(item.get("status")))] += 1
    lines = [
        "# Provenance And Confidence",
        "",
        "This catalog preserves discovered evidence and marks uncertainty explicitly. A record with an unknown release is still useful as a tracked identity, but it is not release-authoritative until a primary source fills the release fields.",
        "",
        "[Catalog index](index.md) · [Release watch](release-watch.md) · [Apache/MIT license index](license-index.md)",
        "",
        category_index_block(count_categories(records), "by-category/"),
        "",
        "## Source Labels",
        "",
        "| Label | Records |",
        "| --- | ---: |",
    ]
    for source, count in source_counts.most_common():
        lines.append(f"| {md_escape(source)} | {count} |")
    lines.extend(["", "## Provenance Kinds", "", "| Kind | Status | Records |", "| --- | --- | ---: |"])
    for (kind, status), count in provenance_counts.most_common():
        lines.append(f"| {md_escape(kind)} | {md_escape(status)} | {count} |")
    lines.extend(
        [
            "",
            "## Fetch Errors",
            "",
        ]
    )
    errors = payload.get("fetch_errors", [])
    if not errors:
        lines.append("No fetch errors recorded.")
    else:
        for error in errors[:200]:
            lines.append(f"- `{md_escape(error)}`")
        if len(errors) > 200:
            lines.append(f"- {len(errors) - 200} more errors omitted.")
    return "\n".join(lines)


def render_enrichment_report(payload: dict[str, Any]) -> str:
    stats = payload.get("statistics", {})
    records = payload.get("records", [])
    lines = [
        "# Enrichment Report",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
        "",
        "[Catalog index](index.md) · [Release watch](release-watch.md) · [Apache/MIT license index](license-index.md)",
        "",
        category_index_block(count_categories(records), "by-category/"),
        "",
        "| Metric | Count |",
        "| --- | ---: |",
    ]
    for key, value in stats.items():
        lines.append(f"| {md_escape(key)} | {value} |")
    lines.extend(["", "## Fetch Errors", ""])
    errors = payload.get("fetch_errors", [])
    if not errors:
        lines.append("No fetch errors recorded.")
    else:
        for error in errors[:200]:
            lines.append(f"- `{md_escape(error)}`")
        if len(errors) > 200:
            lines.append(f"- {len(errors) - 200} more errors omitted.")
    return "\n".join(lines)


def render_source_map(payload: dict[str, Any]) -> str:
    records = payload["records"]
    rows = []
    for record in records:
        for source_id in record.get("source_record_ids", [record.get("id", "")]):
            rows.append((source_id, record))
    rows.sort(key=lambda item: item[0])
    lines = [
        "# Source Record Map",
        "",
        "[Catalog index](index.md) · [Release watch](release-watch.md) · [Apache/MIT license index](license-index.md)",
        "",
        category_index_block(count_categories(records), "by-category/"),
        "",
        "| Source record id | Identity | Page |",
        "| --- | --- | --- |",
    ]
    for source_id, record in rows:
        lines.append(f"| `{md_escape(source_id)}` | {md_escape(record['name'])} | [open](records/{record['slug']}.md) |")
    return "\n".join(lines)


def check(source_path: Path) -> int:
    failures: list[str] = []
    if not ENRICHED_JSON.exists():
        failures.append(f"Missing {ENRICHED_JSON}")
    if not (ROOT / "README.md").exists():
        failures.append("Missing README.md")
    payload = load_enriched_or_source(source_path)
    for record in payload["records"]:
        page = CATALOG_DIR / "records" / f"{record['slug']}.md"
        if not page.exists():
            failures.append(f"Missing record page: {page}")
    source = merged_source_payload(source_path)
    source_ids = {clean_text(item.get("id")) for item in source.get("records", []) if item.get("id")}
    mapped_ids = set()
    for record in payload["records"]:
        mapped_ids.update(record.get("source_record_ids", []))
    missing_source_ids = sorted(source_ids - mapped_ids)
    if missing_source_ids:
        failures.append(f"Missing source id mappings: {', '.join(missing_source_ids[:20])}")
    scope = {normalize_branch(item) for item in source.get("scope", LANGUAGE_ORDER)}
    invalid_branches = sorted({record["catalog_branch"] for record in payload["records"]} - scope)
    if invalid_branches:
        failures.append(f"Unexpected language branches: {', '.join(invalid_branches)}")
    failures.extend(check_markdown_links())
    if failures:
        for failure in failures:
            print(f"CHECK FAIL: {failure}", file=sys.stderr)
        return 1
    print(
        f"CHECK OK: {len(payload['records'])} identity pages, {len(source_ids)} source records mapped."
    )
    return 0


def check_markdown_links() -> list[str]:
    failures: list[str] = []
    markdown_files = [ROOT / "README.md"]
    if CATALOG_DIR.exists():
        markdown_files.extend(CATALOG_DIR.rglob("*.md"))
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in markdown_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (path.parent / urllib.parse.unquote(target)).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                failures.append(f"Markdown link leaves repo: {path.relative_to(ROOT)} -> {raw_target}")
                continue
            if not candidate.exists():
                failures.append(f"Missing Markdown link target: {path.relative_to(ROOT)} -> {raw_target}")
    return failures[:200]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["render", "enrich", "all", "check", "recover", "sqlite"],
        help="Operation to run.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help="Path to master JSON. Defaults to repo data/source, then the original absolute path.",
    )
    parser.add_argument(
        "--target-records",
        type=int,
        default=None,
        help="Desired canonical identity count after expansion. Defaults to the source target or 9000.",
    )
    parser.add_argument(
        "--no-network",
        action="store_true",
        help="Disable registry and release HTTP fetches.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help="Concurrent release enrichment workers.",
    )
    parser.add_argument(
        "--cache-ttl",
        type=int,
        default=3600,
        help="HTTP cache TTL in seconds. Use 0 to disable HTTP cache reads and writes.",
    )
    parser.add_argument(
        "--max-enrich-records",
        type=int,
        default=1200,
        help="Cap per-run detailed release lookups. Expansion metadata is still used.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    source_path = args.source or default_source()
    if not source_path.exists():
        print(f"Source catalog not found: {source_path}", file=sys.stderr)
        return 2
    if source_path != LOCAL_SOURCE:
        copy_source_if_needed(source_path)
    source = merged_source_payload(source_path)
    target_records = args.target_records
    if target_records is None:
        target_records = int(source.get("statistics", {}).get("target_control_unique_entities", DEFAULT_TARGET_RECORDS))
    if args.command == "enrich":
        enrich_records(
            source_path,
            network=not args.no_network,
            target_records=target_records,
            workers=args.workers,
            cache_ttl=args.cache_ttl,
            max_enrich_records=args.max_enrich_records,
        )
        return 0
    if args.command == "render":
        render(source_path)
        return 0
    if args.command == "all":
        enrich_records(
            source_path,
            network=not args.no_network,
            target_records=target_records,
            workers=args.workers,
            cache_ttl=args.cache_ttl,
            max_enrich_records=args.max_enrich_records,
        )
        render(source_path)
        return check(source_path)
    if args.command == "check":
        return check(source_path)
    if args.command == "recover":
        if recover_from_sqlite(source_path):
            print(f"Recovered records from {SQLITE_DB}")
        else:
            print(f"No recovery needed or {SQLITE_DB} not found.")
        return 0
    if args.command == "sqlite":
        payload = load_enriched_or_source(source_path)
        count = export_to_sqlite(payload)
        print(f"Exported {count} records to {SQLITE_DB}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
