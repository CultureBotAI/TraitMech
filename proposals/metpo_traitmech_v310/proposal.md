# METPO ROBOT Template Proposal - DS-9 System (v310, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v309 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-9 system, the
genome-level possession trait for DefensePredictor-discovered system 9.
DeWeirdt et al. mapped the working identifier MHAD to display name DS-9 and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The final Science supplementary tables report HAD
phosphatase and metallophosphatase HHpred rows for the two MHAD products, and
the article/Table S7 mutant assays indicate that D207A and N292A mutations
reduce Bas1 protection. The pinned DefenseFinder HMM inventory records custom
DS-9A and DS-9B rows, while the pinned DefenseFinder rules table has no DS-9
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-9 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038700` is reserved for this one-row class cohort. The v309 cohort used
`METPO:1038600`, so v310 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus and pinned METPO OWL. It found no exact same-scope DS-9
TraitMech, METPO, history, or prior proposal record, no exact `WP_000770925.1`
or `WP_000665639.1` product-accession mention, no `NZ_QOWZ01000056.1` contig
mention, no `GCF_003334705.1` assembly mention, no `ds_9_system` slug, no
`traitmech:000433`, no `metpo_traitmech_v310`, and no `METPO:1038700` /
`METPO:10387xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038700` | DS-9 system | `METPO:1016300` phage defense system |

DS-9 system captures genome-level possession of the two-gene
DefensePredictor-discovered system represented by the validated MHAD
transcriptional unit and by the DefenseFinder DS-9A and DS-9B HMM-profile rows.
It excludes the MHAD source working identifier, the individual DS-9 genes and
proteins, the DS-9 HMM profiles, Table S8 HAD phosphatase and
metallophosphatase HHpred domain rows, cloned-TU plaquing assays, the absent
DefenseFinder rule-level model, the unresolved direct metallophosphoesterase
substrate and HAD phosphatase target, and other DS/phage-defense systems.

`traitmech:000433` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `MHAD` is retained only as a related
source working identifier, and `DS-9__DS-9A` and `DS-9__DS-9B` are kept as
related synonyms because they name DefenseFinder profile keys rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-9` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000433` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000433` as traceability during the migration.

## Change Log

- v310, 2026-09: lifts `traitmech:000433 DS-9 system` into the
  `METPO:1038700` block.
