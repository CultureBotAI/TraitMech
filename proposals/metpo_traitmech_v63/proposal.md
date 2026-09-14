# METPO ROBOT Template Proposal - Siderophore Production (v63, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v62 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the bacterial
physiology trait in which cells biosynthesize and release siderophores for
extracellular iron scavenging. This cohort lifts the local fallback record for
broad siderophore production and keeps it separate from process-level
biosynthesis or transport terms and from molecule-level siderophore classes.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000186` was minted locally because METPO has no active equivalent siderophore production class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014000` is reserved for this one-row class cohort. The v62 cohort used
`METPO:1013900`, so v63 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014000` appeared only in the v62
next-block reservation note and its matching history record, no prior proposal
reserved `metpo_traitmech_v63`, and no `traitmech:000186` or exact live
`siderophore production` TraitRecord/proposal row existed before this addition.
The search found only the deprecated `METPO:1000277 obsolete siderophore` class
in the pinned METPO snapshot plus siderophore-related causal nodes and research
leads whose scope is siderophore secretion, biosynthesis, or iron import inside
broader ecology records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014000` | siderophore production | `METPO:1000059` phenotype |

Siderophore production is a physiology trait in which bacteria synthesize and
release siderophores that scavenge extracellular iron for uptake. The class is
kept separate from GO process terms for siderophore biosynthesis or transport
and from CHEBI's molecule-level siderophore class.

## External Mappings

No exact external mapping is proposed. GO:0019290 denotes the siderophore
biosynthetic process without secretion or organism-level phenotype scope,
GO:0015891 denotes siderophore transport, and CHEBI:26672 denotes the
siderophore molecule class.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000186` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000186` as traceability during the migration.

## Change Log

- v63, 2026-09: lifts `traitmech:000186 siderophore production` into the
  `METPO:1014000` block.
