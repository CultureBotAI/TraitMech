# METPO ROBOT Template Proposal - DS-31 System (v331, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-31 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `RED7`
to DS-31, marked the cloned transcriptional unit as defensive, and measured
reduced Bas19 bacteriophage plaquing. The final Science Table S8 maps `RED7`
to the replicated DS-31 display name and reports a high-probability PDDEXK
HHpred row for the DS-31 product. The pinned DefenseFinder article registry
maps DS-31 to the DefensePredictor preprint, the pinned DefenseFinder HMM
inventory records one DS-31 custom profile, `DS-31__DS-31`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-31 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-31 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040800` is reserved for this one-row class cohort. The v330 cohort
used `METPO:1040700`, so v331 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-31 TraitMech, METPO, history,
or prior proposal record, no `DS-31__DS-31` profile-key mention, no `RED7`
source working identifier mention outside DS-19 source image filenames, no
`WP_001703029.1` product-accession mention, no `GCF_003334245.1` assembly
mention, no `NZ_QOWW01000064.1` contig mention, no `ds_31_system` slug, no
`traitmech:000454`, no `metpo_traitmech_v331`, and no `METPO:1040800`
proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040800` | DS-31 system | `METPO:1016300` phage defense system |

DS-31 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
RED7 and represented by one DefenseFinder DS-31 custom HMM-profile row. It
excludes the RED7 source working identifier, the individual DS-31 protein, the
DS-31 HMM profile row, cloned-transcriptional-unit plaquing assays, the PDDEXK
HHpred-domain annotation, the absent DS-31 rule-level DefenseFinder model,
unresolved component activity, unresolved phage breadth, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000454` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `RED7` is kept as a related synonym
because it names the source working identifier, and `DS-31__DS-31` is kept as
a related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-31` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000454` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000454` as traceability during the migration.

## Change Log

- v331, 2026-09: lifts `traitmech:000454 DS-31 system` into the
  `METPO:1040800` placeholder block.
