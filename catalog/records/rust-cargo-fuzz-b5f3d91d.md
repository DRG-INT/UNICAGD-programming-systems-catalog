# cargo-fuzz

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Fuzzer |
| Source type | fuzzer |
| Verification | unverified_seed |
| Canonical URL | [https://crates.io/crates/cargo-fuzz](https://crates.io/crates/cargo-fuzz) |
| Source record ids | corpus-eac3bc0ef10ee7 |

## System Engineer Summary

A `cargo` subcommand for fuzzing with `libFuzzer`! Easy to use!

## Operational Role

For a systems engineer, cargo-fuzz belongs in the Rust inventory as part of input-space exploration,
parser hardening, and unsafe edge-case discovery.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.13.2 | 2026-06-09T18:37:27.158092Z | [https://crates.io/api/v1/crates/cargo-fuzz](https://crates.io/api/v1/crates/cargo-fuzz) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `fuzzer` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/cargo-fuzz` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_corpus | unverified_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_corpus", "status": "unverified_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `corpus-eac3bc0ef10ee7` from `master_json` as `fuzzer`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| afl.rs | Fuzzer | [open](rust-afl-rs-68eee63c.md) |
| fuzzy-matcher | Fuzzer | [open](rust-fuzzy-matcher-6c3d5bb7.md) |
| honggfuzz-rs | Fuzzer | [open](rust-honggfuzz-rs-aa21e4f2.md) |
