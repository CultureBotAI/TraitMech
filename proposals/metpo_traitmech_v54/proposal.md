# METPO ROBOT Template Proposal - Specialist (v54, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v53 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

TraitMech has a seeded METPO record for `generalist` (`METPO:1005040`), but
the pinned METPO snapshot has no exact reciprocal class for the specialist
niche-breadth phenotype. Specialist/generalist contrasts recur in the tracked
TraitMech research corpus, and the proposed class gives the narrow ecological
niche phenotype the same first-class shape as `generalist`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000177` was minted locally because METPO has no equivalent specialist class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013100` is reserved for this one-row class cohort. The v53 cohort used
`METPO:1013000`, so v54 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013100` appeared only in the
v53 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v54`, and no `traitmech:000177` or exact specialist
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013100` | specialist | `METPO:1000059` phenotype |

`specialist` is the narrow-niche complement to `generalist`: the record covers
organisms restricted to a limited resource, habitat, host, or environmental
range, not one-axis child phenotypes such as `stenohaline` or contextual
phrases such as pH-specialist growth determinants.

## External Mappings

No exact external ontology mapping is asserted.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related synonym column.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000177` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000177` as traceability during the migration.

## Change Log

- v54, 2026-09: lifts `traitmech:000177 specialist` into the
  `METPO:1013100` block.
