# str_stack

## Navigation

[Catalog index](../index.md) · [Language: Rust](../by-language/rust.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://crates.io/crates/str_stack -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Build System |
| Source type |  |
| Verification | crates_io |
| Canonical URL | [https://crates.io/crates/str_stack](https://crates.io/crates/str_stack) |
| Source record ids | crates_io-3cddded8eb0531 |

## System Engineer Summary

A string allocator for allocating many write-once strings. This library is primarily useful for
parsing where you need to repeatedly build many strings, use them, and then throw them away. Instead
of allocating many independent strings, this library will put them all in the same buffer.

## Operational Role

For a systems engineer, str_stack belongs in the Rust inventory as part of build graph control,
artifact reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.1.1 | 2026-05-10T23:04:34.744162Z | [https://crates.io/api/v1/crates?page=14&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=14&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | MIT |
| Evidence | MIT License; https://api.github.com/licenses/mit |
| Alert | Showcase candidate: permissive MIT family; keep copyright and permission notices attached. |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=14&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
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
| android-activity | Build System | [open](rust-android-activity-958c810f.md) |
| async-task | Build System | [open](rust-async-task-7248a7cd.md) |
| backon | Build System | [open](rust-backon-59db9d30.md) |
| bon | Build System | [open](rust-bon-5c756277.md) |
| build_const | Build System | [open](rust-build-const-0aeeb00d.md) |
| cargo-make | Build System | [open](rust-cargo-make-dcab0faa.md) |
| chrono-tz-build | Build System | [open](rust-chrono-tz-build-0484d9ba.md) |
| clap_builder | Build System | [open](rust-clap-builder-81592afe.md) |

## Category Index

[Api Abi Checker (214)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (136)](../by-category/async-runtime.md)
[Benchmarking (193)](../by-category/benchmarking.md) · **[Build System (978)](../by-category/build-system.md)** · [Cli (559)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (116)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (50)](../by-category/compression.md)
[Concurrency Parallelism (89)](../by-category/concurrency-parallelism.md) · [Configuration (128)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (173)](../by-category/cryptography.md) · [Data Science (38)](../by-category/data-science.md) · [Database Datastore (886)](../by-category/database-datastore.md) · [Datetime (223)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (44)](../by-category/debugger.md) · [Dependency Manager (101)](../by-category/dependency-manager.md) · [Documentation (103)](../by-category/documentation.md)
[Embedded Hardware (56)](../by-category/embedded-hardware.md) · [Ffi Bindings (448)](../by-category/ffi-bindings.md) · [Filesystem Os (1559)](../by-category/filesystem-os.md) · [Formatter (640)](../by-category/formatter.md)
[Framework (63)](../by-category/framework.md) · [Fuzzer (57)](../by-category/fuzzer.md) · [Game Engine Game Dev (354)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1430)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (423)](../by-category/image-audio-dsp.md) · [Interop Bindings (61)](../by-category/interop-bindings.md) · [Interpreter Runtime (267)](../by-category/interpreter-runtime.md) · [Jit Vm (63)](../by-category/jit-vm.md)
[Language Server (29)](../by-category/language-server.md) · [Language Specification (1428)](../by-category/language-specification.md) · [Library (5547)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (48)](../by-category/lint-rule-pack.md) · [Linter (348)](../by-category/linter.md) · [Logging Observability (517)](../by-category/logging-observability.md) · [Machine Learning (767)](../by-category/machine-learning.md)
[Math Numeric Scientific (87)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (95)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1024)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (438)](../by-category/package-manager.md) · [Parser Lexer Ast (1086)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (297)](../by-category/precommit-ci-quality.md)
[Profiler (86)](../by-category/profiler.md) · [Project Scaffolding (132)](../by-category/project-scaffolding.md) · [Registry Repository (133)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (336)](../by-category/security-sast.md) · [Serialization (393)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (595)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (603)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (62)](../by-category/tutorial-book-styleguide.md) · [Type Checker (313)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1586)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (102)](../by-category/utility-library.md) · [Visualization Gui (542)](../by-category/visualization-gui.md) · [Web Framework (476)](../by-category/web-framework.md)
