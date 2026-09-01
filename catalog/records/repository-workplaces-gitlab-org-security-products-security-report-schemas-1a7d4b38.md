# gitlab-org/security-products/security-report-schemas

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Dependency Manager](../by-category/dependency-manager.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Dependency Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/gitlab-org/security-products/security-report-schemas](https://gitlab.com/gitlab-org/security-products/security-report-schemas) |
| Source record ids | gitlab_projects_api-d452384e904bca |

## System Engineer Summary

This project contains schemas documenting the report format for dependency scanning, container
scanning, SAST, DAST, and other analyzers.

## Operational Role

For a systems engineer, gitlab-org/security-products/security-report-schemas belongs in the
Repository Workplaces inventory as part of ecosystem capability mapping, dependency review, release
awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-09-01T08:25:34.110Z | [https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `dependency_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gitlab_projects_api_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gitlab_projects_api_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gitlab_projects_api | forge-api-derived | 2026-09-01 | `{"kind": "gitlab_projects_api", "query": "security", "retrieved": "2026-09-01", "status": "forge-api-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `gitlab_projects_api-d452384e904bca` from `gitlab_projects_api` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| gitlab-org/security-products/gemnasium-db | Dependency Manager | [open](repository-workplaces-gitlab-org-security-products-gemnasium-db-646d6d68.md) |

## Category Index

[Api Abi Checker (171)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (37)](../by-category/assertion-mocking.md) · [Async Runtime (113)](../by-category/async-runtime.md)
[Benchmarking (93)](../by-category/benchmarking.md) · [Build System (721)](../by-category/build-system.md) · [Cli (478)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (80)](../by-category/community-reference.md) · [Compiler (146)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (42)](../by-category/compression.md)
[Concurrency Parallelism (68)](../by-category/concurrency-parallelism.md) · [Configuration (93)](../by-category/configuration.md) · [Container Deployment (7)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (152)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (517)](../by-category/database-datastore.md) · [Datetime (135)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (39)](../by-category/debugger.md) · **[Dependency Manager (74)](../by-category/dependency-manager.md)** · [Documentation (73)](../by-category/documentation.md)
[Embedded Hardware (42)](../by-category/embedded-hardware.md) · [Ffi Bindings (361)](../by-category/ffi-bindings.md) · [Filesystem Os (1053)](../by-category/filesystem-os.md) · [Formatter (511)](../by-category/formatter.md)
[Framework (42)](../by-category/framework.md) · [Fuzzer (43)](../by-category/fuzzer.md) · [Game Engine Game Dev (131)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1018)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (212)](../by-category/image-audio-dsp.md) · [Interop Bindings (50)](../by-category/interop-bindings.md) · [Interpreter Runtime (194)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (26)](../by-category/language-server.md) · [Language Specification (1060)](../by-category/language-specification.md) · [Library (4575)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (342)](../by-category/linter.md) · [Logging Observability (315)](../by-category/logging-observability.md) · [Machine Learning (533)](../by-category/machine-learning.md)
[Math Numeric Scientific (76)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (71)](../by-category/memory-analyzer.md) · [Message Broker (29)](../by-category/message-broker.md) · [Networking Http (817)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (236)](../by-category/package-manager.md) · [Parser Lexer Ast (842)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (227)](../by-category/precommit-ci-quality.md)
[Profiler (64)](../by-category/profiler.md) · [Project Scaffolding (102)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (11)](../by-category/sanitizer.md)
[Security Sast (284)](../by-category/security-sast.md) · [Serialization (320)](../by-category/serialization.md) · [Standard Library (23)](../by-category/standard-library.md) · [Static Analyzer (396)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (475)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (51)](../by-category/tutorial-book-styleguide.md) · [Type Checker (276)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1291)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (89)](../by-category/utility-library.md) · [Visualization Gui (381)](../by-category/visualization-gui.md) · [Web Framework (329)](../by-category/web-framework.md)
