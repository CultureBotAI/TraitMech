# METPO ROBOT Template Proposal - Chlorate Respiration (v75, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v74 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anaerobic
respiration in which microorganisms use chlorate as the terminal electron
acceptor and reduce it through chlorite to chloride for energy conservation.
The snapshot has only an obsolete broad `(Per)chlorate respiration` class, so
this cohort lifts the local fallback record for chlorate respiration. The local
TraitMech record is parented to `METPO:1000802` anaerobic respiration; the
proposal keeps that parent because this is a same-axis specialization by
non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000198` was minted locally because METPO has no active exact chlorate respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015200` is reserved for this one-row class cohort. The v74 cohort used
`METPO:1015100`, so v75 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v75`, no live record used
`traitmech:000198`, and no prior proposal reserved `METPO:1015200`. The pinned
METPO snapshot contains only the obsolete broad `(Per)chlorate respiration`
class and the obsolete perchlorate-specific classes.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015200` | chlorate respiration | `METPO:1000802` Anaerobic respiration |

Chlorate respiration is the chlorate-terminal-electron-acceptor branch of
anaerobic respiration. It captures organism-level respiratory use of chlorate
and excludes narrower terms for the ClrABDC chlorate reductase or Cld chlorite
dismutase enzyme systems.

## External Mappings

No exact external mapping is proposed. Candidate EC, Rhea, and protein-family
terms for chlorate reductase and chlorite dismutase describe enzyme activities,
reactions, or protein families rather than the organism-level anaerobic
respiration phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, one related synonym, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000198` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000198` as traceability during the migration.

## Change Log

- v75, 2026-09: lifts `traitmech:000198 chlorate respiration` into the
  `METPO:1015200` block.
