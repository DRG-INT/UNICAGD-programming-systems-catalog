# rustup

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Dependency Manager |
| Source type | dependency_manager |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/rustup](https://crates.io/crates/rustup) |
| Source record ids | master-22b5b8b65ad9 |

## System Engineer Summary

Rust toolchain installer/manager

## Operational Role

For a systems engineer, rustup belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.0.0 | 2018-03-29T19:59:26.006143Z | [https://crates.io/api/v1/crates/rustup](https://crates.io/api/v1/crates/rustup) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `dependency_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/rustup` at `2026-09-01T01:59:21+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-22b5b8b65ad9` from `master_json` as `dependency_manager`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| basic-toml | Dependency Manager | [open](rust-basic-toml-5cd7ab13.md) |
| configparser | Dependency Manager | [open](rust-configparser-ce31efc8.md) |
| hex-conservative | Dependency Manager | [open](rust-hex-conservative-879cabf9.md) |
| minijinja | Dependency Manager | [open](rust-minijinja-a500af64.md) |
| precomputed-hash | Dependency Manager | [open](rust-precomputed-hash-2150f344.md) |
| protobuf-parse | Dependency Manager | [open](rust-protobuf-parse-5321e0ad.md) |
| raw-cpuid | Dependency Manager | [open](rust-raw-cpuid-e0c8cffb.md) |
| sha1_smol | Dependency Manager | [open](rust-sha1-smol-5c432295.md) |
