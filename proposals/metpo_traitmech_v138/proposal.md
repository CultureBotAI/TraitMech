# METPO ROBOT Template Proposal - Tiamat System (v138, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v137 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Tiamat system, the
genome-level possession trait for a bacterial antiphage locus named in Millman
et al. DefenseFinder models Tiamat with a required TmtA profile in its article
registry, rules table, and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000261` was minted locally because METPO has no active exact Tiamat-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021500` is reserved for this one-row class cohort. The v137 cohort used
`METPO:1021400`, so v138 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v138`, no live record used
`traitmech:000261`, and no prior proposal reserved `METPO:1021500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021500` | Tiamat system | `METPO:1016300` phage defense system |

Tiamat system captures genome-level possession of a Tiamat antiphage locus
represented by a TmtA DefenseFinder profile. It excludes individual TmtA genes;
standalone TmtA proteins; unresolved molecular trigger or effector activities;
DefenseFinder HMM profiles; predicted source-database rows naming one Tiamat
locus; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual TmtA genes, TmtA protein
profiles, DefenseFinder HMMs, and predicted locus calls are shifted from this
organism-level GENOMICS possession trait.

The pinned DefenseFinder registry row for Tiamat uses the 2022 bioRxiv preprint
DOI/title used by its sibling Millman-system rows.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Tiamat synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000261` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000261` as traceability during the migration.

## Change Log

- v138, 2026-09: lifts `traitmech:000261 Tiamat system` into the
  `METPO:1021500` block.
