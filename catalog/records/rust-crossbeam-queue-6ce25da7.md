# crossbeam-queue

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Message Broker |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/crossbeam-queue](https://crates.io/crates/crossbeam-queue) |
| Source record ids | crates_io-2157564904e279 |

## System Engineer Summary

crossbeam-queue is tracked as a message broker record in the Rust branch. The source did not provide
a long description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, crossbeam-queue belongs in the Rust inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.3.13 | 2026-07-06T15:52:58.228649Z | [https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `message_broker` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-2157564904e279` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| concurrent-queue | Message Broker | [open](rust-concurrent-queue-be84d7d6.md) |
| kqueue | Message Broker | [open](rust-kqueue-133c94cf.md) |
| kqueue-sys | Message Broker | [open](rust-kqueue-sys-0b0fdb03.md) |
| polling | Message Broker | [open](rust-polling-f3d01a29.md) |
| rdkafka | Message Broker | [open](rust-rdkafka-b7aefe42.md) |
