# METPO ROBOT Template Proposal - DRT8 System (v418, 2026-10)

## Summary

This cohort reserves `METPO:1049500` for `DRT8 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT8`
subsystem with the required `DRT8__DRT8` profile and optional
`DRT8__DRT8b` accessory profile. The local TraitMech fallback is
`traitmech:000541`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT8 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049500` is reserved for this one-row class cohort. The v417 cohort used
`METPO:1049400`, so v418 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or
prior proposal record for `traitmech:000541`, `METPO:1049500`,
`metpo_traitmech_v418`, `DRT8 system`, `DRT type 8`, `DRT type VIII`,
`DRT8__DRT8`, `DRT8__DRT8a`, `DRT8__DRT8b`, or `DRT_8`. The existing DRT
record and v156 proposal only used the `DRT_1` DefenseFinder subtype as
representative family-level evidence and made contextual sibling-subtype
mentions.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049500` | DRT8 system | `METPO:1023300` DRT system |

DRT8 system captures organism-level possession of the DRT subtype VIII locus
represented by the pinned DefenseFinder HMM inventory with `DRT8__DRT8` and
`DRT8__DRT8b` named profiles and by the pinned rules table as the `DRT8`
subsystem. It excludes the broader DRT system, the individual DRT8
reverse-transcriptase profile rows, the `DRT8__DRT8a` HMM inventory row that
lacks an emitted HMM name and rule membership, exact DRT8 RT products, exact
DRT8 phage triggers, host breadth, accessory-profile roles, other DRT
subtypes, source registry rows that only name the broad `DRT` key, and other
phage-defense systems.

`traitmech:000541` is a direct local child of `traitmech:000279` DRT system.
This proposal uses `METPO:1023300`, the v156 placeholder for
`traitmech:000279`.

## External Mappings

No exact external mapping is proposed. Individual DRT reverse-transcriptase
proteins, exact DRT enzymatic products, phage triggers, host ranges, accessory
components, DefenseFinder HMM or rule rows, and unresolved DRT inventory rows
are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000541` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000541` as traceability during the migration.

## Change Log

- v418, 2026-10: lifts `traitmech:000541 DRT8 system` into the
  `METPO:1049500` placeholder block.
