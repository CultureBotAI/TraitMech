# METPO ROBOT Template Proposal - DNase Activity (v15, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v14 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; DNase
activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000138` was minted locally because METPO has no equivalent DNase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1009200` is reserved for this one-row class cohort. The v14 cohort used
`METPO:1009100`, so v15 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1009200`,
`metpo_traitmech_v15`, `traitmech:000138`, or existing `DNase activity`
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1009200` | DNase activity | `METPO:1000059` phenotype |

DNase activity is parallel to the existing diagnostic-enzyme physiology records
for catalase, oxidase, urease, coagulase, gelatinase, and caseinase activity.
The proposed term captures the organismal enzyme-activity phenotype where a
cell produces active DNase enzymes that hydrolyze DNA.

## External Mappings

No exact external mapping is proposed. `GO:0004536` is a DNA nuclease molecular
function rather than an exact organism-level DNase production phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related-synonym column for `DNase production`.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000138` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000138` as traceability during the migration.

## Change Log

- v15, 2026-09: lifts `traitmech:000138 DNase activity` into the
  `METPO:1009200` block.
