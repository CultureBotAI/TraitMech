# METPO ROBOT Template Proposal - Arginine Dihydrolase Activity (v41, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v40 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme and pathway activities as reusable
microbial physiology candidates not yet represented as standalone TraitMech
records. METPO already carries catalase, oxidase, urease, and coagulase
activity; arginine deiminase pathway activity remains absent from the local METPO
snapshot and was still absent from TraitMech before this cohort minted a local
fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000164` was minted locally because METPO has no equivalent arginine deiminase pathway activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011800` is reserved for this one-row class cohort. The v40 cohort used
`METPO:1011700`, so v41 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1011800` only appeared in
`.claude/skills/metpo-proposal/SKILL.md` as the next free block pointer after
v40; no prior proposal reserved the ID, and no `metpo_traitmech_v41`,
`traitmech:000164`, or arginine dihydrolase / arginine deiminase pathway
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011800` | arginine dihydrolase activity | `METPO:1000059` phenotype |

Arginine dihydrolase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, carboxylesterase, the phosphatase
activity records, leucine, valine, cystine, alanine, and pyrrolidonyl
arylamidase activity, alpha-glucosidase activity, beta-glucosidase activity,
beta-galactosidase activity, alpha-galactosidase activity,
alpha-mannosidase activity, beta-glucuronidase activity,
alpha-fucosidase activity, lysine decarboxylase activity, ornithine
decarboxylase activity, beta-N-acetylhexosaminidase activity, trypsin
activity, alpha-chymotrypsin activity, gamma-glutamyltransferase activity,
amylase activity, and pyrazinamidase activity. The proposed term captures the
organismal pathway-activity phenotype where a cell converts L-arginine through
the arginine deiminase pathway to generate ATP.

## External Mappings

No exact external mapping is proposed. `GO:0016990` names arginine deiminase
activity and corresponds to EC 3.5.3.6, the arginine deiminase reaction that
hydrolyzes L-arginine to L-citrulline and ammonia. That molecular function is
the first diagnostic step of the arginine deiminase pathway rather than the
full organism-level pathway-activity phenotype, so it remains a close
causal-node grounding lead and not an equivalent TraitRecord xref.

The source phrases `arginine dihydrolase` and `arginine deiminase` name the
first enzyme in the pathway rather than the full organismal phenotype, so they
are retained as related synonyms only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000164` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000164` as traceability during the migration.

## Change Log

- v41, 2026-09: lifts `traitmech:000164 arginine dihydrolase activity` into the
  `METPO:1011800` block.
