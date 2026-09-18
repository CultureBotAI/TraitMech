# METPO ROBOT Template Proposal - Pycsar System (v113, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v112 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Pycsar system, the
genome-level possession trait for PycC/cyclic-pyrimidine-receptor antiphage
systems. The v86 cohort proposed a `phage defense system` parent, v87 through
v112 proposed BREX, DISARM, CBASS, phosphorothioate, abortive-infection,
Gabija, Thoeris, Zorya, Wadjet, Hachiman, Shedu, Dnd, Ssp,
DndCDEA-PbeABCD, Kiwa, abortive-infection-family, Lamassu, Septu, Druantia,
and Retron children, and this cohort adds Pycsar as another narrower
phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000236` was minted locally because METPO has no active exact Pycsar-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019000` is reserved for this one-row class cohort. The v112 cohort used
`METPO:1018900`, so v113 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v113`, no live record used
`traitmech:000236`, and no prior proposal reserved `METPO:1019000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019000` | Pycsar system | `METPO:1016300` phage defense system |

Pycsar system captures genome-level possession of an antiphage Pycsar locus
with a PycC pyrimidine cyclase that produces cyclic CMP or cyclic UMP second
messengers during phage infection and a cognate cyclic-pyrimidine receptor
effector. It excludes individual pycC genes; PycC cyclases; PycTIR and PycTM
receptor proteins; cyclic CMP or cyclic UMP second messengers; PycC
pyrimidine-cyclase activity without a complete antiphage locus; source database
rows naming one Pycsar locus; Pycsar clades or effector-specific subtypes; and
other antiphage systems such as CBASS, CRISPR-Cas, and other
nucleotide-signaling phage defense systems.

## External Mappings

No exact external mapping is proposed. PycC cyclase, cyclic-pyrimidine
messenger, effector-protein, PADLOC, and DefenseFinder records are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact Pycsar-system synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000236` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000236` as traceability during the migration.

## Change Log

- v113, 2026-09: lifts `traitmech:000236 Pycsar system` into the
  `METPO:1019000` block.
