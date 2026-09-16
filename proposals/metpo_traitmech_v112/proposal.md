# METPO ROBOT Template Proposal - Retron System (v112, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v111 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Retron system, the
genome-level possession trait for RT/ncRNA/effector antiphage retrons. The v86
cohort proposed a `phage defense system` parent, v87 through v111 proposed
BREX, DISARM, CBASS, phosphorothioate, abortive-infection, Gabija, Thoeris,
Zorya, Wadjet, Hachiman, Shedu, Dnd, Ssp, DndCDEA-PbeABCD, Kiwa,
abortive-infection-family, Lamassu, Septu, and Druantia children, and this
cohort adds Retron as another narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000235` was minted locally because METPO has no active exact Retron-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018900` is reserved for this one-row class cohort. The v111 cohort used
`METPO:1018800`, so v112 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v112`, no live record used
`traitmech:000235`, and no prior proposal reserved `METPO:1018900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018900` | Retron system | `METPO:1016300` phage defense system |

Retron system captures genome-level possession of an antiphage retron locus
with reverse transcriptase, msr/msd non-coding RNA, msDNA production, and an
associated effector. It excludes individual retron reverse-transcriptase genes;
reverse transcriptase proteins; msr/msd non-coding RNAs; msDNA biosynthesis
without a complete antiphage locus; RcaT-containing tripartite toxin-antitoxin
mechanism classes; RecBCD guarding by Ec48; Retron-Septu subtypes; source
database rows naming one retron locus; and other antiphage systems such as
BREX, DISARM, CBASS, Gabija, Hachiman, Shedu, Thoeris, Zorya, Kiwa, Lamassu,
Septu, Druantia, phosphorothioate defense, CRISPR-Cas, and abortive infection
families.

## External Mappings

No exact external mapping is proposed. Retron reverse-transcriptase, ncRNA,
msDNA-biosynthesis, toxin-antitoxin, PADLOC, and DefenseFinder records are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact Retron-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000235` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000235` as traceability during the migration.

## Change Log

- v112, 2026-09: lifts `traitmech:000235 Retron system` into the
  `METPO:1018900` block.
