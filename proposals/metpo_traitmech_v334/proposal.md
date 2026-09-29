# METPO ROBOT Template Proposal - DS-34 System (v334, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-34 system, the
genome-level possession trait for the two-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `CITO`
to DS-34, marked the cloned transcriptional unit as defensive, and measured
reduced Bas19 bacteriophage plaquing. The final Science Table S8 maps `CITO`
to the replicated DS-34 display name and reports high-probability phage
repressor and HTH HHpred rows for one DS-34 product. The pinned DefenseFinder
article registry maps DS-34 to the DefensePredictor preprint, the pinned
DefenseFinder HMM inventory records two DS-34 custom profiles,
`DS-34__DS-34A` and `DS-34__DS-34B`, and the pinned DefenseFinder rules table
checked in this curation pass has no DS-34 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-34 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041100` is reserved for this one-row class cohort. The v333 cohort
used `METPO:1041000`, so v334 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-34 TraitMech, METPO, history,
or prior proposal record, no `DS-34__DS-34A` or `DS-34__DS-34B` profile-key
mention, no `NZ_QOXN01000005.1` contig mention, no `WP_001589054.1` or
`WP_000377448.1` product-accession mention, no `ds_34_system` slug, no
`traitmech:000457`, no `metpo_traitmech_v334`, and no `METPO:1041100`
proposal block. The `CITO` source working identifier was also absent as an
existing DS-34 label, synonym, causal node, history target, or proposal target.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041100` | DS-34 system | `METPO:1016300` phage defense system |

DS-34 system captures genome-level possession of the two-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
CITO and represented by two DefenseFinder DS-34 custom HMM-profile rows. It
excludes the CITO source working identifier, individual DS-34A and DS-34B
genes or proteins, the DS-34 HMM profile rows, cloned-transcriptional-unit
plaquing assays, phage-repressor and HTH HHpred-domain annotations, the
absent DS-34 rule-level DefenseFinder model, unresolved DS-34 component
activity and phage readouts, and other DefensePredictor-discovered or
phage-defense systems.

`traitmech:000457` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `CITO` is kept as a related synonym
because it names the source working identifier, and `DS-34__DS-34A` plus
`DS-34__DS-34B` are kept as related synonyms because they name DefenseFinder
profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-34` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000457` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000457` as traceability during the migration.

## Change Log

- v334, 2026-09: lifts `traitmech:000457 DS-34 system` into the
  `METPO:1041100` placeholder block.
