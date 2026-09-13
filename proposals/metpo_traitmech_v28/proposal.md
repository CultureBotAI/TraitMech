# METPO ROBOT Template Proposal - Beta-Glucuronidase Activity (v28, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v27 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
beta-glucuronidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000151` was minted locally because METPO has no equivalent beta-glucuronidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010500` is reserved for this one-row class cohort. The v27 cohort used
`METPO:1010400`, so v28 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010500`,
`metpo_traitmech_v28`, `traitmech:000151`, or existing beta-glucuronidase
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010500` | beta-glucuronidase activity | `METPO:1000059` phenotype |

Beta-glucuronidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records,
leucine, valine, and cystine arylamidase activity, alpha-glucosidase activity,
beta-glucosidase activity, beta-galactosidase activity,
alpha-galactosidase activity, and alpha-mannosidase activity. The proposed term
captures the organismal enzyme-activity phenotype where a cell produces active
beta-glucuronidase enzymes that hydrolyze beta-D-glucuronosides to
D-glucuronate and an alcohol.

## External Mappings

No exact external mapping is proposed. `GO:0004566` denotes the
beta-glucuronidase catalytic molecular function rather than the organism-level
beta-glucuronidase production phenotype, so it is appropriate as a causal-node
grounding only when a graph needs the beta-glucuronidase catalytic activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000151` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000151` as traceability during the migration.

## Change Log

- v28, 2026-09: lifts `traitmech:000151 beta-glucuronidase activity` into the
  `METPO:1010500` block.
