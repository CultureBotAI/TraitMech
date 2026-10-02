# METPO ROBOT Template Proposal - CARD-NLR GasderMIN System (v432, 2026-10)

## Summary

This cohort reserves `METPO:1050900` for `CARD-NLR GasderMIN system`, a
CARD-NLR subtype trait represented in the pinned DefenseFinder rules table as
the `CARD_NLR_GasderMIN` subsystem requiring the `GasderMIN__bGSDM` profile.
The local TraitMech fallback is `traitmech:000555`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR GasderMIN system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050900` is reserved for this one-row class cohort. The v431 cohort used
`METPO:1050800`, so v432 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000555`, `METPO:1050900`,
`metpo_traitmech_v432`, `CARD-NLR GasderMIN system`, or
`card_nlr_gasdermin_system`. Existing `CARD_NLR_GasderMIN` mentions were
supporting evidence on the broad CARD-NLR parent or GasderMIN records, not
exact child records.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050900` | CARD-NLR GasderMIN system | `METPO:1029100` CARD-NLR system |

CARD-NLR GasderMIN system captures organism-level possession of the
CARD_NLR_GasderMIN subtype locus represented by the pinned DefenseFinder rules
table as requiring `GasderMIN__bGSDM`. It excludes the broader CARD-NLR
system, standalone GasderMIN contexts, other CARD-NLR rule subtypes,
individual CARD-like, NLR-like, Trypsin, or bGSDM-family proteins, the
individual DefenseFinder HMM or rule profile rows, exact phage triggers, native
host breadth, exact bGSDM proteolysis route, CARD-to-gasdermin activation
sequence, and other phage-defense systems.

`traitmech:000555` is a direct local child of `traitmech:000337` CARD-NLR
system. This proposal uses `METPO:1029100`, the v214 placeholder for
`traitmech:000337`.

## External Mappings

No exact external mapping is proposed. Individual CARD-like domains, NLR
profiles, bGSDM-family proteins, gasdermin proteolysis, pore assembly, cell
death, phage triggers, standalone GasderMIN systems, other CARD-NLR subtypes,
and DefenseFinder HMM or rule rows are shifted from this organism-level
GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000555` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000555` as traceability during the migration.

## Change Log

- v432, 2026-10: lifts `traitmech:000555 CARD-NLR GasderMIN system` into the
  `METPO:1050900` placeholder block.
