# kqueue

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Message Broker |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/kqueue](https://crates.io/crates/kqueue) |
| Source record ids | crates_io-dc8db419010c15 |

## System Engineer Summary

kqueue interface for BSDs

## Operational Role

For a systems engineer, kqueue belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.2.1 | 2026-08-04T14:04:27.587775Z | [https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `message_broker` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-dc8db419010c15` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| concurrent-queue | Message Broker | [open](rust-concurrent-queue-be84d7d6.md) |
| crossbeam-queue | Message Broker | [open](rust-crossbeam-queue-6ce25da7.md) |
| kqueue-sys | Message Broker | [open](rust-kqueue-sys-0b0fdb03.md) |
| polling | Message Broker | [open](rust-polling-f3d01a29.md) |
| rdkafka | Message Broker | [open](rust-rdkafka-b7aefe42.md) |
