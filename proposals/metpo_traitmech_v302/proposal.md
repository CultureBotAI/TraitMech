# METPO ROBOT Template Proposal - DS-2 System (v302, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v301 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-2 system, the
genome-level possession trait for DefensePredictor-discovered system 2.
DeWeirdt et al. mapped the working identifier DISA to display name DS-2 and
experimentally validated the cloned three-gene transcriptional unit in E. coli
MG1655 plaquing assays. The pinned DefenseFinder HMM inventory records a
custom DS-2C row, while the pinned DefenseFinder rules table has no DS-2 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-2 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037900` is reserved for this one-row class cohort. The v301 cohort used
`METPO:1037800`, so v302 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-2 TraitMech, METPO, history,
or prior proposal record, no `DISA` working-identifier mention, no
`WP_016240614.1`, `WP_016240615.1`, or `WP_001593459.1` product-accession
mention, no `ds_2_system` slug, no `traitmech:000425`, no
`metpo_traitmech_v302`, and no `METPO:1037900` / `METPO:10379xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037900` | DS-2 system | `METPO:1016300` phage defense system |

DS-2 system captures genome-level possession of the three-gene
DefensePredictor-discovered system represented by the validated DISA
transcriptional unit and by a DefenseFinder DS-2C HMM-profile row. It excludes
the individual DS-2 genes and proteins, the DISA working identifier, individual
DefenseFinder HMM profile rows, source database rows naming one DS-2 model,
cloned-transcriptional-unit plaquing assays, the absent DS-2 rule-level
DefenseFinder model, unresolved component functions, unresolved effector
chemistry, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000425` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `DISA` is retained only as a related
source working identifier, and `DS-2__DS-2C` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-2` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000425` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000425` as traceability during the migration.

## Change Log

- v302, 2026-09: lifts `traitmech:000425 DS-2 system` into the
  `METPO:1037900` block.
