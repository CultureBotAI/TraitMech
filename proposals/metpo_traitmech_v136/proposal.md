# METPO ROBOT Template Proposal - SEFIR System (v136, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v135 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SEFIR system, the
genome-level possession trait for a bacterial antiphage defense locus named in
Millman et al. DefenseFinder models SEFIR with a required bSEFIR profile in its
article registry, rules table, and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000259` was minted locally because METPO has no active exact SEFIR-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021300` is reserved for this one-row class cohort. The v135 cohort used
`METPO:1021200`, so v136 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v136`, no live record used
`traitmech:000259`, and no prior proposal reserved `METPO:1021300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021300` | SEFIR system | `METPO:1016300` phage defense system |

SEFIR system captures genome-level possession of a SEFIR antiphage locus
represented by a bSEFIR DefenseFinder profile. It excludes individual genes;
standalone bSEFIR proteins; unresolved molecular trigger or effector activities;
DefenseFinder HMM profiles; predicted source-database rows naming one SEFIR
locus; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual SEFIR genes, bSEFIR protein
profiles, DefenseFinder HMMs, and predicted locus calls are shifted from this
organism-level GENOMICS possession trait.

The pinned DefenseFinder registry row for SEFIR uses the 2022 bioRxiv preprint
DOI/title used by its sibling Millman-system rows.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact SEFIR synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000259` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000259` as traceability during the migration.

## Change Log

- v136, 2026-09: lifts `traitmech:000259 SEFIR system` into the
  `METPO:1021300` block.
