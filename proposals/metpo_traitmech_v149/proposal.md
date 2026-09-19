# METPO ROBOT Template Proposal - Damona System (v149, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v148 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Damona system, the
genome-level possession trait for a Damona anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Damona with a VCA0399 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000272` was minted locally because METPO has no active exact Damona-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022600` is reserved for this one-row class cohort. The v148 cohort used
`METPO:1022500`, so v149 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v149`, no live record used
`traitmech:000272`, and no prior proposal reserved `METPO:1022600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022600` | Damona system | `METPO:1016300` phage defense system |

Damona system captures genome-level possession of a Damona locus represented by
a VCA0399 DefenseFinder profile. It excludes individual VCA0399 genes; VCA0399
proteins; DefenseFinder HMM profiles; predicted source-database rows naming one
Damona locus; unresolved Damona trigger or effector activities; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0399 genes, the
corresponding proteins, DefenseFinder HMMs, and unresolved Damona molecular
activities are shifted from this organism-level GENOMICS possession trait.

`VCA0399` is proposed as a related synonym, not an exact synonym, because it is
a source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Damona source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000272` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000272` as traceability during the migration.

## Change Log

- v149, 2026-09: lifts `traitmech:000272 Damona system` into the
  `METPO:1022600` block.
