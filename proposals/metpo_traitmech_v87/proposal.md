# METPO ROBOT Template Proposal - BREX System (v87, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v86 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for a BREX system, the
genome-level possession trait for bacteriophage exclusion loci that use host
DNA methylation to distinguish self from non-self and block phage DNA
replication. The only exact prior phage-defense parent was
`METPO:1000237 obsolete phage defense`; v86 proposed a replacement
`phage defense system` parent, and this cohort adds BREX as a narrower child
under that pending parent.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000210` was minted locally because METPO has no active exact BREX-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016400` is reserved for this one-row class cohort. The v86 cohort used
`METPO:1016300`, so v87 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v87`, no live record used
`traitmech:000210`, and no prior proposal reserved `METPO:1016400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016400` | BREX system | `METPO:1016300` phage defense system |

BREX system captures genome-level possession of a methylation-based
bacteriophage-exclusion locus. It excludes the individual `pglX`, `pglZ`, and
`brx` gene products, generic Pgl growth-limitation labels without
BREX-equivalent locus evidence, source database rows that merely identify one
locus, and other antiphage systems such as DISARM, CBASS, abortive infection,
and phosphorothioate defense.

## External Mappings

No exact external mapping is proposed. GO has biological-process terms that can
ground causal nodes, and several domain databases name BREX-family component
proteins, but those are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000210` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000210` as traceability during the migration.

## Change Log

- v87, 2026-09: lifts `traitmech:000210 BREX system` into the
  `METPO:1016400` block.
