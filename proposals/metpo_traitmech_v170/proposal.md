# METPO ROBOT Template Proposal - Oshun System (v170, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v169 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Oshun system, the
genome-level possession trait for an Oshun anti-phage locus. Mordret et al.
validated Oshun among six named Streptomyces antiphage defense systems, and
DefenseFinder catalogs Oshun with an OsnA2 HMM profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Oshun |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024700` is reserved for this one-row class cohort. The v169 cohort used
`METPO:1024600`, so v170 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v170`, no live record used
`traitmech:000293`, and no prior proposal reserved `METPO:1024700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024700` | Oshun system | `METPO:1016300` phage defense system |

Oshun system captures genome-level possession of an Oshun locus cataloged by
DefenseFinder under an Oshun model namespace with an OsnA2 HMM profile entry.
It excludes individual OsnA2 genes; OsnA2 proteins; DefenseFinder HMM profiles;
predicted source-database rows naming one Oshun locus; unresolved Oshun trigger
or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. OsnA2 genes, OsnA2 proteins,
DefenseFinder HMMs, and unresolved Oshun molecular outputs are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Oshun synonym, one related OsnA2 source-profile label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000293` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000293` as traceability during the migration.

## Change Log

- v170, 2026-09: lifts `traitmech:000293 Oshun system` into the
  `METPO:1024700` block.
