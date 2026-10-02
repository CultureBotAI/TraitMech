# METPO ROBOT Template Proposal - CARD-NLR Endonuclease System (v427, 2026-10)

## Summary

This cohort reserves `METPO:1050400` for `CARD-NLR endonuclease system`, a
CARD-NLR subtype trait represented in the pinned DefenseFinder rules table as
the `CARD_NLR_Endonuclease` subsystem with a mandatory
`CARD_NLR__Endonuclease` profile and `CARD_NLR__CARD_Protease`,
`CARD_NLR__NLR_new`, and `CARD_NLR__Trypsin` accessory profiles. The local
TraitMech fallback is `traitmech:000550`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR endonuclease system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050400` is reserved for this one-row class cohort. The v426 cohort used
`METPO:1050300`, so v427 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000550`, `METPO:1050400`,
`metpo_traitmech_v427`, `CARD-NLR endonuclease system`, or
`card_nlr_endonuclease_system`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050400` | CARD-NLR endonuclease system | `METPO:1029100` CARD-NLR system |

CARD-NLR endonuclease system captures organism-level possession of the
CARD_NLR_Endonuclease subtype locus represented by the pinned DefenseFinder
rules table as requiring the `CARD_NLR__Endonuclease` profile in a CARD-NLR
locus context. It excludes the broader CARD-NLR system, individual
`CARD_NLR_Endonuclease` or accessory HMM profile rows, exact phage triggers,
native host breadth, exact endonuclease effector substrate, CARD-to-effector
activation sequence, other CARD_NLR subtypes, and other phage-defense systems.

`traitmech:000550` is a direct local child of `traitmech:000337` CARD-NLR
system. This proposal uses `METPO:1029100`, the v214 placeholder for
`traitmech:000337`.

## External Mappings

No exact external mapping is proposed. Individual bacterial CARD-like domains,
NLR-like profiles, trypsin-like accessory profiles, endonuclease-domain protein
families, phage triggers, native host ranges, and DefenseFinder HMM or rule rows
are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000550` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000550` as traceability during the migration.

## Change Log

- v427, 2026-10: lifts `traitmech:000550 CARD-NLR endonuclease system` into
  the `METPO:1050400` placeholder block.
