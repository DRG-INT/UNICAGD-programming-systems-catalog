# trapper-project/trapper

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Async Runtime](../by-category/async-runtime.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/trapper-project/trapper -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Async Runtime |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/trapper-project/trapper](https://gitlab.com/trapper-project/trapper) |
| Source record ids | gitlab_projects_api-334d9e19f7177e |

## System Engineer Summary

Trapper Expert - serves as the core web application (TRAPPER), encompassing all essential
functionalities of the system. It features an Angular-based and Bootstrap frontend, coupled with a
Django-based backend. The application utilizes a PostgreSQL database with PostGIS extension for
spatial data handling, and employs RabbitMQ as a message broker with Celery workers for asynchronous
task processing.

## Operational Role

For a systems engineer, trapper-project/trapper belongs in the Repository Workplaces inventory as
part of concurrency scheduling, I/O throughput, cancellation, and latency management.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-09-11T15:36:22.247Z | [https://gitlab.com/api/v4/projects?search=database&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=database&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `async_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gitlab_projects_api_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gitlab_projects_api_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gitlab_projects_api | forge-api-derived | 2026-09-12 | `{"kind": "gitlab_projects_api", "query": "database", "retrieved": "2026-09-12", "status": "forge-api-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-334d9e19f7177e` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Gitea: EchORM/ormdantic | Async Runtime | [open](repository-workplaces-gitea-echorm-ormdantic-10c1ef15.md) |

## Category Index

[Api Abi Checker (236)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · **[Async Runtime (139)](../by-category/async-runtime.md)**
[Benchmarking (209)](../by-category/benchmarking.md) · [Build System (1040)](../by-category/build-system.md) · [Cli (596)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (125)](../by-category/community-reference.md) · [Compiler (180)](../by-category/compiler.md) · [Compiler Diagnostics (26)](../by-category/compiler-diagnostics.md) · [Compression (55)](../by-category/compression.md)
[Concurrency Parallelism (95)](../by-category/concurrency-parallelism.md) · [Configuration (141)](../by-category/configuration.md) · [Container Deployment (10)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (182)](../by-category/cryptography.md) · [Data Science (40)](../by-category/data-science.md) · [Database Datastore (981)](../by-category/database-datastore.md) · [Datetime (253)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (45)](../by-category/debugger.md) · [Dependency Manager (110)](../by-category/dependency-manager.md) · [Documentation (115)](../by-category/documentation.md)
[Embedded Hardware (68)](../by-category/embedded-hardware.md) · [Ffi Bindings (486)](../by-category/ffi-bindings.md) · [Filesystem Os (1706)](../by-category/filesystem-os.md) · [Formatter (667)](../by-category/formatter.md)
[Framework (64)](../by-category/framework.md) · [Fuzzer (63)](../by-category/fuzzer.md) · [Game Engine Game Dev (377)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1511)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (448)](../by-category/image-audio-dsp.md) · [Interop Bindings (65)](../by-category/interop-bindings.md) · [Interpreter Runtime (289)](../by-category/interpreter-runtime.md) · [Jit Vm (67)](../by-category/jit-vm.md)
[Language Server (31)](../by-category/language-server.md) · [Language Specification (1470)](../by-category/language-specification.md) · [Library (6091)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (51)](../by-category/lint-rule-pack.md) · [Linter (350)](../by-category/linter.md) · [Logging Observability (552)](../by-category/logging-observability.md) · [Machine Learning (856)](../by-category/machine-learning.md)
[Math Numeric Scientific (97)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (102)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1087)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (450)](../by-category/package-manager.md) · [Parser Lexer Ast (1241)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (324)](../by-category/precommit-ci-quality.md)
[Profiler (98)](../by-category/profiler.md) · [Project Scaffolding (142)](../by-category/project-scaffolding.md) · [Registry Repository (134)](../by-category/registry-repository.md) · [Sanitizer (16)](../by-category/sanitizer.md)
[Security Sast (341)](../by-category/security-sast.md) · [Serialization (407)](../by-category/serialization.md) · [Standard Library (26)](../by-category/standard-library.md) · [Static Analyzer (668)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (649)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (73)](../by-category/tutorial-book-styleguide.md) · [Type Checker (318)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1662)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (107)](../by-category/utility-library.md) · [Visualization Gui (650)](../by-category/visualization-gui.md) · [Web Framework (496)](../by-category/web-framework.md)
