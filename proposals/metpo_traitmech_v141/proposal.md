# METPO ROBOT Template Proposal - Sirona System (v141, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v140 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Sirona system, the
genome-level possession trait for a Sirona anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Sirona with a VCA0356 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000264` was minted locally because METPO has no active exact Sirona-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021800` is reserved for this one-row class cohort. The v140 cohort used
`METPO:1021700`, so v141 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v141`, no live record used
`traitmech:000264`, and no prior proposal reserved `METPO:1021800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021800` | Sirona system | `METPO:1016300` phage defense system |

Sirona system captures genome-level possession of a Sirona locus represented
by a VCA0356 DefenseFinder profile. It excludes individual VCA0356 genes;
VCA0356 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Sirona locus; unresolved Sirona trigger or effector activities; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0356 genes, VCA0356
proteins, DefenseFinder HMMs, and unresolved Sirona molecular activities are
shifted from this organism-level GENOMICS possession trait.

`VCA0356` is proposed as a related synonym, not an exact synonym, because it is
the source-profile label for the component HMM rather than a lexical name for
the organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  the related VCA0356 source-profile label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000264` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000264` as traceability during the migration.

## Change Log

- v141, 2026-09: lifts `traitmech:000264 Sirona system` into the
  `METPO:1021800` block.
