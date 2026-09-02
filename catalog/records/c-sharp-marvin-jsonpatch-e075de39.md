# Marvin.JsonPatch

## Navigation

[Catalog index](../index.md) · [Language: C-Sharp](../by-language/c-sharp.md) · [Category: Language Specification](../by-category/language-specification.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://www.nuget.org/packages/Marvin.JsonPatch -->
<!-- crawl-delay: 10 -->

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

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| nuget_search_api | registry-derived | 2026-09-01 | `{"kind": "nuget_search_api", "query": "json", "retrieved": "2026-09-01", "status": "registry-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `nuget_search-1717571d0c1d19` from `nuget_search` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Apache.Avro | Language Specification | [open](c-sharp-apache-avro-c14620d8.md) |
| FubarCoder.RestSharp.Portable.HttpClient | Language Specification | [open](c-sharp-fubarcoder-restsharp-portable-httpclient-41c31b4c.md) |
| json2 | Language Specification | [open](c-sharp-json2-4761fde6.md) |
| Microsoft.OpenApi | Language Specification | [open](c-sharp-microsoft-openapi-439cd0f6.md) |
| StreamJsonRpc | Language Specification | [open](c-sharp-streamjsonrpc-0ef82e6c.md) |

## Category Index

[Api Abi Checker (190)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (42)](../by-category/assertion-mocking.md) · [Async Runtime (129)](../by-category/async-runtime.md)
[Benchmarking (123)](../by-category/benchmarking.md) · [Build System (827)](../by-category/build-system.md) · [Cli (507)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (88)](../by-category/community-reference.md) · [Compiler (171)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (45)](../by-category/compression.md)
[Concurrency Parallelism (73)](../by-category/concurrency-parallelism.md) · [Configuration (101)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (11)](../by-category/coverage.md)
[Cryptography (156)](../by-category/cryptography.md) · [Data Science (34)](../by-category/data-science.md) · [Database Datastore (774)](../by-category/database-datastore.md) · [Datetime (160)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (41)](../by-category/debugger.md) · [Dependency Manager (87)](../by-category/dependency-manager.md) · [Documentation (88)](../by-category/documentation.md)
[Embedded Hardware (49)](../by-category/embedded-hardware.md) · [Ffi Bindings (390)](../by-category/ffi-bindings.md) · [Filesystem Os (1220)](../by-category/filesystem-os.md) · [Formatter (548)](../by-category/formatter.md)
[Framework (51)](../by-category/framework.md) · [Fuzzer (48)](../by-category/fuzzer.md) · [Game Engine Game Dev (159)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1149)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (301)](../by-category/image-audio-dsp.md) · [Interop Bindings (55)](../by-category/interop-bindings.md) · [Interpreter Runtime (236)](../by-category/interpreter-runtime.md) · [Jit Vm (56)](../by-category/jit-vm.md)
[Language Server (27)](../by-category/language-server.md) · **[Language Specification (1241)](../by-category/language-specification.md)** · [Library (4877)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (41)](../by-category/lint-rule-pack.md) · [Linter (346)](../by-category/linter.md) · [Logging Observability (397)](../by-category/logging-observability.md) · [Machine Learning (594)](../by-category/machine-learning.md)
[Math Numeric Scientific (79)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (86)](../by-category/memory-analyzer.md) · [Message Broker (34)](../by-category/message-broker.md) · [Networking Http (926)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (278)](../by-category/package-manager.md) · [Parser Lexer Ast (928)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (262)](../by-category/precommit-ci-quality.md)
[Profiler (73)](../by-category/profiler.md) · [Project Scaffolding (120)](../by-category/project-scaffolding.md) · [Registry Repository (107)](../by-category/registry-repository.md) · [Sanitizer (12)](../by-category/sanitizer.md)
[Security Sast (314)](../by-category/security-sast.md) · [Serialization (370)](../by-category/serialization.md) · [Standard Library (24)](../by-category/standard-library.md) · [Static Analyzer (448)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (501)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (53)](../by-category/tutorial-book-styleguide.md) · [Type Checker (292)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1403)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (93)](../by-category/utility-library.md) · [Visualization Gui (415)](../by-category/visualization-gui.md) · [Web Framework (415)](../by-category/web-framework.md)
