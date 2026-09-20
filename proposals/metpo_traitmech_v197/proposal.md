# METPO ROBOT Template Proposal - AbiC System (v197, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v196 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiC system, the
genome-level possession trait for an `abiC` abortive-infection locus.
Durmaz et al. subcloned the Prf determinant from the Lactococcus lactis subsp.
lactis ME2 conjugative plasmid pTN20, identified its abiC structural gene,
showed that abiC expression was sufficient for Prf-positive activity, and
measured reduced p2 plaquing, plaque size, and burst size with death of most
Prf-positive phage p2-infected cells. DefenseFinder models AbiC with one
required `AbiC__AbiC` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiC |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027400` is reserved for this one-row class cohort. The v196 cohort used
`METPO:1027300`, so v197 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. No exact same-scope record, `abic_system` slug, `AbiC system`
label, `AbiC__AbiC` model row, `traitmech:000320`,
`metpo_traitmech_v197`, `METPO:1027400`,
`DOI:10.1128/jb.174.22.7463-7469.1992`, or `PMID:1429469` was present
before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027400` | AbiC system | `METPO:1016800` abortive infection system |

AbiC system captures genome-level possession of an `abiC` locus represented by
DefenseFinder's `AbiC__AbiC` HMM profile and exemplified by the lactococcal
ME2 pTN20 determinant. It excludes the individual `abiC` gene; AbiC proteins;
the pTN20 plasmid; the individual DefenseFinder HMM profile; source database
rows naming one AbiC locus; individual lactococcal phage host-range outcomes;
unresolved AbiC triggers or cell-death routes; and other abortive-infection
systems.

## External Mappings

No exact external mapping is proposed. AbiC, pTN20, the DefenseFinder HMM,
individual phage-resistance outcomes, and infected-cell death processes are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000320` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000320` as traceability during the migration.

## Change Log

- v197, 2026-09: lifts `traitmech:000320 AbiC system` into the
  `METPO:1027400` block.
