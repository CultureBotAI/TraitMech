# METPO ROBOT Template Proposal - CARD-NLR Phospho System (v428, 2026-10)

## Summary

This cohort reserves `METPO:1050500` for `CARD-NLR phospho system`, a
CARD-NLR subtype trait represented in the pinned DefenseFinder rules table as
the `CARD_NLR_Phospho` subsystem with a mandatory
`CARD_NLR__Trypsin_Phospho` profile and `CARD_NLR__CARD_Protease`,
`CARD_NLR__NLR_new`, and `CARD_NLR__Trypsin` accessory profiles. The local
TraitMech fallback is `traitmech:000551`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR phospho system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050500` is reserved for this one-row class cohort. The v427 cohort used
`METPO:1050400`, so v428 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000551`, `METPO:1050500`,
`metpo_traitmech_v428`, `CARD-NLR phospho system`, or
`card_nlr_phospho_system`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050500` | CARD-NLR phospho system | `METPO:1029100` CARD-NLR system |

CARD-NLR phospho system captures organism-level possession of the
CARD_NLR_Phospho subtype locus represented by the pinned DefenseFinder rules
table as requiring the `CARD_NLR__Trypsin_Phospho` profile in a CARD-NLR locus
context. It excludes the broader CARD-NLR system, individual
`CARD_NLR_Phospho` or accessory HMM profile rows, exact phage triggers, native
host breadth, exact phosphorylated substrate, CARD-to-effector activation
sequence, other CARD_NLR subtypes, and other phage-defense systems.

`traitmech:000551` is a direct local child of `traitmech:000337` CARD-NLR
system. This proposal uses `METPO:1029100`, the v214 placeholder for
`traitmech:000337`.

## External Mappings

No exact external mapping is proposed. Individual bacterial CARD-like domains,
NLR-like profiles, trypsin-like accessory profiles, phosphorylation-associated
protein families or substrates, phage triggers, native host ranges, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000551` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000551` as traceability during the migration.

## Change Log

- v428, 2026-10: lifts `traitmech:000551 CARD-NLR phospho system` into the
  `METPO:1050500` placeholder block.
