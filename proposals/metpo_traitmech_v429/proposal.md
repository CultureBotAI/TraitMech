# METPO ROBOT Template Proposal - Zorya Type II System (v429, 2026-10)

## Summary

This cohort reserves `METPO:1050600` for `Zorya type II system`, a
Zorya subtype trait represented in the pinned DefenseFinder rules table as the
`Zorya_TypeII` subsystem with `Zorya_TypeII__ZorE`, `Zorya__ZorA2`, and
`Zorya__ZorB` rule profiles. The local TraitMech fallback is
`traitmech:000552`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Zorya type II system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050600` is reserved for this one-row class cohort. The v428 cohort used
`METPO:1050500`, so v429 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000552`, `METPO:1050600`,
`metpo_traitmech_v429`, `Zorya type II system`, `Zorya_TypeII`,
`Zorya__ZorE`, `Zorya__ZorA2`, or `zorya_type_ii_system`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050600` | Zorya type II system | `METPO:1017100` Zorya system |

Zorya type II system captures organism-level possession of the Zorya_TypeII
subtype locus represented by the pinned DefenseFinder rules table as requiring
the `Zorya_TypeII__ZorE`, `Zorya__ZorA2`, and `Zorya__ZorB` profiles. It
excludes the broader Zorya system, individual ZorA2, ZorB, or ZorE proteins,
the individual DefenseFinder HMM profile rows, exact phage triggers, native
host breadth outside experimentally transferred loci, exact ZorE substrates,
ZorAB-to-ZorE activation sequence, other Zorya subtypes, and other
phage-defense systems.

`traitmech:000552` is a direct local child of `traitmech:000217` Zorya system.
This proposal uses `METPO:1017100`, the v94 placeholder for
`traitmech:000217`.

## External Mappings

No exact external mapping is proposed. Individual Zorya core or effector
proteins, ZorE nuclease activities, ZorAB motor activity, phage triggers,
native host ranges, Zorya type I or type III systems, and DefenseFinder HMM or
rule rows are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000552` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000552` as traceability during the migration.

## Change Log

- v429, 2026-10: lifts `traitmech:000552 Zorya type II system` into the
  `METPO:1050600` placeholder block.
