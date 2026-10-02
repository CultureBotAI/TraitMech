# METPO ROBOT Template Proposal - Lamassu-Amidase System (v433, 2026-10)

## Summary

This cohort reserves `METPO:1051000` for `Lamassu-Amidase system`, a
Lamassu subtype trait represented in the pinned DefenseFinder rules table as
the `Lamassu-Amidase` subsystem requiring
`Lamassu-Fam__LmuA_effector_Amidase` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. The local TraitMech fallback is
`traitmech:000556`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Lamassu-Amidase system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1051000` is reserved for this one-row class cohort. The v432 cohort used
`METPO:1050900`, so v433 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000556`, `METPO:1051000`,
`metpo_traitmech_v433`, `Lamassu-Amidase system`, `Lamassu-Amidase`,
`Lamassu-Fam__LmuA_effector_Amidase`, or `lamassu_amidase_system`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1051000` | Lamassu-Amidase system | `METPO:1018600` Lamassu system |

Lamassu-Amidase system captures organism-level possession of the
Lamassu-Amidase subtype locus represented by the pinned DefenseFinder rules
table as requiring `Lamassu-Fam__LmuA_effector_Amidase` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. It excludes the broader Lamassu
system, the other Lamassu-Fam rule subtypes, individual LmuA, LmuB, or LmuC
proteins, the individual DefenseFinder HMM or rule profile rows, exact viral DNA
triggers, exact amidase effector substrates, native host breadth, cell-death
outputs, and other phage-defense systems.

`traitmech:000556` is a direct local child of `traitmech:000232` Lamassu
system. This proposal uses `METPO:1018600`, the v109 placeholder for
`traitmech:000232`.

## External Mappings

No exact external mapping is proposed. Individual LmuA, LmuB, and LmuC
proteins, SMC-family ATPases, amidase activities, LmuABC complexes, dsDNA-end
binding, other Lamassu-Fam subtypes, phage triggers, and DefenseFinder HMM or
rule rows are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000556` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000556` as traceability during the migration.

## Change Log

- v433, 2026-10: lifts `traitmech:000556 Lamassu-Amidase system` into the
  `METPO:1051000` placeholder block.
