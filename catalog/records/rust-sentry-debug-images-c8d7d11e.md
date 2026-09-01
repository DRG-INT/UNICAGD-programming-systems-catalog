# sentry-debug-images

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Debugger |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/sentry-debug-images](https://crates.io/crates/sentry-debug-images) |
| Source record ids | crates_io-003af1c975a737 |

## System Engineer Summary

Sentry integration that adds the list of loaded libraries to events.

## Operational Role

For a systems engineer, sentry-debug-images belongs in the Rust inventory as part of fault
isolation, live inspection, breakpoints, and production-adjacent diagnosis.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.49.2 | 2026-08-26T14:42:34.599896Z | [https://crates.io/api/v1/crates?page=19&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=19&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `debugger` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=19&per_page=100&sort=downloads` at `2026-09-01T01:59:16+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-003af1c975a737` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| debugid | Debugger | [open](rust-debugid-9261fd14.md) |
| more-asserts | Debugger | [open](rust-more-asserts-547082fd.md) |
| new_debug_unreachable | Debugger | [open](rust-new-debug-unreachable-36e02c8b.md) |
| opaque-debug | Debugger | [open](rust-opaque-debug-788ae81c.md) |
| sval_fmt | Debugger | [open](rust-sval-fmt-a722981f.md) |
