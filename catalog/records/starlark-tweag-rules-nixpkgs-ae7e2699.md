# tweag/rules_nixpkgs

## Navigation

[Catalog index](../index.md) · [Language: Starlark](../by-language/starlark.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | Starlark |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/tweag/rules_nixpkgs](https://github.com/tweag/rules_nixpkgs) |
| Source record ids | github_search_starlark-14b872ed7bf063 |

## System Engineer Summary

Rules for importing Nixpkgs packages into Bazel.

## Operational Role

For a systems engineer, tweag/rules_nixpkgs belongs in the Starlark inventory as part of build graph
control, artifact reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-08-28T22:33:46Z | gh search repos topic:bazel rules stars:>100 | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Apache-2.0 |
| Evidence | Apache License 2.0; https://api.github.com/licenses/apache-2.0 |
| Alert | Showcase candidate: permissive Apache-2.0 family; keep notices and patent/license obligations visible. |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-01 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "topic:bazel rules stars:>100", "retrieved": "2026-09-01", "status": "forge-cli-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `github_search_starlark-14b872ed7bf063` from `github_search_starlark` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| adobe/rules_gitops | Build System | [open](starlark-adobe-rules-gitops-09140ed0.md) |
| aspect-build/rules_js | Build System | [open](starlark-aspect-build-rules-js-fd75b379.md) |
| aspect-build/rules_py | Build System | [open](starlark-aspect-build-rules-py-910f4833.md) |
| Bazel | Build System | [open](starlark-bazel-189ae4a2.md) |
| bazel-contrib/bazel-lib | Build System | [open](starlark-bazel-contrib-bazel-lib-fce95ce1.md) |
| bazel-contrib/rules_cuda | Build System | [open](starlark-bazel-contrib-rules-cuda-00a89ba0.md) |
| bazel-contrib/rules_dotnet | Build System | [open](starlark-bazel-contrib-rules-dotnet-8c8a841c.md) |
| bazel-contrib/rules_go | Build System | [open](starlark-bazel-contrib-rules-go-4b6a62de.md) |

## Category Index

[Api Abi Checker (173)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (40)](../by-category/assertion-mocking.md) · [Async Runtime (119)](../by-category/async-runtime.md)
[Benchmarking (100)](../by-category/benchmarking.md) · **[Build System (764)](../by-category/build-system.md)** · [Cli (484)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (80)](../by-category/community-reference.md) · [Compiler (155)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (42)](../by-category/compression.md)
[Concurrency Parallelism (70)](../by-category/concurrency-parallelism.md) · [Configuration (94)](../by-category/configuration.md) · [Container Deployment (8)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (153)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (638)](../by-category/database-datastore.md) · [Datetime (143)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (40)](../by-category/debugger.md) · [Dependency Manager (79)](../by-category/dependency-manager.md) · [Documentation (77)](../by-category/documentation.md)
[Embedded Hardware (43)](../by-category/embedded-hardware.md) · [Ffi Bindings (367)](../by-category/ffi-bindings.md) · [Filesystem Os (1080)](../by-category/filesystem-os.md) · [Formatter (526)](../by-category/formatter.md)
[Framework (44)](../by-category/framework.md) · [Fuzzer (45)](../by-category/fuzzer.md) · [Game Engine Game Dev (135)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1072)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (216)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (216)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (26)](../by-category/language-server.md) · [Language Specification (1189)](../by-category/language-specification.md) · [Library (4647)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (344)](../by-category/linter.md) · [Logging Observability (317)](../by-category/logging-observability.md) · [Machine Learning (544)](../by-category/machine-learning.md)
[Math Numeric Scientific (78)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (73)](../by-category/memory-analyzer.md) · [Message Broker (31)](../by-category/message-broker.md) · [Networking Http (883)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (244)](../by-category/package-manager.md) · [Parser Lexer Ast (866)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (252)](../by-category/precommit-ci-quality.md)
[Profiler (66)](../by-category/profiler.md) · [Project Scaffolding (107)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (306)](../by-category/security-sast.md) · [Serialization (361)](../by-category/serialization.md) · [Standard Library (23)](../by-category/standard-library.md) · [Static Analyzer (406)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (486)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (52)](../by-category/tutorial-book-styleguide.md) · [Type Checker (276)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1328)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (89)](../by-category/utility-library.md) · [Visualization Gui (389)](../by-category/visualization-gui.md) · [Web Framework (372)](../by-category/web-framework.md)
