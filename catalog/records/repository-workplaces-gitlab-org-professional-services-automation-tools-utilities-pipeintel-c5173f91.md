# gitlab-org/professional-services-automation/tools/utilities/pipeintel

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Package Manager](../by-category/package-manager.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/pipeintel -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Package Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/pipeintel](https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/pipeintel) |
| Source record ids | gitlab_projects_api-2e92c029d144e1 |

## System Engineer Summary

GitLab PipeIntel - Scan GitLab CI pipelines for security and correctness issues using OPA policies
and ShellCheck

## Operational Role

For a systems engineer, gitlab-org/professional-services-automation/tools/utilities/pipeintel
belongs in the Repository Workplaces inventory as part of dependency acquisition, lockfile policy,
provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-08-30T10:08:11.464Z | [https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
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
| gitlab_projects_api | forge-api-derived | 2026-09-01 | `{"kind": "gitlab_projects_api", "query": "security", "retrieved": "2026-09-01", "status": "forge-api-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-2e92c029d144e1` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| apk-tools | Package Manager | [open](repository-workplaces-apk-tools-8f57bb38.md) |
| dslackw/slpkg | Package Manager | [open](repository-workplaces-dslackw-slpkg-a996713a.md) |
| Gitea: 3rd/gitea | Package Manager | [open](repository-workplaces-gitea-3rd-gitea-57181cad.md) |
| Gitea: franklxw/action-setup | Package Manager | [open](repository-workplaces-gitea-franklxw-action-setup-ed18751e.md) |
| Gitea: liangruisen/action-setup | Package Manager | [open](repository-workplaces-gitea-liangruisen-action-setup-434563ff.md) |
| Gitea: trabalho/devops-app | Package Manager | [open](repository-workplaces-gitea-trabalho-devops-app-c6ffee99.md) |
| Gitea: VitorDiv/devops-pipeline | Package Manager | [open](repository-workplaces-gitea-vitordiv-devops-pipeline-b7f831c7.md) |
| juliendehos/nix42b | Package Manager | [open](repository-workplaces-juliendehos-nix42b-fe0574e7.md) |

## Category Index

[Api Abi Checker (176)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (41)](../by-category/assertion-mocking.md) · [Async Runtime (121)](../by-category/async-runtime.md)
[Benchmarking (106)](../by-category/benchmarking.md) · [Build System (787)](../by-category/build-system.md) · [Cli (488)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (81)](../by-category/community-reference.md) · [Compiler (157)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (43)](../by-category/compression.md)
[Concurrency Parallelism (70)](../by-category/concurrency-parallelism.md) · [Configuration (94)](../by-category/configuration.md) · [Container Deployment (8)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (153)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (681)](../by-category/database-datastore.md) · [Datetime (147)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (40)](../by-category/debugger.md) · [Dependency Manager (79)](../by-category/dependency-manager.md) · [Documentation (77)](../by-category/documentation.md)
[Embedded Hardware (46)](../by-category/embedded-hardware.md) · [Ffi Bindings (376)](../by-category/ffi-bindings.md) · [Filesystem Os (1125)](../by-category/filesystem-os.md) · [Formatter (533)](../by-category/formatter.md)
[Framework (45)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (138)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1098)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (265)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (223)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (26)](../by-category/language-server.md) · [Language Specification (1217)](../by-category/language-specification.md) · [Library (4679)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (344)](../by-category/linter.md) · [Logging Observability (381)](../by-category/logging-observability.md) · [Machine Learning (555)](../by-category/machine-learning.md)
[Math Numeric Scientific (78)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (75)](../by-category/memory-analyzer.md) · [Message Broker (31)](../by-category/message-broker.md) · [Networking Http (893)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · **[Package Manager (252)](../by-category/package-manager.md)** · [Parser Lexer Ast (887)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (254)](../by-category/precommit-ci-quality.md)
[Profiler (67)](../by-category/profiler.md) · [Project Scaffolding (116)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (308)](../by-category/security-sast.md) · [Serialization (363)](../by-category/serialization.md) · [Standard Library (23)](../by-category/standard-library.md) · [Static Analyzer (415)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (487)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (52)](../by-category/tutorial-book-styleguide.md) · [Type Checker (282)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1350)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (91)](../by-category/utility-library.md) · [Visualization Gui (399)](../by-category/visualization-gui.md) · [Web Framework (378)](../by-category/web-framework.md)
