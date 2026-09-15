# METPO ROBOT Template Proposal - Kiwa System (v108, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v107 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Kiwa system, the
genome-level possession trait for KwaA/KwaB-centered antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v107 proposed
BREX, DISARM, CBASS, phosphorothioate, abortive-infection, Gabija, Thoeris,
Zorya, Wadjet, Hachiman, Shedu, Dnd, Ssp, DndCDEA-PbeABCD, and
abortive-infection-family children, and this cohort adds Kiwa as another
narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000231` was minted locally because METPO has no active exact Kiwa-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018500` is reserved for this one-row class cohort. The v107 cohort used
`METPO:1018400`, so v108 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v108`, no live record used
`traitmech:000231`, and no prior proposal reserved `METPO:1018500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018500` | Kiwa system | `METPO:1016300` phage defense system |

Kiwa system captures genome-level possession of a Kiwa antiphage locus whose
transmembrane KwaA sensor and DNA-binding KwaB effector assemble into a
membrane-associated supercomplex and coordinate phage-attachment sensing with
inhibition of phage DNA replication and late transcription. It excludes
individual `kwaA` or `kwaB` genes, KwaA or KwaB proteins, KwaA-KwaB
supercomplex assembly, phage DNA binding, Gam-mediated phage counter-defense,
RecBCD rescue, source database rows naming one Kiwa locus, and other antiphage
systems such as BREX, DISARM, CBASS, Gabija, Hachiman, Shedu, Thoeris, Zorya,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. Kiwa gene, protein, structural-complex,
DNA-binding, RecBCD-associated, phage counter-defense, PADLOC, and
DefenseFinder records are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Kiwa synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000231` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000231` as traceability during the migration.

## Change Log

- v108, 2026-09: lifts `traitmech:000231 Kiwa system` into the
  `METPO:1018500` block.
