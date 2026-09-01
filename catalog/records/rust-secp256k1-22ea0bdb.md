# secp256k1

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Visualization Gui |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/secp256k1](https://crates.io/crates/secp256k1) |
| Source record ids | crates_io-bf1ffa57ed61bc |

## System Engineer Summary

Rust wrapper library for Pieter Wuille's `libsecp256k1`. Implements ECDSA and BIP 340 signatures for
the SECG elliptic curve group secp256k1 and related utilities.

## Operational Role

For a systems engineer, secp256k1 belongs in the Rust inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.33.1 | 2026-08-29T19:42:51.505142Z | [https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `visualization_gui` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-bf1ffa57ed61bc` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| anyhow | Visualization Gui | [open](rust-anyhow-cc216d40.md) |
| ascii | Visualization Gui | [open](rust-ascii-d18e2693.md) |
| bstr | Visualization Gui | [open](rust-bstr-dd1e73fc.md) |
| cpuid-bool | Visualization Gui | [open](rust-cpuid-bool-fdcabe96.md) |
| criterion-plot | Visualization Gui | [open](rust-criterion-plot-7b9f5798.md) |
| dpi | Visualization Gui | [open](rust-dpi-438777ef.md) |
| egui | Visualization Gui | [open](rust-egui-bbe081e8.md) |
| eyre | Visualization Gui | [open](rust-eyre-3ea5277e.md) |
