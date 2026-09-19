# METPO ROBOT Template Proposal - Esos System (v159, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v158 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Esos system, the
genome-level possession trait for an Esos anti-phage locus. Darracq et al.
reported novel antiphage functions from Vibrio cholerae sedentary chromosomal
integron cassettes, and DefenseFinder models Esos with a VCA0450 profile in
its HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000282` was minted locally because METPO has no active exact Esos-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023600` is reserved for this one-row class cohort. The v158 cohort used
`METPO:1023500`, so v159 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v159`, no live record used
`traitmech:000282`, and no prior proposal reserved `METPO:1023600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023600` | Esos system | `METPO:1016300` phage defense system |

Esos system captures genome-level possession of an Esos locus represented by
the VCA0450 DefenseFinder profile. It excludes individual VCA0450 genes;
VCA0450 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Esos locus; unresolved Esos trigger or effector activities; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. SCI cassette genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Esos molecular outputs are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Esos synonym, one related VCA0450 source-profile label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000282` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000282` as traceability during the migration.

## Change Log

- v159, 2026-09: lifts `traitmech:000282 Esos system` into the
  `METPO:1023600` block.
