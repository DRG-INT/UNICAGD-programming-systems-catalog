# octave_boost

## Navigation

[Catalog index](../index.md) · [Language: Octave](../by-language/octave.md) · [Category: Language Specification](../by-category/language-specification.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://gnu-octave.github.io/packages/octave_boost -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Octave |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://gnu-octave.github.io/packages/octave_boost](https://gnu-octave.github.io/packages/octave_boost) |
| Source record ids | octave_packages_index-e75b6b252d75f0 |

## System Engineer Summary

A comprehensive open-source high performance processing package for GNU Octave based on Boost C++
Libraries. Built with C++17 standard. Provides direct access to Boost.Accumulators statistical
accumulators for online computation of count, covariance, density, error of mean, extended P^2
quantiles, kurtosis, max/min, mean, median, moments, P^2 cumulative distribution, P^2 quantile,
peaks over threshold, POT quantile, POT tail mean, skewness, sum, tail statistics, coherent/non-
coherent tail mean, tail quantile, tail variate, tail variate means, variance, weighted covariance,
weighted density, weighted extended P^2 quantiles, and weighted kurtosis. Also provides Boost.Chrono
duration operations including count, add, subtract, multiply, divide, remainder, equality and
inequality comparison, clock elapsed time measurement (system_clock, steady_clock,
high_resolution_clock, process_cpu_clock, thread_clock), and time formatting (time_fmt for duration
and system_clock). Also provides Boost.Date_Time Gregorian date handling: get year/month/day,
year_month_day, day_of_week, day_of_year, end_of_month (get_end_of_month and end_of_month),
is_infinity, is_neg_infinity, is_pos_infinity, is_not_a_date, is_special, modjulian_day, julian_day,
week_number, to_simple_string, to_iso_string, to_iso_extended_string, date_eq, date_ne, date_gt,
date_lt, date_ge, date_le, add_days, minus_days, minus_date, to_tm, and date_from_tm. Also provides
Boost.Thread multi-threading: run Octave files, call functions, eval expressions, and feval
expressions in parallel using boost::thread, with per-thread output capture and thread ID labeling.
The plural variants (boost_multi_thread_run_octave_files, boost_multi_thread_call_octave_functions,
boost_multi_thread_eval_octave_expressions, boost_multi_thread_feval_octave_expressions) accept cell
arrays and launch one thread per element. Also provides Boost.PropertyTree config format conversion,
including XML, JSON, INI and INFO(INF) formats.

## Operational Role

For a systems engineer, octave_boost belongs in the Octave inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.1.0 | 2026-05-27 | [https://gnu-octave.github.io/packages/](https://gnu-octave.github.io/packages/) |  |
| preview/nightly | unknown |  |  | unknown | octave_packages_have_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
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

- `octave_packages_index-e75b6b252d75f0` from `octave_packages_index` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| interval | Language Specification | [open](octave-interval-1e13aeec.md) |
| llms | Language Specification | [open](octave-llms-ec471a7a.md) |
| pythonic | Language Specification | [open](octave-pythonic-bc8dc034.md) |
| statistics-resampling | Language Specification | [open](octave-statistics-resampling-5c6b2a82.md) |

## Category Index

[Api Abi Checker (180)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (41)](../by-category/assertion-mocking.md) · [Async Runtime (122)](../by-category/async-runtime.md)
[Benchmarking (110)](../by-category/benchmarking.md) · [Build System (803)](../by-category/build-system.md) · [Cli (491)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (83)](../by-category/community-reference.md) · [Compiler (170)](../by-category/compiler.md) · [Compiler Diagnostics (22)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (71)](../by-category/concurrency-parallelism.md) · [Configuration (97)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (154)](../by-category/cryptography.md) · [Data Science (32)](../by-category/data-science.md) · [Database Datastore (687)](../by-category/database-datastore.md) · [Datetime (157)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (83)](../by-category/dependency-manager.md) · [Documentation (80)](../by-category/documentation.md)
[Embedded Hardware (47)](../by-category/embedded-hardware.md) · [Ffi Bindings (379)](../by-category/ffi-bindings.md) · [Filesystem Os (1160)](../by-category/filesystem-os.md) · [Formatter (542)](../by-category/formatter.md)
[Framework (47)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (153)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1114)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (292)](../by-category/image-audio-dsp.md) · [Interop Bindings (52)](../by-category/interop-bindings.md) · [Interpreter Runtime (227)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · **[Language Specification (1223)](../by-category/language-specification.md)** · [Library (4765)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (40)](../by-category/lint-rule-pack.md) · [Linter (346)](../by-category/linter.md) · [Logging Observability (386)](../by-category/logging-observability.md) · [Machine Learning (572)](../by-category/machine-learning.md)
[Math Numeric Scientific (79)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (76)](../by-category/memory-analyzer.md) · [Message Broker (31)](../by-category/message-broker.md) · [Networking Http (905)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (260)](../by-category/package-manager.md) · [Parser Lexer Ast (895)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (259)](../by-category/precommit-ci-quality.md)
[Profiler (68)](../by-category/profiler.md) · [Project Scaffolding (118)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (311)](../by-category/security-sast.md) · [Serialization (367)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (426)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (492)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (286)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1361)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (92)](../by-category/utility-library.md) · [Visualization Gui (413)](../by-category/visualization-gui.md) · [Web Framework (387)](../by-category/web-framework.md)
