# METPO ROBOT Template Proposal - ApsAB System (v205, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v204 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for ApsAB system, the
genome-level possession trait for an ApsAB anti-plasmid defense locus. Zongo et
al. renamed the F3141-F3140 locus `apsAB` for antiplasmid system AB, showed
that ApsAB combines a nuclease/helicase protein and an Argonaute-like protein,
and reported activity against high- and low-copy-number plasmids.
DefenseFinder maps the named ApsAB system to the Zongo et al. Escherichia coli
anti-plasmid-system paper.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ApsAB |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028200` is reserved for this one-row class cohort. The v204 cohort used
`METPO:1028100`, so v205 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `apsab_system` slug, `ApsAB system`
label, `traitmech:000328`, `metpo_traitmech_v205`, or `METPO:1028200` was
present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028200` | ApsAB system | `METPO:1000188` quality |

ApsAB system captures genome-level possession of an ApsAB anti-plasmid locus
encoding ApsA nuclease/helicase and Argonaute-like ApsB components. It excludes
the individual `apsA` and `apsB` genes; the individual ApsA and ApsB proteins;
the F3141-F3140 source locus from ST38_1 Escherichia coli; DefenseFinder
article-registry rows; DefenseFinder HMM or rule rows; the pOXA-48
destabilization process itself; the distinct DdmDE and Wadjet anti-plasmid
systems; and generic plasmid carriage.

## External Mappings

No exact external mapping is proposed. The individual ApsA and ApsB proteins,
the `apsA` and `apsB` genes, the F3141-F3140 locus, DefenseFinder registry
rows, DdmDE, Wadjet, and plasmid destabilization are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact ApsAB synonyms, no related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000328` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000328` as traceability during the migration.

## Change Log

- v205, 2026-09: lifts `traitmech:000328 ApsAB system` into the
  `METPO:1028200` block.
