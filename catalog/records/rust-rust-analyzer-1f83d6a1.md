# rust-analyzer

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Language Server |
| Source type | language_server |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/rust-analyzer](https://crates.io/crates/rust-analyzer) |
| Source record ids | master-22d154e5bff7 |

## System Engineer Summary

rust-analyzer is tracked as a language server record in the Rust branch. The source did not provide
a long description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, rust-analyzer belongs in the Rust inventory as part of editor intelligence,
refactoring assistance, diagnostics, and navigation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.0.1 | 2019-09-17T14:03:23.702114Z | [https://crates.io/api/v1/crates/rust-analyzer](https://crates.io/api/v1/crates/rust-analyzer) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `language_server` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/rust-analyzer` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-22d154e5bff7` from `master_json` as `language_server`
