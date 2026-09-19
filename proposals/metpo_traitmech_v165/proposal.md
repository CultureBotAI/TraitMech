# METPO ROBOT Template Proposal - Ceres System (v165, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v164 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ceres system, the
genome-level possession trait for a Ceres anti-phage locus. Mordret et al.
reported a protein- and genomic-language-model workflow that experimentally
validated Ceres among six named Streptomyces antiphage defense systems, and
DefenseFinder catalogs Ceres with CrsA1 and CrsA2 HMM profile entries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ceres |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024200` is reserved for this one-row class cohort. The v164 cohort used
`METPO:1024100`, so v165 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v165`, no live record used
`traitmech:000288`, and no prior proposal reserved `METPO:1024200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024200` | Ceres system | `METPO:1016300` phage defense system |

Ceres system captures genome-level possession of a Ceres locus cataloged by
DefenseFinder under a Ceres model namespace with CrsA1 and CrsA2 HMM profile
entries. It excludes individual CrsA genes; CrsA proteins; DefenseFinder HMM
profiles; predicted source-database rows naming one Ceres locus; unresolved
Ceres trigger or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. CrsA genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Ceres molecular outputs are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Ceres synonym, two related CrsA source-profile labels, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000288` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000288` as traceability during the migration.

## Change Log

- v165, 2026-09: lifts `traitmech:000288 Ceres system` into the
  `METPO:1024200` block.
