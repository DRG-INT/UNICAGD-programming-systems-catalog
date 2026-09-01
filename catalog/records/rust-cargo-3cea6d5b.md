# Cargo

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Package Manager |
| Source type | package_manager |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/Cargo](https://crates.io/crates/Cargo) |
| Source record ids | master-d274f23bcee3 |

## System Engineer Summary

Rust build system and package manager

## Operational Role

For a systems engineer, Cargo belongs in the Rust inventory as part of dependency acquisition,
lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.99.0 | 2026-08-20T17:10:57.036221Z | [https://crates.io/api/v1/crates/Cargo](https://crates.io/api/v1/crates/Cargo) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/Cargo` at `2026-09-01T02:12:59+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-d274f23bcee3` from `master_json` as `package_manager`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| cargo-lock | Package Manager | [open](rust-cargo-lock-a883070b.md) |
| cargo-platform | Package Manager | [open](rust-cargo-platform-63e0b745.md) |
| cargo-util-schemas | Package Manager | [open](rust-cargo-util-schemas-52eca356.md) |
| cargo_metadata | Package Manager | [open](rust-cargo-metadata-08b46fd4.md) |
| cargo_toml | Package Manager | [open](rust-cargo-toml-c9d5ba6f.md) |
| document-features | Package Manager | [open](rust-document-features-87c303ad.md) |
| embed-resource | Package Manager | [open](rust-embed-resource-394d9ab2.md) |
| find-msvc-tools | Package Manager | [open](rust-find-msvc-tools-14b1752c.md) |
