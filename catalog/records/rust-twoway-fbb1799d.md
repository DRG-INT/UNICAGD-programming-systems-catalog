# twoway

## Navigation

[Catalog index](../index.md) · [Language: Rust](../by-language/rust.md) · [Category: Interpreter Runtime](../by-category/interpreter-runtime.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://crates.io/crates/twoway -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Interpreter Runtime |
| Source type |  |
| Verification | crates_io |
| Canonical URL | [https://crates.io/crates/twoway](https://crates.io/crates/twoway) |
| Source record ids | crates_io-d6c7f287eae2f2 |

## System Engineer Summary

(Deprecated - use crate memchr instead.) Fast substring search for strings and byte strings.
Optional SSE4.2 acceleration (if detected at runtime) using pcmpestri. Memchr is the only mandatory
dependency. The two way algorithm is also used by rust's libstd itself, but here it is exposed both
for byte strings, using memchr, and optionally using a SSE4.2 accelerated version.

## Operational Role

For a systems engineer, twoway belongs in the Rust inventory as part of runtime behavior, deployment
packaging, embedding, upgrade cadence, and compatibility validation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.2 | 2021-05-19T22:06:38.467348Z | [https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `interpreter_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

No provenance entries recorded.

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Raw evidence is compacted in `catalog/enriched_records.json` for repository-size control.

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-macros | Interpreter Runtime | [open](rust-actix-macros-ca794fb7.md) |
| actix-rt | Interpreter Runtime | [open](rust-actix-rt-aef83aa1.md) |
| actix-web-codegen | Interpreter Runtime | [open](rust-actix-web-codegen-9aba0585.md) |
| aws-runtime | Interpreter Runtime | [open](rust-aws-runtime-ac213e01.md) |
| aws-smithy-async | Interpreter Runtime | [open](rust-aws-smithy-async-9d69cd7f.md) |
| aws-smithy-runtime | Interpreter Runtime | [open](rust-aws-smithy-runtime-e27d173f.md) |
| aws-smithy-runtime-api | Interpreter Runtime | [open](rust-aws-smithy-runtime-api-706cee25.md) |
| aws-smithy-runtime-api-macros | Interpreter Runtime | [open](rust-aws-smithy-runtime-api-macros-08700463.md) |

## Category Index

[Api Abi Checker (199)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (131)](../by-category/async-runtime.md)
[Benchmarking (160)](../by-category/benchmarking.md) · [Build System (871)](../by-category/build-system.md) · [Cli (521)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (91)](../by-category/community-reference.md) · [Compiler (173)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (75)](../by-category/concurrency-parallelism.md) · [Configuration (107)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (160)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (791)](../by-category/database-datastore.md) · [Datetime (167)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (91)](../by-category/dependency-manager.md) · [Documentation (93)](../by-category/documentation.md)
[Embedded Hardware (52)](../by-category/embedded-hardware.md) · [Ffi Bindings (400)](../by-category/ffi-bindings.md) · [Filesystem Os (1300)](../by-category/filesystem-os.md) · [Formatter (578)](../by-category/formatter.md)
[Framework (51)](../by-category/framework.md) · [Fuzzer (50)](../by-category/fuzzer.md) · [Game Engine Game Dev (164)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1257)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (314)](../by-category/image-audio-dsp.md) · [Interop Bindings (56)](../by-category/interop-bindings.md) · **[Interpreter Runtime (240)](../by-category/interpreter-runtime.md)** · [Jit Vm (58)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1260)](../by-category/language-specification.md) · [Library (5057)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (42)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (464)](../by-category/logging-observability.md) · [Machine Learning (620)](../by-category/machine-learning.md)
[Math Numeric Scientific (82)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (35)](../by-category/message-broker.md) · [Networking Http (946)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (402)](../by-category/package-manager.md) · [Parser Lexer Ast (962)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (269)](../by-category/precommit-ci-quality.md)
[Profiler (78)](../by-category/profiler.md) · [Project Scaffolding (125)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (325)](../by-category/security-sast.md) · [Serialization (375)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (465)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (511)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (293)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1457)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (430)](../by-category/visualization-gui.md) · [Web Framework (443)](../by-category/web-framework.md)
