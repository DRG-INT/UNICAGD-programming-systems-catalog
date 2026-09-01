# scoped-tls

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/scoped-tls](https://crates.io/crates/scoped-tls) |
| Source record ids | crates_io-24bc7766f07f18 |

## System Engineer Summary

Library implementation of the standard library's old `scoped_thread_local!` macro for providing
scoped access to thread local storage (TLS) so any type can be stored into TLS.

## Operational Role

For a systems engineer, scoped-tls belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.0.1 | 2022-10-31T15:01:56.394137Z | [https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-24bc7766f07f18` from `crates_io` as `registry_expansion`

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
