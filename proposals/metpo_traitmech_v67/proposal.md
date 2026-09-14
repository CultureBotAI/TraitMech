# METPO ROBOT Template Proposal - Lipolysis (v67, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v66 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the microbial
metabolism trait in which a microorganism hydrolyzes triacylglycerols into
fatty acids and glycerol through lipase-catalyzed ester cleavage. This cohort
lifts the local fallback record for lipolysis and keeps it separate from
organismal lipase activity assay traits, which model the phenotype of showing
lipase enzyme activity rather than the lipid-hydrolysis metabolism itself.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000190` was minted locally because METPO has no active equivalent lipolysis class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014400` is reserved for this one-row class cohort. The v66 cohort used
`METPO:1014300`, so v67 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014400` appeared only in the v66
next-block reservation note, no prior proposal reserved `metpo_traitmech_v67`,
and no `traitmech:000190` or exact live `lipolysis` or `lipid degradation`
TraitRecord/proposal row existed before this addition. The search found only
the deprecated `METPO:1000175 obsolete lipolysis` class in the pinned METPO
snapshot, generated ROBOT copies of that obsolete class, an old proposal
follow-up footnote, and lipolysis boundary notes in research artifacts.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014400` | lipolysis | `METPO:1000060` metabolism |

Lipolysis is a metabolism in which a microorganism hydrolyzes
triacylglycerols into fatty acids and glycerol through lipase-catalyzed ester
cleavage. The class is parented to metabolism because microbial lipases
catalyze triacylglycerol hydrolysis as an extracellular or cell-associated
metabolic activity.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
the obsolete `METPO:1000175` class, `GO:0016298` denotes lipase molecular
function activity rather than the organism-level microbial lipolysis trait, and
GO lipid catabolic process classes are broader than triacylglycerol hydrolysis.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with an
  exact triacylglycerol hydrolysis synonym, one related microbial-lipolysis
  label, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000190` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000190` as traceability during the migration.

## Change Log

- v67, 2026-09: lifts `traitmech:000190 lipolysis` into the
  `METPO:1014400` block.
