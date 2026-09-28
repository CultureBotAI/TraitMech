# METPO ROBOT Template Proposal - DS-12 System (v313, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-12 system, the
genome-level possession trait for DefensePredictor-discovered system 12.
DeWeirdt et al. mapped the working identifier PD3A to display name DS-12 and
marked the cloned two-gene transcriptional unit as defensive in E. coli MG1655
plaquing assays. The final Table S8 HHpred sheet reports ABC ATPase, PDDEXK,
and NACHT hits across the two PD3A products, the pinned DefenseFinder HMM
inventory records a custom DS-12B row, the pinned DefenseFinder article
registry names DS-12B, and the pinned DefenseFinder rules table has no DS-12
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-12 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039000` is reserved for this one-row class cohort. The v312 cohort used
`METPO:1038900`, so v313 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-12 TraitMech, METPO, history,
or prior proposal record, no `PD3A` working-identifier mention, no
`DS-12__DS-12B` profile-key mention, no `WP_059339975.1` or
`WP_064766070.1` product-accession mention, no `ds_12_system` slug, no
`traitmech:000436`, no `metpo_traitmech_v313`, and no `METPO:1039000`
proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039000` | DS-12 system | `METPO:1016300` phage defense system |

DS-12 system captures genome-level possession of the two-gene
DefensePredictor-discovered system represented by the validated PD3A
transcriptional unit and by the DefenseFinder DS-12B HMM-profile row. It
excludes the individual DS-12 genes and proteins, the PD3A working identifier,
individual DefenseFinder HMM profile rows, source database rows naming one
DS-12B model component, cloned-transcriptional-unit plaquing assays, ABC
ATPase, PDDEXK, and NACHT HHpred-domain rows, the absent DS-12A and rule-level
DefenseFinder model coverage, unresolved component activity, unresolved
effector chemistry, and other DefensePredictor-discovered or phage-defense
systems.

`traitmech:000436` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PD3A` is retained only as a related
source working identifier, and `DS-12__DS-12B` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-12` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000436` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000436` as traceability during the migration.

## Change Log

- v313, 2026-09: lifts `traitmech:000436 DS-12 system` into the
  `METPO:1039000` placeholder block.
