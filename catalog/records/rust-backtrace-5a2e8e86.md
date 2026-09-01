# backtrace

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Interpreter Runtime |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/backtrace](https://crates.io/crates/backtrace) |
| Source record ids | crates_io-f293fedf63b751 |

## System Engineer Summary

A library to acquire a stack trace (backtrace) at runtime in a Rust program.

## Operational Role

For a systems engineer, backtrace belongs in the Rust inventory as part of runtime behavior,
deployment packaging, embedding, upgrade cadence, and compatibility validation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.3.76 | 2025-09-26T02:43:38.784231Z | [https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `interpreter_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads` at `2026-09-01T02:12:57+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-f293fedf63b751` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-macros | Interpreter Runtime | [open](rust-actix-macros-ca794fb7.md) |
| actix-rt | Interpreter Runtime | [open](rust-actix-rt-aef83aa1.md) |
| actix-web-codegen | Interpreter Runtime | [open](rust-actix-web-codegen-9aba0585.md) |
| aws-runtime | Interpreter Runtime | [open](rust-aws-runtime-ac213e01.md) |
| aws-smithy-async | Interpreter Runtime | [open](rust-aws-smithy-async-9d69cd7f.md) |
| aws-smithy-runtime | Interpreter Runtime | [open](rust-aws-smithy-runtime-e27d173f.md) |
| aws-smithy-runtime-api | Interpreter Runtime | [open](rust-aws-smithy-runtime-api-706cee25.md) |
| aws-smithy-runtime-api-macros | Interpreter Runtime | [open](rust-aws-smithy-runtime-api-macros-08700463.md) |
