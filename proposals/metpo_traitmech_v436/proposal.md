# METPO ROBOT Template Proposal - CARD-NLR-like System (v436, 2026-10)

## Summary

This cohort reserves `METPO:1051300` for `CARD-NLR-like system`, a CARD-NLR
subtype trait represented in the pinned DefenseFinder rules table as the
`CARD_NLR_like` subsystem requiring a minimum of two matches from the
`CARD_NLR__Endonuclease`, `CARD_NLR__Phospho_Trypsin`,
`CARD_NLR__Subtilase_long_new`, and `CARD_NLR__Trypsin_Phospho` candidate
effector profiles and four genes overall after considering the
`CARD_NLR__CARD_Protease`, `CARD_NLR__NLR_new`, and `CARD_NLR__Trypsin`
accessory profiles. The local TraitMech fallback is `traitmech:000559`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR-like system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1051300` is reserved for this one-row class cohort. The v435 cohort used
`METPO:1051200`, so v436 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000559`, `METPO:1051300`,
`metpo_traitmech_v436`, `CARD-NLR-like system`, or
`card_nlr_like_system`. Existing `CARD_NLR_like` mentions were supporting
evidence on the broad CARD-NLR parent, not exact child records.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1051300` | CARD-NLR-like system | `METPO:1029100` CARD-NLR system |

CARD-NLR-like system captures organism-level possession of the `CARD_NLR_like`
subtype locus represented by the pinned DefenseFinder rules table as requiring
at least two matches from four candidate effector profiles and four genes
overall after considering three accessory profiles. The label preserves
DefenseFinder's `CARD_NLR_like` subsystem string; `like` is part of that source
row label and is not intended to mean outside or merely similar to CARD-NLR. It
excludes the broader CARD-NLR system, other CARD-NLR rule subtypes, standalone
GasderMIN contexts, individual CARD-like, NLR-like, Trypsin, endonuclease,
phospho-trypsin, or subtilase-family proteins, the individual DefenseFinder HMM
or rule profile rows, exact phage triggers, native host breadth, the unresolved
`CARD_NLR__Subtilase_long_new` HMM inventory row, effector-combination
semantics, CARD-to-effector activation sequence, and other phage-defense
systems.

`traitmech:000559` is a direct local child of `traitmech:000337` CARD-NLR
system. This proposal uses `METPO:1029100`, the v214 placeholder for
`traitmech:000337`.

## External Mappings

No exact external mapping is proposed. Individual CARD-like domains, NLR
profiles, Trypsin family members, endonucleases, phospho-trypsin profiles,
subtilase-family proteins, cell death, phage triggers, other CARD-NLR subtypes,
and DefenseFinder HMM or rule rows are shifted from this organism-level
GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000559` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000559` as traceability during the migration.

## Change Log

- v436, 2026-10: lifts `traitmech:000559 CARD-NLR-like system` into the
  `METPO:1051300` placeholder block.
