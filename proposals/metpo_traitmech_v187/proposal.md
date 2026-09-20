# METPO ROBOT Template Proposal - Kamadhenu System (v187, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v186 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Kamadhenu system, the
genome-level possession trait for a Kamadhenu anti-phage locus. Grafakou et al.
named Kamadhenu among seven novel lactococcal antiphage systems, DefenseFinder
maps the named Kamadhenu system to that discovery paper, and Mosterd et al.
later included Kamadhenu among the plasmid-encoded lactococcal phage-resistance
systems challenged in a phage escape-mutant screen.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Kamadhenu |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026400` is reserved for this one-row class cohort. The v186 cohort used
`METPO:1026300`, so v187 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No exact search hit was found for `Kamadhenu`, `kamadhenu_system`,
`traitmech:000310`, `metpo_traitmech_v187`, or `METPO:1026400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026400` | Kamadhenu system | `METPO:1016300` phage defense system |

Kamadhenu system captures genome-level possession of a named Kamadhenu locus
described among lactococcal plasmid-encoded phage-resistance systems and mapped
by DefenseFinder to the Grafakou et al. lactococcal plasmidome discovery paper.
It excludes individual Kamadhenu genes; Kamadhenu proteins; DefenseFinder
article-registry rows; source-database rows naming one Kamadhenu locus;
unresolved Kamadhenu triggers or effector activities; and other phage-defense
systems.

## External Mappings

No exact external mapping is proposed. Individual Kamadhenu-labeled genes and
proteins, the DefenseFinder registry row, and unresolved Kamadhenu molecular
outputs are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Kamadhenu synonym, no related shifted labels, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000310` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000310` as traceability during the migration.

## Change Log

- v187, 2026-09: lifts `traitmech:000310 Kamadhenu system` into the
  `METPO:1026400` block.
