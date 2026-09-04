# OpenTAP/opentap

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Package Manager](../by-category/package-manager.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/OpenTAP/opentap -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Package Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/OpenTAP/opentap](https://gitlab.com/OpenTAP/opentap) |
| Source record ids | gitlab_projects_api-4f24f34f664506 |

## System Engineer Summary

This is the code for the base OpenTAP package. This includes the OpenTap.dll (base classes and
sequencer), OpenTap.Package.dll (package manager), tap.exe (CLI) and OpenTap.Plugins.BasicSteps.dll
(some basic TestSteps)

## Operational Role

For a systems engineer, OpenTAP/opentap belongs in the Repository Workplaces inventory as part of
dependency acquisition, lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2022-03-07T13:22:54.219Z | [https://gitlab.com/api/v4/projects?search=package%20manager&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=package%20manager&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gitlab_projects_api_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gitlab_projects_api_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gitlab_projects_api | forge-api-derived | 2026-09-04 | `{"kind": "gitlab_projects_api", "query": "package manager", "retrieved": "2026-09-04", "status": "forge-api-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-4f24f34f664506` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| apk-tools | Package Manager | [open](repository-workplaces-apk-tools-8f57bb38.md) |
| dslackw/slpkg | Package Manager | [open](repository-workplaces-dslackw-slpkg-a996713a.md) |
| Gitea: 3rd/gitea | Package Manager | [open](repository-workplaces-gitea-3rd-gitea-57181cad.md) |
| Gitea: dco/gitea | Package Manager | [open](repository-workplaces-gitea-dco-gitea-31572b86.md) |
| Gitea: dh.azdevops.pipeline/dh.azdevops.pipeline | Package Manager | [open](repository-workplaces-gitea-dh-azdevops-pipeline-dh-azdevops-pipeline-2d51c7c4.md) |
| Gitea: donsenxu/gitea | Package Manager | [open](repository-workplaces-gitea-donsenxu-gitea-01b1797c.md) |
| Gitea: franklxw/action-setup | Package Manager | [open](repository-workplaces-gitea-franklxw-action-setup-ed18751e.md) |
| Gitea: imzbf/gitea | Package Manager | [open](repository-workplaces-gitea-imzbf-gitea-dea3091e.md) |

## Category Index

[Api Abi Checker (206)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (45)](../by-category/assertion-mocking.md) · [Async Runtime (134)](../by-category/async-runtime.md)
[Benchmarking (166)](../by-category/benchmarking.md) · [Build System (920)](../by-category/build-system.md) · [Cli (541)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (101)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (48)](../by-category/compression.md)
[Concurrency Parallelism (80)](../by-category/concurrency-parallelism.md) · [Configuration (116)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (165)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (837)](../by-category/database-datastore.md) · [Datetime (189)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (42)](../by-category/debugger.md) · [Dependency Manager (93)](../by-category/dependency-manager.md) · [Documentation (98)](../by-category/documentation.md)
[Embedded Hardware (55)](../by-category/embedded-hardware.md) · [Ffi Bindings (411)](../by-category/ffi-bindings.md) · [Filesystem Os (1411)](../by-category/filesystem-os.md) · [Formatter (615)](../by-category/formatter.md)
[Framework (55)](../by-category/framework.md) · [Fuzzer (55)](../by-category/fuzzer.md) · [Game Engine Game Dev (173)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1337)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (398)](../by-category/image-audio-dsp.md) · [Interop Bindings (58)](../by-category/interop-bindings.md) · [Interpreter Runtime (254)](../by-category/interpreter-runtime.md) · [Jit Vm (60)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1388)](../by-category/language-specification.md) · [Library (5308)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (43)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (486)](../by-category/logging-observability.md) · [Machine Learning (672)](../by-category/machine-learning.md)
[Math Numeric Scientific (85)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (89)](../by-category/memory-analyzer.md) · [Message Broker (39)](../by-category/message-broker.md) · [Networking Http (977)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · **[Package Manager (421)](../by-category/package-manager.md)** · [Parser Lexer Ast (1029)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (284)](../by-category/precommit-ci-quality.md)
[Profiler (82)](../by-category/profiler.md) · [Project Scaffolding (130)](../by-category/project-scaffolding.md) · [Registry Repository (108)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (333)](../by-category/security-sast.md) · [Serialization (383)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (500)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (522)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (58)](../by-category/tutorial-book-styleguide.md) · [Type Checker (301)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1513)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (95)](../by-category/utility-library.md) · [Visualization Gui (477)](../by-category/visualization-gui.md) · [Web Framework (454)](../by-category/web-framework.md)
