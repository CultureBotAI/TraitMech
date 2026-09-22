# METPO ROBOT Template Proposal - Gao-Hhe System (v230, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v229 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Hhe system, the
genome-level possession trait for a `Gao_Hhe` phage-defense locus modeled by
DefenseFinder as a single-profile system requiring `Gao_Hhe__HheA`. Gao et al.
discovered widespread antiviral gene cassettes with diverse enzymatic
activities against specific bacteriophages, and DefenseFinder maps `Gao_Hhe`
to that paper while pinning the custom HheA profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Hhe |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030700` is reserved for this one-row class cohort. The v229 cohort used
`METPO:1030600`, so v230 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_hhe_system` slug,
`Gao-Hhe system` label, `Gao_Hhe` key, `Gao_Hhe__HheA` profile,
`traitmech:000353`, `metpo_traitmech_v230`, or `METPO:1030700` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030700` | Gao-Hhe system | `METPO:1016300` phage defense system |

Gao-Hhe system captures genome-level possession of a `Gao_Hhe` locus
represented by DefenseFinder as a single-profile model requiring
`Gao_Hhe__HheA`. It excludes the individual `Gao_Hhe__HheA` HMM profile;
individual Gao-family genes or proteins; source database rows naming one
`Gao_Hhe` model; other Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom HheA profile and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000353` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000353` as traceability during the migration.

## Change Log

- v230, 2026-09: lifts `traitmech:000353 Gao-Hhe system` into the
  `METPO:1030700` block.
