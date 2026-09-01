# afl-lua

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Fuzzer |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://luarocks.org/modules/ligurio/afl-lua](https://luarocks.org/modules/ligurio/afl-lua) |
| Source record ids | luarocks_root_manifest-9554d471fecd74 |

## System Engineer Summary

A module that enables integration with American Fuzzy Lop

## Operational Role

For a systems engineer, afl-lua belongs in the Lua family inventory as part of input-space
exploration, parser hardening, and unsafe edge-case discovery.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | luarocks_manifest_page_does_not_include_version_date |
| preview/nightly | unknown |  |  | unknown | luarocks_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `fuzzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `luarocks_manifest_page_does_not_include_version_date`.
- Preview/nightly metadata is unknown because `luarocks_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| luarocks_root_manifest | registry-derived | 2026-09-01 | `{"kind": "luarocks_root_manifest", "page": 1, "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `luarocks_root_manifest-9554d471fecd74` from `luarocks_root_manifest` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| fzy | Fuzzer | [open](lua-family-fzy-c0f31b26.md) |
