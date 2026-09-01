# Etxx321/StarDoctor

## Navigation

[Catalog index](../index.md) · [Language: Space Maps](../by-language/space-maps.md) · [Category: Ide Editor Integration](../by-category/ide-editor-integration.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/Etxx321/StarDoctor -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Space Maps |
| Category | Ide Editor Integration |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/Etxx321/StarDoctor](https://github.com/Etxx321/StarDoctor) |
| Source record ids | github_search_space_maps-9ca96fcf502161 |

## System Engineer Summary

StarDoctor is a project we made over the course our bachelor's degree at the Technion Institute of
Technology. Through the course of our project, we implemented an app that allows the user to see the
current position of thousands of stars outside of our solar system. To achieve this, we used 3D
modeling tools, the Unity development environment for 3D applications, and the IAU SOFA’s astronomy
code libraries. In addition, our app uses the HYG (Hipparcos, Yale, Gliese) database, that provides
data crucial to calculate the position of stars relative to the user’s location. Using the database,
and the data from the device’s sensors, the app finds the current position of the observed objects,
using SOFA’s library functions that converts between celestial coordinated systems. After processing
the data, the app visualizes everything in the simulated 3D environment. The orientation of the
device in space is computed using the device’s magnetometer, gyroscope, and accelerometer. According
to the observed field of view, relevant parts of the simulated sky map are shown on screen.

## Operational Role

For a systems engineer, Etxx321/StarDoctor belongs in the Space Maps inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2022-03-19T22:52:20Z | gh search repos astronomy sky map | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | {"key": "", "name": "", "url": ""} |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `ide_editor_integration` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-01 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "astronomy sky map", "retrieved": "2026-09-01", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_space_maps-9ca96fcf502161` from `github_search_space_maps` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| ace-dev-pixel/StargazerAR | Ide Editor Integration | [open](space-maps-ace-dev-pixel-stargazerar-e0b868d3.md) |
| Aldenhovel/bleu-rouge-meteor-cider-spice-eval4imagecaption | Ide Editor Integration | [open](space-maps-aldenhovel-bleu-rouge-meteor-cider-spice-eval4imagecaption-a9840e82.md) |
| Dyalwayshappy/Spice_personal | Ide Editor Integration | [open](space-maps-dyalwayshappy-spice-personal-fbe6d648.md) |
| google/skywater-pdk-libs-sky130_fd_pr | Ide Editor Integration | [open](space-maps-google-skywater-pdk-libs-sky130-fd-pr-63b6c072.md) |
| JuliaSpaceMissionDesign/Ephemerides.jl | Ide Editor Integration | [open](space-maps-juliaspacemissiondesign-ephemerides-jl-b8ea4e8a.md) |
| MuMashhour/NE555-SPICE-Model | Ide Editor Integration | [open](space-maps-mumashhour-ne555-spice-model-b48aca64.md) |
| MWATelescope/mwa_hyperdrive | Ide Editor Integration | [open](space-maps-mwatelescope-mwa-hyperdrive-ec8debf1.md) |
| nyx-space/nyx | Ide Editor Integration | [open](space-maps-nyx-space-nyx-2403bcdd.md) |

## Category Index

[Api Abi Checker (176)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (41)](../by-category/assertion-mocking.md) · [Async Runtime (120)](../by-category/async-runtime.md)
[Benchmarking (106)](../by-category/benchmarking.md) · [Build System (780)](../by-category/build-system.md) · [Cli (488)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (81)](../by-category/community-reference.md) · [Compiler (157)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (43)](../by-category/compression.md)
[Concurrency Parallelism (70)](../by-category/concurrency-parallelism.md) · [Configuration (94)](../by-category/configuration.md) · [Container Deployment (8)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (153)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (679)](../by-category/database-datastore.md) · [Datetime (147)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (40)](../by-category/debugger.md) · [Dependency Manager (79)](../by-category/dependency-manager.md) · [Documentation (77)](../by-category/documentation.md)
[Embedded Hardware (46)](../by-category/embedded-hardware.md) · [Ffi Bindings (375)](../by-category/ffi-bindings.md) · [Filesystem Os (1124)](../by-category/filesystem-os.md) · [Formatter (529)](../by-category/formatter.md)
[Framework (45)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (138)](../by-category/game-engine-game-dev.md) · **[Ide Editor Integration (1085)](../by-category/ide-editor-integration.md)**
[Image Audio Dsp (262)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (223)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (26)](../by-category/language-server.md) · [Language Specification (1216)](../by-category/language-specification.md) · [Library (4675)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (344)](../by-category/linter.md) · [Logging Observability (325)](../by-category/logging-observability.md) · [Machine Learning (555)](../by-category/machine-learning.md)
[Math Numeric Scientific (78)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (75)](../by-category/memory-analyzer.md) · [Message Broker (31)](../by-category/message-broker.md) · [Networking Http (891)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (248)](../by-category/package-manager.md) · [Parser Lexer Ast (885)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (253)](../by-category/precommit-ci-quality.md)
[Profiler (66)](../by-category/profiler.md) · [Project Scaffolding (107)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (307)](../by-category/security-sast.md) · [Serialization (362)](../by-category/serialization.md) · [Standard Library (23)](../by-category/standard-library.md) · [Static Analyzer (413)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (487)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (52)](../by-category/tutorial-book-styleguide.md) · [Type Checker (282)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1344)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (91)](../by-category/utility-library.md) · [Visualization Gui (399)](../by-category/visualization-gui.md) · [Web Framework (377)](../by-category/web-framework.md)
