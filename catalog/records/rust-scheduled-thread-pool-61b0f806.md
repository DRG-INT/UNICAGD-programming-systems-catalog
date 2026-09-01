# scheduled-thread-pool

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Concurrency Parallelism |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/scheduled-thread-pool](https://crates.io/crates/scheduled-thread-pool) |
| Source record ids | crates_io-1cc30f90324daf |

## System Engineer Summary

scheduled-thread-pool is tracked as a concurrency parallelism record in the Rust branch. The source
did not provide a long description, so this page keeps the identity, release state, provenance, and
operational classification explicit for later enrichment.

## Operational Role

For a systems engineer, scheduled-thread-pool belongs in the Rust inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.7 | 2023-03-07T01:36:32.693097Z | [https://crates.io/api/v1/crates?page=15&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=15&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `concurrency_parallelism` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=15&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-1cc30f90324daf` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| blocking | Concurrency Parallelism | [open](rust-blocking-2e4670f8.md) |
| crossbeam | Concurrency Parallelism | [open](rust-crossbeam-52e023ac.md) |
| dashmap | Concurrency Parallelism | [open](rust-dashmap-df61348c.md) |
| event-listener | Concurrency Parallelism | [open](rust-event-listener-217acd9f.md) |
| local-channel | Concurrency Parallelism | [open](rust-local-channel-9b8dd9fc.md) |
| local-waker | Concurrency Parallelism | [open](rust-local-waker-a14cd2ab.md) |
| lockfree-object-pool | Concurrency Parallelism | [open](rust-lockfree-object-pool-f7ac4a3d.md) |
| maybe-rayon | Concurrency Parallelism | [open](rust-maybe-rayon-50ef4904.md) |
