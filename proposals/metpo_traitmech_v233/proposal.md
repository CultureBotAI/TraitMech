# METPO ROBOT Template Proposal - Gao-Ppl System (v233, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v232 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Ppl system, the
genome-level possession trait for a `Gao_Ppl` phage-defense locus modeled by
DefenseFinder as a single-profile system requiring `Gao_Ppl__PplA`. Gao et al.
discovered widespread antiviral gene cassettes with diverse enzymatic
activities against specific bacteriophages, and DefenseFinder maps `Gao_Ppl`
to that paper while pinning the custom PplA profile for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Ppl |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031000` is reserved for this one-row class cohort. The v232 cohort used
`METPO:1030900`, so v233 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_ppl_system` slug,
`Gao-Ppl system` label, `Gao_Ppl` key, `Gao_Ppl__PplA` profile,
`traitmech:000356`, `metpo_traitmech_v233`, or `METPO:1031000` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031000` | Gao-Ppl system | `METPO:1016300` phage defense system |

Gao-Ppl system captures genome-level possession of a `Gao_Ppl` locus
represented by DefenseFinder as a single-profile model requiring
`Gao_Ppl__PplA`. It excludes the individual `Gao_Ppl__PplA` HMM profile;
individual Gao-family genes or proteins; source database rows naming one
`Gao_Ppl` model; other Gao-family systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom PplA profile and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000356` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000356` as traceability during the migration.

## Change Log

- v233, 2026-09: lifts `traitmech:000356 Gao-Ppl system` into the
  `METPO:1031000` block.
