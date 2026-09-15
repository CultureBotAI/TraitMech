# METPO ROBOT Template Proposal - Hachiman System (v96, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v95 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Hachiman system, the
genome-level possession trait for HamA/HamB-centered antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v94 proposed BREX,
DISARM, CBASS, phosphorothioate, abortive-infection, Gabija, Thoeris, and
Zorya children, v95 proposed the parallel anti-plasmid Wadjet system, and this
cohort adds Hachiman as another narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000219` was minted locally because METPO has no active exact Hachiman-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017300` is reserved for this one-row class cohort. The v95 cohort used
`METPO:1017200`, so v96 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v96`, no live record used
`traitmech:000219`, and no prior proposal reserved `METPO:1017300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017300` | Hachiman system | `METPO:1016300` phage defense system |

Hachiman system captures genome-level possession of a Hachiman antiphage locus
encoding a HamA/HamB nuclease-helicase core that couples Hachiman activation to
DNA cleavage and inhibition of bacteriophage propagation. It excludes
individual `hamA`, `hamB`, or `hamC` genes, HamA/HamB proteins, HamAB
nuclease-helicase activity, type I or type II locus subtypes, DUF1837 and Cap4
domain families, source database rows naming one Hachiman locus,
DNA-damage-sensing or DNA-cleavage subactivities, phage-encoded Hachiman
triggers, and other antiphage systems such as BREX, DISARM, CBASS, Gabija,
Thoeris, Zorya, phosphorothioate defense, CRISPR-Cas, and abortive-infection
families.

## External Mappings

No exact external mapping is proposed. Hachiman gene, protein,
predicted-domain, subtype, PADLOC, and DefenseFinder records are shifted from
this organism-level GENOMICS possession trait, and HamAB ATPase or nuclease
activities are mechanistic parts rather than equivalent classes.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact Hachiman spelling variants and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000219` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000219` as traceability during the migration.

## Change Log

- v96, 2026-09: lifts `traitmech:000219 Hachiman system` into the
  `METPO:1017300` block.
