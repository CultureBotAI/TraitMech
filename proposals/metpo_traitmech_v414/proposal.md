# METPO ROBOT Template Proposal - Avs IV System (v414, 2026-10)

## Summary

This cohort reserves `METPO:1049100` for `Avs IV system`, an AVAST
subtype trait represented in the pinned DefenseFinder rules table as the
`Avs_IV` subsystem with an Avs4A profile. The local TraitMech fallback
is `traitmech:000537`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Avs IV system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049100` is reserved for this one-row class cohort. The v413 cohort used
`METPO:1049000`, so v414 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files
across the whole repository. It found no hit for `traitmech:000537`,
`METPO:1049100`, `metpo_traitmech_v414`, `avs_iv_system`, `Avs_IV`,
`Avs IV system`, or `Avs_IV__Avs4A`. The only prior `Avs4` or `Avs IV` hits
were contextual family mentions or sibling-exclusion notes in the broader
AVAST-system and Avs I through Avs III system proposals.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049100` | Avs IV system | `METPO:1019300` AVAST system |

Avs IV system captures organism-level possession of the AVAST subtype IV
locus represented by the pinned DefenseFinder HMM inventory with an Avs4A
profile and by the pinned rules table as the Avs_IV subsystem. It excludes the
broader AVAST system, the individual Avs4A protein, the individual DefenseFinder
Avs_IV profile row, exact Avs IV effector chemistry, the Avs I through Avs III
and Avs V subtypes, Avs-family phage cue detection outside subtype IV, source
registry rows that only name the broad `Avs` key, and other phage-defense
systems.

`traitmech:000537` is a direct local child of `traitmech:000239` AVAST system.
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
2. On mint, replace local `traitmech:000537` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000537` as traceability during the migration.

## Change Log

- v414, 2026-10: lifts `traitmech:000537 Avs IV system` into the
  `METPO:1049100` placeholder block.
