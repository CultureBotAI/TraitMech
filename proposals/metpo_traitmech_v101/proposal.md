# METPO ROBOT Template Proposal - DndCDEA-PbeABCD System (v101, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v100 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the DndCDEA-PbeABCD
system, the genome-level possession trait for an archaeal
phosphorothioate-dependent locus that pairs DndCDEA-mediated host-DNA
phosphorothioation with PbeABCD-dependent viral DNA restriction. The v90 cohort
proposed the broader `phosphorothioate defense system` parent for Dnd, Ssp, and
archaeal phosphorothioate antiviral systems; v98 split out Dnd; v99 split out
SspABCD-SspE; v100 split out SspABCD-SspFGH; and this cohort splits
DndCDEA-PbeABCD into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000224` was minted locally because METPO has no active exact DndCDEA-PbeABCD-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017800` is reserved for this one-row class cohort. The v100 cohort used
`METPO:1017700`, so v101 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v101`, no live record used
`traitmech:000224`, and no prior proposal reserved `METPO:1017800` beyond the
v100 skill note pointing v101 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017800` | DndCDEA-PbeABCD system | `METPO:1016700` phosphorothioate defense system |

DndCDEA-PbeABCD system captures genome-level possession of an archaeal
phosphorothioate-dependent antiviral locus pairing DndCDEA host-DNA
phosphorothioation with PbeABCD effector activity. It excludes individual
`dnd` or `pbe` genes, the DndCDEA modification module by itself, the PbeABCD
effector module by itself, Dnd systems, SspABCD-SspE systems,
SspABCD-SspFGH systems, source database rows naming one predicted PT locus,
phosphorothioate modification as a chemical trait, and the broader
phosphorothioate defense parent.

## External Mappings

No exact external mapping is proposed. Individual `dnd` genes, `pbe` genes,
DndCDEA proteins, PbeABCD proteins, PT biochemical activities, source database
rows, and broader restriction-modification records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact DndCDEA-PbeABCD-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000224` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000224` as traceability during the migration.

## Change Log

- v101, 2026-09: lifts `traitmech:000224 DndCDEA-PbeABCD system` into the
  `METPO:1017800` block.
