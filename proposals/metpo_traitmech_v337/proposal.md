# METPO ROBOT Template Proposal - DS-38 System (v337, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-38 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `HEP2`
to DS-38, marked the cloned transcriptional unit as defensive, and measured
reduced Bas25 and Bas19 bacteriophage plaquing. The final Science Table S8 maps
`HEP2` to the replicated DS-38 display name and reports high-probability HEPN
and zinc-finger HHpred rows for the HEP2 product. The pinned DefenseFinder
article registry maps DS-38 to the DefensePredictor preprint, the pinned
DefenseFinder HMM inventory records one DS-38 custom profile, `DS-38__DS-38`,
and the pinned DefenseFinder rules table checked in this curation pass has no
DS-38 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-38 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041400` is reserved for this one-row class cohort. The v336 cohort
used `METPO:1041300`, so v337 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-38 TraitMech, METPO, history,
or prior proposal record, no `DS-38__DS-38` profile-key mention, no
`NZ_QOYR01000034.1` contig mention, no `WP_001313577.1` product-accession
mention, no `ds_38_system` slug, no `traitmech:000460`, no
`metpo_traitmech_v337`, and no `METPO:1041400` proposal block. The `HEP2`
source working identifier was only reviewed in the final Science workbooks
before minting this first TraitMech record.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041400` | DS-38 system | `METPO:1016300` phage defense system |

DS-38 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
HEP2 and represented by one DefenseFinder DS-38 custom HMM-profile row. It
excludes the HEP2 source working identifier, the individual DS-38 gene or
protein, the DS-38 HMM profile row, cloned-transcriptional-unit plaquing
assays, high-probability HEPN and zinc-finger HHpred-domain annotations, the
absent DS-38 rule-level DefenseFinder model, unresolved DS-38 component
activity and phage readouts, and other DefensePredictor-discovered or
phage-defense systems.

`traitmech:000460` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `HEP2` is kept as a related synonym
because it names the source working identifier, and `DS-38__DS-38` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-38` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000460` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000460` as traceability during the migration.

## Change Log

- v337, 2026-09: lifts `traitmech:000460 DS-38 system` into the
  `METPO:1041400` placeholder block.
