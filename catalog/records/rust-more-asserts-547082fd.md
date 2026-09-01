# more-asserts

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Debugger |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/more-asserts](https://crates.io/crates/more-asserts) |
| Source record ids | crates_io-6f1d4a52e24755 |

## System Engineer Summary

Small library providing additional assert_* and debug_assert_* macros.

## Operational Role

For a systems engineer, more-asserts belongs in the Rust inventory as part of fault isolation, live
inspection, breakpoints, and production-adjacent diagnosis.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.3.1 | 2022-10-01T08:33:45.677928Z | [https://crates.io/api/v1/crates?page=17&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=17&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `debugger` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=17&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-6f1d4a52e24755` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| debugid | Debugger | [open](rust-debugid-9261fd14.md) |
| new_debug_unreachable | Debugger | [open](rust-new-debug-unreachable-36e02c8b.md) |
| opaque-debug | Debugger | [open](rust-opaque-debug-788ae81c.md) |
| sentry-debug-images | Debugger | [open](rust-sentry-debug-images-c8d7d11e.md) |
| sval_fmt | Debugger | [open](rust-sval-fmt-a722981f.md) |
