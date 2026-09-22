# METPO ROBOT Template Proposal - Gao-Mza System (v232, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v231 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Mza system, the
genome-level possession trait for a `Gao_Mza` phage-defense locus modeled by
DefenseFinder as a five-profile system requiring `Gao_Mza__MzaA`,
`Gao_Mza__MzaB`, `Gao_Mza__MzaC`, `Gao_Mza__MzaD`, and `Gao_Mza__MzaE`. Gao et
al. discovered widespread antiviral gene cassettes with diverse enzymatic
activities against specific bacteriophages, and DefenseFinder maps `Gao_Mza` to
that paper while pinning all five custom profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Mza |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030900` is reserved for this one-row class cohort. The v231 cohort used
`METPO:1030800`, so v232 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_mza_system` slug,
`Gao-Mza system` label, `Gao_Mza` key, `Gao_Mza__MzaA` through
`Gao_Mza__MzaE` profile, `traitmech:000355`, `metpo_traitmech_v232`, or
`METPO:1030900` before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030900` | Gao-Mza system | `METPO:1016300` phage defense system |

Gao-Mza system captures genome-level possession of a `Gao_Mza` locus
represented by DefenseFinder as a five-profile model requiring
`Gao_Mza__MzaA` through `Gao_Mza__MzaE`. It excludes the individual Mza HMM
profiles; individual Gao-family genes or proteins; source database rows naming
one `Gao_Mza` model; other Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom Mza profiles and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, six related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000355` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000355` as traceability during the migration.

## Change Log

- v232, 2026-09: lifts `traitmech:000355 Gao-Mza system` into the
  `METPO:1030900` block.
