# METPO ROBOT Template Proposal - Stk2 System (v180, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v179 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Stk2 system, the
genome-level possession trait for an abortive-infection locus encoding the Stk2
serine/threonine kinase. Depardieu et al. identified Stk2 as a staphylococcal
serine/threonine kinase that provides bacteriophage immunity by inducing
abortive infection, and DefenseFinder catalogs Stk2 with a one-profile model.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Stk2 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025700` is reserved for this one-row class cohort. The v179 cohort used
`METPO:1025600`, so v180 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v180`, no live record used
`traitmech:000303`, and no prior proposal reserved `METPO:1025700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025700` | Stk2 system | `METPO:1016800` abortive infection system |

Stk2 system captures genome-level possession of a phage-defense locus encoding
the Stk2 serine/threonine kinase, which can be activated by a phage protein to
phosphorylate host proteins and induce host-cell death that prevents
bacteriophage propagation. It excludes the individual `stk2` gene; Stk2
proteins; the DefenseFinder `Stk2__Stk2` HMM profile; serine/threonine kinase
activity outside a complete Stk2 antiphage locus; Staphylococcus infection by
phage as a host-range output; unresolved Stk2-activating phage proteins;
unresolved lethal phosphorylation targets; and generic abortive infection
systems.

## External Mappings

No exact external mapping is proposed. Stk2, Stk2 proteins,
serine/threonine kinase activity, and DefenseFinder rows are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related Stk2 synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000303` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000303` as traceability during the migration.

## Change Log

- v180, 2026-09: lifts `traitmech:000303 Stk2 system` into the
  `METPO:1025700` block.
