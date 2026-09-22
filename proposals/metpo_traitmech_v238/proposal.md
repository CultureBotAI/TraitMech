# METPO ROBOT Template Proposal - Gao-Her-DUF System (v238, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v237 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Her-DUF system, the
genome-level possession trait for a `Gao_Her_DUF` phage-defense locus modeled by
DefenseFinder as a two-profile system requiring `Gao_Her_DUF__DUF4297` and
`Gao_Her_DUF__HerA_DUF`. Gao et al. discovered widespread antiviral gene
cassettes with diverse enzymatic activities against specific bacteriophages, and
DefenseFinder maps the broader `Gao_Her` family key to that paper while pinning
the custom DUF4297 and HerA_DUF profiles for this subsystem.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Her-DUF |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031500` is reserved for this one-row class cohort. The v237 cohort used
`METPO:1031400`, so v238 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_her_duf_system`
slug, `Gao-Her-DUF system` label, `Gao_Her_DUF` key, Her-DUF HMM profiles,
`traitmech:000361`, `metpo_traitmech_v238`, or `METPO:1031500` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031500` | Gao-Her-DUF system | `METPO:1016300` phage defense system |

Gao-Her-DUF system captures genome-level possession of a `Gao_Her_DUF` locus
represented by DefenseFinder as a two-profile model requiring
`Gao_Her_DUF__DUF4297` and `Gao_Her_DUF__HerA_DUF`. It excludes the individual
Her-DUF HMM profiles; the broader `Gao_Her` article-registry key; the
`Gao_Her_SIR` sibling subsystem; individual Gao-family genes or proteins; other
Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom Her-DUF profiles
and unresolved downstream antiviral activity are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000361` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000361` as traceability during the migration.

## Change Log

- v238, 2026-09: lifts `traitmech:000361 Gao-Her-DUF system` into the
  `METPO:1031500` block.
