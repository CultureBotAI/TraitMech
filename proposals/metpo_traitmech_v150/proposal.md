# METPO ROBOT Template Proposal - DARNA System (v150, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v149 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DARNA system, the
genome-level possession trait for the bacterial DARNA anti-phage defense
system. Puteikiene et al. reported that phage SSB-presented single-stranded DNA
activates DARNA, after which DARNA cleaves a subset of host tRNAs and inhibits
phage propagation. DefenseFinder maps DARNA to that DOI in its article
registry, but the pinned DefenseFinder snapshot has no quoted DARNA HMM or rule
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000273` was minted locally because METPO has no active exact DARNA-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022700` is reserved for this one-row class cohort. The v149 cohort used
`METPO:1022600`, so v150 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v150`, no live record used
`traitmech:000273`, and no prior proposal reserved `METPO:1022700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022700` | DARNA system | `METPO:1016300` phage defense system |

DARNA system captures genome-level possession of the anti-phage defense system
whose DARNA protein can be activated by single-stranded DNA presented by phage
SSB. It excludes the DARNA immunity protein alone; phage or host SSB proteins;
single-stranded DNA presentation as a process; host tRNA cleavage as a process;
DefenseFinder article-registry rows; unresolved DARNA component profiles; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The DARNA immunity protein alone, phage
or host SSB proteins, the activating phage SSB-single-stranded-DNA state, and
host tRNA cleavage are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000273` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000273` as traceability during the migration.

## Change Log

- v150, 2026-09: lifts `traitmech:000273 DARNA system` into the
  `METPO:1022700` block.
