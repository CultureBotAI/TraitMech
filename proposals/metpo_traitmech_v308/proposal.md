# METPO ROBOT Template Proposal - DS-7 System (v308, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v307 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-7 system, the
genome-level possession trait for DefensePredictor-discovered system 7.
DeWeirdt et al. mapped the working identifier SVIR to display name DS-7 and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The final Science supplementary tables include wild-type
SVIR and SVIR H52A Bas60 mutant assays. The pinned DefenseFinder
HMM inventory records one custom DS-7 row, while the pinned DefenseFinder
rules table has no DS-7 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-7 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038500` is reserved for this one-row class cohort. The v307 cohort used
`METPO:1038400`, so v308 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus and pinned METPO OWL. It found no exact same-scope DS-7
TraitMech, METPO, history, or prior proposal record, no exact `WP_225403053.1`
product-accession mention, no `NZ_QOYF01000007.1` contig mention, no
`GCF_003334585.1` assembly mention, no `ds_7_system` slug, no
`traitmech:000431`, no `metpo_traitmech_v308`, and no `METPO:1038500` /
`METPO:10385xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038500` | DS-7 system | `METPO:1016300` phage defense system |

DS-7 system captures genome-level possession of the single-gene
DefensePredictor-discovered system represented by the validated SVIR
transcriptional unit and by the DefenseFinder DS-7 HMM-profile row. It
excludes the individual DS-7 gene and protein, the SVIR working identifier,
the DefenseFinder HMM profile row, Table S8 HHpred domain-annotation rows,
cloned-transcriptional-unit plaquing assays, the absent DS-7 rule-level
DefenseFinder model, unresolved HNH endonuclease activity and
phage-baseplate-like hit, and other DefensePredictor-discovered or
phage-defense systems.

`traitmech:000431` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `SVIR` is retained only as a related
source working identifier, and `DS-7__DS-7` is kept as a related synonym
because it names a DefenseFinder profile key rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-7` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000431` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000431` as traceability during the migration.

## Change Log

- v308, 2026-09: lifts `traitmech:000431 DS-7 system` into the
  `METPO:1038500` block.
