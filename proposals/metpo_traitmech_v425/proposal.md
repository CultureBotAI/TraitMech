# METPO ROBOT Template Proposal - DISARM1 System (v425, 2026-10)

## Summary

This cohort reserves `METPO:1050200` for `DISARM1 system`, a DISARM subtype
trait represented in the pinned DefenseFinder rules table as the `DISARM_1`
subsystem with DISARM_1-specific `DISARM_1__drmD` and `DISARM_1__drmMI`
profiles plus shared `DISARM__drmA`, `DISARM__drmB`, and `DISARM__drmC`
profiles. The local TraitMech fallback is `traitmech:000548`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DISARM1 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050200` is reserved for this one-row class cohort. The v424 cohort used
`METPO:1050100`, so v425 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000548`, `METPO:1050200`,
`metpo_traitmech_v425`, `DISARM1 system`, `DISARM type I`, `DISARM_1`,
`DISARM_1__drmD`, `DISARM_1__drmMI`, `disarm1`, or `disarm_1`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050200` | DISARM1 system | `METPO:1016500` DISARM system |

DISARM1 system captures organism-level possession of the DISARM subtype I locus
represented by the pinned DefenseFinder HMM inventory with shared `DISARM`
profiles and `DISARM_1` profiles and by the pinned rules table as the
`DISARM_1` subsystem. It excludes the broader DISARM system, individual
DISARM_1 or shared DISARM profile rows, exact DISARM1 effector chemistry, native
host breadth, sensitive-phage breadth, shared-core component roles, DISARM2, and
other phage-defense systems.

`traitmech:000548` is a direct local child of `traitmech:000211` DISARM system.
This proposal uses `METPO:1016500`, the v88 placeholder for
`traitmech:000211`.

## External Mappings

No exact external mapping is proposed. Individual Drm proteins, exact DISARM1
enzymatic products, direct phage triggers, native host ranges, sensitive-phage
ranges, and DefenseFinder HMM or rule rows are shifted from this organism-level
GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000548` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000548` as traceability during the migration.

## Change Log

- v425, 2026-10: lifts `traitmech:000548 DISARM1 system` into the
  `METPO:1050200` placeholder block.
