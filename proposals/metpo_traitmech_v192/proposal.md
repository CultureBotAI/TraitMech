# METPO ROBOT Template Proposal - Rugutis System (v192, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v191 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rugutis system, the
genome-level possession trait for a Rugutis anti-phage locus. Grafakou et al.
named Rugutis among seven novel lactococcal antiphage systems, DefenseFinder
maps the named Rugutis system to that discovery paper, and Mosterd et al. later
included Rugutis among the plasmid-encoded lactococcal phage-resistance systems
challenged in a phage escape-mutant screen.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rugutis |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026900` is reserved for this one-row class cohort. The v191 cohort used
`METPO:1026800`, so v192 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository
working tree outside `.git` and `.venv`. Rugutis occurred only in evidence
snippets on already curated sibling records and their writer scripts; no exact
same-scope record, `rugutis_system` slug, `traitmech:000315`,
`metpo_traitmech_v192`, or `METPO:1026900` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026900` | Rugutis system | `METPO:1016300` phage defense system |

Rugutis system captures genome-level possession of a named Rugutis locus
described among lactococcal plasmid-encoded phage-resistance systems and mapped
by DefenseFinder to the Grafakou et al. lactococcal plasmidome discovery paper.
It excludes individual Rugutis genes; Rugutis proteins; DefenseFinder
article-registry rows; source-database rows naming one Rugutis locus; unresolved
Rugutis triggers or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Rugutis-labeled genes and
proteins, the DefenseFinder registry row, and unresolved Rugutis molecular
outputs are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Rugutis synonym, no related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000315` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000315` as traceability during the migration.

## Change Log

- v192, 2026-09: lifts `traitmech:000315 Rugutis system` into the
  `METPO:1026900` block.
