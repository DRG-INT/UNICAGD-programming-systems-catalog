# brotli-decompressor

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/brotli-decompressor](https://crates.io/crates/brotli-decompressor) |
| Source record ids | crates_io-12e7d3ffc8a40d |

## System Engineer Summary

A brotli decompressor that with an interface avoiding the rust stdlib. This makes it suitable for
embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's
allocator may be employed. The default build also includes a stdlib allocator and stream interface.
Disable this with --features=no-stdlib. Alternatively, --features=unsafe turns off array bounds
checks and memory initialization but provides a safe interface for the caller. Without adding the
--features=unsafe argument, all included code is safe. For compression in addition to this library,
download

## Operational Role

For a systems engineer, brotli-decompressor belongs in the Rust inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 5.0.3 | 2026-06-14T18:10:09.204091Z | [https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads` at `2026-09-01T02:12:57+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-12e7d3ffc8a40d` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aes | Language Specification | [open](rust-aes-51a8d565.md) |
| async-attributes | Language Specification | [open](rust-async-attributes-ae37e076.md) |
| async-std | Language Specification | [open](rust-async-std-abaaac81.md) |
| block | Language Specification | [open](rust-block-6b036ded.md) |
| block2 | Language Specification | [open](rust-block2-b93b6216.md) |
| brotli | Language Specification | [open](rust-brotli-6dba38aa.md) |
| codespan-reporting | Language Specification | [open](rust-codespan-reporting-ef7af61c.md) |
| const-oid | Language Specification | [open](rust-const-oid-59e32dc6.md) |
