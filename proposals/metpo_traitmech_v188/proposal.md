# METPO ROBOT Template Proposal - Rhea System (v188, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v187 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rhea system, the
genome-level possession trait for a Rhea anti-phage locus. Grafakou et al. named
Rhea among seven novel lactococcal antiphage systems, DefenseFinder maps the
named Rhea system to that discovery paper, and Mosterd et al. later included
Rhea among the plasmid-encoded lactococcal phage-resistance systems challenged
in a phage escape-mutant screen.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rhea |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026500` is reserved for this one-row class cohort. The v187 cohort used
`METPO:1026400`, so v188 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No exact search hit was found for `Rhea system`, `rhea_system`,
`traitmech:000311`, `metpo_traitmech_v188`, or `METPO:1026500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026500` | Rhea system | `METPO:1016300` phage defense system |

Rhea system captures genome-level possession of a named Rhea locus described
among lactococcal plasmid-encoded phage-resistance systems and mapped by
DefenseFinder to the Grafakou et al. lactococcal plasmidome discovery paper. It
excludes individual Rhea genes; Rhea proteins; DefenseFinder article-registry
rows; source-database rows naming one Rhea locus; unresolved Rhea triggers or
effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Rhea-labeled genes and
proteins, the DefenseFinder registry row, and unresolved Rhea molecular outputs
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Rhea synonym, no related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000311` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000311` as traceability during the migration.

## Change Log

- v188, 2026-09: lifts `traitmech:000311 Rhea system` into the
  `METPO:1026500` block.
