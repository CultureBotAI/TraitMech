# METPO ROBOT Template Proposal - Bacteriocin Production (v60, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v59 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no exact class for bacteriocin production, so this
cohort lifts the local fallback record for the broad bacteriocin-producing
physiology.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000183` was minted locally because METPO has no equivalent bacteriocin production class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013700` is reserved for this one-row class cohort. The v59 cohort used
`METPO:1013600`, so v60 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013700` appeared only in the
v59 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v60`, and no `traitmech:000183` or exact bacteriocin
production TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013700` | bacteriocin production | `METPO:1000059` phenotype |

Bacteriocin production is an organism-level bacterial physiology in which a
cell produces ribosomally synthesized antimicrobial bacteriocin peptides or
proteins that can kill or inhibit other bacteria. The class is not a sequence
feature call for one bacteriocin biosynthetic gene cluster, and it is broader
than any single nisin, colicin, or other bacteriocin-family biosynthetic
branch.

## External Mappings

`GO:0030152` bacteriocin biosynthetic process is proposed as an exact external
mapping because this TraitMech class captures the bacterial capability to
produce bacteriocin products rather than the presence of one narrow
nisin-specific biosynthesis branch or an individual bacteriocin gene family.
The mapping grounds the broad production physiology while staying outside
sequence-feature interpretation.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  one related synonym and one exact external xref.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000183` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000183` as traceability during the migration.

## Change Log

- v60, 2026-09: lifts `traitmech:000183 bacteriocin production` into the
  `METPO:1013700` block.
