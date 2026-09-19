# METPO ROBOT Template Proposal - Lugos System (v160, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v159 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Lugos system, the
genome-level possession trait for a Lugos anti-phage locus. Darracq et al.
reported novel antiphage functions from Vibrio cholerae sedentary chromosomal
integron cassettes, and DefenseFinder models Lugos with a VCA0409 profile in
its HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000283` was minted locally because METPO has no active exact Lugos-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023700` is reserved for this one-row class cohort. The v159 cohort used
`METPO:1023600`, so v160 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v160`, no live record used
`traitmech:000283`, and no prior proposal reserved `METPO:1023700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023700` | Lugos system | `METPO:1016300` phage defense system |

Lugos system captures genome-level possession of a Lugos locus represented by
the VCA0409 DefenseFinder profile. It excludes individual VCA0409 genes;
VCA0409 proteins; DefenseFinder HMM profiles; predicted source-database rows
naming one Lugos locus; unresolved Lugos trigger or effector activities; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. SCI cassette genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Lugos molecular outputs are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Lugos synonym, one related VCA0409 source-profile label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000283` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000283` as traceability during the migration.

## Change Log

- v160, 2026-09: lifts `traitmech:000283 Lugos system` into the
  `METPO:1023700` block.
