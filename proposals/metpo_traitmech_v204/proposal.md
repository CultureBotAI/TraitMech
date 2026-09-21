# METPO ROBOT Template Proposal - Hesat System (v204, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v203 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Hesat system, the
genome-level possession trait for a Hesat anti-phage locus. Grafakou et al.
named Hesat among seven novel lactococcal antiphage systems, described it as a
single-gene system, and proposed a colicin-D-like translation-blocking activity
upon phage infection from AlphaFold2 and Dali structural comparisons.
DefenseFinder maps the named Hesat system to the Grafakou et al. lactococcal
plasmidome discovery paper.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Hesat |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028100` is reserved for this one-row class cohort. The v203 cohort used
`METPO:1028000`, so v204 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `hesat_system` slug, `Hesat system`
label, `traitmech:000327`, `metpo_traitmech_v204`, or `METPO:1028100` was
present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028100` | Hesat system | `METPO:1016300` phage defense system |

Hesat system captures genome-level possession of a single-gene Hesat locus
described among lactococcal plasmid-encoded phage-resistance systems and mapped
by DefenseFinder to the Grafakou et al. lactococcal plasmidome discovery paper.
It excludes the individual Hesat gene; Hesat protein; the pUCCL620_156 source
gene locus; DefenseFinder article-registry rows; the proposed, unvalidated
colicin-D-like translation-blocking mechanism; unresolved Hesat triggers or
effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual Hesat gene and protein,
the DefenseFinder registry row, the pUCCL620_156 source gene locus, and
unresolved Hesat molecular outputs are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Hesat synonym, no related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000327` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000327` as traceability during the migration.

## Change Log

- v204, 2026-09: lifts `traitmech:000327 Hesat system` into the
  `METPO:1028100` block.
