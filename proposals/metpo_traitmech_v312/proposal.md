# METPO ROBOT Template Proposal - DS-11 System (v312, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-11 system, the
genome-level possession trait for DefensePredictor-discovered system 11.
DeWeirdt et al. mapped the working identifier IMPD to display name DS-11 and
marked the cloned single-gene transcriptional unit as defensive in E. coli
MG1655 plaquing assays. The final Table S8 HHpred sheet reports HEPN and CBS
hits for the single IMPD product, the pinned DefenseFinder HMM inventory records
a custom DS-11 row, and the pinned DefenseFinder rules table has no DS-11 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-11 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038900` is reserved for this one-row class cohort. The v311 cohort used
`METPO:1038800`, so v312 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-11 TraitMech, METPO, history,
or prior proposal record, no `DS-11__DS-11` profile-key mention, no
`WP_000257686.1` product-accession mention, no `ds_11_system` slug, no
`traitmech:000435`, no `metpo_traitmech_v312`, and no `METPO:1038900`
proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038900` | DS-11 system | `METPO:1016300` phage defense system |

DS-11 system captures genome-level possession of the single-gene
DefensePredictor-discovered system represented by the validated IMPD
transcriptional unit and by the DefenseFinder DS-11 HMM-profile row. It excludes
the individual DS-11 gene and protein, the IMPD working identifier, individual
DefenseFinder HMM profile rows, source database rows naming one DS-11 model,
cloned-transcriptional-unit plaquing assays, HEPN/CBS HHPred-domain rows, IMPD
Y157A/R330A/H335A mutant-panel rows, the absent DS-11 rule-level DefenseFinder
model, unresolved component activity, unresolved effector chemistry, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000435` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `IMPD` is retained only as a related
source working identifier, and `DS-11__DS-11` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-11` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000435` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000435` as traceability during the migration.

## Change Log

- v312, 2026-09: lifts `traitmech:000435 DS-11 system` into the
  `METPO:1038900` block.
