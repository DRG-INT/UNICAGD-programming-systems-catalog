# zip

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Compression |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/zip](https://crates.io/crates/zip) |
| Source record ids | crates_io-9a62c496beef5c |

## System Engineer Summary

Library to support the reading and writing of zip files.

## Operational Role

For a systems engineer, zip belongs in the Rust inventory as part of ecosystem capability mapping,
dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 8.6.0 | 2026-08-11T01:53:59.789008Z | [https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `compression` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-9a62c496beef5c` from `crates_io` as `registry_expansion`

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
