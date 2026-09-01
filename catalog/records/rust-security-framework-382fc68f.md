# security-framework

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Security Sast |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/security-framework](https://crates.io/crates/security-framework) |
| Source record ids | crates_io-4f4952bf95e0b1 |

## System Engineer Summary

Security.framework bindings for macOS and iOS

## Operational Role

For a systems engineer, security-framework belongs in the Rust inventory as part of supply-chain
review, vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 3.7.0 | 2026-02-20T00:28:54.024219Z | [https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=4&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-4f4952bf95e0b1` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| aws-sdk-sts | Security Sast | [open](rust-aws-sdk-sts-4cfb0f29.md) |
| cargo-audit | Security Sast | [open](rust-cargo-audit-c60e4666.md) |
| cargo-geiger | Security Sast | [open](rust-cargo-geiger-32a45576.md) |
| cargo-semver-checks | Security Sast | [open](rust-cargo-semver-checks-8d894f1c.md) |
| cargo-vet | Security Sast | [open](rust-cargo-vet-8488044c.md) |
| mimalloc | Security Sast | [open](rust-mimalloc-e7d4274d.md) |
| security-framework-sys | Security Sast | [open](rust-security-framework-sys-04a0e5a5.md) |
