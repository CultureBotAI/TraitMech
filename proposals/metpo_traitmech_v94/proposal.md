# METPO ROBOT Template Proposal - Zorya System (v94, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v93 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Zorya system, the
genome-level possession trait for ZorA/ZorB-centered antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v93 proposed BREX,
DISARM, CBASS, phosphorothioate, abortive-infection, Gabija, and Thoeris
children, and this cohort adds Zorya as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000217` was minted locally because METPO has no active exact Zorya-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017100` is reserved for this one-row class cohort. The v93 cohort used
`METPO:1017000`, so v94 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v94`, no live record used
`traitmech:000217`, and no prior proposal reserved `METPO:1017100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017100` | Zorya system | `METPO:1016300` phage defense system |

Zorya system captures genome-level possession of a Zorya antiphage locus
encoding a conserved ZorA/ZorB membrane core and subtype-specific effectors
that couple phage sensing to inhibition of bacteriophage propagation. It
excludes individual `zorA` or `zorB` core genes, subtype effector genes such as
`zorC`, `zorD`, and `zorE`, ZorAB ion-motor proteins, Type I/II/III Zorya locus
subtypes, source database rows naming one Zorya locus, phage-encoded anti-Zorya
inhibitors, mechanistic ion-motor or nuclease subactivities, and other
antiphage systems such as BREX, DISARM, CBASS, Gabija, Thoeris,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. Zorya gene, protein, predicted-domain,
subtype, PADLOC, and DefenseFinder records are shifted from this
organism-level GENOMICS possession trait, and ZorAB motor activation or Zorya
effector nuclease activities are mechanistic parts rather than equivalent
classes.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact Zorya spelling variants and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000217` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000217` as traceability during the migration.

## Change Log

- v94, 2026-09: lifts `traitmech:000217 Zorya system` into the
  `METPO:1017100` block.
