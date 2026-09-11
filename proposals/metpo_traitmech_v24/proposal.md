# METPO ROBOT Template Proposal - Cystine Arylamidase Activity (v24, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v23 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; cystine
arylamidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000147` was minted locally because METPO has no equivalent cystine arylamidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010100` is reserved for this one-row class cohort. The v23 cohort used
`METPO:1010000`, so v24 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010100`,
`metpo_traitmech_v24`, `traitmech:000147`, or existing `cystine arylamidase
activity` TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010100` | cystine arylamidase activity | `METPO:1000059` phenotype |

Cystine arylamidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records,
leucine and valine arylamidase activity, alpha-glucosidase activity, and
beta-glucosidase activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell produces active cystine arylamidase
enzymes that hydrolyze cystine arylamide substrates.

## External Mappings

No exact external mapping is proposed. `GO:0004177` denotes aminopeptidase
activity at enzyme molecular-function scope and is broader than
cystine-residue-specific arylamidase activity, so it is appropriate as a
causal-node grounding only when a graph needs generic aminopeptidase activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000147` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000147` as traceability during the migration.

## Change Log

- v24, 2026-09: lifts `traitmech:000147 cystine arylamidase activity` into the
  `METPO:1010100` block.
