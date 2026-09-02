# gitlab-org/gitlab

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Static Analyzer](../by-category/static-analyzer.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/gitlab-org/gitlab -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Static Analyzer |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab) |
| Source record ids | gitlab_projects_api-f6c556e13fada3 |

## System Engineer Summary

GitLab is the open-source DevSecOps platform that provides a complete software development lifecycle
toolchain including source control, CI/CD, security scanning, and project management in a single
application.

## Operational Role

For a systems engineer, gitlab-org/gitlab belongs in the Repository Workplaces inventory as part of
defect discovery, security review, undefined-state detection, and regression prevention.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-09-02T21:30:37.747Z | [https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `static_analyzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gitlab_projects_api_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gitlab_projects_api_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gitlab_projects_api | forge-api-derived | 2026-09-02 | `{"kind": "gitlab_projects_api", "query": "security", "retrieved": "2026-09-02", "status": "forge-api-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-f6c556e13fada3` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| arturbosch/detekt | Static Analyzer | [open](repository-workplaces-arturbosch-detekt-56d0535b.md) |
| Gitea: awdscan/awdscanserver | Static Analyzer | [open](repository-workplaces-gitea-awdscan-awdscanserver-8258eaa2.md) |
| Gitea: corricca/elibrary-publication-analyzer | Static Analyzer | [open](repository-workplaces-gitea-corricca-elibrary-publication-analyzer-3d1b67ed.md) |
| Gitea: ImageProcessing-ElectronicPublications/imthreshold | Static Analyzer | [open](repository-workplaces-gitea-imageprocessing-electronicpublications-imthreshold-a87c44af.md) |
| gitlab-org/cluster-integration/gitlab-agent | Static Analyzer | [open](repository-workplaces-gitlab-org-cluster-integration-gitlab-agent-4d660b44.md) |
| gitlab-org/security-products/analyzers/container-scanning | Static Analyzer | [open](repository-workplaces-gitlab-org-security-products-analyzers-container-scanning-e8af16f2.md) |
| gitlab-security-oss/cis/gitlabcis | Static Analyzer | [open](repository-workplaces-gitlab-security-oss-cis-gitlabcis-f7ce6047.md) |
| hgraca/app-mapper | Static Analyzer | [open](repository-workplaces-hgraca-app-mapper-4c3b2338.md) |

## Category Index

[Api Abi Checker (198)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (42)](../by-category/assertion-mocking.md) · [Async Runtime (131)](../by-category/async-runtime.md)
[Benchmarking (152)](../by-category/benchmarking.md) · [Build System (858)](../by-category/build-system.md) · [Cli (518)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (90)](../by-category/community-reference.md) · [Compiler (172)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (74)](../by-category/concurrency-parallelism.md) · [Configuration (105)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (13)](../by-category/coverage.md)
[Cryptography (158)](../by-category/cryptography.md) · [Data Science (34)](../by-category/data-science.md) · [Database Datastore (778)](../by-category/database-datastore.md) · [Datetime (166)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (90)](../by-category/dependency-manager.md) · [Documentation (92)](../by-category/documentation.md)
[Embedded Hardware (51)](../by-category/embedded-hardware.md) · [Ffi Bindings (395)](../by-category/ffi-bindings.md) · [Filesystem Os (1271)](../by-category/filesystem-os.md) · [Formatter (570)](../by-category/formatter.md)
[Framework (51)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (162)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1241)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (312)](../by-category/image-audio-dsp.md) · [Interop Bindings (56)](../by-category/interop-bindings.md) · [Interpreter Runtime (240)](../by-category/interpreter-runtime.md) · [Jit Vm (58)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1257)](../by-category/language-specification.md) · [Library (5011)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (42)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (461)](../by-category/logging-observability.md) · [Machine Learning (613)](../by-category/machine-learning.md)
[Math Numeric Scientific (82)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (34)](../by-category/message-broker.md) · [Networking Http (941)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (399)](../by-category/package-manager.md) · [Parser Lexer Ast (947)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (268)](../by-category/precommit-ci-quality.md)
[Profiler (76)](../by-category/profiler.md) · [Project Scaffolding (124)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (324)](../by-category/security-sast.md) · [Serialization (374)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · **[Static Analyzer (464)](../by-category/static-analyzer.md)**
[Templating (2)](../by-category/templating.md) · [Testing Framework (508)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (293)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1443)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (427)](../by-category/visualization-gui.md) · [Web Framework (429)](../by-category/web-framework.md)
