# METPO ROBOT Template Proposal - DS-1 System (v301, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v300 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-1 system, the
genome-level possession trait for DefensePredictor-discovered system 1.
DeWeirdt et al. mapped the working identifier D390 to display name DS-1 and
experimentally validated the cloned two-gene transcriptional unit in E. coli
MG1655 plaquing assays. The pinned DefenseFinder HMM inventory records custom
DS-1A and DS-1B rows, while the pinned DefenseFinder rules table has no DS-1
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037800` is reserved for this one-row class cohort. The v300 cohort used
`METPO:1037700`, so v301 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-1 TraitMech, METPO, history,
or prior proposal record, no `D390` working-identifier mention, no
`WP_000355468.1` or `WP_000150292.1` product-accession mention, no
`10.1126/science.adv7924` or `10.1101/2025.01.08.631726` citation, no
`ds_1_system` slug, no `traitmech:000424`, no `metpo_traitmech_v301`, and no
`METPO:1037800` / `METPO:10378xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037800` | DS-1 system | `METPO:1016300` phage defense system |

DS-1 system captures genome-level possession of the two-gene
DefensePredictor-discovered system represented by the validated D390
transcriptional unit and by DefenseFinder DS-1A and DS-1B HMM-profile rows. It
excludes the individual DS-1A or DS-1B genes and proteins, the D390 working
identifier, individual DefenseFinder HMM profile rows, source database rows
naming one DS-1 model, cloned-transcriptional-unit plaquing assays, the absent
DS-1 rule-level DefenseFinder model, unresolved component functions, unresolved
effector chemistry, and other DefensePredictor-discovered or phage-defense
systems.

`traitmech:000424` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `D390` is retained only as a related
source working identifier, and individual `DS-1__*` HMM row names are kept as
related synonyms because they name DefenseFinder profile keys rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-1` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000424` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000424` as traceability during the migration.

## Change Log

- v301, 2026-09: lifts `traitmech:000424 DS-1 system` into the
  `METPO:1037800` block.
