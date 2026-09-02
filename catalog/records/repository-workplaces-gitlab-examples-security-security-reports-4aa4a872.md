# gitlab-examples/security/security-reports

## Navigation

[Catalog index](../index.md) · [Language: Repository Workplaces](../by-language/repository-workplaces.md) · [Category: Security Sast](../by-category/security-sast.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gitlab.com/gitlab-examples/security/security-reports -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Repository Workplaces |
| Category | Security Sast |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gitlab.com/gitlab-examples/security/security-reports](https://gitlab.com/gitlab-examples/security/security-reports) |
| Source record ids | gitlab_projects_api-d5c098bf8428ed |

## System Engineer Summary

GitLab project discovered from the official GitLab projects API.

## Operational Role

For a systems engineer, gitlab-examples/security/security-reports belongs in the Repository
Workplaces inventory as part of supply-chain review, vulnerability detection, and release gate
enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-06-30T12:05:34.848Z | [https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100](https://gitlab.com/api/v4/projects?search=security&order_by=star_count&sort=desc&simple=true&per_page=100) | gitlab_projects_api_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gitlab_projects_api_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
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

- `gitlab_projects_api-d5c098bf8428ed` from `gitlab_projects_api` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| albertito/chasquid | Security Sast | [open](repository-workplaces-albertito-chasquid-e1db3cbd.md) |
| amrron/setup-scripts | Security Sast | [open](repository-workplaces-amrron-setup-scripts-ba1a0bf0.md) |
| Arszilla/kali-i3 | Security Sast | [open](repository-workplaces-arszilla-kali-i3-77ac7a53.md) |
| ataraxialinux/ataraxia | Security Sast | [open](repository-workplaces-ataraxialinux-ataraxia-2c1d6174.md) |
| components/sast | Security Sast | [open](repository-workplaces-components-sast-06739183.md) |
| comunidade-cloud/aws/atualizar-ip-no-security-group | Security Sast | [open](repository-workplaces-comunidade-cloud-aws-atualizar-ip-no-security-group-2b0060ed.md) |
| d7security/d7security | Security Sast | [open](repository-workplaces-d7security-d7security-e5301244.md) |
| expliot_framework/expliot | Security Sast | [open](repository-workplaces-expliot-framework-expliot-032905f5.md) |

## Category Index

[Api Abi Checker (190)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (41)](../by-category/assertion-mocking.md) · [Async Runtime (125)](../by-category/async-runtime.md)
[Benchmarking (119)](../by-category/benchmarking.md) · [Build System (825)](../by-category/build-system.md) · [Cli (503)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (88)](../by-category/community-reference.md) · [Compiler (171)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (73)](../by-category/concurrency-parallelism.md) · [Configuration (100)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (156)](../by-category/cryptography.md) · [Data Science (33)](../by-category/data-science.md) · [Database Datastore (754)](../by-category/database-datastore.md) · [Datetime (160)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (87)](../by-category/dependency-manager.md) · [Documentation (88)](../by-category/documentation.md)
[Embedded Hardware (49)](../by-category/embedded-hardware.md) · [Ffi Bindings (388)](../by-category/ffi-bindings.md) · [Filesystem Os (1213)](../by-category/filesystem-os.md) · [Formatter (548)](../by-category/formatter.md)
[Framework (49)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (159)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1145)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (301)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (234)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1237)](../by-category/language-specification.md) · [Library (4859)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (41)](../by-category/lint-rule-pack.md) · [Linter (346)](../by-category/linter.md) · [Logging Observability (394)](../by-category/logging-observability.md) · [Machine Learning (594)](../by-category/machine-learning.md)
[Math Numeric Scientific (79)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (86)](../by-category/memory-analyzer.md) · [Message Broker (32)](../by-category/message-broker.md) · [Networking Http (923)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (271)](../by-category/package-manager.md) · [Parser Lexer Ast (926)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (262)](../by-category/precommit-ci-quality.md)
[Profiler (72)](../by-category/profiler.md) · [Project Scaffolding (120)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
**[Security Sast (313)](../by-category/security-sast.md)** · [Serialization (370)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (445)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (498)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (292)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1400)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (415)](../by-category/visualization-gui.md) · [Web Framework (411)](../by-category/web-framework.md)
