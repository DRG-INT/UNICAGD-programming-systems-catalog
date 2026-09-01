# env_logger

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Logging Observability |
| Source type | logging_observability |
| Verification | unverified_seed |
| Canonical URL | [https://crates.io/crates/env_logger](https://crates.io/crates/env_logger) |
| Source record ids | corpus-01bfb2baa384a6, crates_io-a1efee36f71443 |

## System Engineer Summary

A logging implementation for `log` which is configured via an environment variable.

## Operational Role

For a systems engineer, env_logger belongs in the Rust inventory as part of diagnostics, metrics,
auditability, tracing, and incident response.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.11.11 | 2026-06-25T12:42:02.332351Z | [https://crates.io/api/v1/crates/env_logger](https://crates.io/api/v1/crates/env_logger) |  |
| preview | known | 0.5.0-rc.2 | 2018-01-08T01:07:00.223394Z | [https://crates.io/api/v1/crates/env_logger](https://crates.io/api/v1/crates/env_logger) |  |

## Engineering Notes

- Treat category as `logging_observability` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/env_logger` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_corpus | unverified_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_corpus", "status": "unverified_seed"}` |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `2`.

- `corpus-01bfb2baa384a6` from `master_json` as `logging_observability`
- `crates_io-a1efee36f71443` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| android_logger | Logging Observability | [open](rust-android-logger-4234548c.md) |
| arrow-schema | Logging Observability | [open](rust-arrow-schema-3690b891.md) |
| aws-smithy-eventstream | Logging Observability | [open](rust-aws-smithy-eventstream-e8e6d761.md) |
| aws-smithy-observability | Logging Observability | [open](rust-aws-smithy-observability-7204d6c5.md) |
| aws-smithy-query | Logging Observability | [open](rust-aws-smithy-query-b6654ee8.md) |
| console_error_panic_hook | Logging Observability | [open](rust-console-error-panic-hook-a9ab6b4d.md) |
| console_log | Logging Observability | [open](rust-console-log-715f7bc2.md) |
| dialoguer | Logging Observability | [open](rust-dialoguer-3213388c.md) |
