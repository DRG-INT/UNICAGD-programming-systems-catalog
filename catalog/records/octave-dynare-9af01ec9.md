# dynare

## Navigation

[Catalog index](../index.md) · [Language: Octave](../by-language/octave.md) · [Category: Ide Editor Integration](../by-category/ide-editor-integration.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gnu-octave.github.io/packages/dynare -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Octave |
| Category | Ide Editor Integration |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gnu-octave.github.io/packages/dynare](https://gnu-octave.github.io/packages/dynare) |
| Source record ids | octave_packages_index-2aa24e76b14f5e |

## System Engineer Summary

Dynare is a software platform for handling a wide class of economic models, in particular dynamic
stochastic general equilibrium (DSGE) and overlapping generations (OLG) models. The models solved by
Dynare include those relying on the rational expectations hypothesis, wherein agents form their
expectations about the future in a way consistent with the model. But Dynare is also able to handle
models where expectations are formed differently: on one extreme, models where agents perfectly
anticipate the future; on the other extreme, models where agents have limited rationality or
imperfect knowledge of the state of the economy and, hence, form their expectations through a
learning process. In terms of types of agents, models solved by Dynare can incorporate consumers,
productive firms, governments, monetary authorities, investors and financial intermediaries. Some
degree of heterogeneity can be achieved by including several distinct classes of agents in each of
the aforementioned agent categories. Dynare offers a user-friendly and intuitive way of describing
these models. It is able to perform simulations of the model given a calibration of the model
parameters and is also able to estimate these parameters given a dataset. In practice, the user will
write a text file containing the list of model variables, the dynamic equations linking these
variables together, the computing tasks to be performed and the desired graphical or numerical
outputs.

## Operational Role

For a systems engineer, dynare belongs in the Octave inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 6.5 | 2025-11-24 | [https://gnu-octave.github.io/packages/](https://gnu-octave.github.io/packages/) |  |
| preview/nightly | unknown |  |  | unknown | octave_packages_have_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `ide_editor_integration` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://gnu-octave.github.io/packages/` at `2026-09-01T07:22:07+00:00`.
- Preview/nightly metadata is unknown because `octave_packages_have_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| gnu_octave_packages_index | registry-derived | 2026-09-01 | `{"kind": "gnu_octave_packages_index", "retrieved": "2026-09-01", "status": "registry-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `octave_packages_index-2aa24e76b14f5e` from `octave_packages_index` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| fits | Ide Editor Integration | [open](octave-fits-5ff75f1e.md) |
| image-acquisition | Ide Editor Integration | [open](octave-image-acquisition-323a53be.md) |
| joystick | Ide Editor Integration | [open](octave-joystick-a6f23604.md) |
| octave_ffmpeg_free | Ide Editor Integration | [open](octave-octave-ffmpeg-free-efcf587a.md) |
| octave_toml11 | Ide Editor Integration | [open](octave-octave-toml11-760086aa.md) |
| rf | Ide Editor Integration | [open](octave-rf-0076783a.md) |
| sqlp-sedumi | Ide Editor Integration | [open](octave-sqlp-sedumi-0d947c8f.md) |
| video | Ide Editor Integration | [open](octave-video-be18c02a.md) |

## Category Index

[Api Abi Checker (204)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (44)](../by-category/assertion-mocking.md) · [Async Runtime (134)](../by-category/async-runtime.md)
[Benchmarking (165)](../by-category/benchmarking.md) · [Build System (903)](../by-category/build-system.md) · [Cli (534)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (97)](../by-category/community-reference.md) · [Compiler (174)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (46)](../by-category/compression.md)
[Concurrency Parallelism (78)](../by-category/concurrency-parallelism.md) · [Configuration (113)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (162)](../by-category/cryptography.md) · [Data Science (35)](../by-category/data-science.md) · [Database Datastore (832)](../by-category/database-datastore.md) · [Datetime (180)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (42)](../by-category/debugger.md) · [Dependency Manager (92)](../by-category/dependency-manager.md) · [Documentation (96)](../by-category/documentation.md)
[Embedded Hardware (54)](../by-category/embedded-hardware.md) · [Ffi Bindings (402)](../by-category/ffi-bindings.md) · [Filesystem Os (1371)](../by-category/filesystem-os.md) · [Formatter (598)](../by-category/formatter.md)
[Framework (54)](../by-category/framework.md) · [Fuzzer (53)](../by-category/fuzzer.md) · [Game Engine Game Dev (169)](../by-category/game-engine-game-dev.md) · **[Ide Editor Integration (1304)](../by-category/ide-editor-integration.md)**
[Image Audio Dsp (356)](../by-category/image-audio-dsp.md) · [Interop Bindings (57)](../by-category/interop-bindings.md) · [Interpreter Runtime (250)](../by-category/interpreter-runtime.md) · [Jit Vm (60)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · [Language Specification (1373)](../by-category/language-specification.md) · [Library (5232)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (43)](../by-category/lint-rule-pack.md) · [Linter (347)](../by-category/linter.md) · [Logging Observability (481)](../by-category/logging-observability.md) · [Machine Learning (643)](../by-category/machine-learning.md)
[Math Numeric Scientific (83)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (88)](../by-category/memory-analyzer.md) · [Message Broker (36)](../by-category/message-broker.md) · [Networking Http (963)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (411)](../by-category/package-manager.md) · [Parser Lexer Ast (998)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (278)](../by-category/precommit-ci-quality.md)
[Profiler (79)](../by-category/profiler.md) · [Project Scaffolding (130)](../by-category/project-scaffolding.md) · [Registry Repository (108)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (333)](../by-category/security-sast.md) · [Serialization (378)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (490)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (518)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (56)](../by-category/tutorial-book-styleguide.md) · [Type Checker (297)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1497)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (95)](../by-category/utility-library.md) · [Visualization Gui (466)](../by-category/visualization-gui.md) · [Web Framework (448)](../by-category/web-framework.md)
