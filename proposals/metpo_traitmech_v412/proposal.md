# METPO ROBOT Template Proposal - Avs II System (v412, 2026-10)

## Summary

This cohort reserves `METPO:1048900` for `Avs II system`, an AVAST
subtype trait represented in the pinned DefenseFinder rules table as the
`Avs_II` subsystem with an Avs2A profile. The local TraitMech fallback is
`traitmech:000535`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Avs II system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048900` is reserved for this one-row class cohort. The v411 cohort used
`METPO:1048800`, so v412 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files
across the whole repository. It found no hit for `traitmech:000535`,
`METPO:1048900`, `metpo_traitmech_v412`, `avs_ii_system`, `Avs_II`,
`Avs II system`, or `Avs2A`. The only prior `Avs2` hit was a contextual
mention from the broader AVAST-system proposal, and that v116 proposal
explicitly excluded Avs1 through Avs5 subtypes from the AVAST family-level
record.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048900` | Avs II system | `METPO:1019300` AVAST system |

Avs II system captures organism-level possession of the AVAST subtype II locus
represented by the pinned DefenseFinder HMM inventory with an Avs2A profile and
by the pinned rules table as the Avs_II subsystem. It excludes the broader
AVAST system, the individual Avs2A protein, the individual DefenseFinder
Avs_II profile row, exact Avs II effector chemistry, the Avs I and Avs III
through Avs V subtypes, Avs-family phage cue detection outside subtype II,
source registry rows that only name the broad `Avs` key, and other
phage-defense systems.

`traitmech:000535` is a direct local child of `traitmech:000239` AVAST system.
This proposal uses `METPO:1019300`, the v116 placeholder for
`traitmech:000239`.

## External Mappings

No exact external mapping is proposed. Individual Avs proteins, STAND
ATPase/NTPase domains, exact receptor-effector reactions, conserved phage
proteins, and DefenseFinder HMM or rule rows are shifted from this
organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000535` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000535` as traceability during the migration.

## Change Log

- v412, 2026-10: lifts `traitmech:000535 Avs II system` into the
  `METPO:1048900` placeholder block.
