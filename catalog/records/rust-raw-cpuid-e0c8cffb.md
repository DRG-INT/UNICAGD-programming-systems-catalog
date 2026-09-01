# raw-cpuid

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Dependency Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/raw-cpuid](https://crates.io/crates/raw-cpuid) |
| Source record ids | crates_io-5d5f351e1b39c7 |

## System Engineer Summary

A library to parse the x86 CPUID instruction, written in rust with no external dependencies. The
implementation closely resembles the Intel CPUID manual description. The library does only depend on
libcore.

## Operational Role

For a systems engineer, raw-cpuid belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 11.6.0 | 2025-09-05T02:59:39.561516Z | [https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `dependency_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-5d5f351e1b39c7` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| basic-toml | Dependency Manager | [open](rust-basic-toml-5cd7ab13.md) |
| configparser | Dependency Manager | [open](rust-configparser-ce31efc8.md) |
| hex-conservative | Dependency Manager | [open](rust-hex-conservative-879cabf9.md) |
| minijinja | Dependency Manager | [open](rust-minijinja-a500af64.md) |
| precomputed-hash | Dependency Manager | [open](rust-precomputed-hash-2150f344.md) |
| protobuf-parse | Dependency Manager | [open](rust-protobuf-parse-5321e0ad.md) |
| rustup | Dependency Manager | [open](rust-rustup-eaa7a72b.md) |
| sha1_smol | Dependency Manager | [open](rust-sha1-smol-5c432295.md) |
