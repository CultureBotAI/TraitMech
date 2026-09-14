# METPO ROBOT Template Proposal - Acetone-Butanol-Ethanol Fermentation (v57, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v56 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

TraitMech already has reviewed fermentation records under `METPO:1002005`
Fermentation, including product-specific records for lactic acid fermentation,
mixed-acid fermentation, ethanol fermentation, propionic acid fermentation, and
butyric acid fermentation. The pinned METPO snapshot has no exact class for
acetone-butanol-ethanol fermentation, so this cohort lifts the local fallback
record for the solventogenic fermentation phenotype.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000180` was minted locally because METPO has no equivalent acetone-butanol-ethanol fermentation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013400` is reserved for this one-row class cohort. The v56 cohort used
`METPO:1013300`, so v57 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013400` appeared only in the
v56 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v57`, and no `traitmech:000180` or exact
acetone-butanol-ethanol fermentation TraitRecord/proposal row existed before
this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013400` | acetone-butanol-ethanol fermentation | `METPO:1002005` Fermentation |

Acetone-butanol-ethanol fermentation is a product-specific solventogenic
fermentation class parallel to the existing ethanol, propionic acid, and
butyric acid fermentation records. The proposed term captures the bacterial
fermentative phenotype that converts organic carbon sources to organic acids and
then reassimilates those acids to produce acetone, butanol, and ethanol.

## External Mappings

No exact external mapping is proposed. Broader fermentation process terms and
individual solvent-production reactions are shifted relative to the
organism-level acetone-butanol-ethanol fermentation phenotype, so the
TraitRecord leaves `xrefs` empty and records the unresolved external mapping as
a `CURATION_TODO`.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000180` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000180` as traceability during the migration.

## Change Log

- v57, 2026-09: lifts `traitmech:000180 acetone-butanol-ethanol fermentation`
  into the `METPO:1013400` block.
