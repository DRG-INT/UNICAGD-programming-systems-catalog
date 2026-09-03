# line/rules_apple_line

## Navigation

[Catalog index](../index.md) · [Language: Starlark](../by-language/starlark.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/line/rules_apple_line -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Starlark |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/line/rules_apple_line](https://github.com/line/rules_apple_line) |
| Source record ids | github_search_starlark-90cc40467683a1 |

## System Engineer Summary

LINE's Apple rules for Bazel

## Operational Role

For a systems engineer, line/rules_apple_line belongs in the Starlark inventory as part of build
graph control, artifact reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2023-03-20T22:34:01Z | gh search repos topic:bazel rules stars:>100 | gh_search_reports_activity_not_release_version |
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

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-03 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "topic:bazel rules stars:>100", "retrieved": "2026-09-03", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_starlark-90cc40467683a1` from `github_search_starlark` as `registry_expansion`

</details>

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

[Api Abi Checker (204)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (134)](../by-category/async-runtime.md)
[Benchmarking (165)](../by-category/benchmarking.md) · **[Build System (903)](../by-category/build-system.md)** · [Cli (534)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (97)](../by-category/community-reference.md) · [Compiler (174)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (46)](../by-category/compression.md)
[Concurrency Parallelism (78)](../by-category/concurrency-parallelism.md) · [Configuration (113)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (162)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (832)](../by-category/database-datastore.md) · [Datetime (180)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (42)](../by-category/debugger.md) · [Dependency Manager (92)](../by-category/dependency-manager.md) · [Documentation (96)](../by-category/documentation.md)
[Embedded Hardware (54)](../by-category/embedded-hardware.md) · [Ffi Bindings (402)](../by-category/ffi-bindings.md) · [Filesystem Os (1371)](../by-category/filesystem-os.md) · [Formatter (598)](../by-category/formatter.md)
[Framework (54)](../by-category/framework.md) · [Fuzzer (53)](../by-category/fuzzer.md) · [Game Engine Game Dev (169)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1304)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (356)](../by-category/image-audio-dsp.md) · [Interop Bindings (57)](../by-category/interop-bindings.md) · [Interpreter Runtime (250)](../by-category/interpreter-runtime.md) · [Jit Vm (60)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1373)](../by-category/language-specification.md) · [Library (5232)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (43)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (481)](../by-category/logging-observability.md) · [Machine Learning (643)](../by-category/machine-learning.md)
[Math Numeric Scientific (83)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (36)](../by-category/message-broker.md) · [Networking Http (963)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (411)](../by-category/package-manager.md) · [Parser Lexer Ast (998)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (278)](../by-category/precommit-ci-quality.md)
[Profiler (79)](../by-category/profiler.md) · [Project Scaffolding (130)](../by-category/project-scaffolding.md) · [Registry Repository (108)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (333)](../by-category/security-sast.md) · [Serialization (378)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (490)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (518)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (56)](../by-category/tutorial-book-styleguide.md) · [Type Checker (297)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1497)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (95)](../by-category/utility-library.md) · [Visualization Gui (466)](../by-category/visualization-gui.md) · [Web Framework (448)](../by-category/web-framework.md)
