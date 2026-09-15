# METPO ROBOT Template Proposal - Arsenate Respiration (v72, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v71 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anaerobic
respiration in which microorganisms use arsenate, As(V), as the terminal
electron acceptor and reduce it to arsenite, As(III), for energy conservation.
This cohort lifts the local fallback record for arsenate respiration. The local
TraitMech record is parented to `METPO:1000802` anaerobic respiration; the
proposal keeps that parent because this is a same-axis specialization by
non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000195` was minted locally because METPO has no exact arsenate respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014900` is reserved for this one-row class cohort. The v71 cohort used
`METPO:1014800`, so v72 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `data/traits/`, `proposals/`,
`reports/`, `research/`, `history/`, `.claude/`, `docs/`, and ignored/hidden
files. No prior proposal reserved `metpo_traitmech_v72`, no live record used
`traitmech:000195`, and no prior proposal reserved `METPO:1014900`. The pinned
METPO snapshot contains only `obsolete Arsenate reduction` and `obsolete
Arsenate-reducing`, which are broader and ambiguous between ArrAB-dependent
respiration and ArsC-dependent cytosolic detoxification.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014900` | arsenate respiration | `METPO:1000802` Anaerobic respiration |

Arsenate respiration is the As(V)-terminal-electron-acceptor branch of
anaerobic respiration. It captures organism-level respiratory growth with
arsenate and excludes ArsC-mediated arsenate reduction that feeds the arsenite
efflux detoxification route.

## External Mappings

No exact external mapping is proposed. Candidate GO, Rhea, EC, and
protein-family terms for respiratory arsenate reductase describe the ArrAB
enzyme or its reaction rather than the organism-level anaerobic respiration
phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with an
  exact synonym, a related synonym, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000195` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000195` as traceability during the migration.

## Change Log

- v72, 2026-09: lifts `traitmech:000195 arsenate respiration` into the
  `METPO:1014900` block.
