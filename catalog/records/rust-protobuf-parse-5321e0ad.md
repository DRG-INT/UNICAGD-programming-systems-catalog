# protobuf-parse

## Navigation

[Catalog index](../index.md) · [Language: Rust](../by-language/rust.md) · [Category: Dependency Manager](../by-category/dependency-manager.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Dependency Manager |
| Source type |  |
| Verification | crates_io |
| Canonical URL | [https://crates.io/crates/protobuf-parse](https://crates.io/crates/protobuf-parse) |
| Source record ids | crates_io-e60b48fcf3fdb9 |

## System Engineer Summary

Parse `.proto` files. Files are parsed into a `protobuf::descriptor::FileDescriptorSet` object using
either: * pure rust parser (no dependencies) * `protoc` binary (more reliable and compatible with
Google's implementation)

## Operational Role

For a systems engineer, protobuf-parse belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 3.7.2 | 2025-03-10T14:08:28.291564Z | [https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `dependency_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

No provenance entries recorded.

## Evidence

Raw evidence is compacted in `catalog/enriched_records.json` for repository-size control.

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| basic-toml | Dependency Manager | [open](rust-basic-toml-5cd7ab13.md) |
| configparser | Dependency Manager | [open](rust-configparser-ce31efc8.md) |
| hex-conservative | Dependency Manager | [open](rust-hex-conservative-879cabf9.md) |
| minijinja | Dependency Manager | [open](rust-minijinja-a500af64.md) |
| precomputed-hash | Dependency Manager | [open](rust-precomputed-hash-2150f344.md) |
| raw-cpuid | Dependency Manager | [open](rust-raw-cpuid-e0c8cffb.md) |
| rustup | Dependency Manager | [open](rust-rustup-eaa7a72b.md) |
| sha1_smol | Dependency Manager | [open](rust-sha1-smol-5c432295.md) |

## Category Index

[Api Abi Checker (115)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (33)](../by-category/assertion-mocking.md) · [Async Runtime (105)](../by-category/async-runtime.md)
[Benchmarking (73)](../by-category/benchmarking.md) · [Build System (583)](../by-category/build-system.md) · [Cli (450)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (67)](../by-category/community-reference.md) · [Compiler (122)](../by-category/compiler.md) · [Compiler Diagnostics (18)](../by-category/compiler-diagnostics.md) · [Compression (36)](../by-category/compression.md)
[Concurrency Parallelism (63)](../by-category/concurrency-parallelism.md) · [Configuration (71)](../by-category/configuration.md) · [Container Deployment (7)](../by-category/container-deployment.md) · [Coverage (10)](../by-category/coverage.md)
[Cryptography (132)](../by-category/cryptography.md) · [Data Science (30)](../by-category/data-science.md) · [Database Datastore (437)](../by-category/database-datastore.md) · [Datetime (100)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (35)](../by-category/debugger.md) · **[Dependency Manager (61)](../by-category/dependency-manager.md)** · [Documentation (62)](../by-category/documentation.md)
[Embedded Hardware (38)](../by-category/embedded-hardware.md) · [Ffi Bindings (320)](../by-category/ffi-bindings.md) · [Filesystem Os (745)](../by-category/filesystem-os.md) · [Formatter (441)](../by-category/formatter.md)
[Framework (38)](../by-category/framework.md) · [Fuzzer (24)](../by-category/fuzzer.md) · [Game Engine Game Dev (103)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (844)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (183)](../by-category/image-audio-dsp.md) · [Interop Bindings (47)](../by-category/interop-bindings.md) · [Interpreter Runtime (158)](../by-category/interpreter-runtime.md) · [Jit Vm (55)](../by-category/jit-vm.md)
[Language Server (23)](../by-category/language-server.md) · [Language Specification (833)](../by-category/language-specification.md) · [Library (3355)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (34)](../by-category/lint-rule-pack.md) · [Linter (330)](../by-category/linter.md) · [Logging Observability (258)](../by-category/logging-observability.md) · [Machine Learning (382)](../by-category/machine-learning.md)
[Math Numeric Scientific (70)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (54)](../by-category/memory-analyzer.md) · [Message Broker (24)](../by-category/message-broker.md) · [Networking Http (691)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (199)](../by-category/package-manager.md) · [Parser Lexer Ast (592)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (171)](../by-category/precommit-ci-quality.md)
[Profiler (57)](../by-category/profiler.md) · [Project Scaffolding (90)](../by-category/project-scaffolding.md) · [Registry Repository (105)](../by-category/registry-repository.md) · [Sanitizer (8)](../by-category/sanitizer.md)
[Security Sast (268)](../by-category/security-sast.md) · [Serialization (272)](../by-category/serialization.md) · [Standard Library (22)](../by-category/standard-library.md) · [Static Analyzer (270)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (418)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (42)](../by-category/tutorial-book-styleguide.md) · [Type Checker (261)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (996)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (80)](../by-category/utility-library.md) · [Visualization Gui (277)](../by-category/visualization-gui.md) · [Web Framework (298)](../by-category/web-framework.md)
