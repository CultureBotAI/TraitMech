# METPO ROBOT Template Proposal - TIR-VIII System (v361, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for TIR-VIII system, the
genome-level possession trait for one of the newly named TIR-domain anti-phage
systems described by Wang et al. Wang et al. cloned candidate Escherichia coli
TIR systems into MG1655, assayed inhibition of phage plaque formation against a
phage panel, named nine new defense systems TIR-I through TIR-IX, and reported
that TIR-VIII belongs to the group found in a single form with TIR-VII. The
pinned DefenseFinder article registry maps TIR-VIII to the same Wang et al.
paper, and the pinned HMM inventory carries TIR-VIII__TIR-VIII_A and
TIR-VIII__TIR-VIII_B custom profiles. The pinned DefenseFinder rules table
checked in this curation pass has no TIR-VIII row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TIR-VIII system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043800` is reserved for this one-row class cohort. The v360 cohort used
`METPO:1043700`, so v361 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found exact `TIR-VIII`
mentions only as sibling context in the merged TIR-I, TIR-III, TIR-IV, and
TIR-VII records, proposal artifacts, and generated page artifacts; no exact
same-scope TIR-VIII TraitMech, METPO, history, or prior proposal record; no
`tir_viii_system` slug, `TIR-VIII__TIR-VIII_A`, or `TIR-VIII__TIR-VIII_B`
mention; no `traitmech:000484`; no `metpo_traitmech_v361`; and no
`METPO:1043800` proposal block.

Related records such as Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR,
Rst_2TM_1TM_TIR, SDIC, TIR-I, TIR-III, TIR-IV, and TIR-VII already cover other
TIR-domain-containing phage defense systems; none represents the newly named
Wang et al. TIR-VIII branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043800` | TIR-VIII system | `METPO:1016300` phage defense system |

TIR-VIII system captures genome-level possession of a TIR-VIII TIR-domain
anti-phage locus represented by two custom DefenseFinder HMM profiles. It
excludes individual TIR-VIII proteins, individual TIR domains, TIR-domain
signaling outside a complete TIR-VIII locus, the other newly named Wang et al.
TIR systems, Thoeris, Pycsar, CBASS, SPARTA, Rst_TIR-NLR, Rst_2TM_1TM_TIR, SDIC
systems, the DefenseFinder TIR-VIII HMM profile rows, the absent pinned
DefenseFinder rule row, direct phage triggers or effector outputs, exact native
hosts or sensitive phages, and other phage-defense systems.

`traitmech:000484` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `TIR-VIII` synonym and the related `TIR-VIII__TIR-VIII_A` and
  `TIR-VIII__TIR-VIII_B` DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000484` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000484` as traceability during the migration.

## Change Log

- v361, 2026-09: lifts `traitmech:000484 TIR-VIII system` into the
  `METPO:1043800` placeholder block.
