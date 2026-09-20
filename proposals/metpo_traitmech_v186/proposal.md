# METPO ROBOT Template Proposal - Hypnos System (v186, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v185 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Hypnos system, the
genome-level possession trait for a Hypnos anti-phage locus. van den Berg et
al. reported a search over bacterial homologs of innate eukaryotic antiviral
defense genes and validated six phage defense systems, and DefenseFinder
catalogs Hypnos with a `Hypnos__HyoA` HMM profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Hypnos |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026300` is reserved for this one-row class cohort. The v185 cohort used
`METPO:1026200`, so v186 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No exact search hit was found for `Hypnos`, `Hypnos__HyoA`, `HyoA`,
`hypnos_system`, `traitmech:000309`, `metpo_traitmech_v186`, or
`METPO:1026300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026300` | Hypnos system | `METPO:1016300` phage defense system |

Hypnos system captures genome-level possession of a Hypnos locus cataloged by
DefenseFinder under a Hypnos model namespace with a `Hypnos__HyoA` HMM profile
entry. It excludes individual HyoA genes; HyoA proteins; the DefenseFinder
Hypnos__HyoA HMM profile; source-database rows naming one Hypnos locus;
unresolved Hypnos trigger or effector activities; and other phage-defense
systems.

## External Mappings

No exact external mapping is proposed. The `Hypnos__HyoA` HMM, individual
HyoA-labeled genes, their corresponding proteins, and unresolved Hypnos
molecular outputs are shifted from this organism-level GENOMICS possession
trait.

`HyoA` is proposed as a related synonym, not an exact synonym, because it is a
source-profile label for the component HMM rather than a lexical name for the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Hypnos synonym, a related non-exact HyoA label, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000309` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000309` as traceability during the migration.

## Change Log

- v186, 2026-09: lifts `traitmech:000309 Hypnos system` into the
  `METPO:1026300` block.
