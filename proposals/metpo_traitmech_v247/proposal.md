# METPO ROBOT Template Proposal - MADS System (v247, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v246 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for MADS system, the
genome-level possession trait for a methylation-associated bacterial
phage-defense locus. Maestri et al. support MADS as a methylation-associated
defense system active against DNA phages. DefenseFinder maps the `MADS` key to
the Maestri et al. preprint in its article registry and models the system in the
pinned rule and HMM tables with `MADS__mad1` through `MADS__mad8` profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MADS |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032400` is reserved for this one-row class cohort. The v246 cohort used
`METPO:1032300`, so v247 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope MADS system record, `mads_system`
slug, Maestri et al. Cell Host & Microbe DOI, `traitmech:000370`,
`metpo_traitmech_v247`, or `METPO:1032400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032400` | MADS system | `METPO:1016300` phage defense system |

MADS system captures genome-level possession of a
methylation-associated defense system locus whose canonical architecture has
mad1 through mad8 genes and whose methylation-coupled self/non-self
discrimination can restrict bacteriophage infection. It excludes individual Mad
proteins and DefenseFinder `MADS__mad*` profiles, MADS3-4 systems, MADS-like
systems, methylation, specificity, nuclease, ATPase, kinase, CRISPR-Cas
interaction, phage cooperation disruption, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual MADS components, the
MADS-associated methylation and restriction activities, the CRISPR-Cas
interaction in the native host, and source database rows naming one MADS model
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000370` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000370` as traceability during the migration.

## Change Log

- v247, 2026-09: lifts `traitmech:000370 MADS system` into the
  `METPO:1032400` block.
