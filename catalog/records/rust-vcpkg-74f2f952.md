# vcpkg

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/vcpkg](https://crates.io/crates/vcpkg) |
| Source record ids | crates_io-ffb7f64915b631 |

## System Engineer Summary

A library to find native dependencies in a vcpkg tree at build time in order to be used in Cargo
build scripts.

## Operational Role

For a systems engineer, vcpkg belongs in the Rust inventory as part of build graph control, artifact
reproducibility, cross-platform build policy, and CI integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.2.15 | 2021-06-19T16:35:46.573605Z | [https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=3&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-ffb7f64915b631` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| android-activity | Build System | [open](rust-android-activity-958c810f.md) |
| async-task | Build System | [open](rust-async-task-7248a7cd.md) |
| backon | Build System | [open](rust-backon-59db9d30.md) |
| bon | Build System | [open](rust-bon-5c756277.md) |
| build_const | Build System | [open](rust-build-const-0aeeb00d.md) |
| cargo-make | Build System | [open](rust-cargo-make-dcab0faa.md) |
| chrono-tz-build | Build System | [open](rust-chrono-tz-build-0484d9ba.md) |
| clap_builder | Build System | [open](rust-clap-builder-81592afe.md) |
