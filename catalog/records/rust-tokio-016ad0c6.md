# Tokio

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Async Runtime |
| Source type | async_runtime |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/tokio](https://crates.io/crates/tokio) |
| Source record ids | master-241eec3b34c2, crates_io-72101b83a4eedd |

## System Engineer Summary

Tokio is tracked as an async runtime record in the Rust branch. The source did not provide a long
description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, Tokio belongs in the Rust inventory as part of concurrency scheduling, I/O
throughput, cancellation, and latency management.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.53.1 | 2026-07-20T17:06:09.996426Z | [https://crates.io/api/v1/crates/Tokio](https://crates.io/api/v1/crates/Tokio) |  |
| preview | known | 0.2.0-alpha.6 | 2019-10-01T00:49:11.181139Z | [https://crates.io/api/v1/crates/Tokio](https://crates.io/api/v1/crates/Tokio) |  |

## Engineering Notes

- Treat category as `async_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/Tokio` at `2026-09-01T01:59:21+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `2`.

- `master-241eec3b34c2` from `master_json` as `async_runtime`
- `crates_io-72101b83a4eedd` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-service | Async Runtime | [open](rust-actix-service-c35b1c38.md) |
| async-channel | Async Runtime | [open](rust-async-channel-56d40cbc.md) |
| async-compression | Async Runtime | [open](rust-async-compression-1943c86c.md) |
| async-executor | Async Runtime | [open](rust-async-executor-bf2249ed.md) |
| async-fs | Async Runtime | [open](rust-async-fs-73af5d3e.md) |
| async-global-executor | Async Runtime | [open](rust-async-global-executor-51b07d47.md) |
| async-graphql | Async Runtime | [open](rust-async-graphql-71165dd4.md) |
| async-graphql-axum | Async Runtime | [open](rust-async-graphql-axum-eb2105bf.md) |
