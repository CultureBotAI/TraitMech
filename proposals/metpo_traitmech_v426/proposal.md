# METPO ROBOT Template Proposal - DISARM2 System (v426, 2026-10)

## Summary

This cohort reserves `METPO:1050300` for `DISARM2 system`, a DISARM subtype
trait represented in the pinned DefenseFinder rules table as the `DISARM_2`
subsystem with DISARM_2-specific `DISARM_2__drmE` and `DISARM_2__drmMII`
profiles plus shared `DISARM__drmA`, `DISARM__drmB`, and `DISARM__drmC`
profiles. The local TraitMech fallback is `traitmech:000549`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DISARM2 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050300` is reserved for this one-row class cohort. The v425 cohort used
`METPO:1050200`, so v426 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000549`, `METPO:1050300`,
`metpo_traitmech_v426`, `DISARM2 system`, `DISARM type II`, `DISARM_2`,
`DISARM_2__drmE`, `DISARM_2__drmMII`, `disarm2`, or `disarm_2`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050300` | DISARM2 system | `METPO:1016500` DISARM system |

DISARM2 system captures organism-level possession of the DISARM subtype II locus
represented by the pinned DefenseFinder HMM inventory with shared `DISARM`
profiles and `DISARM_2` profiles and by the pinned rules table as the
`DISARM_2` subsystem. It excludes the broader DISARM system, individual
DISARM_2 or shared DISARM profile rows, exact DISARM2 effector chemistry, native
host breadth, sensitive-phage breadth, shared-core component roles, DISARM1, and
other phage-defense systems.

`traitmech:000549` is a direct local child of `traitmech:000211` DISARM system.
This proposal uses `METPO:1016500`, the v88 placeholder for
`traitmech:000211`.

## External Mappings

No exact external mapping is proposed. Individual Drm proteins, exact DISARM2
enzymatic products, direct phage triggers, native host ranges, sensitive-phage
ranges, and DefenseFinder HMM or rule rows are shifted from this organism-level
GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000549` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000549` as traceability during the migration.

## Change Log

- v426, 2026-10: lifts `traitmech:000549 DISARM2 system` into the
  `METPO:1050300` placeholder block.
