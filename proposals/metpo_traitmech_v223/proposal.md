# METPO ROBOT Template Proposal - FS-GIY-YIG System (v223, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v222 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for FS-GIY-YIG system, the
genome-level possession trait for an `FS_GIY_YIG` phage-defense locus modeled
by DefenseFinder as a single-profile system requiring `FS_GIY_YIG__GIY_YIG`.
Fillol-Salom et al. showed that phage-inducible chromosomal islands carry
defense mechanisms that provide broad immunity against phage reproduction,
plasmid transfer, and non-cognate PICI transfer. DefenseFinder maps the
`FS_GIY_YIG` model namespace to that paper and pins a GIY-YIG nuclease-like
profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for FS-GIY-YIG |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030000` is reserved for this one-row class cohort. The v222 cohort used
`METPO:1029900`, so v223 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. It found only a
shifted GIY-YIG restriction-endonuclease mention in a restriction-modification
research report; no exact same-scope record, `fs_giy_yig_system` slug,
`FS-GIY-YIG system` label, `FS_GIY_YIG` key, `traitmech:000346`,
`metpo_traitmech_v223`, or `METPO:1030000` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030000` | FS-GIY-YIG system | `METPO:1016300` phage defense system |

FS-GIY-YIG system captures genome-level possession of an `FS_GIY_YIG` locus
represented by DefenseFinder as a single-profile model requiring
`FS_GIY_YIG__GIY_YIG`. It excludes generic GIY-YIG nucleases; the individual
`FS_GIY_YIG__GIY_YIG` HMM profile; individual PICI-encoded genes;
phage-inducible chromosomal islands; helper phages; the other
Fillol-Salom PICI defense-system namespaces; source database rows naming one
FS_GIY_YIG model; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. GIY-YIG nuclease activities, individual
PICI defense genes, mobile islands, and downstream mobile-element interference
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000346` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000346` as traceability during the migration.

## Change Log

- v223, 2026-09: lifts `traitmech:000346 FS-GIY-YIG system` into the
  `METPO:1030000` block.
