# protobuf-parse

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Dependency Manager |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/protobuf-parse](https://crates.io/crates/protobuf-parse) |
| Source record ids | crates_io-e60b48fcf3fdb9 |

## System Engineer Summary

Parse `.proto` files. Files are parsed into a `protobuf::descriptor::FileDescriptorSet` object using
either: * pure rust parser (no dependencies) * `protoc` binary (more reliable and compatible with
Google's implementation)

## Operational Role

For a systems engineer, protobuf-parse belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 3.7.2 | 2025-03-10T14:08:28.291564Z | [https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `dependency_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=16&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-e60b48fcf3fdb9` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| basic-toml | Dependency Manager | [open](rust-basic-toml-5cd7ab13.md) |
| configparser | Dependency Manager | [open](rust-configparser-ce31efc8.md) |
| hex-conservative | Dependency Manager | [open](rust-hex-conservative-879cabf9.md) |
| minijinja | Dependency Manager | [open](rust-minijinja-a500af64.md) |
| precomputed-hash | Dependency Manager | [open](rust-precomputed-hash-2150f344.md) |
| raw-cpuid | Dependency Manager | [open](rust-raw-cpuid-e0c8cffb.md) |
| rustup | Dependency Manager | [open](rust-rustup-eaa7a72b.md) |
| sha1_smol | Dependency Manager | [open](rust-sha1-smol-5c432295.md) |
