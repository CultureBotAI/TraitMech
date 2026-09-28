# METPO ROBOT Template Proposal - DS-8 System (v309, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v308 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-8 system, the
genome-level possession trait for DefensePredictor-discovered system 8.
DeWeirdt et al. mapped the working identifier MNAC to display name DS-8 and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The final Science supplementary tables report
metallophosphatase and NACHT HHpred rows for the DS-8 product, and the
article/Table S7 mutant assays indicate that D52A, N84A, and K375A mutations
ablate Bas1 protection. The pinned DefenseFinder HMM inventory records one
custom DS-8 row, while the pinned DefenseFinder rules table has no DS-8 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-8 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038600` is reserved for this one-row class cohort. The v308 cohort used
`METPO:1038500`, so v309 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus and pinned METPO OWL. It found no exact same-scope DS-8
TraitMech, METPO, history, or prior proposal record, no exact `WP_032203427.1`
product-accession mention, no `NZ_RRWS01000004.1` contig mention, no
`GCF_003892555.1` assembly mention, no `ds_8_system` slug, no
`traitmech:000432`, no `metpo_traitmech_v309`, and no `METPO:1038600` /
`METPO:10386xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038600` | DS-8 system | `METPO:1016300` phage defense system |

DS-8 system captures genome-level possession of the single-gene
DefensePredictor-discovered system represented by the validated MNAC
transcriptional unit and by the DefenseFinder DS-8 HMM-profile row. It
excludes the MNAC source working identifier, the individual DS-8 gene and
protein, the DS-8 HMM profile, Table S8 Metallophosphatase and NACHT HHpred
domain rows, cloned-TU plaquing assays, the absent DefenseFinder rule-level
model, the unresolved DS-8 cyclic nucleotide substrate and NACHT-mediated
activation route, the unresolved relationship to NLR-like bNACHT systems, and
other DS/phage-defense systems.

`traitmech:000432` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `MNAC` is retained only as a related
source working identifier, and `DS-8__DS-8` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-8` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000432` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000432` as traceability during the migration.

## Change Log

- v309, 2026-09: lifts `traitmech:000432 DS-8 system` into the
  `METPO:1038600` block.
