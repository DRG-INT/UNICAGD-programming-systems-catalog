# Pkg

## Identity

| Field | Value |
| --- | --- |
| Language branch | Julia |
| Category | Package Manager |
| Source type | package_manager |
| Verification | catalog_seed |
| Canonical URL | unknown |
| Source record ids | master-8cc54f2f2690 |

## System Engineer Summary

Julia standard package manager

## Operational Role

For a systems engineer, Pkg belongs in the Julia inventory as part of dependency acquisition,
lockfile policy, provenance control, and supply-chain monitoring.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | unknown |  |  | unknown | julia_registry_entry_missing |
| preview/nightly | unknown |  |  | unknown | julia_registry_entry_missing |

## Engineering Notes

- Treat category as `package_manager` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `julia_registry_entry_missing`.
- Preview/nightly metadata is unknown because `julia_registry_entry_missing`.
- No canonical URL is verified yet; resolve before using this as an authoritative dependency identity.

## Provenance

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| model_knowledge_seed | catalog_seed | 2026-09-01 | `{"as_of": "2026-09-01", "kind": "model_knowledge_seed", "status": "catalog_seed"}` |

## Evidence

Evidence records merged into this identity: `1`.

- `master-8cc54f2f2690` from `master_json` as `package_manager`

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| AMLPipelineBase | Package Manager | [open](julia-amlpipelinebase-0d521acf.md) |
| AssetRegistry | Package Manager | [open](julia-assetregistry-bef07843.md) |
| AutoMLPipeline | Package Manager | [open](julia-automlpipeline-450f8c8b.md) |
| AutoPkg | Package Manager | [open](julia-autopkg-55226f27.md) |
| BrkgaMpIpr | Package Manager | [open](julia-brkgampipr-d28e5cc1.md) |
| BumplessPipeDreams | Package Manager | [open](julia-bumplesspipedreams-70b9f0a5.md) |
| cargo_license_jll | Package Manager | [open](julia-cargo-license-jll-1b5aaed9.md) |
