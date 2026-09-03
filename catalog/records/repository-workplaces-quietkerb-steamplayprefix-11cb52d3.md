# quietkerb/steamplayprefix

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Interpreter Runtime](../by-category/interpreter-runtime.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/quietkerb/steamplayprefix -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Interpreter Runtime |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/quietkerb/steamplayprefix](https://gitlab.com/quietkerb/steamplayprefix) |
| Source record ids | gitlab_projects_api-2beacf54f52d2f |

## System Engineer Summary

`sppfx` can run `winetricks`, `winecfg`, `regedit` and arbitrary Windows executables in a SteamPlay
prefix, using Proton and the Steam runtime instead of your regular Wine installation.

## Operational Role

For a systems engineer, quietkerb/steamplayprefix belongs in the Repository Workplaces inventory as
part of runtime behavior, deployment packaging, embedding, upgrade cadence, and compatibility
validation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2020-02-23T08:40:04.894Z | [https://gitlab.com/api/v4/projects?search=runtime&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=runtime&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `interpreter_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gitlab_projects_api_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gitlab_projects_api_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gitlab_projects_api | forge-api-derived | 2026-09-03 | `{"kind": "gitlab_projects_api", "query": "runtime", "retrieved": "2026-09-03", "status": "forge-api-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-2beacf54f52d2f` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| andreyorst/fenneldoc | Interpreter Runtime | [open](repository-workplaces-andreyorst-fenneldoc-ae269a8d.md) |
| cespedes/ltrace | Interpreter Runtime | [open](repository-workplaces-cespedes-ltrace-7df92cd8.md) |
| cznic/libc | Interpreter Runtime | [open](repository-workplaces-cznic-libc-3b834450.md) |
| DerLinkshaender/csv2xlsx | Interpreter Runtime | [open](repository-workplaces-derlinkshaender-csv2xlsx-bd2e77a2.md) |
| freedesktop-sdk/freedesktop-sdk | Interpreter Runtime | [open](repository-workplaces-freedesktop-sdk-freedesktop-sdk-d7a3f323.md) |
| Gitea: Befaci03/collab-vm-1.2-server-bettetweak | Interpreter Runtime | [open](repository-workplaces-gitea-befaci03-collab-vm-1-2-server-bettetweak-82605f6b.md) |
| Gitea: cvmuser1000/collab-vm-1.2-server-bettetweak-better | Interpreter Runtime | [open](repository-workplaces-gitea-cvmuser1000-collab-vm-1-2-server-bettetweak-better-40a2c6fe.md) |
| Gitea: Gala_Group/GalaRuntime | Interpreter Runtime | [open](repository-workplaces-gitea-gala-group-galaruntime-c30c90ab.md) |

## Category Index

[Api Abi Checker (199)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (131)](../by-category/async-runtime.md)
[Benchmarking (161)](../by-category/benchmarking.md) · [Build System (875)](../by-category/build-system.md) · [Cli (521)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (91)](../by-category/community-reference.md) · [Compiler (173)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (75)](../by-category/concurrency-parallelism.md) · [Configuration (107)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (160)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (791)](../by-category/database-datastore.md) · [Datetime (172)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (91)](../by-category/dependency-manager.md) · [Documentation (93)](../by-category/documentation.md)
[Embedded Hardware (53)](../by-category/embedded-hardware.md) · [Ffi Bindings (401)](../by-category/ffi-bindings.md) · [Filesystem Os (1310)](../by-category/filesystem-os.md) · [Formatter (581)](../by-category/formatter.md)
[Framework (51)](../by-category/framework.md) · [Fuzzer (50)](../by-category/fuzzer.md) · [Game Engine Game Dev (164)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1261)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (350)](../by-category/image-audio-dsp.md) · [Interop Bindings (56)](../by-category/interop-bindings.md) · **[Interpreter Runtime (240)](../by-category/interpreter-runtime.md)** · [Jit Vm (58)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1261)](../by-category/language-specification.md) · [Library (5059)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (42)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (465)](../by-category/logging-observability.md) · [Machine Learning (622)](../by-category/machine-learning.md)
[Math Numeric Scientific (82)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (35)](../by-category/message-broker.md) · [Networking Http (949)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (403)](../by-category/package-manager.md) · [Parser Lexer Ast (965)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (269)](../by-category/precommit-ci-quality.md)
[Profiler (78)](../by-category/profiler.md) · [Project Scaffolding (127)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (325)](../by-category/security-sast.md) · [Serialization (375)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (468)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (511)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (293)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1457)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (435)](../by-category/visualization-gui.md) · [Web Framework (443)](../by-category/web-framework.md)
