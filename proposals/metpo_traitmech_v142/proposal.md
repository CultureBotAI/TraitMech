# METPO ROBOT Template Proposal - Taranis System (v142, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v141 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Taranis system, the
genome-level possession trait for a Taranis anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Taranis with a VCA0396 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000265` was minted locally because METPO has no active exact Taranis-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021900` is reserved for this one-row class cohort. The v141 cohort used
`METPO:1021800`, so v142 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v142`, no live record used
`traitmech:000265`, and no prior proposal reserved `METPO:1021900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021900` | Taranis system | `METPO:1016300` phage defense system |

Taranis system captures genome-level possession of a Taranis locus represented
by a VCA0396 DefenseFinder profile. It excludes individual VCA0396 genes;
VCA0396 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Taranis locus; unresolved Taranis trigger or effector activities;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0396 genes, VCA0396
proteins, DefenseFinder HMMs, and unresolved Taranis molecular activities are
shifted from this organism-level GENOMICS possession trait.

`VCA0396` is proposed as a related synonym, not an exact synonym, because it is
the source-profile label for the component HMM rather than a lexical name for
the organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  the related VCA0396 source-profile label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000265` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000265` as traceability during the migration.

## Change Log

- v142, 2026-09: lifts `traitmech:000265 Taranis system` into the
  `METPO:1021900` block.
