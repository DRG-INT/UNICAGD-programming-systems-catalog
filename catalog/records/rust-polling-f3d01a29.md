# polling

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Message Broker |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/polling](https://crates.io/crates/polling) |
| Source record ids | crates_io-14733a7070f99b |

## System Engineer Summary

Portable interface to epoll, kqueue, event ports, and IOCP

## Operational Role

For a systems engineer, polling belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 3.11.0 | 2025-09-14T14:00:51.946852Z | [https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `message_broker` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads` at `2026-09-01T02:12:57+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-14733a7070f99b` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| concurrent-queue | Message Broker | [open](rust-concurrent-queue-be84d7d6.md) |
| crossbeam-queue | Message Broker | [open](rust-crossbeam-queue-6ce25da7.md) |
| kqueue | Message Broker | [open](rust-kqueue-133c94cf.md) |
| kqueue-sys | Message Broker | [open](rust-kqueue-sys-0b0fdb03.md) |
| rdkafka | Message Broker | [open](rust-rdkafka-b7aefe42.md) |
