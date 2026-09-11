# BrianDMG/conv2mp4-py

## Navigation

[Catalog index](../index.md) · [Language: Video](../by-language/video.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/BrianDMG/conv2mp4-py -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Video |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/BrianDMG/conv2mp4-py](https://github.com/BrianDMG/conv2mp4-py) |
| Source record ids | github_search_video-95d5ba78fbcfa7 |

## System Engineer Summary

Python script that recursively searches through a user-defined file path and converts all videos of
user-specified file types to MP4 with H264 video and AAC audio using ffmpeg. If a conversion failure
is detected, the script re-encodes the file with HandbrakeCLI. Upon successful encoding, Plex
libraries are refreshed and source file is deleted. The purpose of this script is to reduce the
amount of transcoding CPU load on a Plex server.

## Operational Role

For a systems engineer, BrianDMG/conv2mp4-py belongs in the Video inventory as part of build graph
control, artifact reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2020-01-27T23:34:14Z | gh search repos topic:video-encoding stars:>20 | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Mixed license review |
| Evidence | MIT License; https://api.github.com/licenses/mit; GNU General Public License v3.0; https://api.github.com/licenses/gpl-3.0 |
| Alert | Backup plan: mixed expression or dual license detected; choose the permissive option only when the exact terms allow it. |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-09 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "topic:video-encoding stars:>20", "retrieved": "2026-09-09", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_video-95d5ba78fbcfa7` from `github_search_video` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| 75lb/handbrake-js | Build System | [open](video-75lb-handbrake-js-25bf05e0.md) |
| akka/akka-core | Build System | [open](video-akka-akka-core-a55697ca.md) |
| apache/rocketmq | Build System | [open](video-apache-rocketmq-8ba30bb6.md) |
| apache/streampark | Build System | [open](video-apache-streampark-028cf6a0.md) |
| cloudwego/kitex | Build System | [open](video-cloudwego-kitex-8efffcb5.md) |
| dmotz/trystero | Build System | [open](video-dmotz-trystero-528e8e4d.md) |
| encoding-ninja/per-title-analysis | Build System | [open](video-encoding-ninja-per-title-analysis-8f2c75e1.md) |
| HaveAGitGat/Tdarr | Build System | [open](video-haveagitgat-tdarr-91bd4936.md) |

## Category Index

[Api Abi Checker (236)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (139)](../by-category/async-runtime.md)
[Benchmarking (209)](../by-category/benchmarking.md) · **[Build System (1040)](../by-category/build-system.md)** · [Cli (595)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (125)](../by-category/community-reference.md) · [Compiler (177)](../by-category/compiler.md) · [Compiler Diagnostics (25)](../by-category/compiler-diagnostics.md) · [Compression (55)](../by-category/compression.md)
[Concurrency Parallelism (95)](../by-category/concurrency-parallelism.md) · [Configuration (140)](../by-category/configuration.md) · [Container Deployment (10)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (182)](../by-category/cryptography.md) · [Data Science (40)](../by-category/data-science.md) · [Database Datastore (981)](../by-category/database-datastore.md) · [Datetime (252)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (45)](../by-category/debugger.md) · [Dependency Manager (110)](../by-category/dependency-manager.md) · [Documentation (115)](../by-category/documentation.md)
[Embedded Hardware (68)](../by-category/embedded-hardware.md) · [Ffi Bindings (486)](../by-category/ffi-bindings.md) · [Filesystem Os (1699)](../by-category/filesystem-os.md) · [Formatter (665)](../by-category/formatter.md)
[Framework (64)](../by-category/framework.md) · [Fuzzer (63)](../by-category/fuzzer.md) · [Game Engine Game Dev (375)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1511)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (448)](../by-category/image-audio-dsp.md) · [Interop Bindings (65)](../by-category/interop-bindings.md) · [Interpreter Runtime (288)](../by-category/interpreter-runtime.md) · [Jit Vm (67)](../by-category/jit-vm.md)
[Language Server (31)](../by-category/language-server.md) · [Language Specification (1469)](../by-category/language-specification.md) · [Library (6057)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (51)](../by-category/lint-rule-pack.md) · [Linter (350)](../by-category/linter.md) · [Logging Observability (550)](../by-category/logging-observability.md) · [Machine Learning (853)](../by-category/machine-learning.md)
[Math Numeric Scientific (96)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (102)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1085)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (450)](../by-category/package-manager.md) · [Parser Lexer Ast (1238)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (322)](../by-category/precommit-ci-quality.md)
[Profiler (98)](../by-category/profiler.md) · [Project Scaffolding (142)](../by-category/project-scaffolding.md) · [Registry Repository (134)](../by-category/registry-repository.md) · [Sanitizer (16)](../by-category/sanitizer.md)
[Security Sast (340)](../by-category/security-sast.md) · [Serialization (404)](../by-category/serialization.md) · [Standard Library (26)](../by-category/standard-library.md) · [Static Analyzer (666)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (641)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (73)](../by-category/tutorial-book-styleguide.md) · [Type Checker (318)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1658)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (107)](../by-category/utility-library.md) · [Visualization Gui (648)](../by-category/visualization-gui.md) · [Web Framework (495)](../by-category/web-framework.md)
