# METPO ROBOT Template Proposal - FS-Sma System (v228, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v227 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-Sma system, the
genome-level possession trait for an `FS_Sma` phage-defense locus modeled by
DefenseFinder as a single-profile system requiring `FS_Sma__Sma`. Fillol-Salom
et al. showed that phage-inducible chromosomal islands carry defense mechanisms
that provide broad immunity against phage reproduction, plasmid transfer, and
non-cognate PICI transfer. DefenseFinder maps the `FS_Sma` model namespace to
that paper and pins the custom `FS_Sma__Sma` profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-Sma |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030500` is reserved for this one-row class cohort. The v227 cohort used
`METPO:1030400`, so v228 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across
`data/raw/metpo.owl`, `data/traits`, `proposals`, and `history`. It found no
exact same-scope record, `fs_sma_system` slug, `FS-Sma system` label,
`FS_Sma__Sma` profile key, `traitmech:000351`, `metpo_traitmech_v228`, or
`METPO:1030500` before this cohort. A broader search found `FS_Sma` only in
the v227 FS-HsdR-like proposal, where it names FS_Sma as a distinct
neighboring model namespace.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030500` | FS-Sma system | `METPO:1016300` phage defense system |

FS-Sma system captures genome-level possession of an `FS_Sma` locus represented
by DefenseFinder as a single-profile model requiring `FS_Sma__Sma`. It excludes
the individual `FS_Sma__Sma` HMM profile; individual PICI-encoded genes;
phage-inducible chromosomal islands; helper phages; source database rows naming
one `FS_Sma` model; the neighboring `FS_HsdR_like` model namespace; the other
Fillol-Salom PICI defense-system namespaces; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual custom profiles, individual
PICI defense genes, mobile islands, and downstream mobile-element interference
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000351` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000351` as traceability during the migration.

## Change Log

- v228, 2026-09: lifts `traitmech:000351 FS-Sma system` into the
  `METPO:1030500` block.
