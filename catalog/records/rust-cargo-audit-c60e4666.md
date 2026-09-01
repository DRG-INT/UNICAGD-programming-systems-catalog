# cargo-audit

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Security Sast |
| Source type | security_sast |
| Verification | catalog_seed |
| Canonical URL | [https://crates.io/crates/cargo-audit](https://crates.io/crates/cargo-audit) |
| Source record ids | master-43192b707909 |

## System Engineer Summary

Rust dependency vulnerability auditing

## Operational Role

For a systems engineer, cargo-audit belongs in the Rust inventory as part of supply-chain review,
vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.22.2 | 2026-06-05T12:33:04.440539Z | [https://crates.io/api/v1/crates/cargo-audit](https://crates.io/api/v1/crates/cargo-audit) |  |
| preview | known | 0.21.0-rc.0 | 2024-10-16T00:31:09.073854Z | [https://crates.io/api/v1/crates/cargo-audit](https://crates.io/api/v1/crates/cargo-audit) |  |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/cargo-audit` at `2026-09-01T01:59:23+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-43192b707909` from `master_json` as `security_sast`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aws-sdk-sts | Security Sast | [open](rust-aws-sdk-sts-4cfb0f29.md) |
| cargo-geiger | Security Sast | [open](rust-cargo-geiger-32a45576.md) |
| cargo-semver-checks | Security Sast | [open](rust-cargo-semver-checks-8d894f1c.md) |
| cargo-vet | Security Sast | [open](rust-cargo-vet-8488044c.md) |
| mimalloc | Security Sast | [open](rust-mimalloc-e7d4274d.md) |
| security-framework | Security Sast | [open](rust-security-framework-382fc68f.md) |
| security-framework-sys | Security Sast | [open](rust-security-framework-sys-04a0e5a5.md) |
