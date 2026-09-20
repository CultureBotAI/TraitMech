# METPO ROBOT Template Proposal - Erebus System (v185, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v184 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Erebus system, the
genome-level possession trait for an Erebus anti-phage locus. van den Berg et
al. reported a search over bacterial homologs of innate eukaryotic antiviral
defense genes and validated six phage defense systems, and DefenseFinder
catalogs Erebus with an `Erebus__EruA` HMM profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Erebus |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026200` is reserved for this one-row class cohort. The v184 cohort used
`METPO:1026100`, so v185 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository,
excluding only `.git`, generated `reports/robot`, and large generated page
files. No prior proposal reserved `metpo_traitmech_v185`, no live record used
`traitmech:000308`, and no prior proposal reserved `METPO:1026200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026200` | Erebus system | `METPO:1016300` phage defense system |

Erebus system captures genome-level possession of an Erebus locus cataloged by
DefenseFinder under an Erebus model namespace with an `Erebus__EruA` HMM
profile entry. It excludes individual EruA genes; EruA proteins; DefenseFinder
HMM profiles; predicted source-database rows naming one Erebus locus; unresolved
Erebus trigger or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The `Erebus__EruA` HMM, individual
EruA-labeled genes, their corresponding proteins, and unresolved Erebus
molecular outputs are shifted from this organism-level GENOMICS possession
trait.

`EruA` is proposed as a related synonym, not an exact synonym, because it is a
source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Erebus synonym, a related non-exact EruA label, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000308` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000308` as traceability during the migration.

## Change Log

- v185, 2026-09: lifts `traitmech:000308 Erebus system` into the
  `METPO:1026200` block.
