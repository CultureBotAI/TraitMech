# METPO ROBOT Template Proposal - DS-3 System (v303, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v302 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-3 system, the
genome-level possession trait for DefensePredictor-discovered system 3.
DeWeirdt et al. mapped the working identifier PIN8 to display name DS-3,
identified DS-3 as a one-protein PIN-ribonuclease-domain system, and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The pinned DefenseFinder HMM inventory records a custom DS-3
row, while the pinned DefenseFinder rules table has no DS-3 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-3 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038000` is reserved for this one-row class cohort. The v302 cohort used
`METPO:1037900`, so v303 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-3 TraitMech, METPO, history,
or prior proposal record, no exact `PIN8` working-identifier record, no
`WP_022645725.1` product-accession mention, no `NZ_RRWT01000005.1` contig
mention, no `ds_3_system` slug, no `traitmech:000426`, no
`metpo_traitmech_v303`, and no `METPO:1038000` / `METPO:10380xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038000` | DS-3 system | `METPO:1016300` phage defense system |

DS-3 system captures genome-level possession of the one-gene
DefensePredictor-discovered system represented by the validated PIN8
transcriptional unit and by a DefenseFinder DS-3 HMM-profile row. It excludes
the individual DS-3 gene and protein, the PIN8 working identifier, individual
DefenseFinder HMM profile rows, source database rows naming one DS-3 model,
cloned-transcriptional-unit plaquing assays, the absent DS-3 rule-level
DefenseFinder model, unresolved PIN nuclease chemistry, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000426` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PIN8` is retained only as a related
source working identifier, and `DS-3__DS-3` is kept as a related synonym because
it names a DefenseFinder profile key rather than the genome-level possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-3` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000426` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000426` as traceability during the migration.

## Change Log

- v303, 2026-09: lifts `traitmech:000426 DS-3 system` into the
  `METPO:1038000` block.
