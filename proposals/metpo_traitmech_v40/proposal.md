# METPO ROBOT Template Proposal - Pyrazinamidase Activity (v40, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v39 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
pyrazinamidase activity remains absent from the local METPO snapshot and was
still absent from TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000163` was minted locally because METPO has no equivalent pyrazinamidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011700` is reserved for this one-row class cohort. The v39 cohort used
`METPO:1011600`, so v40 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1011700`,
`metpo_traitmech_v40`, `traitmech:000163`, or existing
pyrazinamidase/nicotinamidase activity TraitRecord/proposal row existed before
this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011700` | pyrazinamidase activity | `METPO:1000059` phenotype |

Pyrazinamidase activity is parallel to the existing diagnostic-enzyme
physiology records for catalase, oxidase, urease, coagulase, gelatinase,
caseinase, DNase, lipase, lecithinase, carboxylesterase, the phosphatase
activity records, leucine, valine, cystine, alanine, and pyrrolidonyl
arylamidase activity, alpha-glucosidase activity, beta-glucosidase activity,
beta-galactosidase activity, alpha-galactosidase activity,
alpha-mannosidase activity, beta-glucuronidase activity,
alpha-fucosidase activity, lysine decarboxylase activity, ornithine
decarboxylase activity, beta-N-acetylhexosaminidase activity, trypsin
activity, alpha-chymotrypsin activity, gamma-glutamyltransferase activity,
and amylase activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell produces active
nicotinamidase/pyrazinamidase enzymes that hydrolyze nicotinamide and can
convert pyrazinamide to pyrazinoic acid.

## External Mappings

No exact external mapping is proposed. `GO:0008936` names nicotinamidase
activity and was the exact molecular-function grounding for the source
`pyrazinamidase` node, but it denotes the catalytic molecular function rather
than the organism-level pyrazinamidase/nicotinamidase phenotype. It is
therefore appropriate as a causal-node grounding and not as an equivalent
TraitRecord xref.

The source phrases `nicotinamidase`, `nicotinamide amidohydrolase`, and
`nicotinamidase/pyrazinamidase` name enzymes rather than the full organismal
phenotype, so they are retained as related synonyms only.

The existing `antibiotic resistance` TraitRecord is also intentionally not an
exact match: that record captures a broad drug-survival disposition, while
pyrazinamidase activity captures a specific PncA enzyme-activity readout.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000163` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000163` as traceability during the migration.

## Change Log

- v40, 2026-09: lifts `traitmech:000163 pyrazinamidase activity` into the
  `METPO:1011700` block.
