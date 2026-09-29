# METPO ROBOT Template Proposal - DS-29 System (v330, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-29 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `HEP3`
to DS-29, marked the cloned transcriptional unit as defensive, and measured
reduced Bas60 bacteriophage plaquing. The final Science Table S8 maps `HEP3`
to the replicated DS-29 display name and reports a lower-probability HEPN-like
HHpred row for the DS-29 product. The pinned DefenseFinder article registry
maps DS-29 to the DefensePredictor preprint, the pinned DefenseFinder HMM
inventory records one DS-29 custom profile, `DS-29__DS-29`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-29 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-29 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040700` is reserved for this one-row class cohort. The v329 cohort
used `METPO:1040600`, so v330 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-29 TraitMech, METPO, history,
or prior proposal record, no `DS-29__DS-29` profile-key mention, no `HEP3`
source working identifier mention, no `WP_061089765.1` product-accession
mention, no `GCF_003892435.1` assembly mention, no `NZ_RRWI01000012.1` contig
mention, no `ds_29_system` slug, no `traitmech:000453`, no
`metpo_traitmech_v330`, and no `METPO:1040700` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040700` | DS-29 system | `METPO:1016300` phage defense system |

DS-29 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
HEP3 and represented by one DefenseFinder DS-29 custom HMM-profile row. It
excludes the HEP3 source working identifier, the individual DS-29 protein, the
DS-29 HMM profile row, cloned-transcriptional-unit plaquing assays, the
HEPN-like HHpred-domain annotation, the absent DS-29 rule-level DefenseFinder
model, unresolved component activity, unresolved phage breadth, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000453` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `HEP3` is kept as a related synonym
because it names the source working identifier, and `DS-29__DS-29` is kept as
a related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-29` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000453` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000453` as traceability during the migration.

## Change Log

- v330, 2026-09: lifts `traitmech:000453 DS-29 system` into the
  `METPO:1040700` placeholder block.
