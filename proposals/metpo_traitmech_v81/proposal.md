# METPO ROBOT Template Proposal - Organohalide Respiration (v81, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v80 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anaerobic
respiration in which microorganisms use organohalides as terminal electron
acceptors for energy conservation. It only contains obsolete
`METPO:1000850` Halogenated compound respiration and obsolete `METPO:1000851`
Organohalide respiration classes. This cohort lifts the local fallback record
for organohalide respiration. The local TraitMech record is parented to
`METPO:1000802` anaerobic respiration; the proposal keeps that parent because
this is a same-axis specialization by non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000204` was minted locally because METPO has no active exact organohalide respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015800` is reserved for this one-row class cohort. The v80 cohort used
`METPO:1015700`, so v81 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v81`, no live record used
`traitmech:000204`, and no prior proposal reserved `METPO:1015800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015800` | organohalide respiration | `METPO:1000802` Anaerobic respiration |

Organohalide respiration is the organohalide terminal-electron-acceptor branch
of anaerobic respiration. It captures organism-level respiratory use of
organohalide electron acceptors and excludes narrower terms for reductive
dehalogenase reactions or enzyme families.

## External Mappings

No exact external mapping is proposed. Candidate reductive dehalogenase enzyme
and protein-family terms describe molecular machinery for organohalide
respiration rather than the organism-level anaerobic respiration phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, no exact external xrefs, and one related enzyme label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000204` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000204` as traceability during the migration.

## Change Log

- v81, 2026-09: lifts `traitmech:000204 organohalide respiration` into the
  `METPO:1015800` block.
