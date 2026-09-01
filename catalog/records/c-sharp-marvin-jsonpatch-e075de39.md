# Marvin.JsonPatch

## Navigation

[Catalog index](../index.md) · [Language: C-Sharp](../by-language/c-sharp.md) · [Category: Language Specification](../by-category/language-specification.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | C-Sharp |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://www.nuget.org/packages/Marvin.JsonPatch](https://www.nuget.org/packages/Marvin.JsonPatch) |
| Source record ids | nuget_search-1717571d0c1d19 |

## System Engineer Summary

JSON Patch defines a JSON document structure for expressing a sequence of operations to apply to a
JavaScript Object Notation (JSON) document; it is suitable for use with the HTTP PATCH method. The
"application/json-patch+json" media type is used to identify such patch documents. One of the things
this can be used for is partial updates for REST-ful API's, or, to quote the IETF: "This format is
also potentially useful in other cases in which it is necessary to make partial updates to a JSON
document or to a data structure that has similar constraints (i.e., they can be serialized as an
object or an array using the JSON grammar)." That's what this package is all about. Web API supports
the HttpPatch method, but there's currently no implementation of the JsonPatchDocument in .NET,
making it hard to pass in a set of changes that have to be applied - especially if you're working
cross-platform and standardization of your API is essential. Have a look at the project site for the
current status of this package and to learn how to get started.

## Operational Role

For a systems engineer, Marvin.JsonPatch belongs in the C-Sharp inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 2.2.1 | 2022-04-06T06:17:37.12+00:00 | [https://api.nuget.org/v3/registration5-gz-semver2/marvin.jsonpatch/index.json](https://api.nuget.org/v3/registration5-gz-semver2/marvin.jsonpatch/index.json) |  |
| preview | known | 2.2.1-rc | 2022-03-29T14:13:01.723+00:00 | [https://api.nuget.org/v3/registration5-gz-semver2/marvin.jsonpatch/index.json](https://api.nuget.org/v3/registration5-gz-semver2/marvin.jsonpatch/index.json) |  |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://api.nuget.org/v3/registration5-gz-semver2/marvin.jsonpatch/index.json` at `2026-09-01T07:23:57+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| nuget_search_api | registry-derived | 2026-09-01 | `{"kind": "nuget_search_api", "query": "json", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `nuget_search-1717571d0c1d19` from `nuget_search` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Apache.Avro | Language Specification | [open](c-sharp-apache-avro-c14620d8.md) |
| FubarCoder.RestSharp.Portable.HttpClient | Language Specification | [open](c-sharp-fubarcoder-restsharp-portable-httpclient-41c31b4c.md) |
| json2 | Language Specification | [open](c-sharp-json2-4761fde6.md) |
| Microsoft.OpenApi | Language Specification | [open](c-sharp-microsoft-openapi-439cd0f6.md) |
| StreamJsonRpc | Language Specification | [open](c-sharp-streamjsonrpc-0ef82e6c.md) |

## Category Index

[Api Abi Checker (105)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (33)](../by-category/assertion-mocking.md) · [Async Runtime (104)](../by-category/async-runtime.md)
[Benchmarking (68)](../by-category/benchmarking.md) · [Build System (529)](../by-category/build-system.md) · [Cli (435)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (61)](../by-category/community-reference.md) · [Compiler (107)](../by-category/compiler.md) · [Compiler Diagnostics (18)](../by-category/compiler-diagnostics.md) · [Compression (36)](../by-category/compression.md)
[Concurrency Parallelism (62)](../by-category/concurrency-parallelism.md) · [Configuration (65)](../by-category/configuration.md) · [Container Deployment (7)](../by-category/container-deployment.md) · [Coverage (10)](../by-category/coverage.md)
[Cryptography (127)](../by-category/cryptography.md) · [Data Science (28)](../by-category/data-science.md) · [Database Datastore (429)](../by-category/database-datastore.md) · [Datetime (93)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (35)](../by-category/debugger.md) · [Dependency Manager (59)](../by-category/dependency-manager.md) · [Documentation (57)](../by-category/documentation.md)
[Embedded Hardware (36)](../by-category/embedded-hardware.md) · [Ffi Bindings (311)](../by-category/ffi-bindings.md) · [Filesystem Os (642)](../by-category/filesystem-os.md) · [Formatter (428)](../by-category/formatter.md)
[Framework (35)](../by-category/framework.md) · [Fuzzer (22)](../by-category/fuzzer.md) · [Game Engine Game Dev (95)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (790)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (167)](../by-category/image-audio-dsp.md) · [Interop Bindings (46)](../by-category/interop-bindings.md) · [Interpreter Runtime (122)](../by-category/interpreter-runtime.md) · [Jit Vm (55)](../by-category/jit-vm.md)
[Language Server (23)](../by-category/language-server.md) · **[Language Specification (610)](../by-category/language-specification.md)** · [Library (3229)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (32)](../by-category/lint-rule-pack.md) · [Linter (328)](../by-category/linter.md) · [Logging Observability (236)](../by-category/logging-observability.md) · [Machine Learning (351)](../by-category/machine-learning.md)
[Math Numeric Scientific (70)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (52)](../by-category/memory-analyzer.md) · [Message Broker (23)](../by-category/message-broker.md) · [Networking Http (676)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (188)](../by-category/package-manager.md) · [Parser Lexer Ast (574)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (167)](../by-category/precommit-ci-quality.md)
[Profiler (53)](../by-category/profiler.md) · [Project Scaffolding (76)](../by-category/project-scaffolding.md) · [Registry Repository (104)](../by-category/registry-repository.md) · [Sanitizer (7)](../by-category/sanitizer.md)
[Security Sast (260)](../by-category/security-sast.md) · [Serialization (270)](../by-category/serialization.md) · [Standard Library (22)](../by-category/standard-library.md) · [Static Analyzer (259)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (410)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (34)](../by-category/tutorial-book-styleguide.md) · [Type Checker (251)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (731)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (74)](../by-category/utility-library.md) · [Visualization Gui (247)](../by-category/visualization-gui.md) · [Web Framework (286)](../by-category/web-framework.md)
