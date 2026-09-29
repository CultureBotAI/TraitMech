# METPO ROBOT Template Proposal - DS-33 System (v333, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-33 system, the
genome-level possession trait for the two-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `GNAT`
to DS-33, marked the cloned transcriptional unit as defensive, and measured
reduced Bas26 bacteriophage plaquing. The final Science Table S8 maps `GNAT`
to the replicated DS-33 display name and reports lower-probability Csa3 plus
high-probability HEPN HHpred rows for the DS-33 products. The pinned
DefenseFinder article registry maps DS-33 to the DefensePredictor preprint,
the pinned DefenseFinder HMM inventory records one DS-33 custom profile,
`DS-33__DS-33`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-33 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-33 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041000` is reserved for this one-row class cohort. The v332 cohort
used `METPO:1040900`, so v333 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-33 TraitMech, METPO, history,
or prior proposal record, no `DS-33__DS-33` profile-key mention, no
`NZ_QOWT01000046.1` contig mention, no `WP_014639476.1` or `WP_000354965.1`
product-accession mention, no `ds_33_system` slug, no `traitmech:000456`, no
`metpo_traitmech_v333`, and no `METPO:1041000` proposal block. The `GNAT`
source working identifier appeared only inside vendored Python package SPDX
license data as the unrelated `GNAT-exception` string, not as an existing
DS-33 label, synonym, causal node, history target, or proposal target.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041000` | DS-33 system | `METPO:1016300` phage defense system |

DS-33 system captures genome-level possession of the two-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
GNAT and represented by one DefenseFinder DS-33 custom HMM-profile row. It
excludes the GNAT source working identifier, individual DS-33 genes or
proteins, the DS-33 HMM profile row, cloned-transcriptional-unit plaquing
assays, Csa3 and HEPN HHpred-domain annotations, the absent DS-33 rule-level
DefenseFinder model, unresolved DS-33 component activity and phage readouts,
and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000456` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `GNAT` is kept as a related synonym
because it names the source working identifier, and `DS-33__DS-33` is kept as
a related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-33` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000456` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000456` as traceability during the migration.

## Change Log

- v333, 2026-09: lifts `traitmech:000456 DS-33 system` into the
  `METPO:1041000` placeholder block.
