# MTG/essentia

## Navigation

[Catalog index](../index.md) · [Language: Audio](../by-language/audio.md) · [Category: Static Analyzer](../by-category/static-analyzer.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/MTG/essentia -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Audio |
| Category | Static Analyzer |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/MTG/essentia](https://github.com/MTG/essentia) |
| Source record ids | github_search_audio-4bd4b29550b48f |

## System Engineer Summary

C++ library for audio and music analysis, description and synthesis, including Python bindings

## Operational Role

For a systems engineer, MTG/essentia belongs in the Audio inventory as part of defect discovery,
security review, undefined-state detection, and regression prevention.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-08-27T18:31:38Z | gh search repos topic:dsp stars:>100 | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Backup plan required |
| Evidence | GNU Affero General Public License v3.0; https://api.github.com/licenses/agpl-3.0 |
| Alert | Backup plan required before embedding, redistributing, or modifying architecture around this dependency. |

## Engineering Notes

- Treat category as `static_analyzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-05 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "topic:dsp stars:>100", "retrieved": "2026-09-05", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_audio-4bd4b29550b48f` from `github_search_audio` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aubio/aubio | Static Analyzer | [open](audio-aubio-aubio-83afbe36.md) |
| AudioKit/AudioKit | Static Analyzer | [open](audio-audiokit-audiokit-8e968f0e.md) |
| GareBear99/FreeEQ8 | Static Analyzer | [open](audio-garebear99-freeeq8-449a3a9b.md) |
| jmerkt/cqt-analyzer | Static Analyzer | [open](audio-jmerkt-cqt-analyzer-19714d3e.md) |
| josevcm/nfc-laboratory | Static Analyzer | [open](audio-josevcm-nfc-laboratory-8a84bc6a.md) |
| jpcima/spectacle | Static Analyzer | [open](audio-jpcima-spectacle-a8709cd5.md) |
| libAudioFlux/audioFlux | Static Analyzer | [open](audio-libaudioflux-audioflux-7311838f.md) |
| librosa/librosa | Static Analyzer | [open](audio-librosa-librosa-8068a972.md) |

## Category Index

[Api Abi Checker (215)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (136)](../by-category/async-runtime.md)
[Benchmarking (194)](../by-category/benchmarking.md) · [Build System (982)](../by-category/build-system.md) · [Cli (561)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (116)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (50)](../by-category/compression.md)
[Concurrency Parallelism (89)](../by-category/concurrency-parallelism.md) · [Configuration (128)](../by-category/configuration.md) · [Container Deployment (10)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (173)](../by-category/cryptography.md) · [Data Science (38)](../by-category/data-science.md) · [Database Datastore (888)](../by-category/database-datastore.md) · [Datetime (223)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (44)](../by-category/debugger.md) · [Dependency Manager (101)](../by-category/dependency-manager.md) · [Documentation (103)](../by-category/documentation.md)
[Embedded Hardware (56)](../by-category/embedded-hardware.md) · [Ffi Bindings (452)](../by-category/ffi-bindings.md) · [Filesystem Os (1569)](../by-category/filesystem-os.md) · [Formatter (643)](../by-category/formatter.md)
[Framework (63)](../by-category/framework.md) · [Fuzzer (57)](../by-category/fuzzer.md) · [Game Engine Game Dev (354)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1444)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (430)](../by-category/image-audio-dsp.md) · [Interop Bindings (61)](../by-category/interop-bindings.md) · [Interpreter Runtime (267)](../by-category/interpreter-runtime.md) · [Jit Vm (63)](../by-category/jit-vm.md)
[Language Server (29)](../by-category/language-server.md) · [Language Specification (1428)](../by-category/language-specification.md) · [Library (5570)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (48)](../by-category/lint-rule-pack.md) · [Linter (348)](../by-category/linter.md) · [Logging Observability (519)](../by-category/logging-observability.md) · [Machine Learning (769)](../by-category/machine-learning.md)
[Math Numeric Scientific (88)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (96)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1029)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (440)](../by-category/package-manager.md) · [Parser Lexer Ast (1089)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (298)](../by-category/precommit-ci-quality.md)
[Profiler (86)](../by-category/profiler.md) · [Project Scaffolding (132)](../by-category/project-scaffolding.md) · [Registry Repository (133)](../by-category/registry-repository.md) · [Sanitizer (14)](../by-category/sanitizer.md)
[Security Sast (336)](../by-category/security-sast.md) · [Serialization (393)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · **[Static Analyzer (596)](../by-category/static-analyzer.md)**
[Templating (2)](../by-category/templating.md) · [Testing Framework (603)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (63)](../by-category/tutorial-book-styleguide.md) · [Type Checker (313)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1595)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (103)](../by-category/utility-library.md) · [Visualization Gui (547)](../by-category/visualization-gui.md) · [Web Framework (476)](../by-category/web-framework.md)
