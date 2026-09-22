# METPO ROBOT Template Proposal - FS-HsdR-like System (v227, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v226 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-HsdR-like system,
the genome-level possession trait for an `FS_HsdR_like` phage-defense locus
modeled by DefenseFinder as a two-gene system drawing from custom
`FS_HsdR_like__DUF6731`, `FS_HsdR_like__HP`, and `FS_HsdR_like__HdrR`
profiles. Fillol-Salom et al. showed that phage-inducible chromosomal islands
carry defense mechanisms that provide broad immunity against phage
reproduction, plasmid transfer, and non-cognate PICI transfer. DefenseFinder
maps the `FS_HsdR_like` model namespace to that paper and pins its two-of-three
custom profile rule in the same model snapshot.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-HsdR-like |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030400` is reserved for this one-row class cohort. The v226 cohort used
`METPO:1030300`, so v227 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. It found no exact
same-scope record, `fs_hsdr_like_system` slug, `FS-HsdR-like system` label,
`FS_HsdR_like` key, `traitmech:000350`, `metpo_traitmech_v227`, or
`METPO:1030400` before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030400` | FS-HsdR-like system | `METPO:1016300` phage defense system |

FS-HsdR-like system captures genome-level possession of an `FS_HsdR_like`
locus represented by DefenseFinder as a two-gene model drawing from custom
`FS_HsdR_like__DUF6731`, `FS_HsdR_like__HP`, and `FS_HsdR_like__HdrR`
profiles. It excludes the individual custom HMM profiles; individual
PICI-encoded genes; phage-inducible chromosomal islands; helper phages; source
database rows naming one `FS_HsdR_like` model; the neighboring `FS_HP_SDH_sah`
and `FS_Sma` model namespaces; the other Fillol-Salom PICI defense-system
namespaces; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual custom profiles, individual
PICI defense genes, mobile islands, and downstream mobile-element interference
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, four related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000350` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000350` as traceability during the migration.

## Change Log

- v227, 2026-09: lifts `traitmech:000350 FS-HsdR-like system` into the
  `METPO:1030400` block.
