# METPO ROBOT Template Proposal - Pyrrolidonyl Arylamidase Activity (v32, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v31 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; pyrrolidonyl
arylamidase activity remains absent from the local METPO snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000155` was minted locally because METPO has no equivalent pyrrolidonyl arylamidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1010900` is reserved for this one-row class cohort. The v31 cohort used
`METPO:1010800`, so v32 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1010900`,
`metpo_traitmech_v32`, `traitmech:000155`, or existing pyrrolidonyl arylamidase
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1010900` | pyrrolidonyl arylamidase activity | `METPO:1000059` phenotype |

Pyrrolidonyl arylamidase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, the phosphatase activity
records, leucine, valine, and cystine arylamidase activity,
alpha-glucosidase activity, beta-glucosidase activity, beta-galactosidase
activity, alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, lysine
decarboxylase activity, and ornithine decarboxylase activity. The proposed term
captures the organismal enzyme-activity phenotype where a cell produces active
pyrrolidonyl arylamidase enzymes that release N-terminal pyroglutamyl groups
from peptide substrates.

## External Mappings

No exact external mapping is proposed. `GO:0016920` denotes the
pyroglutamyl-peptidase molecular function rather than the organism-level
pyrrolidonyl arylamidase production phenotype, so it is appropriate as a
causal-node grounding only when a graph needs the pyroglutamyl-peptidase
catalytic activity.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000155` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000155` as traceability during the migration.

## Change Log

- v32, 2026-09: lifts `traitmech:000155 pyrrolidonyl arylamidase activity` into
  the `METPO:1010900` block.
