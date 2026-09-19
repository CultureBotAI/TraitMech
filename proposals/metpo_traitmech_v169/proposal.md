# METPO ROBOT Template Proposal - Ukko System (v169, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v168 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ukko system, the
genome-level possession trait for a Ukko anti-phage locus. Mordret et al.
validated Ukko among six named Streptomyces antiphage defense systems, and
DefenseFinder catalogs Ukko with UkkA1, UkkA2, UkkB1, UkkB2, UkkC1, UkkC2,
UkkD1, and UkkD2 HMM profile entries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ukko |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024600` is reserved for this one-row class cohort. The v168 cohort used
`METPO:1024500`, so v169 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v169`, no live record used
`traitmech:000292`, and no prior proposal reserved `METPO:1024600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024600` | Ukko system | `METPO:1016300` phage defense system |

Ukko system captures genome-level possession of a Ukko locus cataloged by
DefenseFinder under a Ukko model namespace with UkkA1, UkkA2, UkkB1, UkkB2,
UkkC1, UkkC2, UkkD1, and UkkD2 HMM profile entries. It excludes individual
UkkA, UkkB, UkkC, and UkkD genes; UkkA, UkkB, UkkC, and UkkD proteins;
DefenseFinder HMM profiles; predicted source-database rows naming one Ukko
locus; unresolved Ukko trigger or effector activities; and other phage-defense
systems.

## External Mappings

No exact external mapping is proposed. UkkA, UkkB, UkkC, and UkkD genes, their
corresponding proteins, DefenseFinder HMMs, and unresolved Ukko molecular
outputs are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Ukko synonym, eight related Ukk source-profile labels, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000292` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000292` as traceability during the migration.

## Change Log

- v169, 2026-09: lifts `traitmech:000292 Ukko system` into the
  `METPO:1024600` block.
