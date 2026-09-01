# afl.rs

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Fuzzer |
| Source type | fuzzer |
| Verification | unverified_seed |
| Canonical URL | unknown |
| Source record ids | corpus-43f1fb1bfe02fe |

## System Engineer Summary

afl.rs is tracked as a fuzzer record in the Rust branch. The source did not provide a long
description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, afl.rs belongs in the Rust inventory as part of input-space exploration,
parser hardening, and unsafe edge-case discovery.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | crate_metadata_missing |
| preview/nightly | unknown |  |  | unknown | crate_metadata_missing |

## Engineering Notes

- Treat category as `fuzzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `crate_metadata_missing`.
- Preview/nightly metadata is unknown because `crate_metadata_missing`.
- No canonical URL is verified yet; resolve before using this as an authoritative dependency identity.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_corpus | unverified_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_corpus", "status": "unverified_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `corpus-43f1fb1bfe02fe` from `master_json` as `fuzzer`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| cargo-fuzz | Fuzzer | [open](rust-cargo-fuzz-b5f3d91d.md) |
| fuzzy-matcher | Fuzzer | [open](rust-fuzzy-matcher-6c3d5bb7.md) |
| honggfuzz-rs | Fuzzer | [open](rust-honggfuzz-rs-aa21e4f2.md) |
