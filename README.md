# UNICAGD Programming Systems Discovery Catalog

Generated: `2026-09-01T02:14:41+00:00`

This repository is a Markdown explorer for a systems-engineering programming corpus. It preserves the master JSON seed, expands it with registry-derived ecosystem records, and tracks release metadata without guessing unknown dates.

## Browse

- [Catalog index](catalog/index.md)
- [Release watch](catalog/release-watch.md)
- [Provenance and confidence](catalog/provenance.md)
- [Source record map](catalog/source-map.md)

## Category Index

[Api Abi Checker (66)](catalog/by-category/api-abi-checker.md) · [Api Doc Generator (5)](catalog/by-category/api-doc-generator.md) · [Assertion Mocking (31)](catalog/by-category/assertion-mocking.md) · [Async Runtime (84)](catalog/by-category/async-runtime.md)
[Benchmarking (39)](catalog/by-category/benchmarking.md) · [Build System (405)](catalog/by-category/build-system.md) · [Cli (300)](catalog/by-category/cli.md) · [Codegen Codemod Refactoring (14)](catalog/by-category/codegen-codemod-refactoring.md)
[Community Reference (39)](catalog/by-category/community-reference.md) · [Compiler (82)](catalog/by-category/compiler.md) · [Compiler Diagnostics (8)](catalog/by-category/compiler-diagnostics.md) · [Compression (26)](catalog/by-category/compression.md)
[Concurrency Parallelism (42)](catalog/by-category/concurrency-parallelism.md) · [Configuration (46)](catalog/by-category/configuration.md) · [Container Deployment (2)](catalog/by-category/container-deployment.md) · [Coverage (8)](catalog/by-category/coverage.md)
[Cryptography (114)](catalog/by-category/cryptography.md) · [Data Science (14)](catalog/by-category/data-science.md) · [Database Datastore (225)](catalog/by-category/database-datastore.md) · [Datetime (44)](catalog/by-category/datetime.md)
[Dead Code Dependency Analysis (5)](catalog/by-category/dead-code-dependency-analysis.md) · [Debugger (31)](catalog/by-category/debugger.md) · [Dependency Manager (36)](catalog/by-category/dependency-manager.md) · [Documentation (21)](catalog/by-category/documentation.md)
[Embedded Hardware (15)](catalog/by-category/embedded-hardware.md) · [Ffi Bindings (256)](catalog/by-category/ffi-bindings.md) · [Filesystem Os (299)](catalog/by-category/filesystem-os.md) · [Formatter (324)](catalog/by-category/formatter.md)
[Framework (11)](catalog/by-category/framework.md) · [Fuzzer (10)](catalog/by-category/fuzzer.md) · [Game Engine Game Dev (54)](catalog/by-category/game-engine-game-dev.md) · [Ide Editor Integration (399)](catalog/by-category/ide-editor-integration.md)
[Image Audio Dsp (43)](catalog/by-category/image-audio-dsp.md) · [Interop Bindings (34)](catalog/by-category/interop-bindings.md) · [Interpreter Runtime (77)](catalog/by-category/interpreter-runtime.md) · [Jit Vm (47)](catalog/by-category/jit-vm.md)
[Language Server (19)](catalog/by-category/language-server.md) · [Language Specification (216)](catalog/by-category/language-specification.md) · [Library (2365)](catalog/by-category/library.md) · [Lint Plugin (1)](catalog/by-category/lint-plugin.md)
[Lint Rule Pack (27)](catalog/by-category/lint-rule-pack.md) · [Linter (318)](catalog/by-category/linter.md) · [Logging Observability (181)](catalog/by-category/logging-observability.md) · [Machine Learning (215)](catalog/by-category/machine-learning.md)
[Math Numeric Scientific (37)](catalog/by-category/math-numeric-scientific.md) · [Memory Analyzer (39)](catalog/by-category/memory-analyzer.md) · [Message Broker (12)](catalog/by-category/message-broker.md) · [Networking Http (423)](catalog/by-category/networking-http.md)
[Other (14)](catalog/by-category/other.md) · [Package Manager (116)](catalog/by-category/package-manager.md) · [Parser Lexer Ast (314)](catalog/by-category/parser-lexer-ast.md) · [Precommit Ci Quality (115)](catalog/by-category/precommit-ci-quality.md)
[Profiler (41)](catalog/by-category/profiler.md) · [Project Scaffolding (38)](catalog/by-category/project-scaffolding.md) · [Registry Repository (10)](catalog/by-category/registry-repository.md) · [Sanitizer (4)](catalog/by-category/sanitizer.md)
[Security Sast (203)](catalog/by-category/security-sast.md) · [Serialization (162)](catalog/by-category/serialization.md) · [Standard Library (18)](catalog/by-category/standard-library.md) · [Static Analyzer (68)](catalog/by-category/static-analyzer.md)
[Templating (2)](catalog/by-category/templating.md) · [Testing Framework (333)](catalog/by-category/testing-framework.md) · [Tutorial Book Styleguide (7)](catalog/by-category/tutorial-book-styleguide.md) · [Type Checker (229)](catalog/by-category/type-checker.md)
[Undefined Behavior Analyzer (218)](catalog/by-category/undefined-behavior-analyzer.md) · [Utility Library (51)](catalog/by-category/utility-library.md) · [Visualization Gui (93)](catalog/by-category/visualization-gui.md) · [Web Framework (199)](catalog/by-category/web-framework.md)

## Corpus Shape

| Metric | Count |
| --- | ---: |
| Source records | 968 |
| Canonical identity pages | 9344 |
| Expansion records added | 8433 |
| Release checks attempted | 556 |
| Known stable release fields | 4941 |
| Unknown stable release fields | 4403 |
| Fetch errors recorded | 294 |
| Target identity count | 9000 |

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

## Update Commands

```bash
python3 tools/build_catalog.py all
python3 tools/build_catalog.py enrich
python3 tools/build_catalog.py render
python3 tools/build_catalog.py check
```

The generated pages are intentionally explicit about uncertainty. Unknown release dates are kept visible with a reason, because the corpus is for operational decisions, not optimistic summaries.
