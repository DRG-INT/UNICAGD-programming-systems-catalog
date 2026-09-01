# flamegraph

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Profiler |
| Source type | profiler |
| Verification | unverified_seed |
| Canonical URL | [https://crates.io/crates/flamegraph](https://crates.io/crates/flamegraph) |
| Source record ids | corpus-669a1ca3f6cfca |

## System Engineer Summary

A simple cargo subcommand for generating flamegraphs, using inferno under the hood

## Operational Role

For a systems engineer, flamegraph belongs in the Rust inventory as part of hot-path discovery,
allocation analysis, latency control, and capacity planning.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.6.14 | 2026-08-12T10:10:54.656242Z | [https://crates.io/api/v1/crates/flamegraph](https://crates.io/api/v1/crates/flamegraph) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `profiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/flamegraph` at `2026-09-01T01:59:23+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_corpus | unverified_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_corpus", "status": "unverified_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `corpus-669a1ca3f6cfca` from `master_json` as `profiler`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| backtrace-ext | Profiler | [open](rust-backtrace-ext-c5bc093e.md) |
| color-spantrace | Profiler | [open](rust-color-spantrace-96dba6ba.md) |
| opentelemetry_api | Profiler | [open](rust-opentelemetry-api-879f3d0b.md) |
| opentelemetry_sdk | Profiler | [open](rust-opentelemetry-sdk-568a410d.md) |
| reqwest-tracing | Profiler | [open](rust-reqwest-tracing-a9c9d39c.md) |
| samply | Profiler | [open](rust-samply-515906c6.md) |
| sentry-backtrace | Profiler | [open](rust-sentry-backtrace-2b40e31a.md) |
| symbolic-common | Profiler | [open](rust-symbolic-common-93c3c096.md) |
