# libfuzzer-sys

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Compiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/libfuzzer-sys](https://crates.io/crates/libfuzzer-sys) |
| Source record ids | crates_io-ca60c467c3788a |

## System Engineer Summary

A wrapper around LLVM's libFuzzer runtime.

## Operational Role

For a systems engineer, libfuzzer-sys belongs in the Rust inventory as part of compiler selection,
diagnostics behavior, target support, ABI expectations, and build reproducibility.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.4.13 | 2026-06-04T18:55:34.718132Z | [https://crates.io/api/v1/crates?page=12&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=12&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `compiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=12&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-ca60c467c3788a` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| autocfg | Compiler | [open](rust-autocfg-ca0f8a64.md) |
| cc | Compiler | [open](rust-cc-40676e0b.md) |
| clang-sys | Compiler | [open](rust-clang-sys-f1961db1.md) |
| cmov | Compiler | [open](rust-cmov-061e5bcb.md) |
| compiler_builtins | Compiler | [open](rust-compiler-builtins-aa173dbd.md) |
| cxxbridge-flags | Compiler | [open](rust-cxxbridge-flags-c95fbc04.md) |
| gcc | Compiler | [open](rust-gcc-09b58dce.md) |
| miette | Compiler | [open](rust-miette-197355ef.md) |
