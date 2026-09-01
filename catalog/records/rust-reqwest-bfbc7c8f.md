# reqwest

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Networking Http |
| Source type | networking_http |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/reqwest](https://crates.io/crates/reqwest) |
| Source record ids | master-16190d03fc60, crates_io-0d1450ad52c996 |

## System Engineer Summary

reqwest is tracked as a networking http record in the Rust branch. The source did not provide a long
description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, reqwest belongs in the Rust inventory as part of service communication,
clients/servers, protocol handling, and edge integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.13.4 | 2026-05-25T17:12:48.317444Z | [https://crates.io/api/v1/crates/reqwest](https://crates.io/api/v1/crates/reqwest) |  |
| preview | known | 0.13.0-rc.1 | 2025-12-23T21:05:51.164079Z | [https://crates.io/api/v1/crates/reqwest](https://crates.io/api/v1/crates/reqwest) |  |

## Engineering Notes

- Treat category as `networking_http` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/reqwest` at `2026-09-01T02:12:59+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `2`.

- `master-16190d03fc60` from `master_json` as `networking_http`
- `crates_io-0d1450ad52c996` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-http | Networking Http | [open](rust-actix-http-649d5d41.md) |
| actix-server | Networking Http | [open](rust-actix-server-e5a4daec.md) |
| attohttpc | Networking Http | [open](rust-attohttpc-ed4c6017.md) |
| aws-http | Networking Http | [open](rust-aws-http-8b04a69b.md) |
| aws-sigv4 | Networking Http | [open](rust-aws-sigv4-3f7fb63e.md) |
| aws-smithy-http | Networking Http | [open](rust-aws-smithy-http-1b0c4b7a.md) |
| aws-smithy-http-client | Networking Http | [open](rust-aws-smithy-http-client-f416ca39.md) |
| axum | Networking Http | [open](rust-axum-0b78744a.md) |
