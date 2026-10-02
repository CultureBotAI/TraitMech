# METPO ROBOT Template Proposal - DRT6 System (v416, 2026-10)

## Summary

This cohort reserves `METPO:1049300` for `DRT6 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT6`
subsystem with the `DRT6__DRT6` profile. The local TraitMech fallback
is `traitmech:000539`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT6 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049300` is reserved for this one-row class cohort. The v415 cohort used
`METPO:1049200`, so v416 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the curated records, proposals, history, scripts, generated reports, app data,
pages, and `.claude`. It found no hit for `traitmech:000539`,
`METPO:1049300`, `metpo_traitmech_v416`, `DRT6 system`, `DRT type 6`,
`DRT6__`, or `DRT6`. The existing DRT record and v156 proposal only used the
`DRT_1` DefenseFinder subtype as representative family-level evidence and made
contextual sibling-subtype mentions.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049300` | DRT6 system | `METPO:1023300` DRT system |

DRT6 system captures organism-level possession of the DRT subtype VI locus
represented by the pinned DefenseFinder HMM inventory with a `DRT6__DRT6`
profile and by the pinned rules table as the `DRT6` subsystem. It excludes the
broader DRT system, the individual DRT6 reverse-transcriptase profile row,
exact DRT6 RT products, exact DRT6 phage triggers, host breadth, partner
features, other DRT subtypes, source registry rows that only name the broad
`DRT` key, and other phage-defense systems.

`traitmech:000539` is a direct local child of `traitmech:000279` DRT system.
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
2. On mint, replace local `traitmech:000539` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000539` as traceability during the migration.

## Change Log

- v416, 2026-10: lifts `traitmech:000539 DRT6 system` into the
  `METPO:1049300` placeholder block.
