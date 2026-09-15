# METPO ROBOT Template Proposal - Iodate Respiration (v80, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v79 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no exact class for the anaerobic respiration in
which microorganisms use iodate as the terminal electron acceptor for energy
conservation. This cohort lifts the local fallback record for iodate
respiration. The local TraitMech record is parented to `METPO:1000802`
anaerobic respiration; the proposal keeps that parent because this is a
same-axis specialization by non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000203` was minted locally because METPO has no active exact iodate respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015700` is reserved for this one-row class cohort. The v79 cohort used
`METPO:1015600`, so v80 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v80`, no live record used
`traitmech:000203`, and no prior proposal reserved `METPO:1015700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015700` | iodate respiration | `METPO:1000802` Anaerobic respiration |

Iodate respiration is the iodate terminal-electron-acceptor branch of
anaerobic respiration. It captures organism-level respiratory use of iodate and
excludes narrower terms for iodate reductase reactions or enzyme complexes.

## External Mappings

No exact external mapping is proposed. Candidate Idr, DmsAB, EC, Rhea, and
protein-family terms for iodate reductase describe enzyme activities,
reactions, or protein complexes rather than the organism-level anaerobic
respiration phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact synonym, no exact external xrefs, and one related enzyme label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000203` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000203` as traceability during the migration.

## Change Log

- v80, 2026-09: lifts `traitmech:000203 iodate respiration` into the
  `METPO:1015700` block.
