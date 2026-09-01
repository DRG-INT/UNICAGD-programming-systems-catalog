# scopeguard

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Filesystem Os |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/scopeguard](https://crates.io/crates/scopeguard) |
| Source record ids | crates_io-d98736dfad9ffb |

## System Engineer Summary

A RAII scope guard that will run a given closure when it goes out of scope, even if the code between
panics (assuming unwinding panic). Defines the macros `defer!`, `defer_on_unwind!`,
`defer_on_success!` as shorthands for guards with one of the implemented strategies.

## Operational Role

For a systems engineer, scopeguard belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.2.0 | 2023-07-17T13:47:53.232324Z | [https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `filesystem_os` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-d98736dfad9ffb` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-cors | Filesystem Os | [open](rust-actix-cors-a4813363.md) |
| actix-utils | Filesystem Os | [open](rust-actix-utils-4c94a8a9.md) |
| addr2line | Filesystem Os | [open](rust-addr2line-822b58a0.md) |
| alloca | Filesystem Os | [open](rust-alloca-113b2fd1.md) |
| alloy-sol-macro-input | Filesystem Os | [open](rust-alloy-sol-macro-input-462ea342.md) |
| ark-ff-macros | Filesystem Os | [open](rust-ark-ff-macros-5ecdc709.md) |
| arrayref | Filesystem Os | [open](rust-arrayref-3be2f129.md) |
| asn1-rs-derive | Filesystem Os | [open](rust-asn1-rs-derive-919456da.md) |
