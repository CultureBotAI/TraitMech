# METPO ROBOT Template Proposal - Druantia III System (v437, 2026-10)

## Summary

This cohort reserves `METPO:1051400` for `Druantia III system`, a
DruE/DruH-containing Druantia subtype trait represented in the pinned
DefenseFinder rules table as the `Druantia_III` subsystem requiring the
`Druantia_III__DruH` and `Druantia__DruE_1` profiles. Wu et al. support
Druantia III as a recurring late-acting Druantia system defined by the presence
of DruE and DruH. The local TraitMech fallback is `traitmech:000560`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Druantia III system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1051400` is reserved for this one-row class cohort. The v436 cohort used
`METPO:1051300`, so v437 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000560`, `METPO:1051400`,
`metpo_traitmech_v437`, `Druantia III system`, `Druantia_III`, or
`druantia_iii_system`. Existing `Druantia III` mentions were supporting
evidence on the broad Druantia and ARMADA records, not exact child records.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1051400` | Druantia III system | `METPO:1018800` Druantia system |

Druantia III system captures organism-level possession of the Type III branch
of the Druantia antiphage-system family, represented by DruE and DruH in the
primary literature and by the pinned DefenseFinder `Druantia_III` rule row
requiring `Druantia_III__DruH` and `Druantia__DruE_1`. It excludes the broader
Druantia system, Type I, Type II, and Type IV Druantia contexts, individual
`druE` or `druH` genes, DruE or DruH proteins, individual DefenseFinder HMM
rows, exact late phage triggers, RecBCD-dependent DNA processing, Zorya II
synergy, native host breadth, and other phage-defense systems.

`traitmech:000560` is a direct local child of `traitmech:000234` Druantia
system. This proposal uses `METPO:1018800`, the v111 placeholder for
`traitmech:000234`.

## External Mappings

No exact external mapping is proposed. Druantia genes, Druantia proteins,
DruE/DruH molecular activities, RecBCD/Zorya dependency states, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000560` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000560` as traceability during the migration.

## Change Log

- v437, 2026-10: lifts `traitmech:000560 Druantia III system` into the
  `METPO:1051400` placeholder block.
