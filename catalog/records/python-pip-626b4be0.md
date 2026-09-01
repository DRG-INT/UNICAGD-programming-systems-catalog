# pip

## Identity

| Field | Value |
| --- | --- |
| Language branch | Python |
| Category | Package Manager |
| Source type | package_manager |
| Verification | catalog_seed |
| Canonical URL | [https://pypi.org/project/pip/](https://pypi.org/project/pip/) |
| Source record ids | master-fd60c2aa5c07 |

## System Engineer Summary

Python package installer

## Operational Role

For a systems engineer, pip belongs in the Python inventory as part of dependency acquisition,
lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 26.2.1 | 2026-08-04T22:51:14.148997Z | [https://pypi.org/pypi/pip/json](https://pypi.org/pypi/pip/json) |  |
| preview | known | 24.1b2 | 2024-06-12T06:38:43.188646Z | [https://pypi.org/pypi/pip/json](https://pypi.org/pypi/pip/json) |  |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://pypi.org/pypi/pip/json` at `2026-09-01T02:12:59+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-fd60c2aa5c07` from `master_json` as `package_manager`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Hatch | Package Manager | [open](python-hatch-656769d4.md) |
| Poetry | Package Manager | [open](python-poetry-60a7474a.md) |
| uv | Package Manager | [open](python-uv-c01e60f7.md) |
