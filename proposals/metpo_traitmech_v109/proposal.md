# METPO ROBOT Template Proposal - Lamassu System (v109, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v108 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Lamassu system, the
genome-level possession trait for SMC-like LmuB-centered antiphage defenses.
The v86 cohort proposed a `phage defense system` parent, v87 through v108
proposed BREX, DISARM, CBASS, phosphorothioate, abortive-infection, Gabija,
Thoeris, Zorya, Wadjet, Hachiman, Shedu, Dnd, Ssp, DndCDEA-PbeABCD, Kiwa,
and abortive-infection-family children, and this cohort adds Lamassu as another
narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000232` was minted locally because METPO has no active exact Lamassu-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018600` is reserved for this one-row class cohort. The v108 cohort used
`METPO:1018500`, so v109 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v109`, no live record used
`traitmech:000232`, and no prior proposal reserved `METPO:1018600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018600` | Lamassu system | `METPO:1016300` phage defense system |

Lamassu system captures genome-level possession of a Lamassu antiphage locus
built around a conserved SMC-like LmuB core sensor with modular LmuA effectors
and subfamily-specific partner architecture. It excludes individual `lmuA`,
`lmuB`, or `lmuC` genes; LmuA, LmuB, or LmuC proteins; SMC-family ATPases;
LmuABC complex assembly; Cap4 nuclease activity; dsDNA-end binding; source
database rows naming one Lamassu locus; and other antiphage systems such as
BREX, DISARM, CBASS, Gabija, Hachiman, Shedu, Thoeris, Zorya, Kiwa,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. Lamassu gene, protein, structural-complex,
ATPase, nuclease, DNA-binding, PADLOC, and DefenseFinder records are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Lamassu synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000232` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000232` as traceability during the migration.

## Change Log

- v109, 2026-09: lifts `traitmech:000232 Lamassu system` into the
  `METPO:1018600` block.
