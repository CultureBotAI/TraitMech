# METPO ROBOT Template Proposal - AVAST System (v116, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v115 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AVAST system, the
genome-level possession trait for antiviral ATPase/NTPase of the STAND
superfamily loci that encode Avs receptor-effectors during antiphage defense.
The v86 cohort proposed a `phage defense system` parent, v87-v115 proposed a
series of narrower BREX, DISARM, CBASS, phosphorothioate-defense,
abortive-infection, Zorya, Thoeris, Hachiman, Shedu, Druantia, Septu, Retron,
Pycsar, PARIS, and RADAR children, and this cohort adds AVAST as another
narrower phage-defense-system child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000239` was minted locally because METPO has no active exact AVAST-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019300` is reserved for this one-row class cohort. The v115 cohort used
`METPO:1019200`, so v116 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v116`, no live record used
`traitmech:000239`, and no prior proposal reserved `METPO:1019300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019300` | AVAST system | `METPO:1016300` phage defense system |

AVAST system captures genome-level possession of a locus encoding an antiviral
STAND-family Avs receptor-effector that detects conserved phage proteins and
activates a subtype-specific antiviral output. It excludes individual `avs`
genes; individual Avs proteins, domains, or effector reactions; standalone
STAND ATPases without a complete antiphage locus; source database rows naming
one AVAST locus; Avs1, Avs2, Avs3, Avs4, Avs5, or jumbo-phage-restricted
subtypes; and other antiphage systems such as BREX, DISARM, CBASS, Gabija,
Hachiman, Shedu, Thoeris, Zorya, Kiwa, PARIS, RADAR, phosphorothioate defense,
CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. Avs proteins, STAND ATPases, TIR
domains, Sir2-like domains, C-terminal effector domains, conserved phage
proteins, DefenseFinder/PADLOC records, and subtype-specific Avs1-Avs5 entries
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact AVAST long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000239` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000239` as traceability during the migration.

## Change Log

- v116, 2026-09: lifts `traitmech:000239 AVAST system` into the
  `METPO:1019300` block.
