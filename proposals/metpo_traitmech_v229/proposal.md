# METPO ROBOT Template Proposal - Gao-RL System (v229, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v228 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-RL system, the
genome-level possession trait for a `Gao_RL` phage-defense locus modeled by
DefenseFinder as a four-profile system requiring `Gao_RL__RL_A`,
`Gao_RL__RL_B`, `Gao_RL__RL_C`, and `Gao_RL__RL_D`. Gao et al.
discovered widespread antiviral gene cassettes with diverse enzymatic
activities against specific bacteriophages, and DefenseFinder maps `Gao_RL`
to that paper while pinning the four custom RL profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-RL |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1030600` is reserved for this one-row class cohort. The v228 cohort used
`METPO:1030500`, so v229 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across
`data/raw/metpo.owl`, `data/traits`, `proposals`, `history`, and `scripts`. It
found no exact same-scope record, `gao_rl_system` slug, `Gao-RL system` label,
`Gao_RL` key, `traitmech:000352`, `metpo_traitmech_v229`, or `METPO:1030600`
before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1030600` | Gao-RL system | `METPO:1016300` phage defense system |

Gao-RL system captures genome-level possession of a `Gao_RL` locus represented
by DefenseFinder as a four-profile model requiring `Gao_RL__RL_A` through
`Gao_RL__RL_D`. It excludes the individual `Gao_RL__RL_A`, `Gao_RL__RL_B`,
`Gao_RL__RL_C`, and `Gao_RL__RL_D` HMM profiles; individual Gao-family genes or
proteins; source database rows naming one `Gao_RL` model; other Gao-family
systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual custom profiles, Gao-family
proteins, and unresolved downstream mobile-element interference are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, five related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000352` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000352` as traceability during the migration.

## Change Log

- v229, 2026-09: lifts `traitmech:000352 Gao-RL system` into the
  `METPO:1030600` block.
