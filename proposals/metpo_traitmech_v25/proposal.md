# METPO ROBOT Template Proposal - Beta-Galactosidase Activity (v25, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v24 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
beta-galactosidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000148` was minted locally because METPO has no equivalent beta-galactosidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010200` is reserved for this one-row class cohort. The v24 cohort used
`METPO:1010100`, so v25 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010200`,
`metpo_traitmech_v25`, `traitmech:000148`, or existing beta-galactosidase
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010200` | beta-galactosidase activity | `METPO:1000059` phenotype |

Beta-galactosidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records,
leucine, valine, and cystine arylamidase activity, alpha-glucosidase activity,
and beta-glucosidase activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell produces active beta-galactosidase
enzymes that hydrolyze lactose into glucose and galactose.

## External Mappings

No exact external mapping is proposed. `GO:0004565` carries the same
beta-galactosidase activity label but denotes the catalytic molecular function
rather than the organism-level beta-galactosidase production phenotype, so it
is appropriate as a causal-node grounding only when a graph needs the
beta-galactosidase catalytic activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000148` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000148` as traceability during the migration.

## Change Log

- v25, 2026-09: lifts `traitmech:000148 beta-galactosidase activity` into the
  `METPO:1010200` block.
