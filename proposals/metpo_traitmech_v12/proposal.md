# METPO ROBOT Template Proposal - Pectin Degradation (v12, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v11 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

Metabolism round 2 left `pectinolysis` as a thinner-review follow-up next to
starch degradation, proteolysis, and lipolysis. Starch degradation and
proteolysis landed in the leftover cohort; lipolysis is obsolete in the local
METPO snapshot; pectin degradation remained a reusable microbial
biopolymer-degradation capability without a TraitMech record.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000135` was minted locally because METPO has no equivalent pectin degradation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1008900` is reserved for this one-row class cohort. The v11 cohort used
`METPO:1008800`-`METPO:1008814`, so v12 starts at the next hundred block to keep
cohorts visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, and ignored/hidden generated pages. No `METPO:1008900` use and no
existing `pectin degradation`, `pectinolysis`, `pectinolytic`, `pectinase`,
`polygalacturonase`, or `pectate lyase` TraitRecord/proposal row existed before
this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1008900` | pectin degradation | `METPO:1007709` biopolymer degradation |

Pectin degradation is parallel to the v5 biopolymer-degradation children for
cellulose, xylan, lignin, starch, protein, and chitin breakdown. Its pectinase
systems depolymerize pectin outside the cell or in the periplasm and feed
intracellular catabolism of oligogalacturonides.

## External Mappings

The term maps exactly to `GO:0045490` **pectin catabolic process**. GO uses the
same "catabolic process" convention already accepted for v5 `xylan degradation`
and `starch degradation`.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related-synonym column for the adjectival provenance label `pectinolytic`.
- `metpo_proposal_mappings.sssom.tsv` - one `skos:exactMatch` to `GO:0045490`.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` and
   `metpo_proposal_mappings.sssom.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000135` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000135` as traceability during the migration.

## Change Log

- v12, 2026-09: lifts `traitmech:000135 pectin degradation` into the
  `METPO:1008900` block.
