# starlark-rust

## Navigation

[Catalog index](../index.md) · [Language: Starlark](../by-language/starlark.md) · [Category: Interpreter Runtime](../by-category/interpreter-runtime.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/facebookexperimental/starlark-rust -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Starlark |
| Category | Interpreter Runtime |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/facebookexperimental/starlark-rust](https://github.com/facebookexperimental/starlark-rust) |
| Source record ids | curated_language_routes-c9ec2007ee3e22 |

## System Engineer Summary

Rust implementation of Starlark used by Buck2 and embeddable build/configuration tooling.

## Operational Role

For a systems engineer, starlark-rust belongs in the Starlark inventory as part of runtime behavior,
deployment packaging, embedding, upgrade cadence, and compatibility validation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | curated_language_route_requires_source_specific_release_lookup |
| preview/nightly | unknown |  |  | unknown | curated_language_route_requires_source_specific_preview_lookup |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `interpreter_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `curated_language_route_requires_source_specific_release_lookup`.
- Preview/nightly metadata is unknown because `curated_language_route_requires_source_specific_preview_lookup`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| official_language_route | curated-extension-derived | 2026-09-05 | `{"kind": "official_language_route", "retrieved": "2026-09-05", "status": "curated-extension-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `curated_language_routes-c9ec2007ee3e22` from `curated_language_routes` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| bazel-contrib/rules_jvm_external | Interpreter Runtime | [open](starlark-bazel-contrib-rules-jvm-external-5d599720.md) |
| starlark-go | Interpreter Runtime | [open](starlark-starlark-go-17e4e439.md) |

## Category Index

[Api Abi Checker (215)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (136)](../by-category/async-runtime.md)
[Benchmarking (194)](../by-category/benchmarking.md) · [Build System (980)](../by-category/build-system.md) · [Cli (559)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (116)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (50)](../by-category/compression.md)
[Concurrency Parallelism (89)](../by-category/concurrency-parallelism.md) · [Configuration (128)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (173)](../by-category/cryptography.md) · [Data Science (38)](../by-category/data-science.md) · [Database Datastore (887)](../by-category/database-datastore.md) · [Datetime (223)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (44)](../by-category/debugger.md) · [Dependency Manager (101)](../by-category/dependency-manager.md) · [Documentation (103)](../by-category/documentation.md)
[Embedded Hardware (56)](../by-category/embedded-hardware.md) · [Ffi Bindings (449)](../by-category/ffi-bindings.md) · [Filesystem Os (1561)](../by-category/filesystem-os.md) · [Formatter (641)](../by-category/formatter.md)
[Framework (63)](../by-category/framework.md) · [Fuzzer (57)](../by-category/fuzzer.md) · [Game Engine Game Dev (354)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1433)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (428)](../by-category/image-audio-dsp.md) · [Interop Bindings (61)](../by-category/interop-bindings.md) · **[Interpreter Runtime (267)](../by-category/interpreter-runtime.md)** · [Jit Vm (63)](../by-category/jit-vm.md)
[Language Server (29)](../by-category/language-server.md) · [Language Specification (1428)](../by-category/language-specification.md) · [Library (5551)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (48)](../by-category/lint-rule-pack.md) · [Linter (348)](../by-category/linter.md) · [Logging Observability (518)](../by-category/logging-observability.md) · [Machine Learning (769)](../by-category/machine-learning.md)
[Math Numeric Scientific (87)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (95)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1026)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (438)](../by-category/package-manager.md) · [Parser Lexer Ast (1088)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (298)](../by-category/precommit-ci-quality.md)
[Profiler (86)](../by-category/profiler.md) · [Project Scaffolding (132)](../by-category/project-scaffolding.md) · [Registry Repository (133)](../by-category/registry-repository.md) · [Sanitizer (14)](../by-category/sanitizer.md)
[Security Sast (336)](../by-category/security-sast.md) · [Serialization (393)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (595)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (603)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (62)](../by-category/tutorial-book-styleguide.md) · [Type Checker (313)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1587)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (103)](../by-category/utility-library.md) · [Visualization Gui (542)](../by-category/visualization-gui.md) · [Web Framework (476)](../by-category/web-framework.md)
