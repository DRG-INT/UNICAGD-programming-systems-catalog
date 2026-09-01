# Buildsoftwaresphere/SAP-HANA

## Navigation

[Catalog index](../index.md) · [Language: SAPJava](../by-language/sapjava.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

## Identity

| Field | Value |
| --- | --- |
| Language branch | SAPJava |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/Buildsoftwaresphere/SAP-HANA](https://github.com/Buildsoftwaresphere/SAP-HANA) |
| Source record ids | github_search_sapjava-ac5dfa4af19f3e |

## System Engineer Summary

import org.gradle.internal.os.OperatingSystem apply plugin: 'java' apply plugin: 'maven' apply
plugin: 'war' group = 'com.yourCompany.hcp-project' version = '0.0.1-SNAPSHOT' description = """"""
sourceCompatibility = 1.7 targetCompatibility = 1.7 project.buildDir = 'target'
project.webAppDirName = 'WebContent' project.ext { localServer = "${buildDir}" + File.separator +
"server" sdk = "${buildDir}" + File.separator +"sdk" neo = { ->
if(OperatingSystem.current().isWindows()) return "${sdk}" + File.separator + "tools" +
File.separator + "neo.bat" if(OperatingSystem.current().isLinux()) return "${sdk}" + File.separator
+ "tools" + File.separator + "neo.sh" } httpPort = "8083" waitUrl = " +
war.archiveName.replace(".war", "/") account = "abcdef" application = "abc" host =
"hana.ondemand.com" //Shoudl go into local .gradle/gradle.properties which should be excluded fom
SCM (e.g. Git) password = "secret" user = "p12345678" } repositories { maven { url " } }
dependencies { compile group: 'commons-io', name: 'commons-io', version:'2.4' compile group:
'org.apache.maven.plugins', name: 'maven-enforcer-plugin', version:'1.0.1' compile group:
'org.apache.olingo', name: 'olingo-odata2-api', version:'2.0.6' compile group: 'org.apache.olingo',
name: 'olingo-odata2-core', version:'2.0.6' compile group: 'javax.servlet', name: 'servlet-api',
version:'3.0-alpha-1' compile group: 'org.apache.cxf', name: 'cxf-rt-frontend-jaxrs',
version:'2.7.5' compile group: 'org.apache.olingo', name: 'olingo-odata2-jpa-processor-api',
version:'2.0.6' compile group: 'org.apache.olingo', name: 'olingo-odata2-jpa-processor-core',
version:'2.0.6' compile group: 'org.slf4j', name: 'slf4j-log4j12', version:'1.7.1' compile group:
'org.eclipse.persistence', name: 'eclipselink', version:'2.6.1-RC1' testCompile group: 'junit',
name: 'junit', version:'4.12' testCompile group: 'com.sap.cloud', name: 'neo-javaee6-wp-maven-
plugin', version:'2.78.13' testCompile group: 'org.mockito', name: 'mockito-core',
version:'2.0.31-beta' providedCompile 'com.sap.cloud:neo-javaee6-wp-sdk:2.78.13@zip' providedCompile
group: 'com.sap.cloud', name: 'neo-javaee6-wp-api', version:'2.78.13' } task installSdk(type:Copy){
description 'Task will install Neo SDK' def outputDir = file(project.sdk) def a = file(findJar('neo-
javaee6-wp-sdk')) from zipTree(a) into(outputDir) } task installServer(type: Exec){ description
'Task will install local server and the SDK in case it is missing' doFirst{
if(!file(project.sdk).exists()) tasks.installSdk.execute() } commandLine neo(), 'install-local', '--
location', localServer, '--http-port', httpPort } task startServer(type: Exec){ description 'Task
will start local server' commandLine neo(), 'start-local', '--location', localServer, '--wait-url',
waitUrl } task deploy(type:Exec, dependsOn: war){ description 'Task will deploy war to local server'
commandLine neo(), 'deploy-local', '--location', localServer, '--source', war.archivePath } task
cloudDeploy(type:Exec, dependsOn: war){ description "Task will deploy war in hana Cloud Platform
Account" commandLine neo(), 'deploy', '--account', account, '--application', application, '--host',
host, '--password', password, '--user', user, '--source', war.archivePath } def findJar(prefix) {
configurations.providedCompile.files.find { it.name.contains(prefix) } }

## Operational Role

For a systems engineer, Buildsoftwaresphere/SAP-HANA belongs in the SAPJava inventory as part of
build graph control, artifact reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | not_a_maven_coordinate |
| preview/nightly | unknown |  |  | unknown | not_a_maven_coordinate |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | {"key": "", "name": "", "url": ""} |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `not_a_maven_coordinate`.
- Preview/nightly metadata is unknown because `not_a_maven_coordinate`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-01 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "SAP Cloud SDK Java", "retrieved": "2026-09-01", "status": "forge-cli-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `github_search_sapjava-ac5dfa4af19f3e` from `github_search_sapjava` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| AES0P/Purchase_order | Build System | [open](sapjava-aes0p-purchase-order-62e61840.md) |
| beroca/sap-mission.cap-java-app | Build System | [open](sapjava-beroca-sap-mission-cap-java-app-ca4542de.md) |
| buildwithrenuka/SAP-UI5-FIORI-CAP-JAVA | Build System | [open](sapjava-buildwithrenuka-sap-ui5-fiori-cap-java-f080ae72.md) |
| DumsR/incident-management_2025_java | Build System | [open](sapjava-dumsr-incident-management-2025-java-52f1829d.md) |
| njgarg22/bookstore-products | Build System | [open](sapjava-njgarg22-bookstore-products-daaef4ff.md) |
| SAP-samples/ams-samples-java | Build System | [open](sapjava-sap-samples-ams-samples-java-fd68629e.md) |
| SAP-samples/cap-sflight | Build System | [open](sapjava-sap-samples-cap-sflight-49ffa5d9.md) |
| SAP/ai-sdk-java | Build System | [open](sapjava-sap-ai-sdk-java-e59084a9.md) |

## Category Index

[Api Abi Checker (112)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (33)](../by-category/assertion-mocking.md) · [Async Runtime (104)](../by-category/async-runtime.md)
[Benchmarking (69)](../by-category/benchmarking.md) · **[Build System (563)](../by-category/build-system.md)** · [Cli (441)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (63)](../by-category/community-reference.md) · [Compiler (111)](../by-category/compiler.md) · [Compiler Diagnostics (18)](../by-category/compiler-diagnostics.md) · [Compression (36)](../by-category/compression.md)
[Concurrency Parallelism (62)](../by-category/concurrency-parallelism.md) · [Configuration (69)](../by-category/configuration.md) · [Container Deployment (7)](../by-category/container-deployment.md) · [Coverage (10)](../by-category/coverage.md)
[Cryptography (128)](../by-category/cryptography.md) · [Data Science (29)](../by-category/data-science.md) · [Database Datastore (436)](../by-category/database-datastore.md) · [Datetime (96)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (35)](../by-category/debugger.md) · [Dependency Manager (59)](../by-category/dependency-manager.md) · [Documentation (61)](../by-category/documentation.md)
[Embedded Hardware (36)](../by-category/embedded-hardware.md) · [Ffi Bindings (312)](../by-category/ffi-bindings.md) · [Filesystem Os (678)](../by-category/filesystem-os.md) · [Formatter (434)](../by-category/formatter.md)
[Framework (38)](../by-category/framework.md) · [Fuzzer (23)](../by-category/fuzzer.md) · [Game Engine Game Dev (98)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (812)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (168)](../by-category/image-audio-dsp.md) · [Interop Bindings (46)](../by-category/interop-bindings.md) · [Interpreter Runtime (138)](../by-category/interpreter-runtime.md) · [Jit Vm (55)](../by-category/jit-vm.md)
[Language Server (23)](../by-category/language-server.md) · [Language Specification (825)](../by-category/language-specification.md) · [Library (3295)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (33)](../by-category/lint-rule-pack.md) · [Linter (328)](../by-category/linter.md) · [Logging Observability (246)](../by-category/logging-observability.md) · [Machine Learning (365)](../by-category/machine-learning.md)
[Math Numeric Scientific (70)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (52)](../by-category/memory-analyzer.md) · [Message Broker (23)](../by-category/message-broker.md) · [Networking Http (684)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (193)](../by-category/package-manager.md) · [Parser Lexer Ast (583)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (168)](../by-category/precommit-ci-quality.md)
[Profiler (56)](../by-category/profiler.md) · [Project Scaffolding (84)](../by-category/project-scaffolding.md) · [Registry Repository (105)](../by-category/registry-repository.md) · [Sanitizer (8)](../by-category/sanitizer.md)
[Security Sast (263)](../by-category/security-sast.md) · [Serialization (270)](../by-category/serialization.md) · [Standard Library (22)](../by-category/standard-library.md) · [Static Analyzer (263)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (414)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (39)](../by-category/tutorial-book-styleguide.md) · [Type Checker (258)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (901)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (79)](../by-category/utility-library.md) · [Visualization Gui (268)](../by-category/visualization-gui.md) · [Web Framework (294)](../by-category/web-framework.md)
