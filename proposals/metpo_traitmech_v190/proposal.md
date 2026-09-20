# METPO ROBOT Template Proposal - Aristaios System (v190, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v189 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Aristaios system, the
genome-level possession trait for an Aristaios anti-phage locus. Grafakou et
al. named Aristaios among seven novel lactococcal antiphage systems,
DefenseFinder maps the named Aristaios system to that discovery paper, and
Grafakou et al. later experimentally characterized Aristaios among three
plasmid-encoded lactococcal antiphage systems.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Aristaios |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026700` is reserved for this one-row class cohort. The v189 cohort used
`METPO:1026600`, so v190 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No exact search hit was found for `Aristaios system`, `aristaios_system`,
`traitmech:000313`, `metpo_traitmech_v190`, or `METPO:1026700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026700` | Aristaios system | `METPO:1016300` phage defense system |

Aristaios system captures genome-level possession of a named Aristaios locus
described among lactococcal plasmid-encoded phage-resistance systems and mapped
by DefenseFinder to the Grafakou et al. lactococcal plasmidome discovery paper.
It excludes individual Aristaios genes; Aristaios proteins; DefenseFinder
article-registry rows; source-database rows naming one Aristaios locus;
unresolved Aristaios triggers or effector activities; and other phage-defense
systems.

## External Mappings

No exact external mapping is proposed. Individual Aristaios-labeled genes and
proteins, the DefenseFinder registry row, and unresolved Aristaios molecular
outputs are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Aristaios synonym, no related shifted labels, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000313` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000313` as traceability during the migration.

## Change Log

- v190, 2026-09: lifts `traitmech:000313 Aristaios system` into the
  `METPO:1026700` block.
