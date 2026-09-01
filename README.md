# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-01T13:23:26+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (127)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (12)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (33)](catalog/by-category/assertion-mocking.md) · [Async Runtime (106)](catalog/by-category/async-runtime.md)
[Benchmarking (75)](catalog/by-category/benchmarking.md) · [Build System (596)](catalog/by-category/build-system.md) · [Cli (453)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (23)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (67)](catalog/by-category/community-reference.md) · [Compiler (122)](catalog/by-category/compiler.md) · [Compiler Diagnostics (18)](catalog/by-category/compiler-diagnostics.md) · [Compression (37)](catalog/by-category/compression.md)
[Concurrency Parallelism (63)](catalog/by-category/concurrency-parallelism.md) · [Configuration (75)](catalog/by-category/configuration.md) · [Container Deployment (7)](catalog/by-category/container-deployment.md) · [Coverage (10)](catalog/by-category/coverage.md)
[Cryptography (132)](catalog/by-category/cryptography.md) · [Data Science (30)](catalog/by-category/data-science.md) · [Database Datastore (441)](catalog/by-category/database-datastore.md) · [Datetime (105)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (35)](catalog/by-category/debugger.md) · [Dependency Manager (61)](catalog/by-category/dependency-manager.md) · [Documentation (62)](catalog/by-category/documentation.md)
[Embedded Hardware (40)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (327)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (784)](catalog/by-category/filesystem-os.md) · [Formatter (450)](catalog/by-category/formatter.md)
[Framework (38)](catalog/by-category/framework.md) · [Fuzzer (40)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (109)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (860)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (186)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (48)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (162)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (55)](catalog/by-category/jit-vm.md)
[Language Server (24)](catalog/by-category/language-server.md) · [Language Specification (843)](catalog/by-category/language-specification.md) · [Library (3399)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (38)](catalog/by-category/lint-rule-pack.md) · [Linter (336)](catalog/by-category/linter.md) · [Logging Observability (265)](catalog/by-category/logging-observability.md) · [Machine Learning (393)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (71)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (54)](catalog/by-category/memory-analyzer.md) · [Message Broker (24)](catalog/by-category/message-broker.md) · [Networking Http (700)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (206)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (613)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (176)](catalog/by-category/precommit-ci-quality.md)
[Profiler (58)](catalog/by-category/profiler.md) · [Project Scaffolding (91)](catalog/by-category/project-scaffolding.md) · [Registry Repository (105)](catalog/by-category/registry-repository.md) · [Sanitizer (9)](catalog/by-category/sanitizer.md)
[Security Sast (270)](catalog/by-category/security-sast.md) · [Serialization (282)](catalog/by-category/serialization.md) · [Standard Library (22)](catalog/by-category/standard-library.md) · [Static Analyzer (297)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (421)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (43)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (271)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (1203)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (82)](catalog/by-category/utility-library.md) · [Visualization Gui (284)](catalog/by-category/visualization-gui.md) · [Web Framework (307)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 16698 |
| Expansion records added | 8605 |
| Release checks attempted | 1200 |
| Known stable release fields | 8515 |
| Unknown stable release fields | 8183 |
| Fetch errors recorded | 621 |
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
