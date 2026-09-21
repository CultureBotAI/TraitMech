# METPO ROBOT Template Proposal - SpbK System (v202, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v201 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SpbK system, the
genome-level possession trait for an ICEBs1-like SpbK-family abortive-infection
locus. Johnson et al. showed that the ICEBs1 `spbK` gene inhibits SPβ phage
production in *Bacillus subtilis* and that SpbK with the SPβ `yonE` gene
constitutes an abortive infection system that leads to cell death. DefenseFinder
maps the named `SpbK` namespace to the required `SpbK__SpbK` HMM profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SpbK |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027900` is reserved for this one-row class cohort. The v201 cohort used
`METPO:1027800`, so v202 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `spbk_system` slug, `SpbK system`
label, `SpbK__SpbK` model row, `traitmech:000325`,
`metpo_traitmech_v202`, `METPO:1027900`, or
`DOI:10.1371/journal.pgen.1010065` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027900` | SpbK system | `METPO:1016800` abortive infection system |

SpbK system captures genome-level possession of a SpbK-family locus represented
by DefenseFinder's `SpbK__SpbK` HMM profile and exemplified by the ICEBs1
`spbK` gene whose SPβ-YonE-dependent activity inhibits SPβ production and kills
infected cells. It excludes individual `spbK` genes; SpbK proteins; ICEBs1
elements; SPβ `yonE` triggers; bacteriophage SPβ; the individual DefenseFinder
HMM profile; source database rows naming one SpbK locus; unresolved SpbK-YonE
coupling; TIR-domain effector chemistry; and generic abortive-infection
systems.

## External Mappings

No exact external mapping is proposed. SpbK, ICEBs1, SPβ, YonE, the
DefenseFinder HMM, individual phage-exclusion outcomes, and abortive-infection
processes are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000325` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000325` as traceability during the migration.

## Change Log

- v202, 2026-09: lifts `traitmech:000325 SpbK system` into the
  `METPO:1027900` block.
