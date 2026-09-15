# METPO ROBOT Template Proposal - Shedu System (v97, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v96 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Shedu system, the
genome-level possession trait for single-protein Shedu/SduA antiphage immune
nucleases. The v86 cohort proposed a `phage defense system` parent, v87 through
v94 proposed BREX, DISARM, CBASS, phosphorothioate, abortive-infection, Gabija,
Thoeris, and Zorya children, v95 proposed the parallel anti-plasmid Wadjet
system, v96 proposed Hachiman, and this cohort adds Shedu as another narrower
phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000220` was minted locally because METPO has no active exact Shedu-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017400` is reserved for this one-row class cohort. The v96 cohort used
`METPO:1017300`, so v97 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v97`, no live record used
`traitmech:000220`, and no prior proposal reserved `METPO:1017400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017400` | Shedu system | `METPO:1016300` phage defense system |

Shedu system captures genome-level possession of a Shedu antiphage locus
encoding a single-protein immune nuclease whose sensor domain architecture
regulates a common antiphage nuclease core. It excludes individual `sduA`
genes, SduA or DUF4263-domain proteins, individual Shedu N-terminal
sensor-domain classes, PD-(D/E)XK nuclease activity, DNA-end nicking or
degradation subactivities, source database rows naming one predicted Shedu
locus or domain, phage escape strategies, and other antiphage systems such as
BREX, DISARM, CBASS, Gabija, Hachiman, Thoeris, Zorya, phosphorothioate
defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. Shedu genes, SduA/DUF4263 proteins,
predicted-domain records, source database rows, DNA-end-sensing or nicking
subactivities, and other phage-defense-system records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Shedu system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000220` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000220` as traceability during the migration.

## Change Log

- v97, 2026-09: lifts `traitmech:000220 Shedu system` into the
  `METPO:1017400` block.
