# METPO ROBOT Template Proposal - FS-HP System (v225, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v224 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-HP system, the
genome-level possession trait for an `FS_HP` phage-defense locus modeled by
DefenseFinder as a single-profile system requiring `FS_HP__HP`. Fillol-Salom
et al. showed that phage-inducible chromosomal islands carry defense mechanisms
that provide broad immunity against phage reproduction, plasmid transfer, and
non-cognate PICI transfer. DefenseFinder maps the `FS_HP` model namespace to
that paper and pins the custom `FS_HP__HP` profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-HP |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030200` is reserved for this one-row class cohort. The v224 cohort used
`METPO:1030100`, so v225 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. It found no exact
same-scope record, `fs_hp_system` slug, `FS-HP system` label, `FS_HP` key,
`traitmech:000348`, `metpo_traitmech_v225`, or `METPO:1030200` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030200` | FS-HP system | `METPO:1016300` phage defense system |

FS-HP system captures genome-level possession of an `FS_HP` locus represented
by DefenseFinder as a single-profile model requiring `FS_HP__HP`. It excludes
the individual `FS_HP__HP` HMM profile; individual PICI-encoded genes;
phage-inducible chromosomal islands; helper phages; source database rows naming
one `FS_HP` model; the paired `FS_HP_SDH_sah` model namespace; the other
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
2. On mint, replace local `traitmech:000348` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000348` as traceability during the migration.

## Change Log

- v225, 2026-09: lifts `traitmech:000348 FS-HP system` into the
  `METPO:1030200` block.
