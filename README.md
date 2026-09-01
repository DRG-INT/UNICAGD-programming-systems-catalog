# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-01T14:24:44+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (171)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (12)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (36)](catalog/by-category/assertion-mocking.md) · [Async Runtime (111)](catalog/by-category/async-runtime.md)
[Benchmarking (90)](catalog/by-category/benchmarking.md) · [Build System (697)](catalog/by-category/build-system.md) · [Cli (474)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (23)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (78)](catalog/by-category/community-reference.md) · [Compiler (143)](catalog/by-category/compiler.md) · [Compiler Diagnostics (22)](catalog/by-category/compiler-diagnostics.md) · [Compression (42)](catalog/by-category/compression.md)
[Concurrency Parallelism (67)](catalog/by-category/concurrency-parallelism.md) · [Configuration (92)](catalog/by-category/configuration.md) · [Container Deployment (7)](catalog/by-category/container-deployment.md) · [Coverage (10)](catalog/by-category/coverage.md)
[Cryptography (150)](catalog/by-category/cryptography.md) · [Data Science (32)](catalog/by-category/data-science.md) · [Database Datastore (514)](catalog/by-category/database-datastore.md) · [Datetime (130)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (37)](catalog/by-category/debugger.md) · [Dependency Manager (70)](catalog/by-category/dependency-manager.md) · [Documentation (71)](catalog/by-category/documentation.md)
[Embedded Hardware (41)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (356)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (1015)](catalog/by-category/filesystem-os.md) · [Formatter (496)](catalog/by-category/formatter.md)
[Framework (42)](catalog/by-category/framework.md) · [Fuzzer (43)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (129)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (965)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (198)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (50)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (188)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (55)](catalog/by-category/jit-vm.md)
[Language Server (26)](catalog/by-category/language-server.md) · [Language Specification (1042)](catalog/by-category/language-specification.md) · [Library (4510)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (40)](catalog/by-category/lint-rule-pack.md) · [Linter (339)](catalog/by-category/linter.md) · [Logging Observability (306)](catalog/by-category/logging-observability.md) · [Machine Learning (519)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (76)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (69)](catalog/by-category/memory-analyzer.md) · [Message Broker (29)](catalog/by-category/message-broker.md) · [Networking Http (802)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (234)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (793)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (222)](catalog/by-category/precommit-ci-quality.md)
[Profiler (64)](catalog/by-category/profiler.md) · [Project Scaffolding (97)](catalog/by-category/project-scaffolding.md) · [Registry Repository (107)](catalog/by-category/registry-repository.md) · [Sanitizer (10)](catalog/by-category/sanitizer.md)
[Security Sast (282)](catalog/by-category/security-sast.md) · [Serialization (312)](catalog/by-category/serialization.md) · [Standard Library (23)](catalog/by-category/standard-library.md) · [Static Analyzer (385)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (471)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (50)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (276)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (1280)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (88)](catalog/by-category/utility-library.md) · [Visualization Gui (369)](catalog/by-category/visualization-gui.md) · [Web Framework (320)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 19820 |
| Expansion records added | 8605 |
| Release checks attempted | 1200 |
| Known stable release fields | 10119 |
| Unknown stable release fields | 9701 |
| Fetch errors recorded | 979 |
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
