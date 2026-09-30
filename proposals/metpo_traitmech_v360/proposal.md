# METPO ROBOT Template Proposal - TIR-VII System (v360, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for TIR-VII system, the
genome-level possession trait for one of the newly named TIR-domain anti-phage
systems described by Wang et al. Wang et al. cloned candidate Escherichia coli
TIR systems into MG1655, assayed inhibition of phage plaque formation against a
phage panel, named nine new defense systems TIR-I through TIR-IX, and reported
that TIR-VII belongs to the group found in a single form with TIR-VIII. The
pinned DefenseFinder article registry maps TIR-VII to the same Wang et al.
paper, and the pinned HMM inventory carries TIR-VII__TIR-VII_A and
TIR-VII__TIR-VII_B custom profiles. The pinned DefenseFinder rules table
checked in this curation pass has no TIR-VII row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TIR-VII system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043700` is reserved for this one-row class cohort. The v359 cohort used
`METPO:1043600`, so v360 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found exact `TIR-VII` and
`TIR-VIII` mentions only as sibling context in the merged TIR-I, TIR-III, and
TIR-IV records, writer scripts, and generated page artifacts; no exact
same-scope TIR-VII TraitMech, METPO, history, or prior proposal record; no
`tir_vii_system` slug, `TIR-VII__TIR-VII_A`, or `TIR-VII__TIR-VII_B` mention;
no `traitmech:000483`; no `metpo_traitmech_v360`; and no `METPO:1043700`
proposal block.

Related records such as Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR,
Rst_2TM_1TM_TIR, SDIC, TIR-I, TIR-III, and TIR-IV already cover other
TIR-domain-containing phage defense systems; none represents the newly named
Wang et al. TIR-VII branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043700` | TIR-VII system | `METPO:1016300` phage defense system |

TIR-VII system captures genome-level possession of a TIR-VII TIR-domain
anti-phage locus represented by two custom DefenseFinder HMM profiles. It
excludes individual TIR-VII proteins, individual TIR domains, TIR-domain
signaling outside a complete TIR-VII locus, the other newly named Wang et al.
TIR systems, Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR, Rst_2TM_1TM_TIR, SDIC
systems, the DefenseFinder TIR-VII HMM profile rows, the absent pinned
DefenseFinder rule row, direct phage triggers or effector outputs, exact native
hosts or sensitive phages, and other phage-defense systems.

`traitmech:000483` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `TIR-VII` synonym and the related `TIR-VII__TIR-VII_A` and
  `TIR-VII__TIR-VII_B` DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000483` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000483` as traceability during the migration.

## Change Log

- v360, 2026-09: lifts `traitmech:000483 TIR-VII system` into the
  `METPO:1043700` placeholder block.
