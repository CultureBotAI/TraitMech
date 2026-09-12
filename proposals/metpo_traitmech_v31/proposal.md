# METPO ROBOT Template Proposal - Ornithine Decarboxylase Activity (v31, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v30 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; ornithine
decarboxylase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000154` was minted locally because METPO has no equivalent ornithine decarboxylase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010800` is reserved for this one-row class cohort. The v30 cohort used
`METPO:1010700`, so v31 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010800`,
`metpo_traitmech_v31`, `traitmech:000154`, or existing ornithine decarboxylase
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010800` | ornithine decarboxylase activity | `METPO:1000059` phenotype |

Ornithine decarboxylase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, the phosphatase activity
records, leucine, valine, and cystine arylamidase activity,
alpha-glucosidase activity, beta-glucosidase activity, beta-galactosidase
activity, alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, and lysine
decarboxylase activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell produces active ornithine
decarboxylase enzymes that decarboxylate L-ornithine to putrescine and carbon
dioxide.

## External Mappings

No exact external mapping is proposed. `GO:0004586` denotes the ornithine
decarboxylase catalytic molecular function rather than the organism-level
ornithine decarboxylase production phenotype, so it is appropriate as a
causal-node grounding only when a graph needs the ornithine decarboxylase
catalytic activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000154` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000154` as traceability during the migration.

## Change Log

- v31, 2026-09: lifts `traitmech:000154 ornithine decarboxylase activity` into the
  `METPO:1010800` block.
