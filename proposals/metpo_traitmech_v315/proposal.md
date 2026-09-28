# METPO ROBOT Template Proposal - DS-15 System (v315, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-15 system, the
genome-level possession trait for DefensePredictor-discovered system 15.
DeWeirdt et al. used the DS naming convention for validated transcriptional
units in the DefensePredictor study, the final Science supplementary Table S6
maps the defensive working transcriptional unit `AAA1` to DS-15, and final Table
S8 maps `AAA1` to the replicated DS-15 display name. The pinned DefenseFinder
article registry maps DS-15 to the DefensePredictor preprint, and the pinned
DefenseFinder HMM inventory records three DS-15 custom profiles,
`DS-15__DS-15A`, `DS-15__DS-15B`, and `DS-15__DS-15C`; the pinned
DefenseFinder rules table checked in this curation pass has no DS-15 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-15 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039200` is reserved for this one-row class cohort. The v314 cohort used
`METPO:1039100`, so v315 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-15 TraitMech, METPO, history,
or prior proposal record, no `DS-15__DS-15A`, `DS-15__DS-15B`, or
`DS-15__DS-15C` profile-key mention, no `ds_15_system` slug, no
`traitmech:000438`, no `metpo_traitmech_v315`, and no `METPO:1039200` proposal
block. It found the `10.1101/2025.01.08.631726` preprint DOI in existing
DS-series curation and proposal text, and found `AAA1` only in an existing
DS-12 Table S7 image filename; neither hit represented a same-scope DS-15
record or proposal.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039200` | DS-15 system | `METPO:1016300` phage defense system |

DS-15 system captures genome-level possession of the
DefensePredictor-discovered system 15 locus cataloged as AAA1 and represented by
the DefenseFinder DS-15A, DS-15B, and DS-15C custom HMM-profile rows. It
excludes the AAA1 working identifier, individual DS-15 genes and proteins,
individual DefenseFinder HMM profile rows, cloned-transcriptional-unit plaquing
assays, MinD ATPase and DUF6988 HHpred-domain annotations, the absent DS-15
rule-level DefenseFinder model, unresolved component activity, unresolved phage
readouts, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000438` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `AAA1` is kept as a related synonym
because it names the final Science working transcriptional unit, and
`DS-15__DS-15A`, `DS-15__DS-15B`, and `DS-15__DS-15C` are kept as related
synonyms because they name DefenseFinder profile keys rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-15` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000438` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000438` as traceability during the migration.

## Change Log

- v315, 2026-09: lifts `traitmech:000438 DS-15 system` into the
  `METPO:1039200` placeholder block.
