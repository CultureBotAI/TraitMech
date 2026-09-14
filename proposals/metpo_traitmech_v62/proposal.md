# METPO ROBOT Template Proposal - Akinete (v62, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v61 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for akinetes, the
spore-like dormant cells differentiated by filamentous Nostocales cyanobacteria.
This cohort lifts the local fallback record for the enlarged, thick-coated
cyanobacterial dormant-cell morphology.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000185` was minted locally because METPO has no active equivalent akinete class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013900` is reserved for this one-row class cohort. The v61 cohort used
`METPO:1013800`, so v62 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1013900` appeared only in the v61
next-block reservation note, no prior proposal reserved `metpo_traitmech_v62`,
and no `traitmech:000185` or exact live `akinete` TraitRecord/proposal row
existed before this addition. The search found only deprecated akinete classes
in the pinned METPO snapshot, including `METPO:1000012 obsolete akinete`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013900` | akinete | `METPO:1000059` phenotype |

Akinete is a cyanobacterial morphology trait in which a filamentous cell
differentiates an enlarged, thick-coated, spore-like dormant cell. The class is
kept separate from heterocysts, which are microoxic nitrogen-fixing cells, and
from endosporulation, which produces bacterial endospores by a distinct
developmental program.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
deprecated akinete classes, including `METPO:1000012 obsolete akinete`, which
cannot be reused for new TraitMech records. Broader dormancy or sporulation
classes are scope-shifted from the Nostocales dormant-cell morphology trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000185` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000185` as traceability during the migration.

## Change Log

- v62, 2026-09: lifts `traitmech:000185 akinete` into the
  `METPO:1013900` block.
