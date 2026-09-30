# METPO ROBOT Template Proposal - TIR-IV System (v359, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for TIR-IV system, the
genome-level possession trait for one of the newly named TIR-domain anti-phage
systems described by Wang et al. Wang et al. cloned candidate Escherichia coli
TIR systems into MG1655, assayed inhibition of phage plaque formation against a
phage panel, named nine new defense systems TIR-I through TIR-IX, and reported
that TIR-IV belongs to a group with diverse domain contexts. The pinned
DefenseFinder article registry maps TIR-IV to the same Wang et al. paper, and
the pinned HMM inventory carries TIR-IV__TIR-IV_A and TIR-IV__TIR-IV_B custom
profiles. The pinned DefenseFinder rules table checked in this curation pass has
no TIR-IV row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TIR-IV system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043600` is reserved for this one-row class cohort. The v358 cohort used
`METPO:1043500`, so v359 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found exact `TIR-IV`
mentions only as sibling context in the merged TIR-I and TIR-III records and
proposal artifacts; no exact same-scope TIR-IV TraitMech, METPO, history, or
prior proposal record; no `tir_iv_system` slug, `TIR-IV__TIR-IV_A`, or
`TIR-IV__TIR-IV_B` mention; no `traitmech:000482`; no
`metpo_traitmech_v359`; and no `METPO:1043600` proposal block.

Related records such as Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR,
Rst_2TM_1TM_TIR, SDIC, TIR-I, and TIR-III already cover other
TIR-domain-containing phage defense systems; none represents the newly named
Wang et al. TIR-IV branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043600` | TIR-IV system | `METPO:1016300` phage defense system |

TIR-IV system captures genome-level possession of a TIR-IV TIR-domain
anti-phage locus represented by two custom DefenseFinder HMM profiles. It
excludes individual TIR-IV proteins, individual TIR domains, TIR-domain
signaling outside a complete TIR-IV locus, the other newly named Wang et al.
TIR systems, Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR, Rst_2TM_1TM_TIR, SDIC
systems, the DefenseFinder TIR-IV HMM profile rows, the absent pinned
DefenseFinder rule row, direct phage triggers or effector outputs, exact native
hosts or sensitive phages, and other phage-defense systems.

`traitmech:000482` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `TIR-IV` synonym and the related `TIR-IV__TIR-IV_A` and
  `TIR-IV__TIR-IV_B` DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000482` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000482` as traceability during the migration.

## Change Log

- v359, 2026-09: lifts `traitmech:000482 TIR-IV system` into the
  `METPO:1043600` placeholder block.
