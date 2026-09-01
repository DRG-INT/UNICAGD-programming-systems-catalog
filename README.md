# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-01T16:43:27+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (173)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (12)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (40)](catalog/by-category/assertion-mocking.md) · [Async Runtime (119)](catalog/by-category/async-runtime.md)
[Benchmarking (100)](catalog/by-category/benchmarking.md) · [Build System (764)](catalog/by-category/build-system.md) · [Cli (484)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (23)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (80)](catalog/by-category/community-reference.md) · [Compiler (155)](catalog/by-category/compiler.md) · [Compiler Diagnostics (22)](catalog/by-category/compiler-diagnostics.md) · [Compression (42)](catalog/by-category/compression.md)
[Concurrency Parallelism (70)](catalog/by-category/concurrency-parallelism.md) · [Configuration (94)](catalog/by-category/configuration.md) · [Container Deployment (8)](catalog/by-category/container-deployment.md) · [Coverage (11)](catalog/by-category/coverage.md)
[Cryptography (153)](catalog/by-category/cryptography.md) · [Data Science (32)](catalog/by-category/data-science.md) · [Database Datastore (638)](catalog/by-category/database-datastore.md) · [Datetime (143)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (40)](catalog/by-category/debugger.md) · [Dependency Manager (79)](catalog/by-category/dependency-manager.md) · [Documentation (77)](catalog/by-category/documentation.md)
[Embedded Hardware (43)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (367)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (1080)](catalog/by-category/filesystem-os.md) · [Formatter (526)](catalog/by-category/formatter.md)
[Framework (44)](catalog/by-category/framework.md) · [Fuzzer (45)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (135)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (1072)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (216)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (52)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (216)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (56)](catalog/by-category/jit-vm.md)
[Language Server (26)](catalog/by-category/language-server.md) · [Language Specification (1189)](catalog/by-category/language-specification.md) · [Library (4647)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (40)](catalog/by-category/lint-rule-pack.md) · [Linter (344)](catalog/by-category/linter.md) · [Logging Observability (317)](catalog/by-category/logging-observability.md) · [Machine Learning (544)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (78)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (73)](catalog/by-category/memory-analyzer.md) · [Message Broker (31)](catalog/by-category/message-broker.md) · [Networking Http (883)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (244)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (866)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (252)](catalog/by-category/precommit-ci-quality.md)
[Profiler (66)](catalog/by-category/profiler.md) · [Project Scaffolding (107)](catalog/by-category/project-scaffolding.md) · [Registry Repository (107)](catalog/by-category/registry-repository.md) · [Sanitizer (12)](catalog/by-category/sanitizer.md)
[Security Sast (306)](catalog/by-category/security-sast.md) · [Serialization (361)](catalog/by-category/serialization.md) · [Standard Library (23)](catalog/by-category/standard-library.md) · [Static Analyzer (406)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (486)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (52)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (276)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (1328)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (89)](catalog/by-category/utility-library.md) · [Visualization Gui (389)](catalog/by-category/visualization-gui.md) · [Web Framework (372)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 21147 |
| Expansion records added | 8605 |
| Release checks attempted | 1200 |
| Known stable release fields | 10129 |
| Unknown stable release fields | 11018 |
| Fetch errors recorded | 1071 |
| Target identity count | 24000 |

## Language Scope

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
- Assembly
- Pattern language
- PHP
- WebAssembly
- SAPJava
- Swift
- Cocoa
- Databases
- Repository Workplaces

## Update Commands

```bash
python3 tools/build_catalog.py all
python3 tools/build_catalog.py enrich
python3 tools/build_catalog.py render
python3 tools/build_catalog.py check
```

The generated pages are intentionally explicit about uncertainty. Unknown release dates are kept visible with a reason, because the corpus is for operational decisions, not optimistic summaries.
