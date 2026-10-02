# METPO ROBOT Template Proposal - Avs I System (v411, 2026-10)

## Summary

This cohort reserves `METPO:1048800` for `Avs I system`, an AVAST subtype
trait represented in the pinned DefenseFinder rules table as the `Avs_I`
subsystem with Avs1A, Avs1B, and Avs1C profiles. The local TraitMech fallback
is `traitmech:000534`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Avs I system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048800` is reserved for this one-row class cohort. The v410 cohort used
`METPO:1048700`, so v411 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files
across the whole repository. It found no hit for `traitmech:000534`,
`METPO:1048800`, `metpo_traitmech_v411`, `avs_i_system`, `Avs_I`,
`Avs I system`, or `Avs1A`. The only prior `Avs1` hits were contextual
mentions from the broader AVAST-system record, script, and proposal, and that
v116 proposal explicitly excluded Avs1 through Avs5 subtypes from the AVAST
family-level record.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048800` | Avs I system | `METPO:1019300` AVAST system |

Avs I system captures organism-level possession of the AVAST subtype I locus
represented by the pinned DefenseFinder HMM inventory with Avs1A, Avs1B, and
Avs1C profiles and by the pinned rules table as the Avs_I subsystem. It
excludes the broader AVAST system, individual Avs1A, Avs1B, and Avs1C
proteins, individual DefenseFinder Avs_I profile rows, exact Avs I effector
chemistry, the Avs II through Avs V subtypes, Avs-family phage cue detection
outside subtype I, source registry rows that only name the broad `Avs` key, and
other phage-defense systems.

`traitmech:000534` is a direct local child of `traitmech:000239` AVAST system.
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
2. On mint, replace local `traitmech:000534` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000534` as traceability during the migration.

## Change Log

- v411, 2026-10: lifts `traitmech:000534 Avs I system` into the
  `METPO:1048800` placeholder block.
