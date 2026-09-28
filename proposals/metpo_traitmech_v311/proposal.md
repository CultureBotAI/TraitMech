# METPO ROBOT Template Proposal - DS-10 System (v311, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-10 system, the
genome-level possession trait for DefensePredictor-discovered system 10.
DeWeirdt et al. mapped the working identifier ZAPB to display name DS-10 and
marked the cloned single-gene transcriptional unit as defensive in E. coli
MG1655 plaquing assays. The pinned DefenseFinder HMM inventory records a custom
DS-10 row, while the pinned DefenseFinder rules table has no DS-10 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-10 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038800` is reserved for this one-row class cohort. The v310 cohort used
`METPO:1038700`, so v311 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-10 TraitMech, METPO, history,
or prior proposal record, no `ZAPB` working-identifier mention, no
`WP_087897267.1` product-accession mention, no `ds_10_system` slug, no
`traitmech:000434`, no `metpo_traitmech_v311`, and no `METPO:1038800`
proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038800` | DS-10 system | `METPO:1016300` phage defense system |

DS-10 system captures genome-level possession of the single-gene
DefensePredictor-discovered system represented by the validated ZAPB
transcriptional unit and by the DefenseFinder DS-10 HMM-profile row. It excludes
the individual DS-10 gene and protein, the ZAPB working identifier, individual
DefenseFinder HMM profile rows, source database rows naming one DS-10 model,
cloned-transcriptional-unit plaquing assays, the absent final Table S7 and
HHPred-domain rows, the absent DS-10 rule-level DefenseFinder model, unresolved
component activity, unresolved effector chemistry, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000434` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `ZAPB` is retained only as a related
source working identifier, and `DS-10__DS-10` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-10` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000434` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000434` as traceability during the migration.

## Change Log

- v311, 2026-09: lifts `traitmech:000434 DS-10 system` into the
  `METPO:1038800` block.
