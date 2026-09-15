# METPO ROBOT Template Proposal - Fumarate Respiration (v73, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v72 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anaerobic
respiration in which microorganisms use fumarate as the terminal electron
acceptor and reduce it to succinate for energy conservation. The snapshot has
only obsolete `Fumarate respiration`, so this cohort lifts the local fallback
record for fumarate respiration. The local TraitMech record is parented to
`METPO:1000802` anaerobic respiration; the proposal keeps that parent because
this is a same-axis specialization by non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000196` was minted locally because METPO has no active exact fumarate respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015000` is reserved for this one-row class cohort. The v72 cohort used
`METPO:1014900`, so v73 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `data/traits/`, `proposals/`,
`reports/`, `research/`, `history/`, `.claude/`, `docs/`, and ignored/hidden
files. No prior proposal reserved `metpo_traitmech_v73`, no live record used
`traitmech:000196`, and no prior proposal reserved `METPO:1015000`. The pinned
METPO snapshot contains only `obsolete Fumarate respiration`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015000` | fumarate respiration | `METPO:1000802` Anaerobic respiration |

Fumarate respiration is the fumarate-terminal-electron-acceptor branch of
anaerobic respiration. It captures organism-level respiratory use of fumarate
with succinate as the reduced product and excludes narrower terms for fumarate
reductase complexes or nonrespiratory fumarate reduction reactions.

## External Mappings

No exact external mapping is proposed. Candidate GO, Rhea, EC, and
protein-family terms for fumarate reductase describe the enzyme or its reaction
rather than the organism-level anaerobic respiration phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, one related synonym, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000196` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000196` as traceability during the migration.

## Change Log

- v73, 2026-09: lifts `traitmech:000196 fumarate respiration` into the
  `METPO:1015000` block.
