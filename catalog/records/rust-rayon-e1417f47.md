# Rayon

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Concurrency Parallelism |
| Source type | concurrency_parallelism |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/rayon](https://crates.io/crates/rayon) |
| Source record ids | master-ceac7538e56e, crates_io-8abaf94c196300 |

## System Engineer Summary

Data parallelism library

## Operational Role

For a systems engineer, Rayon belongs in the Rust inventory as part of ecosystem capability mapping,
dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.12.0 | 2026-04-14T00:56:56.454086Z | [https://crates.io/api/v1/crates/Rayon](https://crates.io/api/v1/crates/Rayon) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `concurrency_parallelism` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/Rayon` at `2026-09-01T01:59:21+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `2`.

- `master-ceac7538e56e` from `master_json` as `concurrency_parallelism`
- `crates_io-8abaf94c196300` from `crates_io` as `registry_expansion`

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
