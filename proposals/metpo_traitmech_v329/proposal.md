# METPO ROBOT Template Proposal - DS-28 System (v329, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-28 system, the
genome-level possession trait for the two-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `ANEX` to DS-28, marked the cloned
transcriptional unit as defensive, and measured reduced Bas60 bacteriophage
plaquing. The final Science Table S8 maps `ANEX` to the replicated DS-28
display name and reports a high-probability HEPN HHpred row plus a
lower-probability TF HHpred row. The pinned DefenseFinder article registry maps
DS-28 to the DefensePredictor preprint, the pinned DefenseFinder HMM inventory
records two DS-28 custom profiles, `DS-28__DS-28A` and `DS-28__DS-28B`, and the
pinned DefenseFinder rules table checked in this curation pass has no DS-28
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-28 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040600` is reserved for this one-row class cohort. The v328 cohort used
`METPO:1040500`, so v329 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-28 TraitMech, METPO, history,
or prior proposal record, no `DS-28__DS-28A` or `DS-28__DS-28B` profile-key
mention, no `ANEX` source working identifier mention, no `WP_000494510.1` or
`WP_000528930.1` product-accession mention, no `NZ_RRWS01000106.1` contig
mention, no `ds_28_system` slug, no `traitmech:000452`, no
`metpo_traitmech_v329`, and no `METPO:1040600` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040600` | DS-28 system | `METPO:1016300` phage defense system |

DS-28 system captures genome-level possession of the two-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
ANEX and represented by two DefenseFinder DS-28 custom HMM-profile rows. It
excludes the ANEX source working identifier, individual DS-28A and DS-28B genes
or proteins, the DS-28 HMM profile rows, cloned-transcriptional-unit plaquing
assays, HEPN and transcription-factor HHpred-domain rows, the absent DS-28
rule-level DefenseFinder model, unresolved component activity, unresolved phage
breadth, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000452` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `ANEX` is kept as a related synonym
because it names the source working identifier, and `DS-28__DS-28A` plus
`DS-28__DS-28B` are kept as related synonyms because they name DefenseFinder
profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-28` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000452` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000452` as traceability during the migration.

## Change Log

- v329, 2026-09: lifts `traitmech:000452 DS-28 system` into the
  `METPO:1040600` placeholder block.
