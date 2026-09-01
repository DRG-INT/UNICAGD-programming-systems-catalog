# cc

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Compiler |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/cc](https://crates.io/crates/cc) |
| Source record ids | crates_io-8315438633e1d2 |

## System Engineer Summary

A build-time dependency for Cargo build scripts to assist in invoking the native C compiler to
compile native C code into a static archive to be linked into Rust code.

## Operational Role

For a systems engineer, cc belongs in the Rust inventory as part of compiler selection, diagnostics
behavior, target support, ABI expectations, and build reproducibility.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.4.4 | 2026-08-21T08:20:10.205770Z | [https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=1&per_page=100&sort=downloads) |  |
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

- `crates_io-8315438633e1d2` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| autocfg | Compiler | [open](rust-autocfg-ca0f8a64.md) |
| clang-sys | Compiler | [open](rust-clang-sys-f1961db1.md) |
| cmov | Compiler | [open](rust-cmov-061e5bcb.md) |
| compiler_builtins | Compiler | [open](rust-compiler-builtins-aa173dbd.md) |
| cxxbridge-flags | Compiler | [open](rust-cxxbridge-flags-c95fbc04.md) |
| gcc | Compiler | [open](rust-gcc-09b58dce.md) |
| libfuzzer-sys | Compiler | [open](rust-libfuzzer-sys-61022c5c.md) |
| miette | Compiler | [open](rust-miette-197355ef.md) |
