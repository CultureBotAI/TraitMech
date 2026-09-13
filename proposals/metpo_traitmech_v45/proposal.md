# METPO ROBOT Template Proposal - Phenylalanine Arylamidase Activity (v45, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v44 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; phenylalanine
arylamidase activity remains absent from the local METPO snapshot and was still
absent from TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000168` was minted locally because METPO has no equivalent phenylalanine arylamidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1012200` is reserved for this one-row class cohort. The v44 cohort used
`METPO:1012100`, so v45 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1012200` had no hits, no prior
proposal reserved `metpo_traitmech_v45`, and no `traitmech:000168` or
phenylalanine arylamidase activity TraitRecord/proposal row existed before this
addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1012200` | phenylalanine arylamidase activity | `METPO:1000059` phenotype |

Phenylalanine arylamidase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, carboxylesterase, the
phosphatase activity records, leucine, valine, cystine, alanine, arginine,
prolyl, and pyrrolidonyl arylamidase activity, alpha-glucosidase activity,
beta-glucosidase activity, beta-galactosidase activity, alpha-galactosidase
activity, alpha-mannosidase activity, beta-glucuronidase activity,
alpha-fucosidase activity, lysine decarboxylase activity, ornithine
decarboxylase activity, beta-N-acetylhexosaminidase activity, trypsin activity,
alpha-chymotrypsin activity, gamma-glutamyltransferase activity, amylase
activity, pyrazinamidase activity, arginine dihydrolase activity, and
NAD-dependent alcohol dehydrogenase activity. The proposed term captures the
organismal enzyme-activity phenotype where a cell produces active
phenylalanine arylamidase enzymes that hydrolyze phenylalanine arylamide
substrates.

## External Mappings

No exact external mapping is proposed. `GO:0004177` names the broader
aminopeptidase molecular function rather than the organism-level phenylalanine
arylamidase production phenotype, so it remains a close causal-node grounding
lead and not an equivalent TraitRecord xref.

The source phrase `phenylalanine arylamidase` names an enzyme or diagnostic
panel row rather than an organismal phenotype, so it is retained as a related
synonym only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000168` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000168` as traceability during the migration.

## Change Log

- v45, 2026-09: lifts `traitmech:000168 phenylalanine arylamidase activity`
  into the `METPO:1012200` block.
