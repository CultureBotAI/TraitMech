# METPO ROBOT Template Proposal - DS-32 System (v332, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-32 system, the
genome-level possession trait for the two-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `NADR`
to DS-32, marked the cloned transcriptional unit as defensive, and measured
reduced Bas26 bacteriophage plaquing. The final Science Table S8 maps `NADR`
to the replicated DS-32 display name and reports lower-probability RecR plus
high-probability PRTase and NADAR HHpred rows for the DS-32 products. The
pinned DefenseFinder article registry maps DS-32 to the DefensePredictor
preprint, the pinned DefenseFinder HMM inventory records two DS-32 custom
profiles, `DS-32__DS-32A` and `DS-32__DS-32B`, and the pinned DefenseFinder
rules table checked in this curation pass has no DS-32 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-32 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040900` is reserved for this one-row class cohort. The v331 cohort
used `METPO:1040800`, so v332 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-32 TraitMech, METPO, history,
or prior proposal record, no `DS-32__DS-32A` or `DS-32__DS-32B` profile-key
mention, no `NZ_QOXQ01000027.1` contig mention, no `WP_000097610.1` or
`WP_032260665.1` product-accession mention, no `ds_32_system` slug, no
`traitmech:000455`, no `metpo_traitmech_v332`, and no `METPO:1040900`
proposal block. The `NADR` source working identifier appeared only inside
Table S7 screen-plate filenames on neighboring DS-1, DS-3, and DS-7 records,
not as an existing DS-32 label, synonym, causal node, history target, or
proposal target.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040900` | DS-32 system | `METPO:1016300` phage defense system |

DS-32 system captures genome-level possession of the two-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
NADR and represented by two DefenseFinder DS-32 custom HMM-profile rows. It
excludes the NADR source working identifier, individual DS-32A and DS-32B genes
or proteins, the DS-32 HMM profile rows, cloned-transcriptional-unit plaquing
assays, RecR, PRTase, and NADAR HHpred-domain annotations, the absent DS-32
rule-level DefenseFinder model, unresolved DS-32 component activity and phage
readouts, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000455` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `NADR` is kept as a related synonym
because it names the source working identifier, and `DS-32__DS-32A` plus
`DS-32__DS-32B` are kept as related synonyms because they name DefenseFinder
profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-32` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000455` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000455` as traceability during the migration.

## Change Log

- v332, 2026-09: lifts `traitmech:000455 DS-32 system` into the
  `METPO:1040900` placeholder block.
