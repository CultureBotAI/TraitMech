# METPO ROBOT Template Proposal - DRT7 System (v417, 2026-10)

## Summary

This cohort reserves `METPO:1049400` for `DRT7 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT7`
subsystem with one required profile from the `DRT7__DRT7` or
`DRT7__DRT7_small` profile rows. The local TraitMech fallback is
`traitmech:000540`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT7 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049400` is reserved for this one-row class cohort. The v416 cohort used
`METPO:1049300`, so v417 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or
prior proposal record for `traitmech:000540`, `METPO:1049400`,
`metpo_traitmech_v417`, `DRT7 system`, `DRT type 7`, `DRT type VII`,
`DRT7__DRT7`, `DRT7__DRT7_small`, or `DRT_7`; the only exact whole-tree
`DRT7` hit was an unrelated ignored `.venv` package checksum. The existing DRT
record and v156 proposal only used the `DRT_1` DefenseFinder subtype as
representative family-level evidence and made contextual sibling-subtype
mentions.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049400` | DRT7 system | `METPO:1023300` DRT system |

DRT7 system captures organism-level possession of the DRT subtype VII locus
represented by the pinned DefenseFinder HMM inventory with `DRT7__DRT7` and
`DRT7__DRT7_small` profiles and by the pinned rules table as the `DRT7`
subsystem. It excludes the broader DRT system, the individual DRT7
reverse-transcriptase profile rows, exact DRT7 RT products, exact DRT7 phage
triggers, host breadth, partner features, other DRT subtypes, source registry
rows that only name the broad `DRT` key, and other phage-defense systems.

`traitmech:000540` is a direct local child of `traitmech:000279` DRT system.
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
2. On mint, replace local `traitmech:000540` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000540` as traceability during the migration.

## Change Log

- v417, 2026-10: lifts `traitmech:000540 DRT7 system` into the
  `METPO:1049400` placeholder block.
