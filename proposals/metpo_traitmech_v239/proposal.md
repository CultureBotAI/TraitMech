# METPO ROBOT Template Proposal - Gao-Her-SIR System (v239, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v238 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Her-SIR system, the
genome-level possession trait for a `Gao_Her_SIR` phage-defense locus modeled by
DefenseFinder as a two-profile system requiring `Gao_Her_SIR__HerA_SIR2` and
`Gao_Her_SIR__SIR2`. Gao et al. discovered widespread antiviral gene cassettes
with diverse enzymatic activities against specific bacteriophages, and
DefenseFinder maps the broader `Gao_Her` family key to that paper while pinning
the custom HerA_SIR2 and SIR2 profiles for this subsystem.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Her-SIR |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031600` is reserved for this one-row class cohort. The v238 cohort used
`METPO:1031500`, so v239 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_her_sir_system`
slug, `Gao-Her-SIR system` label, `HerA_SIR2` or `Gao_Her_SIR__SIR2` HMM
profiles, `traitmech:000362`, `metpo_traitmech_v239`, or `METPO:1031600`.
The only `Gao_Her_SIR` mentions were in the v238 Gao-Her-DUF proposal as
explicit sibling exclusions.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031600` | Gao-Her-SIR system | `METPO:1016300` phage defense system |

Gao-Her-SIR system captures genome-level possession of a `Gao_Her_SIR` locus
represented by DefenseFinder as a two-profile model requiring
`Gao_Her_SIR__HerA_SIR2` and `Gao_Her_SIR__SIR2`. It excludes the individual
Her-SIR HMM profiles; the broader `Gao_Her` article-registry key; the
`Gao_Her_DUF` sibling subsystem; individual Gao-family genes or proteins; other
Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom Her-SIR profiles
and unresolved downstream antiviral activity are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000362` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000362` as traceability during the migration.

## Change Log

- v239, 2026-09: lifts `traitmech:000362 Gao-Her-SIR system` into the
  `METPO:1031600` block.
