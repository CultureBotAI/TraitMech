# METPO ROBOT Template Proposal - SDIC1 System (v297, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v296 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SDIC1 system, the
genome-level possession trait for loci containing the SDIC1A and SDIC1B
components from the Serratia defense-island candidate system 1 family. Bayer et
al. identify SDIC1 in a cohort of newly reported anti-phage systems from
Serratia multi-conflict islands, connect SDIC1 to a TIR-domain and
ubiquitin-ligase-like architecture, and the pinned DefenseFinder HMM inventory
records SDIC1A and SDIC1B custom profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SDIC1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037400` is reserved for this one-row class cohort. The v296 cohort used
`METPO:1037300`, so v297 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope SDIC1 TraitMech, METPO, history,
or prior proposal record, no `sdic1_system` slug, no `traitmech:000420`, no
`metpo_traitmech_v297`, and no `METPO:1037400` / `METPO:10374xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037400` | SDIC1 system | `METPO:1016300` phage defense system |

SDIC1 system captures genome-level possession of an SDIC1 anti-phage locus
represented by DefenseFinder as SDIC1A and SDIC1B custom profiles. It excludes
individual `SDIC1A` or `SDIC1B` genes, individual TIR-domain or
ubiquitin-ligase-like proteins, ubiquitination reactions, Serratia
multi-conflict islands as a genome-organization feature, source database rows
naming one SDIC1 model, individual DefenseFinder HMM profiles, the absent
DefenseFinder rule-level model, unresolved phage-trigger and substrate biology,
and other phage-defense systems.

`traitmech:000420` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `SDIC1__SDIC1A` and `SDIC1__SDIC1B` are
kept as related synonyms because they name DefenseFinder profiles rather than
the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `SDIC1` synonym and the related DefenseFinder profile names.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000420` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000420` as traceability during the migration.

## Change Log

- v297, 2026-09: lifts `traitmech:000420 SDIC1 system` into the
  `METPO:1037400` block.
