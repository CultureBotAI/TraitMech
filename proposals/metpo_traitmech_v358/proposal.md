# METPO ROBOT Template Proposal - TIR-III System (v358, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for TIR-III system, the
genome-level possession trait for one of the newly named TIR-domain anti-phage
systems described by Wang et al. Wang et al. cloned candidate Escherichia coli
TIR systems into MG1655, assayed inhibition of phage plaque formation against a
phage panel, named nine new defense systems TIR-I through TIR-IX, and reported
that TIR-III belongs to a group with diverse domain contexts. The pinned
DefenseFinder article registry maps TIR-III to the same Wang et al. paper, and
the pinned HMM inventory carries TIR-III__TIR-III_A and TIR-III__TIR-III_B custom
profiles. The pinned DefenseFinder rules table checked in this curation pass has
no TIR-III row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TIR-III system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043500` is reserved for this one-row class cohort. The v357 cohort used
`METPO:1043400`, so v358 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found exact `TIR-III`
mentions only as sibling context in the merged TIR-I record and proposal; no
exact same-scope TIR-III TraitMech, METPO, history, or prior proposal record; no
`tir_iii_system` slug, `TIR-III__TIR-III_A`, or `TIR-III__TIR-III_B` mention; no
`traitmech:000481`; no `metpo_traitmech_v358`; and no `METPO:1043500` proposal
block.

Related records such as Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR,
Rst_2TM_1TM_TIR, SDIC1, and TIR-I already cover other TIR-domain-containing
phage defense systems; none represents the newly named Wang et al. TIR-III
branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043500` | TIR-III system | `METPO:1016300` phage defense system |

TIR-III system captures genome-level possession of a TIR-III TIR-domain
anti-phage locus represented by two custom DefenseFinder HMM profiles. It
excludes individual TIR-III proteins, individual TIR domains, TIR-domain
signaling outside a complete TIR-III locus, the other newly named Wang et al.
TIR systems, Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR, Rst_2TM_1TM_TIR, SDIC
systems, the DefenseFinder TIR-III HMM profile rows, the absent pinned
DefenseFinder rule row, direct phage triggers or effector outputs, exact native
hosts or sensitive phages, and other phage-defense systems.

`traitmech:000481` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `TIR-III` synonym and the related `TIR-III__TIR-III_A` and
  `TIR-III__TIR-III_B` DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000481` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000481` as traceability during the migration.

## Change Log

- v358, 2026-09: lifts `traitmech:000481 TIR-III system` into the
  `METPO:1043500` placeholder block.
