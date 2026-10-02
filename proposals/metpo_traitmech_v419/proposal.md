# METPO ROBOT Template Proposal - DRT9 System (v419, 2026-10)

## Summary

This cohort reserves `METPO:1049600` for `DRT9 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT9`
subsystem with the required `DRT9__DRT9` profile. The local TraitMech
fallback is `traitmech:000542`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT9 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049600` is reserved for this one-row class cohort. The v418 cohort used
`METPO:1049500`, so v419 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or
prior proposal record for `traitmech:000542`, `METPO:1049600`,
`metpo_traitmech_v419`, `DRT9 system`, `DRT type 9`, `DRT type IX`,
`DRT9__DRT9`, `DRT9__SLATT`, or `DRT_9`. The existing DRT record and v156
proposal only used the `DRT_1` DefenseFinder subtype as representative
family-level evidence and made contextual sibling-subtype mentions that include
DRT9 in excluded HMM profiles.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049600` | DRT9 system | `METPO:1023300` DRT system |

DRT9 system captures organism-level possession of the DRT subtype IX locus
represented by the pinned DefenseFinder HMM inventory with the `DRT9__DRT9`
named profile and by the pinned rules table as the `DRT9` subsystem. It
excludes the broader DRT system, the individual DRT9 reverse-transcriptase
profile row, the `DRT9__SLATT` HMM inventory row that lacks an emitted HMM name
and rule membership, exact DRT9 RT products, exact DRT9 phage triggers, host
breadth, other DRT subtypes, source registry rows that only name the broad
`DRT` key, and other phage-defense systems.

`traitmech:000542` is a direct local child of `traitmech:000279` DRT system.
This proposal uses `METPO:1023300`, the v156 placeholder for
`traitmech:000279`.

## External Mappings

No exact external mapping is proposed. Individual DRT reverse-transcriptase
proteins, exact DRT enzymatic products, phage triggers, host ranges,
DefenseFinder HMM or rule rows, and unresolved DRT inventory rows are shifted
from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000542` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000542` as traceability during the migration.

## Change Log

- v419, 2026-10: lifts `traitmech:000542 DRT9 system` into the
  `METPO:1049600` placeholder block.
