# METPO ROBOT Template Proposal - Alpha-Fucosidase Activity (v29, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v28 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
alpha-fucosidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000152` was minted locally because METPO has no equivalent alpha-fucosidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010600` is reserved for this one-row class cohort. The v28 cohort used
`METPO:1010500`, so v29 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010600`,
`metpo_traitmech_v29`, `traitmech:000152`, or existing alpha-fucosidase
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010600` | alpha-fucosidase activity | `METPO:1000059` phenotype |

Alpha-fucosidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records,
leucine, valine, and cystine arylamidase activity, alpha-glucosidase activity,
beta-glucosidase activity, beta-galactosidase activity,
alpha-galactosidase activity, alpha-mannosidase activity, and
beta-glucuronidase activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell produces active alpha-fucosidase
enzymes that hydrolyze alpha-L-fucosides to L-fucose and an alcohol.

## External Mappings

No exact external mapping is proposed. `GO:0004560` denotes the
alpha-L-fucosidase catalytic molecular function rather than the organism-level
alpha-fucosidase production phenotype, so it is appropriate as a causal-node
grounding only when a graph needs the alpha-L-fucosidase catalytic activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000152` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000152` as traceability during the migration.

## Change Log

- v29, 2026-09: lifts `traitmech:000152 alpha-fucosidase activity` into the
  `METPO:1010600` block.
