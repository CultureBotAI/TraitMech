# METPO ROBOT Template Proposal - Rst_2TM_1TM_TIR System (v277, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v276 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst_2TM_1TM_TIR
system, the genome-level possession trait for a three-gene P2-like-phage AC1
phage-defense locus. The pinned DefenseFinder wiki maps the
`Rst_2TM_1TM_TIR` key to Rousset et al. 2022 and describes the AC1 system as
protective in *Escherichia coli* C against lambda, LF82_P8, and P2 phages.
DefenseFinder models Rst_2TM_1TM_TIR in the pinned rule and HMM tables with
three required profiles, `Rst_2TM_1TM_TIR__Rst_1TM_TIR`,
`Rst_2TM_1TM_TIR__Rst_2TM_TIR`, and `Rst_2TM_1TM_TIR__Rst_TIR_tm`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_2TM_1TM_TIR |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035400` is reserved for this one-row class cohort. The v276 cohort used
`METPO:1035300`, so v277 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_2TM_1TM_TIR system record,
`rst_2tm_1tm_tir_system` slug, validation or RefSeq source protein accessions,
`traitmech:000400`, `metpo_traitmech_v277`, or `METPO:1035400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035400` | Rst_2TM_1TM_TIR system | `METPO:1016300` phage defense system |

Rst_2TM_1TM_TIR system captures genome-level possession of a three-gene
Rst_TIR_tm/Rst_1TM_TIR/Rst_2TM_TIR locus represented by DefenseFinder as three
required custom profiles and experimentally linked to multi-phage protection
when expressed in *Escherichia coli* C. It excludes individual Rst_TIR_tm,
Rst_1TM_TIR, or Rst_2TM_TIR proteins, DefenseFinder HMM profiles, the source
key `Rst_2TM_1TM_TIR`, TIR-derived nucleotide-messenger signaling outside a
complete Rst_2TM_1TM_TIR locus, unvalidated RefSeq examples, and other Rst or
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Rst proteins, DefenseFinder
HMM profiles, source database rows naming one Rousset et al. system model, and
candidate RefSeq genomic examples are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Rousset et al. citation, no exact synonyms, no exact external xrefs,
  and four related source-key or HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000400` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000400` as traceability during the migration.

## Change Log

- v277, 2026-09: lifts `traitmech:000400 Rst_2TM_1TM_TIR system` into the
  `METPO:1035400` block.
