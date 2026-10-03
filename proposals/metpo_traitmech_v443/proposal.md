# METPO ROBOT Template Proposal - Lamassu-Sir2 System (v443, 2026-10)

## Summary

This cohort reserves `METPO:1052000` for `Lamassu-Sir2 system`, a
Lamassu subtype trait represented in the pinned DefenseFinder rules table as
the `Lamassu-Sir2` subsystem requiring
`Lamassu-Fam__LmuA_effector_Sir2` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. The local TraitMech fallback is
`traitmech:000566`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Lamassu-Sir2 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1052000` is reserved for this one-row class cohort. The v442 cohort used
`METPO:1051900`, so v443 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository, excluding only `.git`. It found no exact live TraitMech,
METPO, history, or prior proposal record for `traitmech:000566`,
`METPO:1052000`, `metpo_traitmech_v443`, `Lamassu-Sir2 system`,
`Lamassu-Sir2`, or `lamassu_sir2_system`. Existing matches for
`Lamassu-Fam__LmuA_effector_Sir2` were limited to forbidden-profile evidence on
neighboring Lamassu-Fam subtype records, their earlier writer scripts, and
rendered pages; they did not define an organism-level Lamassu-Sir2 child.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1052000` | Lamassu-Sir2 system | `METPO:1018600` Lamassu system |

Lamassu-Sir2 system captures organism-level possession of the Lamassu-Sir2
subtype locus represented by the pinned DefenseFinder rules table as requiring
`Lamassu-Fam__LmuA_effector_Sir2` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. It excludes the broader Lamassu
system, the other Lamassu-Fam rule subtypes, individual LmuA, LmuB, or LmuC
proteins, individual DefenseFinder HMM or rule profile rows, exact viral DNA
triggers, exact Sir2 effector activity, native host breadth, cell-death outputs,
and other phage-defense systems.

`traitmech:000566` is a direct local child of `traitmech:000232` Lamassu
system. This proposal uses `METPO:1018600`, the v109 placeholder for
`traitmech:000232`.

## External Mappings

No exact external mapping is proposed. Individual LmuA, LmuB, and LmuC
proteins, SMC-family ATPases, Sir2 proteins or molecular activities, LmuABC
complexes, dsDNA-end binding, other Lamassu-Fam subtypes, phage triggers, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000566` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000566` as traceability during the migration.

## Change Log

- v443, 2026-10: lifts `traitmech:000566 Lamassu-Sir2 system` into the
  `METPO:1052000` placeholder block.
