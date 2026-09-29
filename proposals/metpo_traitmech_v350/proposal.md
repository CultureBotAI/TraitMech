# METPO ROBOT Template Proposal - DS-25 System (v350, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-25 system, the
genome-level possession trait for DefensePredictor-discovered system 25.
DeWeirdt et al. used the DS naming convention for validated transcriptional
units in the DefensePredictor preprint, and the pinned DefenseFinder article
registry maps DS-25 to that preprint. The pinned DefenseFinder HMM inventory
records two DS-25 custom profiles, `DS-25__DS-25A` and `DS-25__DS-25B`, while
the final Science Table S6/S7/S8 files and the pinned DefenseFinder rules table
checked in this curation pass have no DS-25 rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-25 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042700` is reserved for this one-row class cohort. The v349 cohort used
`METPO:1042600`, so v350 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-25 TraitMech, METPO, history,
or prior proposal record, no `DS-25__DS-25A` or `DS-25__DS-25B` profile-key
mention, no `ds_25_system` slug, no `traitmech:000473`, no
`metpo_traitmech_v350`, and no `METPO:1042700` proposal block. It found the
`10.1101/2025.01.08.631726` preprint DOI only in earlier DS-series records and
proposal text that introduced DeWeirdt et al. evidence.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042700` | DS-25 system | `METPO:1016300` phage defense system |

DS-25 system captures genome-level possession of the
DefensePredictor-discovered system 25 locus represented by the DefenseFinder
DS-25A and DS-25B custom HMM-profile rows. It excludes the individual DS-25
genes and proteins, individual DefenseFinder HMM profile rows, preprint Table
S5/S6 rows, cloned-transcriptional-unit plaquing assays, the absent final
Science Table S6/S7/S8 rows, the absent DS-25 rule-level DefenseFinder model,
unresolved component activity, unresolved phage readouts, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000473` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `DS-25__DS-25A` and `DS-25__DS-25B` are
kept as related synonyms because they name DefenseFinder profile keys rather
than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-25` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000473` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000473` as traceability during the migration.

## Change Log

- v350, 2026-09: lifts `traitmech:000473 DS-25 system` into the
  `METPO:1042700` placeholder block.
