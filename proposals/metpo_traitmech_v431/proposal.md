# METPO ROBOT Template Proposal - Zorya Type I System (v431, 2026-10)

## Summary

This cohort reserves `METPO:1050800` for `Zorya type I system`, a
Zorya subtype trait whose pinned DefenseFinder `Zorya_TypeI` rule row lists
`Zorya_TypeI__ZorC`, `Zorya_TypeI__ZorD`, `Zorya__ZorA`, and `Zorya__ZorB`
in its mandatory profile set with 3 mandatory matches and 3 genes required.
The local TraitMech fallback is `traitmech:000554`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Zorya type I system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050800` is reserved for this one-row class cohort. The v430 cohort used
`METPO:1050700`, so v431 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000554`, `METPO:1050800`,
`metpo_traitmech_v431`, `Zorya type I system`, `Zorya_TypeI`,
`Zorya_TypeI__ZorC`, `Zorya_TypeI__ZorD`, or `zorya_type_i_system`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050800` | Zorya type I system | `METPO:1017100` Zorya system |

Zorya type I system captures organism-level possession of a Zorya_TypeI
subtype locus whose pinned DefenseFinder rule row lists
`Zorya_TypeI__ZorC`, `Zorya_TypeI__ZorD`, `Zorya__ZorA`, and `Zorya__ZorB`
in its mandatory profile set with 3 mandatory matches and 3 genes required.
It excludes the broader Zorya system, individual ZorA, ZorB, ZorC, or ZorD
proteins, the individual DefenseFinder HMM profile rows, exact phage triggers,
native host breadth outside experimentally transferred loci, exact ZorC or
ZorD substrates, ZorAB-to-ZorC/ZorD activation sequence, other Zorya subtypes,
and other phage-defense systems.

`traitmech:000554` is a direct local child of `traitmech:000217` Zorya system.
This proposal uses `METPO:1017100`, the v94 placeholder for
`traitmech:000217`.

## External Mappings

No exact external mapping is proposed. Individual Zorya core or effector
proteins, ZorC or ZorD nuclease activities, ZorAB motor activity, phage
triggers, native host ranges, Zorya type II or type III systems, and
DefenseFinder HMM or rule rows are shifted from this organism-level GENOMICS
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000554` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000554` as traceability during the migration.

## Change Log

- v431, 2026-10: lifts `traitmech:000554 Zorya type I system` into the
  `METPO:1050800` placeholder block.
