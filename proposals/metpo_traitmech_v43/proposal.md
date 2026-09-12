# METPO ROBOT Template Proposal - Prolyl Aminopeptidase Activity (v43, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v42 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity; prolyl
aminopeptidase activity remains absent from the local METPO snapshot and was
still absent from TraitMech before this cohort minted a local fallback class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000166` was minted locally because METPO has no equivalent prolyl aminopeptidase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1012000` is reserved for this one-row class cohort. The v42 cohort used
`METPO:1011900`, so v43 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1012000` had no hits, no prior
proposal reserved `metpo_traitmech_v43`, and no `traitmech:000166` or
prolyl aminopeptidase activity TraitRecord/proposal row existed before this
addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1012000` | prolyl aminopeptidase activity | `METPO:1000059` phenotype |

Prolyl aminopeptidase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, carboxylesterase, the
phosphatase activity records, leucine, valine, cystine, alanine, and
pyrrolidonyl arylamidase activity, alpha-glucosidase activity,
beta-glucosidase activity, beta-galactosidase activity,
alpha-galactosidase activity, alpha-mannosidase activity,
beta-glucuronidase activity, alpha-fucosidase activity, lysine decarboxylase
activity, ornithine decarboxylase activity, beta-N-acetylhexosaminidase
activity, trypsin activity, alpha-chymotrypsin activity,
gamma-glutamyltransferase activity, amylase activity, pyrazinamidase activity,
arginine dihydrolase activity, and NAD-dependent alcohol dehydrogenase
activity. The proposed term captures the organismal enzyme-activity phenotype
where a cell produces active prolyl aminopeptidases that release N-terminal
proline residues from peptides.

## External Mappings

No exact external mapping is proposed. `GO:0004177` names the broader
aminopeptidase molecular function, and EC 3.4.11.5 defines the prolyl
aminopeptidase molecular function. Those identifiers denote molecule-level
catalytic activities rather than the organism-level production phenotype, so
they remain close causal-node grounding leads and not equivalent TraitRecord
xrefs.

The source phrases `proline aminopeptidase`, `Pro-X aminopeptidase`, `proline
iminopeptidase`, and `proline arylamidase` name enzymes or diagnostic panel
rows rather than organismal phenotypes, so they are retained as related synonyms
only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000166` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000166` as traceability during the migration.

## Change Log

- v43, 2026-09: lifts `traitmech:000166 prolyl aminopeptidase activity` into
  the `METPO:1012000` block.
