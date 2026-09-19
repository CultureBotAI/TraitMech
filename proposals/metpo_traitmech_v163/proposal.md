# METPO ROBOT Template Proposal - Ogmios System (v163, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v162 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ogmios system, the
genome-level possession trait for an Ogmios anti-phage locus. Darracq et al.
reported novel antiphage functions from Vibrio cholerae sedentary chromosomal
integron cassettes, and DefenseFinder models Ogmios with a VCA0308 profile in
its HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ogmios |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024000` is reserved for this one-row class cohort. The v162 cohort used
`METPO:1023900`, so v163 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v163`, no live record used
`traitmech:000286`, and no prior proposal reserved `METPO:1024000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024000` | Ogmios system | `METPO:1016300` phage defense system |

Ogmios system captures genome-level possession of an Ogmios locus represented
by the VCA0308 DefenseFinder profile. It excludes individual VCA0308 genes;
VCA0308 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Ogmios locus; unresolved Ogmios trigger or effector activities; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. SCI cassette genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Ogmios molecular outputs are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Ogmios synonym, one related VCA0308 source-profile label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000286` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000286` as traceability during the migration.

## Change Log

- v163, 2026-09: lifts `traitmech:000286 Ogmios system` into the
  `METPO:1024000` block.
