# METPO ROBOT Template Proposal - DS-37 System (v336, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-37 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `SC24`
to DS-37, marked the cloned transcriptional unit as defensive, and measured
reduced Bas1 and Bas9 bacteriophage plaquing. The final Science Table S8 maps
`SC24` to the replicated DS-37 display name and reports a low-probability
PDDEXK HHpred row for the SC24 product. The pinned DefenseFinder article
registry maps DS-37 to the DefensePredictor preprint, the pinned DefenseFinder
HMM inventory records one DS-37 custom profile, `DS-37__DS-37`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-37 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-37 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041300` is reserved for this one-row class cohort. The v335 cohort
used `METPO:1041200`, so v336 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-37 TraitMech, METPO, history,
or prior proposal record, no `DS-37__DS-37` profile-key mention, no
`NZ_QOXM01000003.1` contig mention, no `WP_000982358.1` product-accession
mention, no `ds_37_system` slug, no `traitmech:000459`, no
`metpo_traitmech_v336`, and no `METPO:1041300` proposal block. The `SC24`
source working identifier appeared only in neighboring DS-18 Science Table S7
screen-plate filenames, not as a trait label, synonym, causal node, history
target, or proposal target.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041300` | DS-37 system | `METPO:1016300` phage defense system |

DS-37 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
SC24 and represented by one DefenseFinder DS-37 custom HMM-profile row. It
excludes the SC24 source working identifier, the individual DS-37 gene or
protein, the DS-37 HMM profile row, cloned-transcriptional-unit plaquing
assays, low-probability PDDEXK HHpred-domain annotations, the absent DS-37
rule-level DefenseFinder model, unresolved DS-37 component activity and phage
readouts, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000459` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `SC24` is kept as a related synonym
because it names the source working identifier, and `DS-37__DS-37` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-37` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000459` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000459` as traceability during the migration.

## Change Log

- v336, 2026-09: lifts `traitmech:000459 DS-37 system` into the
  `METPO:1041300` placeholder block.
