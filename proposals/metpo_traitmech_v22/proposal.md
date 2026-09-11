# METPO ROBOT Template Proposal - Alpha-Glucosidase Activity (v22, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v21 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
alpha-glucosidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000145` was minted locally because METPO has no equivalent alpha-glucosidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1009900` is reserved for this one-row class cohort. The v21 cohort used
`METPO:1009800`, so v22 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1009900`,
`metpo_traitmech_v22`, `traitmech:000145`, or existing `alpha-glucosidase
activity` TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1009900` | alpha-glucosidase activity | `METPO:1000059` phenotype |

Alpha-glucosidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records, and
the leucine and valine arylamidase activity records. The proposed term captures
the organismal enzyme-activity phenotype where a cell produces active
alpha-glucosidase enzymes that hydrolyze alpha-glucosidic bonds in
alpha-D-glucosides.

## External Mappings

No exact external mapping is proposed. `GO:0090599` carries the same
alpha-glucosidase activity label but denotes the enzyme molecular function
rather than the organism-level alpha-glucosidase production phenotype, so it is
appropriate as a causal-node grounding rather than an equivalent TraitRecord
xref.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000145` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000145` as traceability during the migration.

## Change Log

- v22, 2026-09: lifts `traitmech:000145 alpha-glucosidase activity` into the
  `METPO:1009900` block.
