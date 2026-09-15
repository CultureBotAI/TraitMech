# METPO ROBOT Template Proposal - Dnd System (v98, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v97 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Dnd system, the
genome-level possession trait for phosphorothioate-dependent Dnd
restriction-modification loci. The v86 cohort proposed a `phage defense system`
parent, v90 proposed a broader `phosphorothioate defense system` parent for Dnd,
Ssp, and archaeal phosphorothioate antiviral systems, and this cohort splits Dnd
into its own narrower child of that parent.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000221` was minted locally because METPO has no active exact Dnd-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017500` is reserved for this one-row class cohort. The v97 cohort used
`METPO:1017400`, so v98 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v98`, no live record used
`traitmech:000221`, and no prior proposal reserved `METPO:1017500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017500` | Dnd system | `METPO:1016700` phosphorothioate defense system |

Dnd system captures genome-level possession of a DNA
phosphorothioation-dependent Dnd restriction-modification locus pairing a
Dnd-family host-DNA modification module with DndFGH restriction activity. It
excludes individual `dnd` genes, DndABCDE modification proteins, the DndFGH
restriction complex by itself, DndA-replacement cysteine desulfurases, source
database rows naming one predicted PT locus, phosphorothioate modification as a
chemical trait, SspBCD-E, SspABCD-SspFGH, archaeal phosphorothioate antiviral
systems, and the broader phosphorothioate defense parent.

## External Mappings

No exact external mapping is proposed. Individual `dnd` genes, Dnd proteins,
PT biochemical activities, Dnd-family restriction subcomplexes, source database
rows, and broader restriction-modification records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  three exact Dnd-system synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000221` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000221` as traceability during the migration.

## Change Log

- v98, 2026-09: lifts `traitmech:000221 Dnd system` into the `METPO:1017500`
  block.
