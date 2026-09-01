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
import hashlib
import html
import json
import os
import re
import shutil
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
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LOCAL_SOURCE = ROOT / "data" / "source" / "UNICAGD_programming_catalog_MASTER_FULL.json"
ORIGINAL_SOURCE = Path("/Users/peter/Intercom •refract/UNICAGD_programming_catalog_MASTER_FULL.json")
CATALOG_DIR = ROOT / "catalog"
ENRICHED_JSON = CATALOG_DIR / "enriched_records.json"
REPORT_MD = CATALOG_DIR / "enrichment_report.md"
HTTP_CACHE_DIR = ROOT / ".cache" / "catalog_http"

USER_AGENT = "catarepo-programming-catalog/1.0 (+https://github.com/local/catarepo)"
DEFAULT_TIMEOUT = 12
DEFAULT_TARGET_RECORDS = 9000
DEFAULT_WORKERS = 12

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
    tmp.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
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
    normalized = {
        "id": clean_text(record.get("id")) or stable_hash(json.dumps(record, sort_keys=True)),
        "source": "master_json",
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


class HttpCache:
    def __init__(
        self,
        cache_dir: Path,
        *,
        enabled: bool = True,
        ttl_seconds: int = 3600,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.cache_dir = cache_dir
        self.enabled = enabled
        self.ttl_seconds = ttl_seconds
        self.timeout = timeout
        self.errors: list[str] = []
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _key(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def _paths(self, url: str) -> tuple[Path, Path]:
        digest = self._key(url)
        return self.cache_dir / f"{digest}.body", self.cache_dir / f"{digest}.json"

    def get_bytes(self, url: str, *, accept: str = "application/json") -> bytes | None:
        body_path, meta_path = self._paths(url)
        if self.enabled and body_path.exists() and meta_path.exists():
            try:
                meta = read_json(meta_path)
                fetched_at = float(meta.get("fetched_at", 0))
                if time.time() - fetched_at <= self.ttl_seconds:
                    return body_path.read_bytes()
            except Exception:
                pass
        if not self.enabled:
            self.errors.append(f"network disabled: {url}")
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
    if ecosystem in {"pypi", "crates"}:
        if re.search(r"\s|/|\\|:", name):
            return ""
    if ecosystem == "npm":
        if re.search(r"\s|\\", name):
            return ""
    return name


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
    records: list[dict[str, Any]] = []
    for name in candidates:
        if len(records) >= limit:
            break
        stable, nightly, extra = pypi_release(fetcher, name)
        if stable["status"] == "unknown":
            continue
        normalized = extra.get("normalized_name", name)
        description = extra.get("summary", "")
        category = infer_category_from_text(normalized, description, "library")
        records.append(
            expansion_record(
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
        )
    return records


def expand_awesome_lists(fetcher: HttpCache, limit: int) -> list[dict[str, Any]]:
    sources = [
        ("Python", "https://raw.githubusercontent.com/vinta/awesome-python/master/README.md"),
        ("Rust", "https://raw.githubusercontent.com/rust-unofficial/awesome-rust/main/README.md"),
        ("C++23", "https://raw.githubusercontent.com/fffaraz/awesome-cpp/master/README.md"),
        ("Node.js/JavaScript", "https://raw.githubusercontent.com/sindresorhus/awesome-nodejs/main/readme.md"),
    ]
    records: list[dict[str, Any]] = []
    for branch, url in sources:
        if len(records) >= limit:
            break
        text = fetcher.get_text(url, accept="text/markdown, text/plain, */*")
        if not text:
            continue
        records.extend(parse_awesome_markdown(branch, url, text, limit - len(records)))
    return records[:limit]


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


def expand_records(
    existing: list[dict[str, Any]],
    fetcher: HttpCache,
    target_records: int,
) -> list[dict[str, Any]]:
    if len(existing) >= target_records:
        return []
    needed = target_records - len(existing)
    expansion_goal = needed + min(700, max(200, needed // 20))
    budgets = {
        "crates": min(2500, max(0, expansion_goal // 4)),
        "npm": min(2600, max(0, expansion_goal // 3)),
        "julia": min(2600, max(0, expansion_goal // 4)),
        "luarocks": min(1800, max(0, expansion_goal // 5)),
        "pypi": min(800, max(0, expansion_goal // 12)),
        "awesome": min(1000, max(0, expansion_goal // 10)),
    }
    # Add any remaining budget to sources that can quickly provide rich metadata.
    assigned = sum(budgets.values())
    if assigned < needed:
        budgets["npm"] += min(expansion_goal - assigned, 1200)
    expansions: list[dict[str, Any]] = []
    source_calls = [
        ("crates.io", lambda: expand_crates(fetcher, budgets["crates"])),
        ("npm", lambda: expand_npm(fetcher, budgets["npm"])),
        ("Julia General", lambda: expand_julia(fetcher, budgets["julia"])),
        ("LuaRocks", lambda: expand_luarocks(fetcher, budgets["luarocks"])),
        ("PyPI", lambda: expand_pypi(fetcher, budgets["pypi"])),
        ("awesome lists", lambda: expand_awesome_lists(fetcher, budgets["awesome"])),
    ]
    for source_name, call in source_calls:
        if len(expansions) >= expansion_goal:
            break
        try:
            records = call()
        except Exception as exc:
            fetcher.errors.append(f"Expansion failed for {source_name}: {exc}")
            continue
        expansions.extend(records)
    return expansions[:expansion_goal]


def enrich_records(
    source_path: Path,
    *,
    network: bool,
    target_records: int,
    workers: int,
    cache_ttl: int,
    max_enrich_records: int,
) -> dict[str, Any]:
    source = read_json(source_path)
    source_records = [normalize_input_record(item) for item in source.get("records", [])]
    fetcher = HttpCache(HTTP_CACHE_DIR, enabled=network, ttl_seconds=cache_ttl)
    expansions = expand_records(source_records, fetcher, target_records) if network else []
    combined = source_records + expansions
    merged = merge_records(combined)

    julia_registry: dict[str, dict[str, str]] | None = None
    if network and any(item["catalog_branch"] == "Julia" for item in merged):
        julia_registry = parse_julia_registry(fetcher)

    to_enrich = [record for record in merged if should_enrich(record)]
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
        "scope": source.get("scope", LANGUAGE_ORDER),
        "taxonomy": source.get("taxonomy", TAXONOMY),
        "target_records": target_records,
        "statistics": dataclasses.asdict(stats),
        "fetch_errors": fetch_errors[:500],
        "records": final_records,
    }
    payload = preserve_generated_at_if_semantically_same(payload)
    write_json(ENRICHED_JSON, payload)
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


def should_enrich(record: dict[str, Any]) -> bool:
    if record.get("source") in {"crates_io", "npm_registry", "pypi_simple"} and record["release"]["status"] == "known":
        return False
    if record.get("source") == "julia_general":
        return False
    if record["catalog_branch"] in {"Python", "Rust", "Julia", "Node.js/JavaScript", "Node.js/TypeScript"}:
        return True
    url = record.get("canonical_url") or record.get("source_url") or ""
    return bool(parse_github_repo(url))


def load_enriched_or_source(source_path: Path) -> dict[str, Any]:
    if ENRICHED_JSON.exists():
        return read_json(ENRICHED_JSON)
    source = read_json(source_path)
    records = merge_records([normalize_input_record(item) for item in source.get("records", [])])
    return {
        "generated_at": now_iso(),
        "source_catalog": str(source_path),
        "source_catalog_id": source.get("catalog_id", ""),
        "source_catalog_version": source.get("catalog_version", ""),
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
    payload = load_enriched_or_source(source_path)
    records = payload["records"]
    clean_generated_catalog()
    write_text(ROOT / "README.md", render_root_readme(payload))
    write_text(CATALOG_DIR / "index.md", render_catalog_index(payload))
    write_text(CATALOG_DIR / "release-watch.md", render_release_watch(payload))
    write_text(CATALOG_DIR / "provenance.md", render_provenance(payload))
    write_text(CATALOG_DIR / "source-map.md", render_source_map(payload))
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
    return f"""# UNICAGD Programming Systems Discovery Catalog

Generated: `{generated}`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

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
    lines = [
        "# Catalog Index",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
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
    lines.extend(["", "## Categories", "", "| Category | Records | Page |", "| --- | ---: | --- |"])
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
    for record in records:
        related_by_branch_category[(record["catalog_branch"], record["category"])].append(record)
    for record in records:
        related = [
            item
            for item in related_by_branch_category[(record["catalog_branch"], record["category"])]
            if item["identity_key"] != record["identity_key"]
        ][:8]
        write_text(CATALOG_DIR / "records" / f"{record['slug']}.md", render_record_page(record, related))


def render_record_page(record: dict[str, Any], related: list[dict[str, Any]]) -> str:
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
            return "```json\n" + json.dumps(raw, ensure_ascii=False, indent=2, sort_keys=True)[:4000] + "\n```"
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


def wrap_md(text: str, width: int = 100) -> str:
    text = plain_markdown_text(text)
    return "\n".join(textwrap.wrap(text, width=width)) if text else ""


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None"


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
    lines = [
        "# Enrichment Report",
        "",
        f"Generated: `{payload.get('generated_at', '')}`",
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
    lines = ["# Source Record Map", "", "| Source record id | Identity | Page |", "| --- | --- | --- |"]
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
    source = read_json(source_path)
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
        choices=["render", "enrich", "all", "check"],
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
        help="HTTP cache TTL in seconds.",
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
    source = read_json(source_path)
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
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
