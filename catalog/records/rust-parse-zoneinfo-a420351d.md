# parse-zoneinfo

## Identity

| Field | Value |
| --- | --- |
| Language branch | Rust |
| Category | Database Datastore |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://crates.io/crates/parse-zoneinfo](https://crates.io/crates/parse-zoneinfo) |
| Source record ids | crates_io-0c2b6fd3cb63fc |

## System Engineer Summary

Parse zoneinfo files from the IANA database

## Operational Role

For a systems engineer, parse-zoneinfo belongs in the Rust inventory as part of state persistence,
migrations, performance, and operational recovery.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 0.5.0 | 2025-07-15T14:33:56.331781Z | [https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads](https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads) |  |
| preview/nightly | unknown |  |  | unknown | crates_io_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `database_datastore` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://crates.io/api/v1/crates?page=10&per_page=100&sort=downloads` at `2026-09-01T01:59:15+00:00`.
- Preview/nightly metadata is unknown because `crates_io_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| crates_io | registry-derived | 2026-09-01 | `{"kind": "crates_io", "retrieved": "2026-09-01", "status": "registry-derived"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `crates_io-0c2b6fd3cb63fc` from `crates_io` as `registry_expansion`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| chrono-tz | Database Datastore | [open](rust-chrono-tz-cbf7d7dd.md) |
| datafusion-sql | Database Datastore | [open](rust-datafusion-sql-9f158393.md) |
| Diesel | Database Datastore | [open](rust-diesel-dfc51e5c.md) |
| gix-odb | Database Datastore | [open](rust-gix-odb-1c5b99c6.md) |
| jiff-tzdb | Database Datastore | [open](rust-jiff-tzdb-f20e13ed.md) |
| jiff-tzdb-platform | Database Datastore | [open](rust-jiff-tzdb-platform-132c06b7.md) |
| mongodb Rust driver | Database Datastore | [open](rust-mongodb-rust-driver-b0dceef4.md) |
| postgres-protocol | Database Datastore | [open](rust-postgres-protocol-1be56c65.md) |
