# METPO ROBOT Template Proposal - Beta-Glucosidase Activity (v23, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v22 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
beta-glucosidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000146` was minted locally because METPO has no equivalent beta-glucosidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010000` is reserved for this one-row class cohort. The v22 cohort used
`METPO:1009900`, so v23 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010000`,
`metpo_traitmech_v23`, `traitmech:000146`, or existing `beta-glucosidase
activity` TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010000` | beta-glucosidase activity | `METPO:1000059` phenotype |

Beta-glucosidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records, the
leucine and valine arylamidase activity records, and alpha-glucosidase
activity. The proposed term captures the organismal enzyme-activity phenotype
where a cell produces active beta-glucosidase enzymes that hydrolyze
beta-D-glucosidic bonds in beta-D-glucosides.

## External Mappings

No exact external mapping is proposed. `GO:0008422` denotes beta-D-glucosidase
activity at enzyme molecular-function scope rather than the organism-level
beta-glucosidase production phenotype, so it is appropriate as a causal-node
grounding rather than an equivalent TraitRecord xref.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000146` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000146` as traceability during the migration.

## Change Log

- v23, 2026-09: lifts `traitmech:000146 beta-glucosidase activity` into the
  `METPO:1010000` block.
