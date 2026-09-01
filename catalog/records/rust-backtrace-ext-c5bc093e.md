# backtrace-ext

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Profiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/backtrace-ext](https://crates.io/crates/backtrace-ext) |
| Source record ids | crates_io-912ecce2af75e9 |

## System Engineer Summary

minor conveniences on top of the backtrace crate

## Operational Role

For a systems engineer, backtrace-ext belongs in the Rust inventory as part of hot-path discovery,
allocation analysis, latency control, and capacity planning.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.1 | 2023-03-31T18:00:25.343863Z | [https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `profiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=21&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-912ecce2af75e9` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| color-spantrace | Profiler | [open](rust-color-spantrace-96dba6ba.md) |
| flamegraph | Profiler | [open](rust-flamegraph-27cbc597.md) |
| opentelemetry_api | Profiler | [open](rust-opentelemetry-api-879f3d0b.md) |
| opentelemetry_sdk | Profiler | [open](rust-opentelemetry-sdk-568a410d.md) |
| reqwest-tracing | Profiler | [open](rust-reqwest-tracing-a9c9d39c.md) |
| samply | Profiler | [open](rust-samply-515906c6.md) |
| sentry-backtrace | Profiler | [open](rust-sentry-backtrace-2b40e31a.md) |
| symbolic-common | Profiler | [open](rust-symbolic-common-93c3c096.md) |
