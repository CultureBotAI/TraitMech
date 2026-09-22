# METPO ROBOT Template Proposal - Gao-Qat System (v236, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v235 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Qat system, the
genome-level possession trait for a `Gao_Qat` phage-defense locus modeled by
DefenseFinder as a four-profile system requiring `Gao_Qat__QatA`,
`Gao_Qat__QatB`, `Gao_Qat__QatC`, and `Gao_Qat__QatD`. Gao et al. discovered
widespread antiviral gene cassettes with diverse enzymatic activities against
specific bacteriophages, and DefenseFinder maps `Gao_Qat` to that paper while
pinning the custom QatA through QatD profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Qat |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031300` is reserved for this one-row class cohort. The v235 cohort used
`METPO:1031200`, so v236 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_qat_system` slug,
`Gao-Qat system` label, `Gao_Qat` key, Qat HMM profiles, `traitmech:000359`,
`metpo_traitmech_v236`, or `METPO:1031300` before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031300` | Gao-Qat system | `METPO:1016300` phage defense system |

Gao-Qat system captures genome-level possession of a `Gao_Qat` locus represented
by DefenseFinder as a four-profile model requiring `Gao_Qat__QatA`,
`Gao_Qat__QatB`, `Gao_Qat__QatC`, and `Gao_Qat__QatD`. It excludes the
individual Qat HMM profiles; individual Gao-family genes or proteins; source
database rows naming one `Gao_Qat` model; other Gao-family systems; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom Qat profiles and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, five related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000359` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000359` as traceability during the migration.

## Change Log

- v236, 2026-09: lifts `traitmech:000359 Gao-Qat system` into the
  `METPO:1031300` block.
