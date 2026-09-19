# METPO ROBOT Template Proposal - Belenos System (v145, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v144 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Belenos system, the
genome-level possession trait for a Belenos anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Belenos with a VCA0457 profile in its
article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000268` was minted locally because METPO has no active exact Belenos-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022200` is reserved for this one-row class cohort. The v144 cohort used
`METPO:1022100`, so v145 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v145`, no live record used
`traitmech:000268`, and no prior proposal reserved `METPO:1022200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022200` | Belenos system | `METPO:1016300` phage defense system |

Belenos system captures genome-level possession of a Belenos locus represented
by a VCA0457 DefenseFinder profile. It excludes individual VCA0457 genes;
VCA0457 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Belenos locus; unresolved Belenos trigger or effector activities;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual VCA0457 genes, the
corresponding proteins, DefenseFinder HMMs, and unresolved Belenos molecular
activities are shifted from this organism-level GENOMICS possession trait.

`VCA0457` is proposed as a related synonym, not an exact synonym, because it is
a source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Belenos source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000268` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000268` as traceability during the migration.

## Change Log

- v145, 2026-09: lifts `traitmech:000268 Belenos system` into the
  `METPO:1022200` block.
