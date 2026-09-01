# cargo-lock

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Package Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/cargo-lock](https://crates.io/crates/cargo-lock) |
| Source record ids | crates_io-ae0296c6c0ce8c |

## System Engineer Summary

Self-contained Cargo.lock parser with optional dependency graph analysis

## Operational Role

For a systems engineer, cargo-lock belongs in the Rust inventory as part of dependency acquisition,
lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 11.1.0 | 2026-07-24T14:17:05.419636Z | [https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-ae0296c6c0ce8c` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Cargo | Package Manager | [open](rust-cargo-3cea6d5b.md) |
| cargo-platform | Package Manager | [open](rust-cargo-platform-63e0b745.md) |
| cargo-util-schemas | Package Manager | [open](rust-cargo-util-schemas-52eca356.md) |
| cargo_metadata | Package Manager | [open](rust-cargo-metadata-08b46fd4.md) |
| cargo_toml | Package Manager | [open](rust-cargo-toml-c9d5ba6f.md) |
| document-features | Package Manager | [open](rust-document-features-87c303ad.md) |
| embed-resource | Package Manager | [open](rust-embed-resource-394d9ab2.md) |
| find-msvc-tools | Package Manager | [open](rust-find-msvc-tools-14b1752c.md) |
