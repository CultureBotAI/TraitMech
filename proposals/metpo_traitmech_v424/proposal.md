# METPO ROBOT Template Proposal - DRT5 System (v424, 2026-10)

## Summary

This cohort reserves `METPO:1050100` for `DRT5 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT_5`
subsystem with the `DRT_5__drt5` profile. The local TraitMech fallback
is `traitmech:000547`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT5 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1050100` is reserved for this one-row class cohort. The v423 cohort used
`METPO:1050000`, so v424 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000547`, `METPO:1050100`,
`metpo_traitmech_v424`, `DRT5 system`, `DRT type 5`, `DRT type V`, `DRT_5`,
`DRT_5__drt5`, or `drt5`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1050100` | DRT5 system | `METPO:1023300` DRT system |

DRT5 system captures organism-level possession of the DRT subtype V locus
represented by the pinned DefenseFinder HMM inventory with a `DRT_5__drt5`
profile and by the pinned rules table as the `DRT_5` subsystem. It excludes the
broader DRT system, the individual DRT5 reverse-transcriptase profile row,
exact DRT5 RT products, exact DRT5 phage triggers, host breadth, partner
features, other DRT subtypes, source registry rows that only name the broad
`DRT` key, and other phage-defense systems.

`traitmech:000547` is a direct local child of `traitmech:000279` DRT system.
This proposal uses `METPO:1023300`, the v156 placeholder for
`traitmech:000279`.

## External Mappings

No exact external mapping is proposed. Individual DRT reverse-transcriptase
proteins, exact DRT enzymatic products, phage triggers, host ranges, partner
features, and DefenseFinder HMM or rule rows are shifted from this
organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000547` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000547` as traceability during the migration.

## Change Log

- v424, 2026-10: lifts `traitmech:000547 DRT5 system` into the
  `METPO:1050100` placeholder block.
