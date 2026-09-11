# METPO ROBOT Template Proposal - Acid Phosphatase Activity (v19, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v18 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; acid
phosphatase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000142` was minted locally because METPO has no equivalent acid phosphatase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1009600` is reserved for this one-row class cohort. The v18 cohort used
`METPO:1009500`, so v19 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1009600`,
`metpo_traitmech_v19`, `traitmech:000142`, or existing `acid phosphatase
activity` TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1009600` | acid phosphatase activity | `METPO:1000059` phenotype |

Acid phosphatase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, and alkaline phosphatase activity. The
proposed term captures the organismal enzyme-activity phenotype where a cell
produces active acid phosphatase enzymes that dephosphorylate
phosphate-containing compounds under acidic conditions.

## External Mappings

No exact external mapping is proposed. `GO:0003993` denotes the acid
phosphatase molecular function rather than an exact organism-level acid
phosphatase production phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000142` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000142` as traceability during the migration.

## Change Log

- v19, 2026-09: lifts `traitmech:000142 acid phosphatase activity` into the
  `METPO:1009600` block.
