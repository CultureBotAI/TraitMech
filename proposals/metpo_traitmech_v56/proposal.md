# METPO ROBOT Template Proposal - Butyric Acid Fermentation (v56, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v55 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

TraitMech already has reviewed product-specific fermentation records for lactic
acid fermentation, mixed-acid fermentation, ethanol fermentation, and propionic
acid fermentation under `METPO:1002005` Fermentation. The pinned METPO snapshot
has no exact butyric acid fermentation term, so this cohort lifts the local
fallback record for the parallel butyrate-producing fermentation phenotype.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000179` was minted locally because METPO has no equivalent butyric acid fermentation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013300` is reserved for this one-row class cohort. The v55 cohort used
`METPO:1013200`, so v56 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013300` appeared only in the
v55 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v56`, and no `traitmech:000179` or exact butyric acid
fermentation TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013300` | butyric acid fermentation | `METPO:1002005` Fermentation |

Butyric acid fermentation is a product-specific fermentation class parallel to
the existing lactic acid, mixed-acid, ethanol, propionic acid, and fermentative
hydrogen production records. The proposed term captures the bacterial
fermentative phenotype that converts organic substrates to butyrate as a major
reduced end product while conserving energy through substrate-level
phosphorylation and reduced-ferredoxin-dependent ion-gradient generation.

## External Mappings

No exact external mapping is proposed. Butyrate-synthesis enzyme molecular
functions and butyrate-producing reactions are shifted relative to the
organism-level butyric acid fermentation phenotype, so the TraitRecord leaves
`xrefs` empty and records the unresolved external mapping as a `CURATION_TODO`.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000179` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000179` as traceability during the migration.

## Change Log

- v56, 2026-09: lifts `traitmech:000179 butyric acid fermentation` into the
  `METPO:1013300` block.
