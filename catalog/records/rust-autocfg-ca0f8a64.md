# autocfg

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Compiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/autocfg](https://crates.io/crates/autocfg) |
| Source record ids | crates_io-ede57395711efe |

## System Engineer Summary

Automatic cfg for Rust compiler features

## Operational Role

For a systems engineer, autocfg belongs in the Rust inventory as part of compiler selection,
diagnostics behavior, target support, ABI expectations, and build reproducibility.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.5.1 | 2026-05-22T11:03:04.576867Z | [https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `compiler` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-ede57395711efe` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| cc | Compiler | [open](rust-cc-40676e0b.md) |
| clang-sys | Compiler | [open](rust-clang-sys-f1961db1.md) |
| cmov | Compiler | [open](rust-cmov-061e5bcb.md) |
| compiler_builtins | Compiler | [open](rust-compiler-builtins-aa173dbd.md) |
| cxxbridge-flags | Compiler | [open](rust-cxxbridge-flags-c95fbc04.md) |
| gcc | Compiler | [open](rust-gcc-09b58dce.md) |
| libfuzzer-sys | Compiler | [open](rust-libfuzzer-sys-61022c5c.md) |
| miette | Compiler | [open](rust-miette-197355ef.md) |
