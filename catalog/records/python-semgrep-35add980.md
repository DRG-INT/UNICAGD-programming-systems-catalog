# Semgrep

## Identity

| Field | Value |
| --- | --- |
| Language branch | Python |
| Category | Security Sast |
| Source type | security_sast |
| Verification | catalog_seed |
| Canonical URL | [https://pypi.org/project/semgrep/](https://pypi.org/project/semgrep/) |
| Source record ids | master-4fec6446e807 |

## System Engineer Summary

Multi-language static analysis

## Operational Role

For a systems engineer, Semgrep belongs in the Python inventory as part of supply-chain review,
vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.175.0 | 2026-08-26T17:10:26.526254Z | [https://pypi.org/pypi/Semgrep/json](https://pypi.org/pypi/Semgrep/json) |  |
| preview | known | 0.8.0b1 | 2020-05-20T22:45:43.775833Z | [https://pypi.org/pypi/Semgrep/json](https://pypi.org/pypi/Semgrep/json) |  |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://pypi.org/pypi/Semgrep/json` at `2026-09-01T01:59:27+00:00`.
- Preview/nightly metadata is present through channel `preview`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-4fec6446e807` from `master_json` as `security_sast`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Bandit | Security Sast | [open](python-bandit-d9eda56d.md) |
