# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-03T10:24:33+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Apache/MIT license index](catalog/license-index.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (201)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (12)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (44)](catalog/by-category/assertion-mocking.md) · [Async Runtime (133)](catalog/by-category/async-runtime.md)
[Benchmarking (164)](catalog/by-category/benchmarking.md) · [Build System (884)](catalog/by-category/build-system.md) · [Cli (528)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (23)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (92)](catalog/by-category/community-reference.md) · [Compiler (174)](catalog/by-category/compiler.md) · [Compiler Diagnostics (23)](catalog/by-category/compiler-diagnostics.md) · [Compression (46)](catalog/by-category/compression.md)
[Concurrency Parallelism (77)](catalog/by-category/concurrency-parallelism.md) · [Configuration (108)](catalog/by-category/configuration.md) · [Container Deployment (9)](catalog/by-category/container-deployment.md) · [Coverage (14)](catalog/by-category/coverage.md)
[Cryptography (162)](catalog/by-category/cryptography.md) · [Data Science (35)](catalog/by-category/data-science.md) · [Database Datastore (830)](catalog/by-category/database-datastore.md) · [Datetime (177)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (42)](catalog/by-category/debugger.md) · [Dependency Manager (91)](catalog/by-category/dependency-manager.md) · [Documentation (95)](catalog/by-category/documentation.md)
[Embedded Hardware (54)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (401)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (1328)](catalog/by-category/filesystem-os.md) · [Formatter (587)](catalog/by-category/formatter.md)
[Framework (52)](catalog/by-category/framework.md) · [Fuzzer (53)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (164)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (1279)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (355)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (57)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (241)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (59)](catalog/by-category/jit-vm.md)
[Language Server (27)](catalog/by-category/language-server.md) · [Language Specification (1270)](catalog/by-category/language-specification.md) · [Library (5112)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (43)](catalog/by-category/lint-rule-pack.md) · [Linter (347)](catalog/by-category/linter.md) · [Logging Observability (472)](catalog/by-category/logging-observability.md) · [Machine Learning (634)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (83)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](catalog/by-category/memory-analyzer.md) · [Message Broker (36)](catalog/by-category/message-broker.md) · [Networking Http (955)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (407)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (993)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (273)](catalog/by-category/precommit-ci-quality.md)
[Profiler (79)](catalog/by-category/profiler.md) · [Project Scaffolding (127)](catalog/by-category/project-scaffolding.md) · [Registry Repository (108)](catalog/by-category/registry-repository.md) · [Sanitizer (13)](catalog/by-category/sanitizer.md)
[Security Sast (331)](catalog/by-category/security-sast.md) · [Serialization (375)](catalog/by-category/serialization.md) · [Standard Library (25)](catalog/by-category/standard-library.md) · [Static Analyzer (486)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (513)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (54)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (297)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (1480)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](catalog/by-category/utility-library.md) · [Visualization Gui (446)](catalog/by-category/visualization-gui.md) · [Web Framework (447)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 24230 |
| Expansion records added | 8605 |
| Release checks attempted | 1200 |
| Known stable release fields | 9900 |
| Unknown stable release fields | 14330 |
| Fetch errors recorded | 1001 |
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
