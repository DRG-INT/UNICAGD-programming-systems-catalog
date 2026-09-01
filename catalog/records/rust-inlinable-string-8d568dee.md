# inlinable_string

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Memory Analyzer |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/inlinable_string](https://crates.io/crates/inlinable_string) |
| Source record ids | crates_io-8162faf5a934ab |

## System Engineer Summary

The `inlinable_string` crate provides the `InlinableString` type -- an owned, grow-able UTF-8 string
that stores small strings inline and avoids heap-allocation -- and the `StringExt` trait which
abstracts string operations over both `std::string::String` and `InlinableString` (or even your own
custom string type).

## Operational Role

For a systems engineer, inlinable_string belongs in the Rust inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.1.15 | 2022-01-04T08:46:15.989765Z | [https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `memory_analyzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-8162faf5a934ab` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| astral-tokio-tar | Memory Analyzer | [open](rust-astral-tokio-tar-cc055656.md) |
| bitvec | Memory Analyzer | [open](rust-bitvec-c2457646.md) |
| bytecheck | Memory Analyzer | [open](rust-bytecheck-fe3284f0.md) |
| compact_str | Memory Analyzer | [open](rust-compact-str-7f4b0cf3.md) |
| dary_heap | Memory Analyzer | [open](rust-dary-heap-2e7eb5bf.md) |
| datafusion | Memory Analyzer | [open](rust-datafusion-9ece1411.md) |
| fontdb | Memory Analyzer | [open](rust-fontdb-db3bfb04.md) |
| git2 | Memory Analyzer | [open](rust-git2-edeb3289.md) |
