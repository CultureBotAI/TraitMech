# METPO ROBOT Template Proposal - DS-14 System (v306, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v305 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-14 system, the
genome-level possession trait for DefensePredictor-discovered system 14.
DeWeirdt et al. mapped the working identifier RMOR to display name DS-14 and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The pinned DefenseFinder HMM inventory records one custom
DS-14 row, while the pinned DefenseFinder rules table has no DS-14 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-14 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038300` is reserved for this one-row class cohort. The v305 cohort used
`METPO:1038200`, so v306 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-14 TraitMech, METPO, history,
or prior proposal record, no exact `RMOR` working-identifier record, no
`WP_040091717.1` product-accession mention, no `NZ_QOZC01000013.1` contig
mention, no `GCF_003333475.1` assembly mention, no `ds_14_system` slug, no
`traitmech:000429`, no `metpo_traitmech_v306`, and no `METPO:1038300` /
`METPO:10383xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038300` | DS-14 system | `METPO:1016300` phage defense system |

DS-14 system captures genome-level possession of the single-gene
DefensePredictor-discovered system represented by the validated RMOR
transcriptional unit and by the DefenseFinder DS-14 HMM-profile row. It
excludes the individual DS-14 gene and protein, the RMOR working identifier,
the individual DefenseFinder HMM profile row, cloned-transcriptional-unit
plaquing assays, the absent DS-14 rule-level DefenseFinder model, unresolved
DS-14 AAA+ ATPase and PDDEXK nuclease chemistry, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000429` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `RMOR` is retained only as a related
source working identifier, and `DS-14__DS-14` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-14` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000429` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000429` as traceability during the migration.

## Change Log

- v306, 2026-09: lifts `traitmech:000429 DS-14 system` into the
  `METPO:1038300` block.
