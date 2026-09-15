# METPO ROBOT Template Proposal - Abortive Infection System (v91, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v90 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for an abortive infection
system, the genome-level possession trait for Abi phage defenses that arrest or
kill infected host cells before phage replication completes. The v86 cohort
proposed a `phage defense system` parent, v87 through v90 proposed BREX,
DISARM, CBASS, and phosphorothioate children, and this cohort adds abortive
infection as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000214` was minted locally because METPO has no active exact abortive-infection-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016800` is reserved for this one-row class cohort. The v90 cohort used
`METPO:1016700`, so v91 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v91`, no live record used
`traitmech:000214`, and no prior proposal reserved `METPO:1016800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016800` | abortive infection system | `METPO:1016300` phage defense system |

Abortive infection system captures genome-level possession of a phage-triggered
defense system that aborts productive infection by arresting or killing the
infected host cell and thereby limiting phage spread through the bacterial
population. It excludes individual ToxIN, AbiQ, AbiE, and other Abi-family
subfamilies; individual toxin, antitoxin, sensor, and effector genes or
proteins; toxin-antitoxin modules without direct Abi evidence; generic cell
death or growth arrest outside phage defense; source database rows naming one
Abi locus; and other antiphage systems such as BREX, DISARM, CBASS,
CRISPR-Cas, and phosphorothioate defense.

## External Mappings

No exact external mapping is proposed. Toxin-antitoxin and abortive-cell-death
process terms are mechanism pieces or narrower families shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  Abi exact synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000214` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000214` as traceability during the migration.

## Change Log

- v91, 2026-09: lifts `traitmech:000214 abortive infection system` into the
  `METPO:1016800` block.
