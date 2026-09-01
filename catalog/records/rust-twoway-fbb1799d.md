# twoway

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Interpreter Runtime |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/twoway](https://crates.io/crates/twoway) |
| Source record ids | crates_io-d6c7f287eae2f2 |

## System Engineer Summary

(Deprecated - use crate memchr instead.) Fast substring search for strings and byte strings.
Optional SSE4.2 acceleration (if detected at runtime) using pcmpestri. Memchr is the only mandatory
dependency. The two way algorithm is also used by rust's libstd itself, but here it is exposed both
for byte strings, using memchr, and optionally using a SSE4.2 accelerated version.

## Operational Role

For a systems engineer, twoway belongs in the Rust inventory as part of runtime behavior, deployment
packaging, embedding, upgrade cadence, and compatibility validation.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.2 | 2021-05-19T22:06:38.467348Z | [https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `interpreter_runtime` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=18&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-d6c7f287eae2f2` from `crates_io` as `registry_expansion`

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
