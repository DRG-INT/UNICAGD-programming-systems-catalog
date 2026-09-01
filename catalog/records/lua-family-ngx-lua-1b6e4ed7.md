# ngx_lua

## Navigation

[Catalog index](../index.md) · [Language: Lua family](../by-language/lua-family.md) · [Category: Async Runtime](../by-category/async-runtime.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Async Runtime |
| Source type | source_list_item |
| Verification | uploaded_file |
| Canonical URL | [https://www.nginx.com/resources/wiki/modules/lua/](https://www.nginx.com/resources/wiki/modules/lua/) |
| Source record ids | lua-source-163 |

## System Engineer Summary

The core piece of OpenResty. Embeds Lua in Nginx and exposes, among other things, the cosocket API
for non-blocking sockets (compatible with LuaSocket's API).

## Operational Role

For a systems engineer, ngx_lua belongs in the Lua family inventory as part of concurrency
scheduling, I/O throughput, cancellation, and latency management.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | not_checked |
| preview/nightly | unknown |  |  | unknown | not_checked |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | unknown |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `async_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `not_checked`.
- Preview/nightly metadata is unknown because `not_checked`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| uploaded_file |  |  | `{"kind": "uploaded_file", "source": {"file": "readme.md", "kind": "uploaded_file", "line": 163}}` |

## Evidence

Evidence records merged into this identity: `1`.

- `lua-source-163` from `master_json` as `source_list_item`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| act | Async Runtime | [open](lua-family-act-4ff0ad7b.md) |
| async | Async Runtime | [open](lua-family-async-1eb5c035.md) |
| async-framework | Async Runtime | [open](lua-family-async-framework-b849d00e.md) |
| async-utils | Async Runtime | [open](lua-family-async-utils-efc85dd0.md) |
| async.lua | Async Runtime | [open](lua-family-async-lua-668c3126.md) |
| asyncio | Async Runtime | [open](lua-family-asyncio-8daeeae9.md) |
| away-dataqueue | Async Runtime | [open](lua-family-away-dataqueue-7107fb30.md) |
| Copas | Async Runtime | [open](lua-family-copas-8a6e8951.md) |

## Category Index

[Api Abi Checker (100)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (33)](../by-category/assertion-mocking.md) · **[Async Runtime (104)](../by-category/async-runtime.md)**
[Benchmarking (64)](../by-category/benchmarking.md) · [Build System (503)](../by-category/build-system.md) · [Cli (431)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (61)](../by-category/community-reference.md) · [Compiler (107)](../by-category/compiler.md) · [Compiler Diagnostics (18)](../by-category/compiler-diagnostics.md) · [Compression (34)](../by-category/compression.md)
[Concurrency Parallelism (61)](../by-category/concurrency-parallelism.md) · [Configuration (64)](../by-category/configuration.md) · [Container Deployment (7)](../by-category/container-deployment.md) · [Coverage (10)](../by-category/coverage.md)
[Cryptography (127)](../by-category/cryptography.md) · [Data Science (26)](../by-category/data-science.md) · [Database Datastore (428)](../by-category/database-datastore.md) · [Datetime (86)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (35)](../by-category/debugger.md) · [Dependency Manager (57)](../by-category/dependency-manager.md) · [Documentation (57)](../by-category/documentation.md)
[Embedded Hardware (34)](../by-category/embedded-hardware.md) · [Ffi Bindings (307)](../by-category/ffi-bindings.md) · [Filesystem Os (544)](../by-category/filesystem-os.md) · [Formatter (416)](../by-category/formatter.md)
[Framework (31)](../by-category/framework.md) · [Fuzzer (20)](../by-category/fuzzer.md) · [Game Engine Game Dev (93)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (657)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (116)](../by-category/image-audio-dsp.md) · [Interop Bindings (45)](../by-category/interop-bindings.md) · [Interpreter Runtime (121)](../by-category/interpreter-runtime.md) · [Jit Vm (51)](../by-category/jit-vm.md)
[Language Server (23)](../by-category/language-server.md) · [Language Specification (586)](../by-category/language-specification.md) · [Library (3146)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (31)](../by-category/lint-rule-pack.md) · [Linter (327)](../by-category/linter.md) · [Logging Observability (231)](../by-category/logging-observability.md) · [Machine Learning (333)](../by-category/machine-learning.md)
[Math Numeric Scientific (69)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (51)](../by-category/memory-analyzer.md) · [Message Broker (23)](../by-category/message-broker.md) · [Networking Http (652)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (173)](../by-category/package-manager.md) · [Parser Lexer Ast (560)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (163)](../by-category/precommit-ci-quality.md)
[Profiler (52)](../by-category/profiler.md) · [Project Scaffolding (74)](../by-category/project-scaffolding.md) · [Registry Repository (104)](../by-category/registry-repository.md) · [Sanitizer (7)](../by-category/sanitizer.md)
[Security Sast (250)](../by-category/security-sast.md) · [Serialization (268)](../by-category/serialization.md) · [Standard Library (22)](../by-category/standard-library.md) · [Static Analyzer (245)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (407)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (34)](../by-category/tutorial-book-styleguide.md) · [Type Checker (248)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (615)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (73)](../by-category/utility-library.md) · [Visualization Gui (240)](../by-category/visualization-gui.md) · [Web Framework (285)](../by-category/web-framework.md)
