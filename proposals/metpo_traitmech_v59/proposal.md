# METPO ROBOT Template Proposal - Citrate Fermentation (v59, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v58 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no exact class for anaerobic citrate
fermentation, so this cohort lifts the local fallback record for citrate
fermentation.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000182` was minted locally because METPO has no equivalent citrate fermentation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013600` is reserved for this one-row class cohort. The v58 cohort used
`METPO:1013500`, so v59 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013600` appeared only in the
v58 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v59`, and no `traitmech:000182` or exact citrate fermentation
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013600` | citrate fermentation | `METPO:1002005` fermentation |

Citrate fermentation is a pathway-scoped microbial fermentation in which
citrate is the primary fermentable substrate. The class is narrower than
fermentation, and does not replace METPO composition with the `uses as carbon
source` or `uses as energy source` object properties for citrate-test or other
substrate-use observations.

## External Mappings

No exact external mapping is proposed. Broader citrate metabolic process terms,
individual citrate lyase or transporter molecular functions, and citrate-test
assay terms are shifted relative to the pathway-scoped citrate-fermentation
class, so the TraitRecord leaves `xrefs` empty and records the unresolved
external mapping as a `CURATION_TODO`.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  one related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000182` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000182` as traceability during the migration.

## Change Log

- v59, 2026-09: lifts `traitmech:000182 citrate fermentation` into the
  `METPO:1013600` block.
