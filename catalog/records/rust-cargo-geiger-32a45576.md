# cargo-geiger

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Security Sast |
| Source type | security_sast |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/cargo-geiger](https://crates.io/crates/cargo-geiger) |
| Source record ids | master-694f47127bc0 |

## System Engineer Summary

Unsafe Rust usage statistics

## Operational Role

For a systems engineer, cargo-geiger belongs in the Rust inventory as part of supply-chain review,
vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.13.0 | 2025-08-31T08:40:31.637036Z | [https://crates.io/api/v1/crates/cargo-geiger](https://crates.io/api/v1/crates/cargo-geiger) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/cargo-geiger` at `2026-09-01T02:12:59+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-694f47127bc0` from `master_json` as `security_sast`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aws-sdk-sts | Security Sast | [open](rust-aws-sdk-sts-4cfb0f29.md) |
| cargo-audit | Security Sast | [open](rust-cargo-audit-c60e4666.md) |
| cargo-semver-checks | Security Sast | [open](rust-cargo-semver-checks-8d894f1c.md) |
| cargo-vet | Security Sast | [open](rust-cargo-vet-8488044c.md) |
| mimalloc | Security Sast | [open](rust-mimalloc-e7d4274d.md) |
| security-framework | Security Sast | [open](rust-security-framework-382fc68f.md) |
| security-framework-sys | Security Sast | [open](rust-security-framework-sys-04a0e5a5.md) |
