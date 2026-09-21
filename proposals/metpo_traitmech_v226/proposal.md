# METPO ROBOT Template Proposal - FS-HP-SDH-sah System (v226, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v225 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-HP-SDH-sah system,
the genome-level possession trait for an `FS_HP_SDH_sah` phage-defense locus
modeled by DefenseFinder as a two-profile system requiring `FS_HP_SDH_sah__HP`
and `FS_HP_SDH_sah__SDH_sah`. Fillol-Salom et al. showed that
phage-inducible chromosomal islands carry defense mechanisms that provide broad
immunity against phage reproduction, plasmid transfer, and non-cognate PICI
transfer. DefenseFinder maps the `FS_HP_SDH_sah` model namespace to that paper
and pins the custom `FS_HP_SDH_sah__HP` and `FS_HP_SDH_sah__SDH_sah` profiles
for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-HP-SDH-sah |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030300` is reserved for this one-row class cohort. The v225 cohort used
`METPO:1030200`, so v226 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. It found no exact
same-scope record, `fs_hp_sdh_sah_system` slug, `FS-HP-SDH-sah system` label,
`FS_HP_SDH_sah` key, `traitmech:000349`, `metpo_traitmech_v226`, or
`METPO:1030300` before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030300` | FS-HP-SDH-sah system | `METPO:1016300` phage defense system |

FS-HP-SDH-sah system captures genome-level possession of an `FS_HP_SDH_sah`
locus represented by DefenseFinder as a two-profile model requiring
`FS_HP_SDH_sah__HP` and `FS_HP_SDH_sah__SDH_sah`. It excludes the individual
`FS_HP_SDH_sah__HP` and `FS_HP_SDH_sah__SDH_sah` HMM profiles; individual
PICI-encoded genes; phage-inducible chromosomal islands; helper phages; source
database rows naming one `FS_HP_SDH_sah` model; the neighboring `FS_HP` model
namespace; the other Fillol-Salom PICI defense-system namespaces; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual custom profiles, individual
PICI defense genes, mobile islands, and downstream mobile-element interference
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000349` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000349` as traceability during the migration.

## Change Log

- v226, 2026-09: lifts `traitmech:000349 FS-HP-SDH-sah system` into the
  `METPO:1030300` block.
