# METPO ROBOT Template Proposal - Nantosuelta System (v161, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v160 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Nantosuelta system, the
genome-level possession trait for a Nantosuelta anti-phage locus. Darracq et
al. reported novel antiphage functions from Vibrio cholerae sedentary
chromosomal integron cassettes, and DefenseFinder models Nantosuelta with a
VCA0322 profile in its HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000284` was minted locally because METPO has no active exact Nantosuelta-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023800` is reserved for this one-row class cohort. The v160 cohort used
`METPO:1023700`, so v161 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v161`, no live record used
`traitmech:000284`, and no prior proposal reserved `METPO:1023800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023800` | Nantosuelta system | `METPO:1016300` phage defense system |

Nantosuelta system captures genome-level possession of a Nantosuelta locus
represented by the VCA0322 DefenseFinder profile. It excludes individual
VCA0322 genes; VCA0322 proteins; DefenseFinder HMM profiles; predicted
source-database rows naming one Nantosuelta locus; unresolved Nantosuelta
trigger or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. SCI cassette genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Nantosuelta molecular outputs are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Nantosuelta synonym, one related VCA0322 source-profile label, and no
  exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000284` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000284` as traceability during the migration.

## Change Log

- v161, 2026-09: lifts `traitmech:000284 Nantosuelta system` into the
  `METPO:1023800` block.
