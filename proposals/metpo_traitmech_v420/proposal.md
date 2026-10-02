# METPO ROBOT Template Proposal - DRT1 System (v420, 2026-10)

## Summary

This cohort reserves `METPO:1049700` for `DRT1 system`, a DRT subtype
trait represented in the pinned DefenseFinder rules table as the `DRT_1`
subsystem with required `DRT_1__drt1a` and `DRT_1__drt1b` profiles.
The local TraitMech fallback is `traitmech:000543`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DRT1 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1049700` is reserved for this one-row class cohort. The v419 cohort used
`METPO:1049600`, so v420 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
the whole repository. It found no exact live TraitMech, METPO, history, or prior
proposal record for `traitmech:000543`, `METPO:1049700`,
`metpo_traitmech_v420`, `DRT1 system`, `DRT type 1`, or `DRT type I`.
It found `DRT_1`, `DRT_1__drt1a`, and `DRT_1__drt1b` only as
representative family-level evidence in the broad DRT record and its v156
upstream placeholder, not as a minted DRT1 subtype trait.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1049700` | DRT1 system | `METPO:1023300` DRT system |

DRT1 system captures organism-level possession of the DRT subtype I locus
represented by the pinned DefenseFinder HMM inventory with the
`DRT_1__drt1a` and `DRT_1__drt1b` named profiles and by the pinned rules
table as the `DRT_1` subsystem. It excludes the broader DRT system, the
individual DRT_1 reverse-transcriptase profile rows, exact DRT1 RT products,
exact DRT1 phage triggers, host breadth, partner-feature requirements,
profile-to-activity requirements, other DRT subtypes, source registry rows
that only name the broad `DRT` key, and other phage-defense systems.

`traitmech:000543` is a direct local child of `traitmech:000279` DRT system.
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
2. On mint, replace local `traitmech:000543` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000543` as traceability during the migration.

## Change Log

- v420, 2026-10: lifts `traitmech:000543 DRT1 system` into the
  `METPO:1049700` placeholder block.
