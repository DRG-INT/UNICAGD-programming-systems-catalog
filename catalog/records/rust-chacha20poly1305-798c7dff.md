# chacha20poly1305

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Cryptography |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/chacha20poly1305](https://crates.io/crates/chacha20poly1305) |
| Source record ids | crates_io-6f92661db20dfb |

## System Engineer Summary

Pure Rust implementation of the ChaCha20Poly1305 Authenticated Encryption with Additional Data
Cipher (RFC 8439) with optional architecture-specific hardware acceleration. Also contains
implementations of the XChaCha20Poly1305 extended nonce variant of ChaCha20Poly1305, and the
reduced-round ChaCha8Poly1305 and ChaCha12Poly1305 lightweight variants.

## Operational Role

For a systems engineer, chacha20poly1305 belongs in the Rust inventory as part of confidentiality,
integrity, authentication, and key-management risk.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.11.0 | 2026-08-05T13:00:37.663365Z | [https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `cryptography` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-6f92661db20dfb` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| actix-tls | Cryptography | [open](rust-actix-tls-4ede0a77.md) |
| aes-gcm | Cryptography | [open](rust-aes-gcm-13ed5a6a.md) |
| aes-gcm-siv | Cryptography | [open](rust-aes-gcm-siv-a8da08fc.md) |
| argon2 | Cryptography | [open](rust-argon2-c3cc4d9c.md) |
| as-slice | Cryptography | [open](rust-as-slice-5a5094e5.md) |
| aws-lc-fips-sys | Cryptography | [open](rust-aws-lc-fips-sys-f719e86d.md) |
| aws-lc-rs | Cryptography | [open](rust-aws-lc-rs-d5b53a9b.md) |
| aws-lc-sys | Cryptography | [open](rust-aws-lc-sys-d4004be2.md) |
