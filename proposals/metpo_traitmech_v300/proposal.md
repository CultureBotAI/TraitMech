# METPO ROBOT Template Proposal - SDIC3 System (v300, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v299 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SDIC3 system, the
genome-level possession trait for a Serratia defense-island candidate
anti-phage locus that Cummins et al. identified among SDIC1-3 and assayed in
heterologous phage-challenge experiments. The pinned DefenseFinder HMM
inventory records custom SDIC3B, SDIC3C, SDIC3D, SDIC3E, and SDIC3F rows, while
the pinned DefenseFinder rules table has no SDIC3 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SDIC3 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037700` is reserved for this one-row class cohort. The v299 cohort used
`METPO:1037600`, so v300 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope SDIC3 TraitMech, METPO, history,
or prior proposal record, no `sdic3_system` slug, no `traitmech:000423`, no
`metpo_traitmech_v300`, and no `METPO:1037700` / `METPO:10377xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037700` | SDIC3 system | `METPO:1016300` phage defense system |

SDIC3 system captures genome-level possession of the Serratia defense-island
candidate locus represented in DefenseFinder by SDIC3B, SDIC3C, SDIC3D,
SDIC3E, and SDIC3F HMM-profile rows. It excludes the individual SDIC3A,
SDIC3B, SDIC3C, SDIC3D, SDIC3E, or SDIC3F genes and proteins, individual
DefenseFinder HMM profile rows, source database rows naming one SDIC3 model,
Serratia defense islands, the related ECOR61 prophage-encoded anti-phage
system, the absent SDIC3 rule-level DefenseFinder model, unresolved SDIC3A
scope, unresolved direct effector chemistry, and other SDIC or phage-defense
systems.

`traitmech:000423` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. Individual `SDIC3__*` HMM row names are
kept as related synonyms because they name DefenseFinder profile keys rather
than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `SDIC3` synonym and related DefenseFinder profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000423` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000423` as traceability during the migration.

## Change Log

- v300, 2026-09: lifts `traitmech:000423 SDIC3 system` into the
  `METPO:1037700` block.
