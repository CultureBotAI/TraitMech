# METPO ROBOT Template Proposal - SDIC4 System (v298, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v297 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SDIC4 system, the
genome-level possession trait for loci containing SDIC4A and the VasI-like
SDIC4B component from the Serratia defense-island candidate system 4 family.
Cummins et al. identify SDIC4 in a cohort of newly reported anti-phage systems
from Serratia multi-conflict islands, connect full-length SDIC4 and SDIC4B with
reduced bacteriophage adsorption, and the pinned DefenseFinder HMM inventory
records SDIC4A and SDIC4B custom profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SDIC4 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037500` is reserved for this one-row class cohort. The v297 cohort used
`METPO:1037400`, so v298 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope SDIC4 TraitMech, METPO, history,
or prior proposal record, no `sdic4_system` slug, no `traitmech:000421`, no
`metpo_traitmech_v298`, and no `METPO:1037500` / `METPO:10375xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037500` | SDIC4 system | `METPO:1016300` phage defense system |

SDIC4 system captures genome-level possession of an SDIC4 anti-phage locus
represented by DefenseFinder as SDIC4A and SDIC4B custom profiles. It excludes
individual `SDIC4A` or `SDIC4B` genes, individual VasI-like proteins, Ig-like
folds, phage adsorption as a process, Serratia multi-conflict islands as a
genome-organization feature, source database rows naming one SDIC4 model,
individual DefenseFinder HMM profiles, the absent DefenseFinder rule-level
model, unresolved receptor or phage-target biology, unresolved SDIC4 subtype
scope, and other phage-defense systems.

`traitmech:000421` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `SDIC4__SDIC4A` and `SDIC4__SDIC4B` are
kept as related synonyms because they name DefenseFinder profiles rather than
the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `SDIC4` synonym and the related DefenseFinder profile names.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000421` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000421` as traceability during the migration.

## Change Log

- v298, 2026-09: lifts `traitmech:000421 SDIC4 system` into the
  `METPO:1037500` block.
