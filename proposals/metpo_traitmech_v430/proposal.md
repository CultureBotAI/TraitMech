# METPO ROBOT Template Proposal - CARD-NLR Subtilase System (v430, 2026-10)

## Summary

This cohort reserves `METPO:1050700` for `CARD-NLR subtilase system`, a
CARD-NLR subtype trait represented in the pinned DefenseFinder rules table as
the `CARD_NLR_Subtilase` subsystem requiring the
`CARD_NLR__Subtilase_long_new` rule profile. The local TraitMech fallback is
`traitmech:000553`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR subtilase system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050700` is reserved for this one-row class cohort. The v429 cohort used
`METPO:1050600`, so v430 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000553`, `METPO:1050700`,
`metpo_traitmech_v430`, `CARD-NLR subtilase system`, or
`card_nlr_subtilase_system`. Existing `CARD_NLR_Subtilase` and
`CARD_NLR__Subtilase_long_new` mentions were supporting evidence on the broad
CARD-NLR parent or neighboring children, not exact child records.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050700` | CARD-NLR subtilase system | `METPO:1029100` CARD-NLR system |

CARD-NLR subtilase system captures organism-level possession of the
CARD_NLR_Subtilase subtype locus represented by the pinned DefenseFinder rules
table as requiring `CARD_NLR__Subtilase_long_new`. It excludes the broader
CARD-NLR system, other CARD-NLR rule subtypes, standalone GasderMIN contexts,
individual CARD-like, NLR-like, Trypsin, or subtilase-family proteins, the
individual DefenseFinder HMM or rule profile rows, exact phage triggers, native
host breadth, exact subtilase substrates, CARD-to-subtilase activation
sequence, and other phage-defense systems.

`traitmech:000553` is a direct local child of `traitmech:000337` CARD-NLR
system. This proposal uses `METPO:1029100`, the v214 placeholder for
`traitmech:000337`.

## External Mappings

No exact external mapping is proposed. Individual CARD-like domains, NLR
profiles, subtilase-family proteins, target substrates, proteolytic cleavage
events, phage triggers, other CARD-NLR subtypes, and DefenseFinder HMM or rule
rows are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000553` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000553` as traceability during the migration.

## Change Log

- v430, 2026-10: lifts `traitmech:000553 CARD-NLR subtilase system` into the
  `METPO:1050700` placeholder block.
