# audit-log

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Security Sast |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://luarocks.org/modules/mykaarma/audit-log](https://luarocks.org/modules/mykaarma/audit-log) |
| Source record ids | luarocks_root_manifest-9cad15c8e2a929 |

## System Engineer Summary

audit-log is a custom plugin made at MyKaarma to generate audit logs whenever a
consumer/credential/rate-limit is created/updated/deleted in Kong

## Operational Role

For a systems engineer, audit-log belongs in the Lua family inventory as part of supply-chain
review, vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | luarocks_manifest_page_does_not_include_version_date |
| preview/nightly | unknown |  |  | unknown | luarocks_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `luarocks_manifest_page_does_not_include_version_date`.
- Preview/nightly metadata is unknown because `luarocks_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| luarocks_root_manifest | registry-derived | 2026-09-01 | `{"kind": "luarocks_root_manifest", "page": 4, "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `luarocks_root_manifest-9cad15c8e2a929` from `luarocks_root_manifest` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| ai-lasso-guardrail | Security Sast | [open](lua-family-ai-lasso-guardrail-25c625a0.md) |
| Apache APISIX | Security Sast | [open](lua-family-apache-apisix-7afbb669.md) |
| exasol-virtual-schema-common-lua | Security Sast | [open](lua-family-exasol-virtual-schema-common-lua-e41c1314.md) |
| haproxy-impart | Security Sast | [open](lua-family-haproxy-impart-5084d2c5.md) |
| luatweetnacl | Security Sast | [open](lua-family-luatweetnacl-9fe17abd.md) |
