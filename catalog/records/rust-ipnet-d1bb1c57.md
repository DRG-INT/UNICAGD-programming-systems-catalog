# ipnet

## Navigation

[Catalog index](../index.md) · [Language: Rust](../by-language/rust.md) · [Category: Language Specification](../by-category/language-specification.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://crates.io/crates/ipnet -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/ipnet](https://crates.io/crates/ipnet) |
| Source record ids | crates_io-781239719b698d |

## System Engineer Summary

Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called
IP prefixes. The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`,
`Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their
design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and
`Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses
stable feature so it is guaranteed to compile using the stable toolchain.

## Operational Role

For a systems engineer, ipnet belongs in the Rust inventory as part of ecosystem capability mapping,
dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 2.12.1 | 2026-08-02T03:20:08.056738Z | [https://crates.io/api/v1/crates?page=2&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=2&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=2&per_page=100&sort=downloads` at `2026-09-01T02:12:57+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-02 | `{"kind": "crates_io", "retrieved": "2026-09-02", "status": "registry-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `crates_io-781239719b698d` from `crates_io` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aes | Language Specification | [open](rust-aes-51a8d565.md) |
| async-attributes | Language Specification | [open](rust-async-attributes-ae37e076.md) |
| async-std | Language Specification | [open](rust-async-std-abaaac81.md) |
| block | Language Specification | [open](rust-block-6b036ded.md) |
| block2 | Language Specification | [open](rust-block2-b93b6216.md) |
| brotli | Language Specification | [open](rust-brotli-6dba38aa.md) |
| brotli-decompressor | Language Specification | [open](rust-brotli-decompressor-dda445d2.md) |
| codespan-reporting | Language Specification | [open](rust-codespan-reporting-ef7af61c.md) |

## Category Index

[Api Abi Checker (185)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (41)](../by-category/assertion-mocking.md) · [Async Runtime (123)](../by-category/async-runtime.md)
[Benchmarking (110)](../by-category/benchmarking.md) · [Build System (813)](../by-category/build-system.md) · [Cli (501)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (85)](../by-category/community-reference.md) · [Compiler (170)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (72)](../by-category/concurrency-parallelism.md) · [Configuration (100)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (155)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (714)](../by-category/database-datastore.md) · [Datetime (158)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (85)](../by-category/dependency-manager.md) · [Documentation (88)](../by-category/documentation.md)
[Embedded Hardware (49)](../by-category/embedded-hardware.md) · [Ffi Bindings (387)](../by-category/ffi-bindings.md) · [Filesystem Os (1197)](../by-category/filesystem-os.md) · [Formatter (545)](../by-category/formatter.md)
[Framework (47)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (157)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1133)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (300)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (227)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · **[Language Specification (1229)](../by-category/language-specification.md)** · [Library (4824)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (346)](../by-category/linter.md) · [Logging Observability (388)](../by-category/logging-observability.md) · [Machine Learning (583)](../by-category/machine-learning.md)
[Math Numeric Scientific (79)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (77)](../by-category/memory-analyzer.md) · [Message Broker (31)](../by-category/message-broker.md) · [Networking Http (916)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (263)](../by-category/package-manager.md) · [Parser Lexer Ast (905)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (262)](../by-category/precommit-ci-quality.md)
[Profiler (72)](../by-category/profiler.md) · [Project Scaffolding (118)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (311)](../by-category/security-sast.md) · [Serialization (368)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (437)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (495)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (290)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1380)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (414)](../by-category/visualization-gui.md) · [Web Framework (391)](../by-category/web-framework.md)
