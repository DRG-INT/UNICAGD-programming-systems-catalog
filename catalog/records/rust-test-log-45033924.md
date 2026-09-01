# test-log

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Profiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/test-log](https://crates.io/crates/test-log) |
| Source record ids | crates_io-402a00680eb386 |

## System Engineer Summary

A replacement of the #test attribute that initializes logging and/or tracing infrastructure before
running tests.

## Operational Role

For a systems engineer, test-log belongs in the Rust inventory as part of hot-path discovery,
allocation analysis, latency control, and capacity planning.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.21 | 2026-05-30T22:41:06.804446Z | [https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `profiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=11&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-402a00680eb386` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| backtrace-ext | Profiler | [open](rust-backtrace-ext-c5bc093e.md) |
| color-spantrace | Profiler | [open](rust-color-spantrace-96dba6ba.md) |
| flamegraph | Profiler | [open](rust-flamegraph-27cbc597.md) |
| opentelemetry_api | Profiler | [open](rust-opentelemetry-api-879f3d0b.md) |
| opentelemetry_sdk | Profiler | [open](rust-opentelemetry-sdk-568a410d.md) |
| reqwest-tracing | Profiler | [open](rust-reqwest-tracing-a9c9d39c.md) |
| samply | Profiler | [open](rust-samply-515906c6.md) |
| sentry-backtrace | Profiler | [open](rust-sentry-backtrace-2b40e31a.md) |
