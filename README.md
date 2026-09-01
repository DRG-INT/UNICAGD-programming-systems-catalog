# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-01T05:53:05+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (66)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (10)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (31)](catalog/by-category/assertion-mocking.md) · [Async Runtime (85)](catalog/by-category/async-runtime.md)
[Benchmarking (39)](catalog/by-category/benchmarking.md) · [Build System (406)](catalog/by-category/build-system.md) · [Cli (304)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (19)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (51)](catalog/by-category/community-reference.md) · [Compiler (83)](catalog/by-category/compiler.md) · [Compiler Diagnostics (8)](catalog/by-category/compiler-diagnostics.md) · [Compression (31)](catalog/by-category/compression.md)
[Concurrency Parallelism (42)](catalog/by-category/concurrency-parallelism.md) · [Configuration (48)](catalog/by-category/configuration.md) · [Container Deployment (6)](catalog/by-category/container-deployment.md) · [Coverage (8)](catalog/by-category/coverage.md)
[Cryptography (117)](catalog/by-category/cryptography.md) · [Data Science (14)](catalog/by-category/data-science.md) · [Database Datastore (312)](catalog/by-category/database-datastore.md) · [Datetime (44)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (31)](catalog/by-category/debugger.md) · [Dependency Manager (38)](catalog/by-category/dependency-manager.md) · [Documentation (49)](catalog/by-category/documentation.md)
[Embedded Hardware (16)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (256)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (299)](catalog/by-category/filesystem-os.md) · [Formatter (326)](catalog/by-category/formatter.md)
[Framework (17)](catalog/by-category/framework.md) · [Fuzzer (10)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (76)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (404)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (77)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (41)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (88)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (50)](catalog/by-category/jit-vm.md)
[Language Server (19)](catalog/by-category/language-server.md) · [Language Specification (240)](catalog/by-category/language-specification.md) · [Library (2366)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (27)](catalog/by-category/lint-rule-pack.md) · [Linter (319)](catalog/by-category/linter.md) · [Logging Observability (183)](catalog/by-category/logging-observability.md) · [Machine Learning (219)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (58)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (39)](catalog/by-category/memory-analyzer.md) · [Message Broker (18)](catalog/by-category/message-broker.md) · [Networking Http (449)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (117)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (317)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (121)](catalog/by-category/precommit-ci-quality.md)
[Profiler (41)](catalog/by-category/profiler.md) · [Project Scaffolding (39)](catalog/by-category/project-scaffolding.md) · [Registry Repository (99)](catalog/by-category/registry-repository.md) · [Sanitizer (4)](catalog/by-category/sanitizer.md)
[Security Sast (215)](catalog/by-category/security-sast.md) · [Serialization (181)](catalog/by-category/serialization.md) · [Standard Library (18)](catalog/by-category/standard-library.md) · [Static Analyzer (68)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (335)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (11)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (229)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (218)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (56)](catalog/by-category/utility-library.md) · [Visualization Gui (161)](catalog/by-category/visualization-gui.md) · [Web Framework (199)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 9890 |
| Expansion records added | 546 |
| Release checks attempted | 0 |
| Known stable release fields | 4667 |
| Unknown stable release fields | 5223 |
| Fetch errors recorded | 454 |
| Target identity count | 24000 |

## Languages

- C99
- C23
- C++23
- Julia
- Rust
- Python
- Node.js/JavaScript
- Node.js/TypeScript
- Lua family
- R
- Haskell
- Matlab
- Octave
- C-Sharp
- bc
- Dart
- Go
- Starlark
- Basilisk
- "aim's"
- nix
- Assembly
- PHP
- Swift
- SAPJava
- Cocoa
- WebAssembly
- Pattern language

## System Categories

- Doctrines
- APIs
- Transmission Protocols
- Renderers
- Computer Graphics Software
- Engines
- Physics Engines
- Game Engines
- Icons and Logos
- Font Briefcase
- Assets
- Maps
- Space Engines
- Space Shuttles
- Space Maps
- Effects
- Audio
- Video
- Photography
- Microscopy
- Telescopes
- Radars
- SatCom Satellites
- Electromagnetoscopes
- Radio Garden Speciality
- Repertoare Catalogs
- Catalogs
- Magazines
- Hubs
- Braces
- Databases
- Repository Workplaces

## How It Works

The catalog is built in three stages:

1. **Seed** — A JSON file in `catalog/seed/` defines source records with identity keys, categories, and metadata.
2. **Enrich** — Registry fetches expand each identity with release checks, license info, and provenance. Records are carried forward across runs (DeltaLake-style merge) so the catalog only grows.
3. **Render** — Markdown pages are generated per identity, per category, and index pages.

## SQLite Database

A SQLite database (`catalog/catalog.sqlite`) is generated alongside the JSON data for database-backed ingestion and recovery.

| Command | Description |
| --- | --- |
| `all` | Enrich + render |
| `enrich` | Fetch release data into JSON |
| `render` | Generate Markdown from JSON |
| `check` | Validate without fetching |
| `sqlite` | Export JSON to SQLite |
| `recover` | Restore JSON from SQLite |

Example:

```bash
# Full build (fetches network data)
python3 tools/build_catalog.py all

# No-network build (uses local data only)
python3 tools/build_catalog.py all --no-network

# Recover from SQLite if enriched_records.json is lost
python3 tools/build_catalog.py recover

# Export to SQLite only
python3 tools/build_catalog.py sqlite
```

## Key Features

- **No guessed dates** — Unknown release dates stay explicit with a reason
- **Incremental upsert** — Re-runs preserve existing records, never shrink
- **Provenance tracking** — Each record records confidence sources
- **SQLite export** — Database-backed ingestion via UPSERT
