# METPO ROBOT Template Proposal - AbiH System (v181, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v180 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiH system, the
genome-level possession trait for an abiH-family abortive-infection locus.
Prevots et al. cloned the Lactococcus lactis S94 abiH gene and showed that it
encodes resistance by abortive infection to bacteriophage, and DefenseFinder
catalogs AbiH with a one-profile model.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiH |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025800` is reserved for this one-row class cohort. The v180 cohort used
`METPO:1025700`, so v181 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v181`, no live record used
`traitmech:000304`, and no prior proposal reserved `METPO:1025800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025800` | AbiH system | `METPO:1016800` abortive infection system |

AbiH system captures genome-level possession of an abiH-family locus
represented by the DefenseFinder AbiH__AbiH profile and exemplified by the
Lactococcus lactis S94 abiH gene that encodes lactococcal phage
abortive-infection resistance. It excludes the individual `abiH` gene; AbiH
proteins; the DefenseFinder `AbiH__AbiH` HMM profile; the Pfam profile used by
that model; individual lactococcal phage host-range outcomes; unresolved AbiH
triggers, targets, and arrest routes; and generic abortive infection systems.

## External Mappings

No exact external mapping is proposed. AbiH, AbiH proteins, the
DefenseFinder HMM row, and the PF14253 profile are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related AbiH synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000304` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000304` as traceability during the migration.

## Change Log

- v181, 2026-09: lifts `traitmech:000304 AbiH system` into the
  `METPO:1025800` block.
