# METPO ROBOT Template Proposal - Brigantia System (v147, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v146 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Brigantia system, the
genome-level possession trait for a Brigantia anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Brigantia with a VCA0419 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000270` was minted locally because METPO has no active exact Brigantia-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022400` is reserved for this one-row class cohort. The v146 cohort used
`METPO:1022300`, so v147 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v147`, no live record used
`traitmech:000270`, and no prior proposal reserved `METPO:1022400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022400` | Brigantia system | `METPO:1016300` phage defense system |

Brigantia system captures genome-level possession of a Brigantia locus
represented by a VCA0419 DefenseFinder profile. It excludes individual VCA0419
genes; VCA0419 proteins; DefenseFinder HMM profiles; predicted source-database
rows naming one Brigantia locus; unresolved Brigantia trigger or effector
activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0419 genes, the
corresponding proteins, DefenseFinder HMMs, and unresolved Brigantia molecular
activities are shifted from this organism-level GENOMICS possession trait.

`VCA0419` is proposed as a related synonym, not an exact synonym, because it is
a source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Brigantia source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000270` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000270` as traceability during the migration.

## Change Log

- v147, 2026-09: lifts `traitmech:000270 Brigantia system` into the
  `METPO:1022400` block.
