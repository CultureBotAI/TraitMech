# METPO ROBOT Template Proposal - Lamassu-FMO System (v435, 2026-10)

## Summary

This cohort reserves `METPO:1051200` for `Lamassu-FMO system`, a
Lamassu subtype trait represented in the pinned DefenseFinder rules table as
the `Lamassu-FMO` subsystem requiring `Lamassu-Fam__LmuA_effector_FMO`
and `Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. The local TraitMech
fallback is `traitmech:000558`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Lamassu-FMO system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1051200` is reserved for this one-row class cohort. The v434 cohort used
`METPO:1051100`, so v435 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000558`, `METPO:1051200`,
`metpo_traitmech_v435`, `Lamassu-FMO system`, `Lamassu-FMO`,
`lamassu_fmo_system`, or `Lamassu-Fam__LmuA_effector_FMO`. Existing matches for
`Lamassu-Fam__LmuA_effector_FMO` were limited to forbidden-profile evidence on
the neighboring `Lamassu-Amidase system` and `Lamassu-Cap4 nuclease system`
records and did not define an organism-level Lamassu-FMO child.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1051200` | Lamassu-FMO system | `METPO:1018600` Lamassu system |

Lamassu-FMO system captures organism-level possession of the Lamassu-FMO subtype
locus represented by the pinned DefenseFinder rules table as requiring
`Lamassu-Fam__LmuA_effector_FMO` and
`Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II`. It excludes the broader Lamassu
system, the other Lamassu-Fam rule subtypes, individual LmuA, LmuB, or LmuC
proteins, individual DefenseFinder HMM or rule profile rows, exact viral DNA
triggers, exact FMO expansion or substrates, native host breadth, cell-death
outputs, and other phage-defense systems.

The first-pass local record follows the pinned `Lamassu-FMO` rule row while
tracking the relationship between its Cap4/Lipase-scoped LmuB/LmuC profiles and
the FMO-scoped `Lamassu-Fam__LmuB_SMC_FMO` /
`Lamassu-Fam__LmuC_acc_FMO` HMM rows as an open curation question.

`traitmech:000558` is a direct local child of `traitmech:000232` Lamassu
system. This proposal uses `METPO:1018600`, the v109 placeholder for
`traitmech:000232`.

## External Mappings

No exact external mapping is proposed. Individual LmuA, LmuB, and LmuC
proteins, SMC-family ATPases, putative FMO-like molecular activities, LmuABC
complexes, dsDNA-end binding, other Lamassu-Fam subtypes, phage triggers, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait. The LmuB/LmuC rows listed in the pinned `Lamassu-FMO` rule are not
carried as related synonyms because the same HMM inventory also carries
FMO-scoped LmuB/LmuC model rows.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000558` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000558` as traceability during the migration.

## Change Log

- v435, 2026-10: lifts `traitmech:000558 Lamassu-FMO system` into the
  `METPO:1051200` placeholder block.
