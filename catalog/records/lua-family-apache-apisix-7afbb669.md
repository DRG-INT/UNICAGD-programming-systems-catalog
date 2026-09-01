# Apache APISIX

## Identity

| Field | Value |
| --- | --- |
| Language branch | Lua family |
| Category | Security Sast |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://luarocks.org/modules/apisix/apisix](https://luarocks.org/modules/apisix/apisix) |
| Source record ids | luarocks_root_manifest-d88a2993859c23 |

## System Engineer Summary

Apache APISIX is a cloud-native microservices API gateway, delivering the ultimate performance,
security, open source and scalable platform for all your APIs and microservices.

## Operational Role

For a systems engineer, Apache APISIX belongs in the Lua family inventory as part of supply-chain
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
| luarocks_root_manifest | registry-derived | 2026-09-01 | `{"kind": "luarocks_root_manifest", "page": 3, "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `luarocks_root_manifest-d88a2993859c23` from `luarocks_root_manifest` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| ai-lasso-guardrail | Security Sast | [open](lua-family-ai-lasso-guardrail-25c625a0.md) |
| audit-log | Security Sast | [open](lua-family-audit-log-8b3ec16e.md) |
| exasol-virtual-schema-common-lua | Security Sast | [open](lua-family-exasol-virtual-schema-common-lua-e41c1314.md) |
| haproxy-impart | Security Sast | [open](lua-family-haproxy-impart-5084d2c5.md) |
| luatweetnacl | Security Sast | [open](lua-family-luatweetnacl-9fe17abd.md) |
