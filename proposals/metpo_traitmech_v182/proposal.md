# METPO ROBOT Template Proposal - JukAB System (v182, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v181 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for JukAB system, the
genome-level possession trait for a two-gene jukAB locus. Li et al. identified
JukAB as a two-component immune system in which JukA binds the PhiKZ-like gp241
early phage protein at the EPI vesicle, directly recruits the JukB effector,
and suppresses early nucleus-forming jumbo-phage infection; DefenseFinder
catalogs JukAB with a two-profile rule.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for JukAB |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025900` is reserved for this one-row class cohort. The v181 cohort used
`METPO:1025800`, so v182 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository,
excluding only `.git`, `.venv`, generated robot/page/app output, and embeddings.
No prior proposal reserved `metpo_traitmech_v182`, no live record used
`traitmech:000305`, and no prior proposal reserved `METPO:1025900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025900` | JukAB system | `METPO:1016300` phage defense system |

JukAB system captures genome-level possession of a two-gene jukAB locus
encoding the JukA sensor and JukB effector that bind gp241 at the EPI vesicle,
destabilize that vesicle, and block early nucleus-forming jumbo-phage
infection. It excludes the individual `jukA` and `jukB` genes; JukA or JukB
proteins; JukA-only and other JukA-containing immune systems; the DefenseFinder
`JukAB__JukA` and `JukAB__JukB` HMM profiles; source database rows naming one
JukAB locus; the PhiKZ-like gp241 trigger protein; EPI vesicles; and other
phage-defense systems such as AVAST Avs5.

## External Mappings

No exact external mapping is proposed. JukAB, JukA, JukB, gp241, EPI vesicles,
DefenseFinder HMMs, and JukB vesicle-destabilization activity are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related JukAB labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000305` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000305` as traceability during the migration.

## Change Log

- v182, 2026-09: lifts `traitmech:000305 JukAB system` into the
  `METPO:1025900` block.
