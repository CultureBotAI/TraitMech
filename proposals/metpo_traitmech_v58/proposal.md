# METPO ROBOT Template Proposal - 2,3-Butanediol Fermentation (v58, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v57 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

TraitMech already has reviewed fermentation records under `METPO:1002005`
Fermentation, including product-specific records for lactic acid fermentation,
mixed-acid fermentation, ethanol fermentation, propionic acid fermentation,
butyric acid fermentation, and acetone-butanol-ethanol fermentation. The pinned
METPO snapshot has no exact class for 2,3-butanediol fermentation, so this
cohort lifts the local fallback record for the acetoin/2,3-butanediol
fermentation phenotype.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000181` was minted locally because METPO has no equivalent 2,3-butanediol fermentation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013500` is reserved for this one-row class cohort. The v57 cohort used
`METPO:1013400`, so v58 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013500` appeared only in the
v57 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v58`, and no `traitmech:000181` or exact
2,3-butanediol fermentation TraitRecord/proposal row existed before this
addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013500` | 2,3-butanediol fermentation | `METPO:1002005` Fermentation |

2,3-Butanediol fermentation is a product-specific fermentation class parallel
to the existing ethanol, propionic acid, butyric acid, and
acetone-butanol-ethanol fermentation records. The proposed term captures the
microbial fermentative phenotype that converts sugars through acetoin to
2,3-butanediol neutral end products.

## External Mappings

No exact external mapping is proposed. Broader fermentation process terms,
Voges-Proskauer assay terms, and individual acetoin or 2,3-butanediol
production reactions are shifted relative to the organism-level
2,3-butanediol fermentation phenotype, so the TraitRecord leaves `xrefs` empty
and records the unresolved external mapping as a `CURATION_TODO`.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000181` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000181` as traceability during the migration.

## Change Log

- v58, 2026-09: lifts `traitmech:000181 2,3-butanediol fermentation`
  into the `METPO:1013500` block.
