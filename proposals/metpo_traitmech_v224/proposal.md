# METPO ROBOT Template Proposal - FS-HEPN-TM System (v224, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v223 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-HEPN-TM system, the
genome-level possession trait for an `FS_HEPN_TM` phage-defense locus modeled
by DefenseFinder as a two-profile system requiring `FS_HEPN_TM__HEPN` and
`FS_HEPN_TM__TM`. Fillol-Salom et al. showed that phage-inducible chromosomal
islands carry defense mechanisms that provide broad immunity against phage
reproduction, plasmid transfer, and non-cognate PICI transfer. DefenseFinder
maps the `FS_HEPN_TM` model namespace to that paper and pins HEPN-family and
transmembrane profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-HEPN-TM |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030100` is reserved for this one-row class cohort. The v223 cohort used
`METPO:1030000`, so v224 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. It found no exact
same-scope record, `fs_hepn_tm_system` slug, `FS-HEPN-TM system` label,
`FS_HEPN_TM` key, `traitmech:000347`, `metpo_traitmech_v224`, or
`METPO:1030100` before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030100` | FS-HEPN-TM system | `METPO:1016300` phage defense system |

FS-HEPN-TM system captures genome-level possession of an `FS_HEPN_TM` locus
represented by DefenseFinder as a two-profile model requiring
`FS_HEPN_TM__HEPN` and `FS_HEPN_TM__TM`. It excludes generic HEPN-family
proteins; generic transmembrane proteins; the individual `FS_HEPN_TM__HEPN` and
`FS_HEPN_TM__TM` HMM profiles; individual PICI-encoded genes;
phage-inducible chromosomal islands; helper phages; the other Fillol-Salom PICI
defense-system namespaces; source database rows naming one `FS_HEPN_TM` model;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. HEPN-family nuclease or RNase
activities, generic transmembrane domains, individual PICI defense genes,
mobile islands, and downstream mobile-element interference are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000347` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000347` as traceability during the migration.

## Change Log

- v224, 2026-09: lifts `traitmech:000347 FS-HEPN-TM system` into the
  `METPO:1030100` block.
