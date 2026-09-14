# METPO ROBOT Template Proposal - Photoferrotrophy (v70, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v69 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anoxygenic
phototrophic metabolism in which Fe(II) is the electron donor oxidized during
light-driven carbon fixation. This cohort lifts the local fallback record for
photoferrotrophy. The local TraitMech record is parented to both
`traitmech:000035` anoxygenic photosynthesis and `traitmech:000107` iron
oxidation; the proposal places it below the v5 placeholder
`METPO:1007634` anoxygenic photosynthesis and records the iron-oxidation
intersection in observations.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000193` was minted locally because METPO has no exact photoferrotrophy or anoxygenic phototrophic Fe(II) oxidation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014700` is reserved for this one-row class cohort. The v69 cohort used
`METPO:1014600`, so v70 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014700` appeared only in the v69
next-block reservation note, no prior proposal reserved `metpo_traitmech_v70`,
and no `traitmech:000193` or exact live `photoferrotrophy` TraitRecord/proposal
row existed before this addition. Exact `photoferrotrophy` mentions were limited
to an ungrounded causal node on the reviewed Photolithotrophic record, generated
pages and reports derived from that node, and research notes.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014700` | photoferrotrophy | `METPO:1007634` anoxygenic photosynthesis |

Photoferrotrophy is the anoxygenic photosynthesis branch in which Fe(II)
donates electrons during light-driven carbon fixation. The local TraitMech
record also parents the class to iron oxidation because the same trait is a
Fe(II)-oxidizing metabolism.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot has no active
photoferrotrophy class, and candidate GO classes for photosynthesis,
photosynthetic electron transport, and carbon fixation are broader than this
Fe(II)-donor organism-level metabolism.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  exact and related synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000193` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000193` as traceability during the migration.

## Change Log

- v70, 2026-09: lifts `traitmech:000193 photoferrotrophy` into the
  `METPO:1014700` block.
