# METPO ROBOT Template Proposal - Carboxylesterase Activity (v33, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v32 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
carboxylesterase activity remains absent from the local METPO snapshot and was
still absent from TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000156` was minted locally because METPO has no equivalent carboxylesterase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011000` is reserved for this one-row class cohort. The v32 cohort used
`METPO:1010900`, so v33 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1011000`,
`metpo_traitmech_v33`, `traitmech:000156`, or existing carboxylesterase activity
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011000` | carboxylesterase activity | `METPO:1000059` phenotype |

Carboxylesterase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, the phosphatase activity records,
leucine, valine, cystine, and pyrrolidonyl arylamidase activity,
alpha-glucosidase activity, beta-glucosidase activity, beta-galactosidase
activity, alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, lysine decarboxylase
activity, and ornithine decarboxylase activity. The proposed term captures the
organismal enzyme-activity phenotype where a cell produces active
carboxylesterase enzymes that hydrolyze carboxylic esters.

## External Mappings

No exact external mapping is proposed. `GO:0106435` denotes the
carboxylesterase molecular function rather than the organism-level
carboxylesterase production phenotype, so it is appropriate as a causal-node
grounding only when a graph needs the catalytic activity.

API strip labels such as `esterase (C 4)`, `esterase lipase (C 8)`, and
`lipase (C 14)` are chain-length assay readouts, not exact organismal
phenotype names. They are retained as related synonyms in the METPO proposal
only so source-system labels remain searchable without over-narrowing the
TraitMech label.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000156` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000156` as traceability during the migration.

## Change Log

- v33, 2026-09: lifts `traitmech:000156 carboxylesterase activity` into the
  `METPO:1011000` block.
