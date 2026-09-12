# METPO ROBOT Template Proposal - Glutamyl Glutamic Acid Arylamidase Activity (v50, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v49 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; glutamyl
glutamic acid arylamidase activity remains absent from the local METPO snapshot
and was still absent from TraitMech before this cohort minted a local fallback
class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000173` was minted locally because METPO has no equivalent glutamyl glutamic acid arylamidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1012700` is reserved for this one-row class cohort. The v49 cohort used
`METPO:1012600`, so v50 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1012700` appeared only in
the v49 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v50`, and no `traitmech:000173` or glutamyl glutamic acid
arylamidase activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1012700` | glutamyl glutamic acid arylamidase activity | `METPO:1000059` phenotype |

Glutamyl glutamic acid arylamidase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, carboxylesterase, the
phosphatase activity records, leucine, valine, cystine, alanine, arginine,
phenylalanine, tyrosine, glycine, histidine, serine, prolyl, and pyrrolidonyl
arylamidase activity, alpha-glucosidase activity, beta-glucosidase activity,
beta-galactosidase activity, alpha-galactosidase activity,
alpha-mannosidase activity, beta-glucuronidase activity,
alpha-fucosidase activity, lysine decarboxylase activity, ornithine
decarboxylase activity, beta-N-acetylhexosaminidase activity, trypsin activity,
alpha-chymotrypsin activity, gamma-glutamyltransferase activity, amylase
activity, pyrazinamidase activity, arginine dihydrolase activity, and
NAD-dependent alcohol dehydrogenase activity. The proposed term captures the
organismal enzyme-activity phenotype where a cell produces active glutamyl
glutamic acid arylamidase enzymes that hydrolyze glutamyl-glutamic-acid
arylamide substrates.

## External Mappings

No exact external mapping is proposed. `GO:0004177` names the broader
aminopeptidase molecular function rather than the organism-level glutamyl
glutamic acid arylamidase production phenotype, so it remains a close
causal-node grounding lead and not an equivalent TraitRecord xref.

The source phrase `glutamyl glutamic acid arylamidase` names an enzyme or
diagnostic panel row rather than an organismal phenotype, so it is retained as a
related synonym only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000173` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000173` as traceability during the migration.

## Change Log

- v50, 2026-09: lifts `traitmech:000173 glutamyl glutamic acid arylamidase
  activity` into the `METPO:1012700` block.
