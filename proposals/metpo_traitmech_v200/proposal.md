# METPO ROBOT Template Proposal - Pif System (v200, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v199 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Pif system, the
genome-level possession trait for an F-plasmid pif-family
abortive-infection locus. Cram et al. molecularly cloned the F plasmid `pif`
region associated with abortive infection of T7 phage and detected two
pif-region polypeptides. DefenseFinder maps the named `Pif` namespace to
required `Pif__PifA` and `Pif__PifC` HMM profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Pif |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027700` is reserved for this one-row class cohort. The v199 cohort used
`METPO:1027600`, so v200 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `pif_system` slug, `Pif system` label,
`Pif__PifA` or `Pif__PifC` model row, `traitmech:000323`,
`metpo_traitmech_v200`, `METPO:1027700`, `DOI:10.1007/BF00327934`, or
`PMID:6096670` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027700` | Pif system | `METPO:1016800` abortive infection system |

Pif system captures genome-level possession of an F-plasmid pif-family locus
represented by DefenseFinder's `Pif__PifA` and `Pif__PifC` HMM profiles and
exemplified by the pif region that specifies abortive infection of T7 phage. It
excludes individual `pif` genes; PifA and PifC proteins; the F plasmid itself;
the individual DefenseFinder HMM profiles; source database rows naming one Pif
locus; T7-specific host-range outcomes; unresolved direct T7 triggers; and
generic abortive-infection systems.

## External Mappings

No exact external mapping is proposed. Pif, PifA, PifC, the F plasmid, the
DefenseFinder HMMs, individual T7-resistance outcomes, and
abortive-infection processes are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000323` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000323` as traceability during the migration.

## Change Log

- v200, 2026-09: lifts `traitmech:000323 Pif system` into the
  `METPO:1027700` block.
