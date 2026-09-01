# safetensors

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Formatter |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/safetensors](https://crates.io/crates/safetensors) |
| Source record ids | crates_io-916c7d592366f5 |

## System Engineer Summary

Provides functions to read and write safetensors which aim to be safer than their PyTorch
counterpart. The format is 8 bytes which is an unsized int, being the size of a JSON header, the
JSON header refers the `dtype` the `shape` and `data_offsets` which are the offsets for the values
in the rest of the file.

## Operational Role

For a systems engineer, safetensors belongs in the Rust inventory as part of low-noise code review,
style consistency, and automation-friendly editing.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.8.0 | 2026-06-09T08:34:43.361780Z | [https://crates.io/api/v1/crates?page=20&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=20&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `formatter` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=20&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-916c7d592366f5` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| annotate-snippets | Formatter | [open](rust-annotate-snippets-0d48506d.md) |
| arrow-csv | Formatter | [open](rust-arrow-csv-364e5a69.md) |
| arrow-ipc | Formatter | [open](rust-arrow-ipc-8a349159.md) |
| arrow-json | Formatter | [open](rust-arrow-json-6fc174f5.md) |
| arrow-row | Formatter | [open](rust-arrow-row-d82ff8a4.md) |
| bech32 | Formatter | [open](rust-bech32-b269289b.md) |
| bitstream-io | Formatter | [open](rust-bitstream-io-76f36e38.md) |
| built | Formatter | [open](rust-built-644f5ff7.md) |
