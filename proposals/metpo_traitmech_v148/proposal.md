# METPO ROBOT Template Proposal - Cernunnos System (v148, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v147 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Cernunnos system, the
genome-level possession trait for a Cernunnos anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Cernunnos with a VCA0410 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000271` was minted locally because METPO has no active exact Cernunnos-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022500` is reserved for this one-row class cohort. The v147 cohort used
`METPO:1022400`, so v148 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v148`, no live record used
`traitmech:000271`, and no prior proposal reserved `METPO:1022500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022500` | Cernunnos system | `METPO:1016300` phage defense system |

Cernunnos system captures genome-level possession of a Cernunnos locus
represented by a VCA0410 DefenseFinder profile. It excludes individual VCA0410
genes; VCA0410 proteins; DefenseFinder HMM profiles; predicted source-database
rows naming one Cernunnos locus; unresolved Cernunnos trigger or effector
activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0410 genes, the
corresponding proteins, DefenseFinder HMMs, and unresolved Cernunnos molecular
activities are shifted from this organism-level GENOMICS possession trait.

`VCA0410` is proposed as a related synonym, not an exact synonym, because it is
a source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Cernunnos source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000271` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000271` as traceability during the migration.

## Change Log

- v148, 2026-09: lifts `traitmech:000271 Cernunnos system` into the
  `METPO:1022500` block.
