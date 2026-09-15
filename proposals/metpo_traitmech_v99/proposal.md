# METPO ROBOT Template Proposal - SspABCD-SspE System (v99, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v98 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the SspABCD-SspE
system, the genome-level possession trait for a bacterial
phosphorothioate-dependent locus that pairs SspABCD host-DNA
phosphorothioation with SspE restriction. The v90 cohort proposed the broader
`phosphorothioate defense system` parent for Dnd, Ssp, and archaeal
phosphorothioate antiviral systems; v98 split out Dnd; and this cohort splits
SspABCD-SspE into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000222` was minted locally because METPO has no active exact SspABCD-SspE-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017600` is reserved for this one-row class cohort. The v98 cohort used
`METPO:1017500`, so v99 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v99`, no live record used
`traitmech:000222`, and no prior proposal reserved `METPO:1017600` beyond the
v98 skill note pointing v99 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017600` | SspABCD-SspE system | `METPO:1016700` phosphorothioate defense system |

SspABCD-SspE system captures genome-level possession of a bacterial
phosphorothioate-dependent locus pairing an SspABCD host-DNA modification module
with SspE single-enzyme restriction activity. It excludes individual `ssp`
genes, the SspABCD modification module by itself, the SspE restriction enzyme by
itself, SspFGH systems, Dnd systems, archaeal phosphorothioate antiviral
systems, source database rows naming one predicted PT locus, phosphorothioate
modification as a chemical trait, and the broader phosphorothioate defense
parent.

## External Mappings

No exact external mapping is proposed. Individual `ssp` genes, Ssp proteins,
PT biochemical activities, SspFGH restriction subcomplexes, source database
rows, and broader restriction-modification records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact SspABCD-SspE-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000222` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000222` as traceability during the migration.

## Change Log

- v99, 2026-09: lifts `traitmech:000222 SspABCD-SspE system` into the
  `METPO:1017600` block.
