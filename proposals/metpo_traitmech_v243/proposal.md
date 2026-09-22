# METPO ROBOT Template Proposal - RloC System (v243, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v242 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for RloC system, the
genome-level possession trait for a genome-encoded `RloC` locus modeled by
DefenseFinder as a one-profile system requiring `RloC__RloC`. Davidov and
Kaufmann identify RloC as a conserved bacterial wobble nucleotide-excising and
zinc-responsive tRNase. Bitton et al. show that an `Acinetobacter baylyi` RloC
expressed in `Escherichia coli` is activated by wild-type phage T4 and impairs
T4 plating. DefenseFinder maps the `RloC` key to the Davidov and Kaufmann paper
while pinning a custom `RloC__RloC` profile for this system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for RloC |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032000` is reserved for this one-row class cohort. The v242 cohort used
`METPO:1031900`, so v243 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, excluding only `.git`. It found no exact same-scope RloC
system record, `rloc_system` slug, `RloC__RloC` profile row, RloC DOI or PMID,
`traitmech:000366`, `metpo_traitmech_v243`, or `METPO:1032000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032000` | RloC system | `METPO:1016300` phage defense system |

RloC system captures genome-level possession of a genome-encoded `RloC` locus
represented by DefenseFinder as a one-profile model requiring `RloC__RloC`. It
excludes the individual RloC anticodon nuclease, anticodon nuclease activity,
the `RloC__RloC` HMM profile, T4-induced ACNase activation in an
`Escherichia coli` expression assay, source database rows naming one RloC model,
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual RloC proteins, ACNase
activity, host DNA-degradation-triggered T4 restriction in an expression
assay, and DefenseFinder profile rows are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, two related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000366` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000366` as traceability during the migration.

## Change Log

- v243, 2026-09: lifts `traitmech:000366 RloC system` into the
  `METPO:1032000` block.
