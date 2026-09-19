# METPO ROBOT Template Proposal - Sucellos System (v143, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v142 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Sucellos system, the
genome-level possession trait for a Sucellos anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Sucellos with SclA_VCA0367 and
SclB_VCA0368 profiles in its article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000266` was minted locally because METPO has no active exact Sucellos-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022000` is reserved for this one-row class cohort. The v142 cohort used
`METPO:1021900`, so v143 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v143`, no live record used
`traitmech:000266`, and no prior proposal reserved `METPO:1022000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022000` | Sucellos system | `METPO:1016300` phage defense system |

Sucellos system captures genome-level possession of a Sucellos locus
represented by SclA_VCA0367 and SclB_VCA0368 DefenseFinder profiles. It
excludes individual SclA_VCA0367 or SclB_VCA0368 genes; SclA_VCA0367 or
SclB_VCA0368 proteins; DefenseFinder HMM profiles; predicted source-database
rows naming one Sucellos locus; unresolved Sucellos trigger or effector
activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual SclA_VCA0367 and
SclB_VCA0368 genes, the corresponding proteins, DefenseFinder HMMs, and
unresolved Sucellos molecular activities are shifted from this organism-level
GENOMICS possession trait.

`SclA_VCA0367` and `SclB_VCA0368` are proposed as related synonyms, not exact
synonyms, because they are source-profile labels for the component HMMs rather
than lexical names for the organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Sucellos source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000266` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000266` as traceability during the migration.

## Change Log

- v143, 2026-09: lifts `traitmech:000266 Sucellos system` into the
  `METPO:1022000` block.
