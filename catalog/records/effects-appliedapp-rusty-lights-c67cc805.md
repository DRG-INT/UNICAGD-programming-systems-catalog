# appliedapp/rusty_lights

## Navigation

[Catalog index](../index.md) · [Language: Effects](../by-language/effects.md) · [Category: Package Manager](../by-category/package-manager.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/appliedapp/rusty_lights -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Effects |
| Category | Package Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/appliedapp/rusty_lights](https://github.com/appliedapp/rusty_lights) |
| Source record ids | github_search_effects-452b8987c99c53 |

## System Engineer Summary

Audio-reactive LED visualizer written in Rust. Captures audio via PipeWire, ALSA, or FIFO (MPD),
runs it through a real-time DSP pipeline (FFT, Mel filterbank, beat detection), and drives LED
strips over E1.31/sACN, DDP, or Art-Net. 7 built-in effects, multi-universe support, lock-free audio
path. Targets Raspberry Pi with <5% CPU usage.

## Operational Role

For a systems engineer, appliedapp/rusty_lights belongs in the Effects inventory as part of
dependency acquisition, lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2026-05-04T20:20:12Z | gh search repos audio effects dsp | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Backup plan required |
| Evidence | GNU General Public License v3.0; https://api.github.com/licenses/gpl-3.0 |
| Alert | Backup plan required before embedding, redistributing, or modifying architecture around this dependency. |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-03 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "audio effects dsp", "retrieved": "2026-09-03", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_effects-452b8987c99c53` from `github_search_effects` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| alexanderrichtertd/plex | Package Manager | [open](effects-alexanderrichtertd-plex-75c31e14.md) |
| Audio4Linux/JDSP4Linux | Package Manager | [open](effects-audio4linux-jdsp4linux-e90e4af9.md) |
| beinteractive/LWRPAmbientOcclusion | Package Manager | [open](effects-beinteractive-lwrpambientocclusion-7b85e0e3.md) |
| CialloKing/ba-click-fx | Package Manager | [open](effects-cialloking-ba-click-fx-b842180a.md) |
| CyberAgentGameEntertainment/NovaShader | Package Manager | [open](effects-cyberagentgameentertainment-novashader-cfdfe2cf.md) |
| demonixis/SSGI-URP | Package Manager | [open](effects-demonixis-ssgi-urp-4db7e7d8.md) |
| GarrettGunnell/Post-Processing | Package Manager | [open](effects-garrettgunnell-post-processing-2bb2ca4a.md) |
| GeorgePyralis/dsp-audio-fx | Package Manager | [open](effects-georgepyralis-dsp-audio-fx-f597d4dc.md) |

## Category Index

[Api Abi Checker (202)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (133)](../by-category/async-runtime.md)
[Benchmarking (164)](../by-category/benchmarking.md) · [Build System (885)](../by-category/build-system.md) · [Cli (528)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (92)](../by-category/community-reference.md) · [Compiler (174)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (46)](../by-category/compression.md)
[Concurrency Parallelism (78)](../by-category/concurrency-parallelism.md) · [Configuration (108)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (162)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (830)](../by-category/database-datastore.md) · [Datetime (180)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (42)](../by-category/debugger.md) · [Dependency Manager (91)](../by-category/dependency-manager.md) · [Documentation (96)](../by-category/documentation.md)
[Embedded Hardware (54)](../by-category/embedded-hardware.md) · [Ffi Bindings (402)](../by-category/ffi-bindings.md) · [Filesystem Os (1343)](../by-category/filesystem-os.md) · [Formatter (590)](../by-category/formatter.md)
[Framework (52)](../by-category/framework.md) · [Fuzzer (53)](../by-category/fuzzer.md) · [Game Engine Game Dev (168)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1289)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (356)](../by-category/image-audio-dsp.md) · [Interop Bindings (57)](../by-category/interop-bindings.md) · [Interpreter Runtime (247)](../by-category/interpreter-runtime.md) · [Jit Vm (59)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1273)](../by-category/language-specification.md) · [Library (5146)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (43)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (477)](../by-category/logging-observability.md) · [Machine Learning (636)](../by-category/machine-learning.md)
[Math Numeric Scientific (83)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (36)](../by-category/message-broker.md) · [Networking Http (957)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · **[Package Manager (409)](../by-category/package-manager.md)** · [Parser Lexer Ast (994)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (275)](../by-category/precommit-ci-quality.md)
[Profiler (79)](../by-category/profiler.md) · [Project Scaffolding (128)](../by-category/project-scaffolding.md) · [Registry Repository (108)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (332)](../by-category/security-sast.md) · [Serialization (377)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (487)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (514)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (54)](../by-category/tutorial-book-styleguide.md) · [Type Checker (297)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1487)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (452)](../by-category/visualization-gui.md) · [Web Framework (447)](../by-category/web-framework.md)
