# METPO ROBOT Template Proposal - Phage Defense System (v86, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v85 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for phage defense system,
the genome-level possession trait for bacterial or archaeal immune systems that
inhibit bacteriophage infection. The only METPO phage-defense label is
`METPO:1000237 obsolete phage defense`, so TraitMech needs a replacement
GENOMICS parent that can group the already accepted `CRISPR-Cas system` and
`restriction-modification system` records while leaving narrower BREX, DISARM,
abortive-infection, CBASS, and related systems for later child proposals.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000209` was minted locally because METPO has no active exact phage-defense-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016300` is reserved for this one-row class cohort. The v85 cohort used
`METPO:1016200`, so v86 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v86`, no live record used
`traitmech:000209`, and no prior proposal reserved `METPO:1016300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016300` | phage defense system | `METPO:1000188` genomics |

Phage defense system captures genome-level possession of one or more microbial
immune systems that inhibit bacteriophage infection. It includes established
defense families such as CRISPR-Cas and restriction-modification systems, and is
intended to parent later child records for narrower phage-defense modules such
as BREX, DISARM, abortive-infection, CBASS, and phosphorothioate defense. It
excludes phage counter-defense mechanisms, surface receptor loss, prophage
possession by itself, individual Cas or restriction-enzyme proteins, and source
database feature rows that merely identify one defense locus.

## External Mappings

No exact external mapping is proposed. GO:0051607 defense response to virus
denotes a biological process that can ground causal nodes but is shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  exact synonyms, no exact external xrefs, and one related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000209` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000209` as traceability during the migration.

## Change Log

- v86, 2026-09: lifts `traitmech:000209 phage defense system` into the
  `METPO:1016300` block.
