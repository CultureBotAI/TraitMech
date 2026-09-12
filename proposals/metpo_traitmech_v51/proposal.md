# METPO ROBOT Template Proposal - Naphthol-AS-BI-Phosphohydrolase Activity (v51, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v50 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
naphthol-AS-BI-phosphohydrolase activity remains absent from the local METPO
snapshot and was still absent from TraitMech before this cohort minted a local
fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000174` was minted locally because METPO has no equivalent naphthol-AS-BI-phosphohydrolase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1012800` is reserved for this one-row class cohort. The v50 cohort used
`METPO:1012700`, so v51 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1012800` appeared only in
the v50 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v51`, and no `traitmech:000174` or
naphthol-AS-BI-phosphohydrolase activity TraitRecord/proposal row existed
before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1012800` | naphthol-AS-BI-phosphohydrolase activity | `METPO:1000059` phenotype |

Naphthol-AS-BI-phosphohydrolase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, carboxylesterase, acid
phosphatase activity, alkaline phosphatase activity, leucine, valine, cystine,
alanine, arginine, phenylalanine, tyrosine, glycine, histidine, serine, and
pyrrolidonyl arylamidase activity, prolyl aminopeptidase activity,
alpha-glucosidase activity, beta-glucosidase activity, beta-galactosidase
activity, alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, lysine decarboxylase
activity, ornithine decarboxylase activity, beta-N-acetylhexosaminidase
activity, trypsin activity, alpha-chymotrypsin activity,
gamma-glutamyltransferase activity, amylase activity, pyrazinamidase activity,
arginine dihydrolase activity, NAD-dependent alcohol dehydrogenase activity,
and glutamyl glutamic acid arylamidase activity. The proposed term captures the
organismal enzyme-activity phenotype where a cell produces active
phosphohydrolases that hydrolyze naphthol-AS-BI-phosphate substrates.

## External Mappings

No exact external mapping is proposed. `GO:0016791` names the broader
phosphatase molecular function rather than the organism-level
naphthol-AS-BI-phosphate-specific phosphohydrolase production phenotype, so it
remains a close causal-node grounding lead and not an equivalent TraitRecord
xref.

The source phrase `naphthol-AS-BI-phosphohydrolase` names an enzyme-panel row
or chromogenic-substrate readout rather than an organismal phenotype, so it is
retained as a related synonym only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000174` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000174` as traceability during the migration.

## Change Log

- v51, 2026-09: lifts `traitmech:000174 naphthol-AS-BI-phosphohydrolase
  activity` into the `METPO:1012800` block.
