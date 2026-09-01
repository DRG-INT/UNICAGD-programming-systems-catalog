# alloc-no-stdlib

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Standard Library |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/alloc-no-stdlib](https://crates.io/crates/alloc-no-stdlib) |
| Source record ids | crates_io-fe805a0b58fe16 |

## System Engineer Summary

A dynamic allocator that may be used with or without the stdlib. This allows a package with nostd to
allocate memory dynamically and be used either with a custom allocator, items on the stack, or by a
package that wishes to simply use Box<>. It also provides options to use calloc or a mutable global
variable for pre-zeroed memory

## Operational Role

For a systems engineer, alloc-no-stdlib belongs in the Rust inventory as part of ecosystem
capability mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 3.0.0 | 2026-06-14T07:37:22.713662Z | [https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `standard_library` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=5&per_page=100&sort=downloads` at `2026-09-01T02:12:58+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-fe805a0b58fe16` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| alloc-stdlib | Standard Library | [open](rust-alloc-stdlib-374940d8.md) |
| is_terminal_polyfill | Standard Library | [open](rust-is-terminal-polyfill-56df339d.md) |
| javascriptcore-rs | Standard Library | [open](rust-javascriptcore-rs-1b6020f2.md) |
| javascriptcore-rs-sys | Standard Library | [open](rust-javascriptcore-rs-sys-64aa7b2d.md) |
| once_cell_polyfill | Standard Library | [open](rust-once-cell-polyfill-bac8545c.md) |
| papergrid | Standard Library | [open](rust-papergrid-fccdef9a.md) |
