# METPO ROBOT Template Proposal - DS-36 System (v351, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-36 system, the
genome-level possession trait for DefensePredictor-discovered system 36.
DeWeirdt et al. used the DS naming convention for validated transcriptional
units in the DefensePredictor preprint, and the pinned DefenseFinder article
registry maps DS-36 to that preprint. The pinned DefenseFinder HMM inventory
records a DS-36 custom profile, `DS-36__DS-36`, while the final Science Table
S6/S7/S8 files and the pinned DefenseFinder rules table checked in this
curation pass have no DS-36 rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-36 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042800` is reserved for this one-row class cohort. The v350 cohort used
`METPO:1042700`, so v351 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-36 TraitMech, METPO, history,
or prior proposal record, no `DS-36__DS-36` profile-key mention, no
`ds_36_system` slug, no `traitmech:000474`, no `metpo_traitmech_v351`, and no
`METPO:1042800` proposal block. It found the
`10.1101/2025.01.08.631726` preprint DOI only in earlier DS-series records and
proposal text that introduced DeWeirdt et al. evidence.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042800` | DS-36 system | `METPO:1016300` phage defense system |

DS-36 system captures genome-level possession of the
DefensePredictor-discovered system 36 locus represented by the DefenseFinder
DS-36 custom HMM-profile row. It excludes the individual DS-36 gene and
protein, the DefenseFinder HMM profile row, preprint Table S5/S6 rows,
cloned-transcriptional-unit plaquing assays, the absent final Science Table
S6/S7/S8 rows, the absent DS-36 rule-level DefenseFinder model, unresolved
component activity, unresolved phage readouts, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000474` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `DS-36__DS-36` is kept as a related
synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-36` synonym and related source/profile key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000474` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000474` as traceability during the migration.

## Change Log

- v351, 2026-09: lifts `traitmech:000474 DS-36 system` into the
  `METPO:1042800` placeholder block.
