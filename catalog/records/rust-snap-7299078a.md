# snap

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Compression |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/snap](https://crates.io/crates/snap) |
| Source record ids | crates_io-b2354cca3a0096 |

## System Engineer Summary

A pure Rust implementation of the Snappy compression algorithm. Includes streaming compression and
decompression.

## Operational Role

For a systems engineer, snap belongs in the Rust inventory as part of ecosystem capability mapping,
dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.1.2 | 2026-07-15T11:40:42.657953Z | [https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `compression` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-b2354cca3a0096` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| compression-codecs | Compression | [open](rust-compression-codecs-b842972a.md) |
| compression-core | Compression | [open](rust-compression-core-ef3f311e.md) |
| deflate | Compression | [open](rust-deflate-11068d3f.md) |
| gzip-header | Compression | [open](rust-gzip-header-55bb5bd8.md) |
| leb128fmt | Compression | [open](rust-leb128fmt-35cf5f0f.md) |
| libbz2-rs-sys | Compression | [open](rust-libbz2-rs-sys-ed662e54.md) |
| rlp | Compression | [open](rust-rlp-08110052.md) |
| roaring | Compression | [open](rust-roaring-2af848fc.md) |
