# new_debug_unreachable

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Debugger |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/new_debug_unreachable](https://crates.io/crates/new_debug_unreachable) |
| Source record ids | crates_io-1c0f5c637e728f |

## System Engineer Summary

panic in debug, intrinsics::unreachable() in release (fork of debug_unreachable)

## Operational Role

For a systems engineer, new_debug_unreachable belongs in the Rust inventory as part of fault
isolation, live inspection, breakpoints, and production-adjacent diagnosis.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.0.6 | 2024-03-15T17:26:05.782555Z | [https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `debugger` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=6&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-1c0f5c637e728f` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| debugid | Debugger | [open](rust-debugid-9261fd14.md) |
| more-asserts | Debugger | [open](rust-more-asserts-547082fd.md) |
| opaque-debug | Debugger | [open](rust-opaque-debug-788ae81c.md) |
| sentry-debug-images | Debugger | [open](rust-sentry-debug-images-c8d7d11e.md) |
| sval_fmt | Debugger | [open](rust-sval-fmt-a722981f.md) |
