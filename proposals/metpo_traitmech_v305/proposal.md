# METPO ROBOT Template Proposal - DS-5 System (v305, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v304 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-5 system, the
genome-level possession trait for DefensePredictor-discovered system 5.
DeWeirdt et al. mapped the working identifier PN12 to display name DS-5,
identified DS-5 as a two-protein system with a PIN ribonuclease and a DUF5830
/ AcrIF4-like component, and experimentally validated the cloned
transcriptional unit in E. coli MG1655 plaquing assays. The pinned
DefenseFinder HMM inventory records two custom DS-5 rows, while the pinned
DefenseFinder rules table has no DS-5 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-5 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038200` is reserved for this one-row class cohort. The v304 cohort used
`METPO:1038100`, so v305 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-5 TraitMech, METPO, history,
or prior proposal record, no exact `PN12` working-identifier record, no
`WP_021513008.1` or `WP_021513009.1` product-accession mention, no
`NZ_QOYG01000008.1` contig mention, no `ds_5_system` slug, no
`traitmech:000428`, no `metpo_traitmech_v305`, and no `METPO:1038200` /
`METPO:10382xx` proposal block. The only prior `PN12` mentions were Science
Table S7 plate-filename strings quoted in existing DS-1, DS-3, and DS-4
records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038200` | DS-5 system | `METPO:1016300` phage defense system |

DS-5 system captures genome-level possession of the two-gene
DefensePredictor-discovered system represented by the validated PN12
transcriptional unit and by DefenseFinder DS-5 HMM-profile rows. It excludes
the individual DS-5 genes and proteins, the PIN and DUF5830 / AcrIF4-like
domain annotations, the PN12 working identifier, individual DefenseFinder HMM
profile rows, cloned-transcriptional-unit plaquing assays, the absent DS-5
rule-level DefenseFinder model, unresolved DS-5 PIN nuclease chemistry and
AcrIF4-like component activity, and other DefensePredictor-discovered or
phage-defense systems.

`traitmech:000428` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PN12` is retained only as a related
source working identifier, and `DS-5__DS-5A` and `DS-5__DS-5B` are kept as
related synonyms because they name DefenseFinder profile keys rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-5` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000428` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000428` as traceability during the migration.

## Change Log

- v305, 2026-09: lifts `traitmech:000428 DS-5 system` into the
  `METPO:1038200` block.
