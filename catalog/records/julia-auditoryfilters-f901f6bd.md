# AuditoryFilters

## Identity

| Field | Value |
| --- | --- |
| Language branch | Julia |
| Category | Security Sast |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/JuliaRegistries/General/tree/master/A/AuditoryFilters](https://github.com/JuliaRegistries/General/tree/master/A/AuditoryFilters) |
| Source record ids | julia_general-5422ea941d1cba |

## System Engineer Summary

Julia package registered in General at A/AuditoryFilters.

## Operational Role

For a systems engineer, AuditoryFilters belongs in the Julia inventory as part of supply-chain
review, vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | julia_expansion_does_not_fetch_versions_by_default |
| preview/nightly | unknown |  |  | unknown | julia_registry_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `julia_expansion_does_not_fetch_versions_by_default`.
- Preview/nightly metadata is unknown because `julia_registry_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| julia_general_registry | registry-derived | 2026-09-01 | `{"kind": "julia_general_registry", "registry_path": "A/AuditoryFilters", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `julia_general-5422ea941d1cba` from `julia_general` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| AuditorySignalUtils | Security Sast | [open](julia-auditorysignalutils-63f61527.md) |
| AuditoryStimuli | Security Sast | [open](julia-auditorystimuli-b3292292.md) |
