# METPO ROBOT Template Proposal - Holdfast (v61, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v60 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the bacterial holdfast
adhesin, so this cohort lifts the local fallback record for the localized polar
adhesive matrix produced by stalked Caulobacterales cells.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000184` was minted locally because METPO has no active equivalent bacterial holdfast class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013800` is reserved for this one-row class cohort. The v60 cohort used
`METPO:1013700`, so v61 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1013800` appeared only in the v60
next-block reservation note, no prior proposal reserved `metpo_traitmech_v61`,
and no `traitmech:000184` or exact holdfast TraitRecord/proposal row existed
before this addition. The search found only the deprecated
`METPO:1000158 obsolete holdfast` class in the pinned METPO snapshot.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013800` | holdfast | `METPO:1000059` phenotype |

Holdfast is a bacterial morphology trait in which cells produce a localized
polar adhesive matrix that mediates permanent attachment to surfaces. The class
denotes the adhesive matrix itself, not prosthecae or stalks that may carry it
at their tips.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
`METPO:1000158 obsolete holdfast`, which is deprecated and cannot be reused for
new TraitMech records. Broader cell-adhesion or biofilm-formation process terms
are scope-shifted from the holdfast adhesive matrix.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  one related synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000184` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000184` as traceability during the migration.

## Change Log

- v61, 2026-09: lifts `traitmech:000184 holdfast` into the
  `METPO:1013800` block.
