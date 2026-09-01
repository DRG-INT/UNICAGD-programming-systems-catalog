# PyPI

## Identity

| Field | Value |
| --- | --- |
| Language branch | Python |
| Category | Registry Repository |
| Source type | registry_repository |
| Verification | catalog_seed |
| Canonical URL | [https://pypi.org/project/pypi/](https://pypi.org/project/pypi/) |
| Source record ids | master-25142da409d7 |

## System Engineer Summary

PyPI is tracked as a registry repository record in the Python branch. The source did not provide a
long description, so this page keeps the identity, release state, provenance, and operational
classification explicit for later enrichment.

## Operational Role

For a systems engineer, PyPI belongs in the Python inventory as part of ecosystem capability
mapping, dependency review, release awareness, and operational fit assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | known | 2.1 | 2018-03-24T22:31:13.968518Z | [https://pypi.org/pypi/PyPI/json](https://pypi.org/pypi/PyPI/json) |  |
| preview/nightly | unknown |  |  | unknown | pypi_has_no_standard_nightly_channel |

## Engineering Notes

- Treat category as `registry_repository` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Latest stable metadata was observed from `https://pypi.org/pypi/PyPI/json` at `2026-09-01T01:59:27+00:00`.
- Preview/nightly metadata is unknown because `pypi_has_no_standard_nightly_channel`.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-25142da409d7` from `master_json` as `registry_repository`
