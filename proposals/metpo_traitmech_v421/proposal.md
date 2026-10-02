# METPO ROBOT Template Proposal - DRT2 System (v421, 2026-10)

## Summary

This cohort reserves `METPO:1049800` for `DRT2 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT_2`
subsystem with the `DRT_2__drt2` profile. The local TraitMech fallback
is `traitmech:000544`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT2 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049800` is reserved for this one-row class cohort. The v420 cohort used
`METPO:1049700`, so v421 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the curated records, proposals, history, scripts, generated reports, app data,
pages, and `.claude`. It found no hit for `traitmech:000544`,
`METPO:1049800`, `metpo_traitmech_v421`, `DRT2 system`, `DRT type 2`,
`DRT type II`, `DRT_2`, `DRT2__drt2`, or `drt2`. The existing DRT record and
v156 proposal only used the `DRT_1` DefenseFinder subtype as representative
family-level evidence and made contextual sibling-subtype mentions.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049800` | DRT2 system | `METPO:1023300` DRT system |

DRT2 system captures organism-level possession of the DRT subtype II locus
represented by the pinned DefenseFinder HMM inventory with a `DRT_2__drt2`
profile and by the pinned rules table as the `DRT_2` subsystem. It excludes the
broader DRT system, the individual DRT2 reverse-transcriptase profile row,
exact DRT2 RT products, exact DRT2 phage triggers, host breadth, partner
features, other DRT subtypes, source registry rows that only name the broad
`DRT` key, and other phage-defense systems.

`traitmech:000544` is a direct local child of `traitmech:000279` DRT system.
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
2. On mint, replace local `traitmech:000544` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000544` as traceability during the migration.

## Change Log

- v421, 2026-10: lifts `traitmech:000544 DRT2 system` into the
  `METPO:1049800` placeholder block.
