# METPO ROBOT Template Proposal - Gamma-Glutamyltransferase Activity (v37, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v36 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Physiology follow-up left diagnostic enzyme activities as reusable microbial
physiology candidates not yet represented as standalone TraitMech records. METPO
already carries catalase, oxidase, urease, and coagulase activity;
gamma-glutamyltransferase activity remains absent from the local METPO snapshot
and was still absent from TraitMech before this cohort minted a local fallback
class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000160` was minted locally because METPO has no equivalent gamma-glutamyltransferase activity class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1011400` is reserved for this one-row class cohort. The v36 cohort used
`METPO:1011300`, so v37 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. No `METPO:1011400`,
`metpo_traitmech_v37`, `traitmech:000160`, or existing
gamma-glutamyltransferase activity TraitRecord/proposal row existed before this
addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1011400` | gamma-glutamyltransferase activity | `METPO:1000059` phenotype |

Gamma-glutamyltransferase activity is parallel to the existing
diagnostic-enzyme physiology records for catalase, oxidase, urease, coagulase,
gelatinase, caseinase, DNase, lipase, lecithinase, carboxylesterase, the
phosphatase activity records, leucine, valine, cystine, and pyrrolidonyl
arylamidase activity, alpha-glucosidase activity, beta-glucosidase activity,
beta-galactosidase activity, alpha-galactosidase activity, alpha-mannosidase
activity, beta-glucuronidase activity, alpha-fucosidase activity, lysine
decarboxylase activity, ornithine decarboxylase activity,
beta-N-acetylhexosaminidase activity, trypsin activity, and
alpha-chymotrypsin activity. The proposed term captures the organismal
enzyme-activity phenotype where a cell exhibits
gamma-glutamyltransferase/glutathione-hydrolase activity on glutathione,
glutathione-S-conjugates, or related N-terminal L-gamma-glutamyl substrates.

## External Mappings

No exact external mapping is proposed. `GO:0003840` is the obsolete GO
gamma-glutamyltransferase activity class, and its replacement `GO:0036374`
denotes the molecular function glutathione gamma-glutamate hydrolase rather than
the organism-level gamma-glutamyltransferase/glutathione-hydrolase phenotype.
`GO:0036374` is appropriate as a causal-node grounding when a graph needs that
hydrolysis half-reaction, not as an equivalent TraitRecord xref.

The API Campy label `gamma-glutamyl transferase` and the enzyme names
`gamma-glutamyl transpeptidase` and `glutathione gamma-glutamate hydrolase` name
the enzyme or molecular function rather than the full organismal phenotype, so
they are retained as related synonyms only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000160` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000160` as traceability during the migration.

## Change Log

- v37, 2026-09: lifts `traitmech:000160 gamma-glutamyltransferase activity` into
  the `METPO:1011400` block.
