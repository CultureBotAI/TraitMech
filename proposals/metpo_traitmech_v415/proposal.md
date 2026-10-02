# METPO ROBOT Template Proposal - Avs V System (v415, 2026-10)

## Summary

This cohort reserves `METPO:1049200` for `Avs V system`, an AVAST
subtype trait represented in the pinned DefenseFinder rules table as the
`Avs_V` subsystem with an Avs5A profile. The local TraitMech fallback
is `traitmech:000538`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Avs V system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049200` is reserved for this one-row class cohort. The v414 cohort used
`METPO:1049100`, so v415 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files
across the whole repository. It found no hit for `traitmech:000538`,
`METPO:1049200`, `metpo_traitmech_v415`, `avs_v_system`, `Avs_V`,
`Avs V system`, or `Avs_V__Avs5A`. The only prior `Avs5` or `Avs V` hits
were contextual family mentions or sibling-exclusion notes in the broader
AVAST-system, Avs I through Avs IV system, and JukAB system proposals.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049200` | Avs V system | `METPO:1019300` AVAST system |

Avs V system captures organism-level possession of the AVAST subtype V
locus represented by the pinned DefenseFinder HMM inventory with an Avs5A
profile and by the pinned rules table as the Avs_V subsystem. It excludes the
broader AVAST system, the individual Avs5A protein, the individual DefenseFinder
Avs_V profile row, exact Avs V effector chemistry, the Avs I through Avs IV
subtypes, jumbo-phage-specific Avs5 immunity outside the named subsystem, source
registry rows that only name the broad `Avs` key, and other phage-defense
systems.

`traitmech:000538` is a direct local child of `traitmech:000239` AVAST system.
This proposal uses `METPO:1019300`, the v116 placeholder for
`traitmech:000239`.

## External Mappings

No exact external mapping is proposed. Individual Avs proteins, STAND
ATPase/NTPase domains, exact receptor-effector reactions, conserved phage
proteins, JADA trigger proteins, jumbo phage infection phenotypes, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000538` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000538` as traceability during the migration.

## Change Log

- v415, 2026-10: lifts `traitmech:000538 Avs V system` into the
  `METPO:1049200` placeholder block.
