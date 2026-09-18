# METPO ROBOT Template Proposal - RADAR System (v115, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v114 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the RADAR system, the
genome-level possession trait for RdrA/RdrB phage-defense loci that assemble a
supramolecular ATPase/deaminase complex during antiphage defense. The v86 cohort
proposed a `phage defense system` parent, v87-v114 proposed a series of
narrower BREX, DISARM, CBASS, phosphorothioate-defense, abortive-infection,
Zorya, Thoeris, Hachiman, Shedu, Druantia, Septu, Retron, Pycsar, and PARIS
children, and this cohort adds RADAR as another narrower phage-defense-system
child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000238` was minted locally because METPO has no active exact RADAR-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019200` is reserved for this one-row class cohort. The v114 cohort used
`METPO:1019100`, so v115 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v115`, no live record used
`traitmech:000238`, and no prior proposal reserved `METPO:1019200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019200` | RADAR system | `METPO:1016300` phage defense system |

RADAR system captures genome-level possession of a restriction by an adenosine
deaminase acting on RNA locus encoding an RdrA AAA+ ATPase and an RdrB
adenosine deaminase that assemble into a supramolecular defense complex. It
excludes individual `rdrA` or `rdrB` genes; RdrA or RdrB proteins; RdrA/RdrB
supramolecular-complex assembly without a complete antiphage locus; ATP-to-ITP
conversion or RNA editing as isolated subactivities; exact RdrA activation
triggers; source database rows naming one RADAR locus; substrate-specific RADAR
subtypes; and other antiphage systems such as BREX, DISARM, CBASS, Gabija,
Hachiman, Shedu, Thoeris, Zorya, Kiwa, PARIS, phosphorothioate defense,
CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. RdrA, RdrB, ATP-to-ITP conversion,
RNA editing, inosine nucleotide accumulation, and PADLOC/DefenseFinder records
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact RADAR long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000238` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000238` as traceability during the migration.

## Change Log

- v115, 2026-09: lifts `traitmech:000238 RADAR system` into the
  `METPO:1019200` block.
