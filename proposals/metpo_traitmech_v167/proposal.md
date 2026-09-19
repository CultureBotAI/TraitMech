# METPO ROBOT Template Proposal - Prithvi System (v167, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v166 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Prithvi system, the
genome-level possession trait for a Prithvi anti-phage locus. Mordret et al.
reported a protein- and genomic-language-model workflow that experimentally
validated Prithvi among six named Streptomyces antiphage defense systems, and
DefenseFinder catalogs Prithvi with a PtvA HMM profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Prithvi |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024400` is reserved for this one-row class cohort. The v166 cohort used
`METPO:1024300`, so v167 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v167`, no live record used
`traitmech:000290`, and no prior proposal reserved `METPO:1024400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024400` | Prithvi system | `METPO:1016300` phage defense system |

Prithvi system captures genome-level possession of a Prithvi locus cataloged by
DefenseFinder under a Prithvi model namespace with a PtvA HMM profile entry. It
excludes individual PtvA genes; PtvA proteins; DefenseFinder HMM profiles;
predicted source-database rows naming one Prithvi locus; unresolved Prithvi
trigger or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. PtvA genes, their corresponding proteins,
DefenseFinder HMMs, and unresolved Prithvi molecular outputs are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Prithvi synonym, one related PtvA source-profile label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000290` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000290` as traceability during the migration.

## Change Log

- v167, 2026-09: lifts `traitmech:000290 Prithvi system` into the
  `METPO:1024400` block.
