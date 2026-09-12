# METPO ROBOT Template Proposal - Alpha-Chymotrypsin Activity (v36, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v35 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
alpha-chymotrypsin activity remains absent from the local METPO snapshot and was
still absent from TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000159` was minted locally because METPO has no equivalent alpha-chymotrypsin activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011300` is reserved for this one-row class cohort. The v35 cohort used
`METPO:1011200`, so v36 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1011300`,
`metpo_traitmech_v36`, `traitmech:000159`, or existing alpha-chymotrypsin
activity TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011300` | alpha-chymotrypsin activity | `METPO:1000059` phenotype |

Alpha-chymotrypsin activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, carboxylesterase, the phosphatase
activity records, leucine, valine, cystine, and pyrrolidonyl arylamidase
activity, alpha-glucosidase activity, beta-glucosidase activity,
beta-galactosidase activity, alpha-galactosidase activity, alpha-mannosidase
activity, beta-glucuronidase activity, alpha-fucosidase activity, lysine
decarboxylase activity, ornithine decarboxylase activity,
beta-N-acetylhexosaminidase activity, and trypsin activity. The proposed term
captures the organismal enzyme-activity phenotype where a cell produces active
alpha-chymotrypsin enzymes that preferentially cleave peptide bonds on the
carboxyl side of tyrosine, tryptophan, phenylalanine, or leucine residues.

## External Mappings

No exact external mapping is proposed. `GO:0004263` is the obsolete GO
chymotrypsin activity class, and its replacement `GO:0004252` denotes broader
serine-type endopeptidase molecular function rather than the organism-level
alpha-chymotrypsin production phenotype. `GO:0004252` is appropriate as a
causal-node grounding when a graph needs generic serine-type endopeptidase
activity, not as an equivalent TraitRecord xref.

The API strip label `alpha-chymotrypsin` names the enzyme rather than the full
organismal phenotype, so it is retained as a related synonym only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000159` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000159` as traceability during the migration.

## Change Log

- v36, 2026-09: lifts `traitmech:000159 alpha-chymotrypsin activity` into the
  `METPO:1011300` block.
