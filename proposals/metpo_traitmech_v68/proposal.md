# METPO ROBOT Template Proposal - Acetoclastic methanogenesis (v68, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v67 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the microbial
methanogenesis branch in which methanogenic archaea split acetate into methane
and carbon dioxide. This cohort lifts the local fallback record for
acetoclastic methanogenesis and keeps it as a child of the reviewed
`METPO:1000844` Methanogenesis class, parallel to the existing local
hydrogenotrophic methanogenesis child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000191` was minted locally because METPO has no active equivalent acetoclastic methanogenesis class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014500` is reserved for this one-row class cohort. The v67 cohort used
`METPO:1014400`, so v68 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014500` appeared only in the v67
next-block reservation note, no prior proposal reserved `metpo_traitmech_v68`,
and no `traitmech:000191` or exact live `acetoclastic methanogenesis`
TraitRecord/proposal row existed before this addition. The search found only
the deprecated `METPO:1000865 obsolete Acetoclastic methanogenesis` class in
the pinned METPO snapshot, generated ROBOT copies of that obsolete class, the
ungrounded causal node on the reviewed Methanogenesis record, and historical
script and report references to that causal node.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014500` | acetoclastic methanogenesis | `METPO:1000844` Methanogenesis |

Acetoclastic methanogenesis is the methanogenesis branch in which acetate is
split into methane and carbon dioxide. The class is parented to Methanogenesis
because it is one of the substrate-defined archaeal methane-producing
pathways.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
the obsolete `METPO:1000865` class, and `GO:0015948` methane biosynthetic
process is exact only for the broader methanogenesis parent.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related acetate-use synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000191` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000191` as traceability during the migration.

## Change Log

- v68, 2026-09: lifts `traitmech:000191 acetoclastic methanogenesis` into the
  `METPO:1014500` block.
