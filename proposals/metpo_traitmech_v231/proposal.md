# METPO ROBOT Template Proposal - Gao-Iet System (v231, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v230 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Iet system, the
genome-level possession trait for a `Gao_Iet` phage-defense locus modeled by
DefenseFinder as a two-profile system requiring `Gao_Iet__IetA` and
`Gao_Iet__IetS`. Gao et al. discovered widespread antiviral gene cassettes with
diverse enzymatic activities against specific bacteriophages, and DefenseFinder
maps `Gao_Iet` to that paper while pinning both custom profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Iet |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030800` is reserved for this one-row class cohort. The v230 cohort used
`METPO:1030700`, so v231 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_iet_system` slug,
`Gao-Iet system` label, `Gao_Iet` key, `Gao_Iet__IetA` or `Gao_Iet__IetS`
profile, `traitmech:000354`, `metpo_traitmech_v231`, or `METPO:1030800`
before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030800` | Gao-Iet system | `METPO:1016300` phage defense system |

Gao-Iet system captures genome-level possession of a `Gao_Iet` locus
represented by DefenseFinder as a two-profile model requiring `Gao_Iet__IetA`
and `Gao_Iet__IetS`. It excludes the individual `Gao_Iet__IetA` and
`Gao_Iet__IetS` HMM profiles; individual Gao-family genes or proteins; source
database rows naming one `Gao_Iet` model; other Gao-family systems; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom IetA/IetS profiles
and unresolved downstream antiviral activity are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000354` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000354` as traceability during the migration.

## Change Log

- v231, 2026-09: lifts `traitmech:000354 Gao-Iet system` into the
  `METPO:1030800` block.
