# METPO ROBOT Template Proposal - Fliodhais System (v203, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v202 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Fliodhais system, the
genome-level possession trait for a two-component Fliodhais anti-phage locus.
Grafakou et al. named Fliodhais among seven novel lactococcal antiphage
systems, reported that both Fliodhais genetic components were necessary for
activity, and described Fliodhais-associated reduction of phage c2 plaque
development. DefenseFinder maps the named Fliodhais system to the Grafakou et
al. lactococcal plasmidome discovery paper.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Fliodhais |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028000` is reserved for this one-row class cohort. The v202 cohort used
`METPO:1027900`, so v203 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `fliodhais_system` slug, `Fliodhais
system` label, `traitmech:000326`, `metpo_traitmech_v203`, or `METPO:1028000`
was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028000` | Fliodhais system | `METPO:1016300` phage defense system |

Fliodhais system captures genome-level possession of a two-component
Fliodhais locus described among lactococcal plasmid-encoded phage-resistance
systems and mapped by DefenseFinder to the Grafakou et al. lactococcal
plasmidome discovery paper. It excludes individual Fliodhais genes; Fliodhais
proteins; DefenseFinder article-registry rows; source-database rows naming one
Fliodhais locus; the c2 plaque morphology itself; unresolved Fliodhais triggers
or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Fliodhais genes and proteins,
the DefenseFinder registry row, the c2 plaque phenotype, and unresolved
Fliodhais molecular outputs are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Fliodhais synonym, no related shifted labels, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000326` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000326` as traceability during the migration.

## Change Log

- v203, 2026-09: lifts `traitmech:000326 Fliodhais system` into the
  `METPO:1028000` block.
