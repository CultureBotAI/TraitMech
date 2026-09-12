# METPO ROBOT Template Proposal - Trypsin Activity (v35, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v34 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; trypsin
activity remains absent from the local METPO snapshot and was still absent from
TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000158` was minted locally because METPO has no equivalent trypsin activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011200` is reserved for this one-row class cohort. The v34 cohort used
`METPO:1011100`, so v35 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1011200`,
`metpo_traitmech_v35`, `traitmech:000158`, or existing trypsin activity
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011200` | trypsin activity | `METPO:1000059` phenotype |

Trypsin activity is parallel to the existing diagnostic-enzyme physiology
records for catalase, oxidase, urease, coagulase, gelatinase, caseinase, DNase,
lipase, lecithinase, carboxylesterase, the phosphatase activity records,
leucine, valine, cystine, and pyrrolidonyl arylamidase activity,
alpha-glucosidase activity, beta-glucosidase activity, beta-galactosidase
activity, alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, lysine decarboxylase
activity, ornithine decarboxylase activity, and
beta-N-acetylhexosaminidase activity. The proposed term captures the
organismal enzyme-activity phenotype where a cell exhibits trypsin-like serine
endopeptidase activity, preferentially cleaving peptide bonds on the carboxyl
side of arginine or lysine residues.

## External Mappings

No exact external mapping is proposed. `GO:0004295` is the obsolete GO trypsin
activity class, and its replacement `GO:0004252` denotes broader serine-type
endopeptidase molecular function rather than the organism-level trypsin-like
serine endopeptidase phenotype. `GO:0004252` is appropriate as a causal-node
grounding when a graph needs generic serine-type endopeptidase activity, not as
an equivalent TraitRecord xref.

The API strip label `trypsin` names the enzyme rather than the full organismal
phenotype, so it is retained as a related synonym only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000158` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000158` as traceability during the migration.

## Change Log

- v35, 2026-09: lifts `traitmech:000158 trypsin activity` into the
  `METPO:1011200` block.
