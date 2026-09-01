# rgb

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/rgb](https://crates.io/crates/rgb) |
| Source record ids | crates_io-1d970c09a9d046 |

## System Engineer Summary

`struct RGB/RGBA/etc.` for sharing pixels between crates + convenience methods for color
manipulation. Allows no-copy high-level interoperability. Also adds common convenience methods and
implements standard Rust traits to make `RGB`/`RGBA` pixels and slices first-class Rust objects.

## Operational Role

For a systems engineer, rgb belongs in the Rust inventory as part of ecosystem capability mapping,
dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.8.53 | 2026-02-25T18:28:51.603642Z | [https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=8&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-1d970c09a9d046` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aes | Language Specification | [open](rust-aes-51a8d565.md) |
| async-attributes | Language Specification | [open](rust-async-attributes-ae37e076.md) |
| async-std | Language Specification | [open](rust-async-std-abaaac81.md) |
| block | Language Specification | [open](rust-block-6b036ded.md) |
| block2 | Language Specification | [open](rust-block2-b93b6216.md) |
| brotli | Language Specification | [open](rust-brotli-6dba38aa.md) |
| brotli-decompressor | Language Specification | [open](rust-brotli-decompressor-dda445d2.md) |
| codespan-reporting | Language Specification | [open](rust-codespan-reporting-ef7af61c.md) |
