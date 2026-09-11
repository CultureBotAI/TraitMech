# METPO ROBOT Template Proposal - Lipase Activity (v16, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v15 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; lipase
activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000139` was minted locally because METPO has no equivalent lipase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1009300` is reserved for this one-row class cohort. The v15 cohort used
`METPO:1009200`, so v16 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1009300`,
`metpo_traitmech_v16`, `traitmech:000139`, or existing `lipase activity`
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1009300` | lipase activity | `METPO:1000059` phenotype |

Lipase activity is parallel to the existing diagnostic-enzyme physiology records
for catalase, oxidase, urease, coagulase, gelatinase, caseinase, and DNase
activity. The proposed term captures the organismal enzyme-activity phenotype
where a cell produces active lipases that hydrolyze triglycerides at
lipid-water interfaces.

## External Mappings

No exact external mapping is proposed. `GO:0016298` is a lipase molecular
function rather than an exact organism-level lipase production phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related-synonym column for `lipase production` and `lipolytic activity`.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000139` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000139` as traceability during the migration.

## Change Log

- v16, 2026-09: lifts `traitmech:000139 lipase activity` into the
  `METPO:1009300` block.
