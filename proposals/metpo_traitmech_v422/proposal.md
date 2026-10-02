# METPO ROBOT Template Proposal - DRT3 System (v422, 2026-10)

## Summary

This cohort reserves `METPO:1049900` for `DRT3 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT_3`
subsystem with required `DRT_3__drt3a` and `DRT_3__drt3b` profiles.
The local TraitMech fallback is `traitmech:000545`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT3 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049900` is reserved for this one-row class cohort. The v421 cohort used
`METPO:1049800`, so v422 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000545`, `METPO:1049900`,
`metpo_traitmech_v422`, `DRT3 system`, `DRT type 3`, `DRT type III`,
`DRT_3`, `DRT_3__drt3a`, `DRT_3__drt3b`, or `DRT_3__SLATT`. It found `drt3`
and `DRT type 3` only as contextual family-level evidence in the broad DRT
record, its original writer, and the generated DRT parent page, not as a minted
DRT3 subtype trait.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049900` | DRT3 system | `METPO:1023300` DRT system |

DRT3 system captures organism-level possession of the DRT subtype III locus
represented by the pinned DefenseFinder HMM inventory with `DRT_3__drt3a` and
`DRT_3__drt3b` named profiles and by the pinned rules table as the `DRT_3`
subsystem. It excludes the broader DRT system, the individual DRT_3
reverse-transcriptase profile rows, exact DRT3 RT products, exact DRT3 phage
triggers, host breadth, partner-feature requirements, the unresolved
`DRT_3__SLATT` inventory row, other DRT subtypes, source registry rows that only
name the broad `DRT` key, and other phage-defense systems.

`traitmech:000545` is a direct local child of `traitmech:000279` DRT system.
This proposal uses `METPO:1023300`, the v156 placeholder for
`traitmech:000279`.

## External Mappings

No exact external mapping is proposed. Individual DRT reverse-transcriptase
proteins, exact DRT enzymatic products, phage triggers, host ranges,
DefenseFinder HMM or rule rows, and unresolved DRT partner-feature
requirements are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000545` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000545` as traceability during the migration.

## Change Log

- v422, 2026-10: lifts `traitmech:000545 DRT3 system` into the
  `METPO:1049900` placeholder block.
