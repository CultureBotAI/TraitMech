# METPO ROBOT Template Proposal - DS-39 System (v338, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-39 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `AAA5`
to DS-39, marked the cloned transcriptional unit as defensive, and measured
reduced Bas1 and Bas3 bacteriophage plaquing. The final Science Table S8 maps
`AAA5` to the replicated DS-39 display name and reports high-probability AAA+
ATPase and HTH HHpred rows plus a moderate-probability zinc-finger HHpred row
for the AAA5 product. The pinned DefenseFinder article registry maps DS-39 to
the DefensePredictor preprint, the pinned DefenseFinder HMM inventory records
one DS-39 custom profile, `DS-39__DS-39`, and the pinned DefenseFinder rules
table checked in this curation pass has no DS-39 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-39 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041500` is reserved for this one-row class cohort. The v337 cohort
used `METPO:1041400`, so v338 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-39 TraitMech, METPO, history,
or prior proposal record, no `DS-39__DS-39` profile-key mention, no
`NZ_RRWS01000024.1` contig mention, no `WP_042346724.1` product-accession
mention, no `ds_39_system` slug, no `traitmech:000461`, no
`metpo_traitmech_v338`, and no `METPO:1041500` proposal block. The `AAA5`
source working identifier was only reviewed in the final Science workbooks
before minting this first TraitMech record.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041500` | DS-39 system | `METPO:1016300` phage defense system |

DS-39 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
AAA5 and represented by one DefenseFinder DS-39 custom HMM-profile row. It
excludes the AAA5 source working identifier, the individual DS-39 gene or
protein, the DS-39 HMM profile row, cloned-transcriptional-unit plaquing
assays, high-probability AAA+ ATPase and HTH HHpred-domain annotations,
moderate-probability zinc-finger HHpred-domain annotations, the absent DS-39
rule-level DefenseFinder model, unresolved DS-39 component activity and phage
readouts, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000461` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `AAA5` is kept as a related synonym
because it names the source working identifier, and `DS-39__DS-39` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-39` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000461` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000461` as traceability during the migration.

## Change Log

- v338, 2026-09: lifts `traitmech:000461 DS-39 system` into the
  `METPO:1041500` placeholder block.
