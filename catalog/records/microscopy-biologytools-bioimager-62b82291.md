# BiologyTools/BioImager

## Navigation

[Catalog index](../index.md) · [Language: Microscopy](../by-language/microscopy.md) · [Category: Logging Observability](../by-category/logging-observability.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/BiologyTools/BioImager -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Microscopy |
| Category | Logging Observability |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/BiologyTools/BioImager](https://github.com/BiologyTools/BioImager) |
| Source record ids | github_search_microscopy-5eb4c23c51c1fb |

## System Engineer Summary

A .NET microscopy imaging application based on Bio library. Supports various microscopes by using
imported libraries & GUI automation. Supports XInput game controllers to move stage, take images,
run ImageJ macros on images or Bio C# scripts.

## Operational Role

For a systems engineer, BiologyTools/BioImager belongs in the Microscopy inventory as part of
diagnostics, metrics, auditability, tracing, and incident response.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-06-19T10:01:50Z | gh search repos topic:microscope stars:>10 | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Backup plan required |
| Evidence | GNU General Public License v3.0; https://api.github.com/licenses/gpl-3.0 |
| Alert | Backup plan required before embedding, redistributing, or modifying architecture around this dependency. |

## Engineering Notes

- Treat category as `logging_observability` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-03 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "topic:microscope stars:>10", "retrieved": "2026-09-03", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_microscopy-5eb4c23c51c1fb` from `github_search_microscopy` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| afermg/cp_measure | Logging Observability | [open](microscopy-afermg-cp-measure-ee9fd0ec.md) |
| Dana-Farber-AIOS/pathml | Logging Observability | [open](microscopy-dana-farber-aios-pathml-b56cd566.md) |
| flika-org/flika | Logging Observability | [open](microscopy-flika-org-flika-fc3890a5.md) |
| henkrijneveld/Microscope-PiCam | Logging Observability | [open](microscopy-henkrijneveld-microscope-picam-4e8a335c.md) |
| holmos-mikroskop/holmos | Logging Observability | [open](microscopy-holmos-mikroskop-holmos-086d35a4.md) |
| ijpb/MorphoLibJ | Logging Observability | [open](microscopy-ijpb-morpholibj-fb1a146e.md) |
| kevinjohncutler/omnipose | Logging Observability | [open](microscopy-kevinjohncutler-omnipose-48a8957e.md) |
| TissueImageAnalytics/tiatoolbox | Logging Observability | [open](microscopy-tissueimageanalytics-tiatoolbox-a18863d3.md) |

## Category Index

[Api Abi Checker (201)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (133)](../by-category/async-runtime.md)
[Benchmarking (164)](../by-category/benchmarking.md) · [Build System (884)](../by-category/build-system.md) · [Cli (528)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (92)](../by-category/community-reference.md) · [Compiler (174)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (46)](../by-category/compression.md)
[Concurrency Parallelism (77)](../by-category/concurrency-parallelism.md) · [Configuration (108)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (162)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (830)](../by-category/database-datastore.md) · [Datetime (178)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (42)](../by-category/debugger.md) · [Dependency Manager (91)](../by-category/dependency-manager.md) · [Documentation (95)](../by-category/documentation.md)
[Embedded Hardware (54)](../by-category/embedded-hardware.md) · [Ffi Bindings (401)](../by-category/ffi-bindings.md) · [Filesystem Os (1331)](../by-category/filesystem-os.md) · [Formatter (587)](../by-category/formatter.md)
[Framework (52)](../by-category/framework.md) · [Fuzzer (53)](../by-category/fuzzer.md) · [Game Engine Game Dev (164)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1280)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (355)](../by-category/image-audio-dsp.md) · [Interop Bindings (57)](../by-category/interop-bindings.md) · [Interpreter Runtime (242)](../by-category/interpreter-runtime.md) · [Jit Vm (59)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1270)](../by-category/language-specification.md) · [Library (5128)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (43)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · **[Logging Observability (473)](../by-category/logging-observability.md)** · [Machine Learning (634)](../by-category/machine-learning.md)
[Math Numeric Scientific (83)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (36)](../by-category/message-broker.md) · [Networking Http (956)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (408)](../by-category/package-manager.md) · [Parser Lexer Ast (993)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (274)](../by-category/precommit-ci-quality.md)
[Profiler (79)](../by-category/profiler.md) · [Project Scaffolding (127)](../by-category/project-scaffolding.md) · [Registry Repository (108)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (332)](../by-category/security-sast.md) · [Serialization (377)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (486)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (513)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (54)](../by-category/tutorial-book-styleguide.md) · [Type Checker (297)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1480)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (446)](../by-category/visualization-gui.md) · [Web Framework (447)](../by-category/web-framework.md)
