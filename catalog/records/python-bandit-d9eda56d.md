# Bandit

## Identity

| Field | Value |
| --- | --- |
| Language branch | Python |
| Category | Security Sast |
| Source type | security_sast |
| Verification | catalog_seed |
| Canonical URL | [https://pypi.org/project/bandit/](https://pypi.org/project/bandit/) |
| Source record ids | master-a79639752378 |

## System Engineer Summary

Bandit is tracked as a security sast record in the Python branch. The source did not provide a long
description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, Bandit belongs in the Python inventory as part of supply-chain review,
vulnerability detection, and release gate enforcement.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 1.9.4 | 2026-02-25T06:44:15.503849Z | [https://pypi.org/pypi/Bandit/json](https://pypi.org/pypi/Bandit/json) |  |
| preview/nightly | unknown |  |  | unknown | pypi_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `security_sast` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://pypi.org/pypi/Bandit/json` at `2026-09-01T01:59:27+00:00`.
- Preview/nightly metadata is unknown because `pypi_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-a79639752378` from `master_json` as `security_sast`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| Semgrep | Security Sast | [open](python-semgrep-35add980.md) |
