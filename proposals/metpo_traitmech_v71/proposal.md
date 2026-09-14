# METPO ROBOT Template Proposal - Aerobic Anoxygenic Phototrophy (v71, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v70 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the aerobic
photoheterotrophy in which bacteria harvest light with
bacteriochlorophyll-containing reaction centers while requiring organic carbon
substrates for growth. This cohort lifts the local fallback record for aerobic
anoxygenic phototrophy. The local TraitMech record is parented to
`METPO:1000657` photoheterotrophic, `traitmech:000035` anoxygenic
photosynthesis, and `METPO:1000602` aerobic; the proposal places it below
photoheterotrophic as the closest active METPO-owned parent and records the
anoxygenic reaction-center and aerobic boundaries in observations.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000194` was minted locally because METPO has no exact aerobic anoxygenic phototrophy class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014800` is reserved for this one-row class cohort. The v70 cohort used
`METPO:1014700`, so v71 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `data/traits/`, `proposals/`,
`reports/`, `research/`, `history/`, `.claude/`, `docs/`, and ignored/hidden
files. No prior proposal reserved `metpo_traitmech_v71`, no live record used
`traitmech:000194`, and no prior proposal reserved `METPO:1014800`. The pinned
METPO snapshot stores `aerobic_anoxygenic_phototrophy` only as a related synonym
on broad `METPO:1000660` phototrophic; this branch moves that source key onto
the new same-scope TraitMech record.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014800` | aerobic anoxygenic phototrophy | `METPO:1000657` photoheterotrophic |

Aerobic anoxygenic phototrophy is the aerobic
bacteriochlorophyll-reaction-center branch of photoheterotrophy. It excludes
anaerobic purple and green sulfur bacterial phototrophy and
proteorhodopsin-only photoheterotrophy.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot has no active
aerobic anoxygenic phototrophy class, and candidate GO photosynthetic electron
transport classes denote intracellular pathways rather than this aerobic
organism-level photoheterotrophic trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  exact and related synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000194` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000194` as traceability during the migration.

## Change Log

- v71, 2026-09: lifts `traitmech:000194 aerobic anoxygenic phototrophy` into
  the `METPO:1014800` block.
