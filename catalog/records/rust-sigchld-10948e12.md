# sigchld

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Concurrency Parallelism |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/sigchld](https://crates.io/crates/sigchld) |
| Source record ids | crates_io-2fbe7049bad69e |

## System Engineer Summary

waiting for SIGCHLD from many threads at once

## Operational Role

For a systems engineer, sigchld belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.4 | 2025-07-05T04:05:05.089814Z | [https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `concurrency_parallelism` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads` at `2026-09-01T01:59:16+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-2fbe7049bad69e` from `crates_io` as `registry_expansion`

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
