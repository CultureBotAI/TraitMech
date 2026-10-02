# METPO ROBOT Template Proposal - Avs III System (v413, 2026-10)

## Summary

This cohort reserves `METPO:1049000` for `Avs III system`, an AVAST
subtype trait represented in the pinned DefenseFinder rules table as the
`Avs_III` subsystem with Avs3A and Avs3B profiles. The local TraitMech
fallback is `traitmech:000536`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Avs III system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049000` is reserved for this one-row class cohort. The v412 cohort used
`METPO:1048900`, so v413 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files
across the whole repository. It found no hit for `traitmech:000536`,
`METPO:1049000`, `metpo_traitmech_v413`, `avs_iii_system`, `Avs_III`,
`Avs III system`, `Avs_III__Avs3A`, or `Avs_III__Avs3B`. The only prior
`Avs3` or `Avs III` hits were contextual family mentions or sibling-exclusion
notes in the broader AVAST-system and Avs II system proposals.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049000` | Avs III system | `METPO:1019300` AVAST system |

Avs III system captures organism-level possession of the AVAST subtype III
locus represented by the pinned DefenseFinder HMM inventory with Avs3A and
Avs3B profiles and by the pinned rules table as the Avs_III subsystem. It
excludes the broader AVAST system, the individual Avs3A or Avs3B proteins,
individual DefenseFinder Avs_III profile rows, exact Avs III effector
chemistry, the Avs I through Avs II and Avs IV through Avs V subtypes,
Avs-family phage cue detection outside subtype III, source registry rows that
only name the broad `Avs` key, and other phage-defense systems.

`traitmech:000536` is a direct local child of `traitmech:000239` AVAST system.
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
2. On mint, replace local `traitmech:000536` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000536` as traceability during the migration.

## Change Log

- v413, 2026-10: lifts `traitmech:000536 Avs III system` into the
  `METPO:1049000` placeholder block.
