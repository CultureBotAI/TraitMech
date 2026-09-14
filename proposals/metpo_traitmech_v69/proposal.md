# METPO ROBOT Template Proposal - Methyl-based methanogenesis (v69, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v68 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the archaeal
methanogenesis branch in which methylated compounds donate methyl groups for
reduction to methane. This cohort lifts the local fallback record for
methyl-based methanogenesis and keeps it as a child of the reviewed
`METPO:1000844` Methanogenesis class, parallel to the existing local
hydrogenotrophic and acetoclastic methanogenesis children.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000192` was minted locally because METPO has no active equivalent methyl-based methanogenesis class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014600` is reserved for this one-row class cohort. The v68 cohort used
`METPO:1014500`, so v69 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014600` appeared only in the v68
next-block reservation note, no prior proposal reserved `metpo_traitmech_v69`,
and no `traitmech:000192` or exact live `methyl-based methanogenesis`
TraitRecord/proposal row existed before this addition. The search found only
the deprecated `METPO:1000866` obsolete Methylotrophic methanogenesis class in
the pinned METPO snapshot, the ungrounded causal node on the reviewed
Methanogenesis record, and historical generated-page, script, and report
references to that causal node.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014600` | methyl-based methanogenesis | `METPO:1000844` Methanogenesis |

Methyl-based methanogenesis is the methanogenesis branch in which methylated
compounds donate methyl groups that are transferred to coenzyme M and reduced
to methane. The class is parented to Methanogenesis because it is one of the
substrate-defined archaeal methane-producing pathways.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
the obsolete `METPO:1000866` class, the existing `METPO:1000651` methylotrophic
class is a broader reduced-one-carbon trophic type, and `GO:0015948` methane
biosynthetic process is exact only for the broader methanogenesis parent.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  methyl-substrate related synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000192` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000192` as traceability during the migration.

## Change Log

- v69, 2026-09: lifts `traitmech:000192 methyl-based methanogenesis` into the
  `METPO:1014600` block.
