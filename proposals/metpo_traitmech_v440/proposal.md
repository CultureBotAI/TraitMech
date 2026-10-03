# METPO ROBOT Template Proposal - Lamassu-Mrr System (v440, 2026-10)

## Summary

This cohort reserves `METPO:1051700` for `Lamassu-Mrr system`, a Lamassu
subtype trait represented in the pinned DefenseFinder rules table as the
`Lamassu-Mrr` subsystem requiring `Lamassu-Fam__LmuA_effector_Mrr` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. The local TraitMech fallback is
`traitmech:000563`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Lamassu-Mrr system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1051700` is reserved for this one-row class cohort. The v439 cohort used
`METPO:1051600`, so v440 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository, excluding only `.git`. It found no exact live TraitMech,
METPO, history, or prior proposal record for `traitmech:000563`,
`METPO:1051700`, `metpo_traitmech_v440`, `Lamassu-Mrr system`,
`Lamassu-Mrr`, or `lamassu_mrr_system`. Existing matches for
`Lamassu-Fam__LmuA_effector_Mrr` were limited to forbidden-profile evidence on
neighboring Lamassu-Fam subtype records, their earlier writer scripts, and
rendered pages; they did not define an organism-level Lamassu-Mrr child.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1051700` | Lamassu-Mrr system | `METPO:1018600` Lamassu system |

Lamassu-Mrr system captures organism-level possession of the Lamassu-Mrr
subtype locus represented by the pinned DefenseFinder rules table as requiring
`Lamassu-Fam__LmuA_effector_Mrr` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. It excludes the broader Lamassu
system, the other Lamassu-Fam rule subtypes, individual LmuA, LmuB, or LmuC
proteins, individual DefenseFinder HMM or rule profile rows, exact viral DNA
triggers, exact Mrr effector activity, native host breadth, cell-death outputs,
and other phage-defense systems.

`traitmech:000563` is a direct local child of `traitmech:000232` Lamassu
system. This proposal uses `METPO:1018600`, the v109 placeholder for
`traitmech:000232`.

## External Mappings

No exact external mapping is proposed. Individual LmuA, LmuB, and LmuC
proteins, SMC-family ATPases, Mrr proteins or molecular activities, LmuABC
complexes, dsDNA-end binding, other Lamassu-Fam subtypes, phage triggers, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000563` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000563` as traceability during the migration.

## Change Log

- v440, 2026-10: lifts `traitmech:000563 Lamassu-Mrr system` into the
  `METPO:1051700` placeholder block.
