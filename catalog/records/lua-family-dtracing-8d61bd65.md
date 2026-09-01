# dtracing

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Profiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://luarocks.org/modules/erosfdz/dtracing](https://luarocks.org/modules/erosfdz/dtracing) |
| Source record ids | luarocks_root_manifest-45e1b0bd840a7f |

## System Engineer Summary

This plugin allows Kong to propagate Zipkin headers and report to a Zipkin server

## Operational Role

For a systems engineer, dtracing belongs in the Lua family inventory as part of hot-path discovery,
allocation analysis, latency control, and capacity planning.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | luarocks_manifest_page_does_not_include_version_date |
| preview/nightly | unknown |  |  | unknown | luarocks_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `profiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `luarocks_manifest_page_does_not_include_version_date`.
- Preview/nightly metadata is unknown because `luarocks_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| luarocks_root_manifest | registry-derived | 2026-09-01 | `{"kind": "luarocks_root_manifest", "page": 17, "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `luarocks_root_manifest-45e1b0bd840a7f` from `luarocks_root_manifest` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| deeptrace | Profiler | [open](lua-family-deeptrace-d01a630c.md) |
| dt-anchor-tools | Profiler | [open](lua-family-dt-anchor-tools-3afdd259.md) |
| ELProfiler | Profiler | [open](lua-family-elprofiler-5281476f.md) |
| luatrace | Profiler | [open](lua-family-luatrace-30f7fe16.md) |
| ProFi | Profiler | [open](lua-family-profi-5f67f00e.md) |
