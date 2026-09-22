# METPO ROBOT Template Proposal - Gao-Tmn System (v234, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v233 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Tmn system, the
genome-level possession trait for a `Gao_Tmn` phage-defense locus modeled by
DefenseFinder as a single-profile system requiring `Gao_Tmn__TmnA`. Gao et al.
discovered widespread antiviral gene cassettes with diverse enzymatic
activities against specific bacteriophages, and DefenseFinder maps `Gao_Tmn`
to that paper while pinning the custom TmnA profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Tmn |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031100` is reserved for this one-row class cohort. The v233 cohort used
`METPO:1031000`, so v234 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_tmn_system` slug,
`Gao-Tmn system` label, `Gao_Tmn` key, `Gao_Tmn__TmnA` profile,
`traitmech:000357`, `metpo_traitmech_v234`, or `METPO:1031100` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031100` | Gao-Tmn system | `METPO:1016300` phage defense system |

Gao-Tmn system captures genome-level possession of a `Gao_Tmn` locus
represented by DefenseFinder as a single-profile model requiring
`Gao_Tmn__TmnA`. It excludes the individual `Gao_Tmn__TmnA` HMM profile;
individual Gao-family genes or proteins; source database rows naming one
`Gao_Tmn` model; other Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom TmnA profile and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000357` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000357` as traceability during the migration.

## Change Log

- v234, 2026-09: lifts `traitmech:000357 Gao-Tmn system` into the
  `METPO:1031100` block.
