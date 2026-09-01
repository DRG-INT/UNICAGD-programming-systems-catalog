# fuzzy-matcher

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Fuzzer |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/fuzzy-matcher](https://crates.io/crates/fuzzy-matcher) |
| Source record ids | crates_io-700b8de8a64aba |

## System Engineer Summary

fuzzy-matcher is tracked as a fuzzer record in the Rust branch. The source did not provide a long
description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, fuzzy-matcher belongs in the Rust inventory as part of input-space
exploration, parser hardening, and unsafe edge-case discovery.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.3.7 | 2020-10-04T07:17:33.156012Z | [https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `fuzzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-700b8de8a64aba` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| afl.rs | Fuzzer | [open](rust-afl-rs-68eee63c.md) |
| cargo-fuzz | Fuzzer | [open](rust-cargo-fuzz-b5f3d91d.md) |
| honggfuzz-rs | Fuzzer | [open](rust-honggfuzz-rs-aa21e4f2.md) |
