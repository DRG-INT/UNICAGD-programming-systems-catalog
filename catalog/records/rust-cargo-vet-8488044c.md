# cargo-vet

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Security Sast |
| Source type | security_sast |
| Verification | unverified_seed |
| Canonical URL | [https://crates.io/crates/cargo-vet](https://crates.io/crates/cargo-vet) |
| Source record ids | corpus-5f04cfd064ad5f |

## System Engineer Summary

Supply-chain security for Rust

## Operational Role

For a systems engineer, cargo-vet belongs in the Rust inventory as part of supply-chain review,
vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.10.2 | 2026-01-13T20:43:49.981081Z | [https://crates.io/api/v1/crates/cargo-vet](https://crates.io/api/v1/crates/cargo-vet) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates/cargo-vet` at `2026-09-01T01:59:23+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_corpus | unverified_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_corpus", "status": "unverified_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `corpus-5f04cfd064ad5f` from `master_json` as `security_sast`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aws-sdk-sts | Security Sast | [open](rust-aws-sdk-sts-4cfb0f29.md) |
| cargo-audit | Security Sast | [open](rust-cargo-audit-c60e4666.md) |
| cargo-geiger | Security Sast | [open](rust-cargo-geiger-32a45576.md) |
| cargo-semver-checks | Security Sast | [open](rust-cargo-semver-checks-8d894f1c.md) |
| mimalloc | Security Sast | [open](rust-mimalloc-e7d4274d.md) |
| security-framework | Security Sast | [open](rust-security-framework-382fc68f.md) |
| security-framework-sys | Security Sast | [open](rust-security-framework-sys-04a0e5a5.md) |
