# METPO ROBOT Template Proposal - Metis System (v379, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Metis system, the
genome-level possession trait for an m6dAMP-sensing anti-phage locus that
activates type-specific toxic effectors after phage-mediated host-genome
degradation. Osterman et al. describe Metis as a bacterial defense system that
directly senses phage-mediated host-genome degradation, and the pinned
DefenseFinder article registry maps the `Metis` source key to the Osterman
et al. preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Metis system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045600` is reserved for this one-row class cohort. The v378 cohort used
`METPO:1045500`, so v379 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` and ROBOT outputs across the curation corpus. It found no exact
same-scope Metis system record, `metis_system` slug, `Metis` label or synonym,
`traitmech:000502`, `metpo_traitmech_v379`, `METPO:1045600`, the Osterman
preprint DOI `10.1101/2025.11.05.686725`, the final Science DOI
`10.1126/science.aed6782`, PMID `42424438`, or the Osterman title.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045600` | Metis system | `METPO:1016300` phage defense system |

Metis system captures genome-level possession of a phage defense system in which
phage-mediated host-genome degradation yields a methylated mononucleotide signal
that activates type-specific toxic effectors. It excludes free m6dAMP, host DNA
methylases, host genome degradation without a complete Metis locus, individual
type I and type II toxic effectors, NAD depletion or membrane-linked toxicity by
themselves, individual DefenseFinder HMM profiles, and source database rows
naming one system model.

`traitmech:000502` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. m6dAMP, NAD depletion, host-genome
degradation, DNA methylation, and type-specific toxic effectors are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one exact
  synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000502` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000502` as traceability during the migration.

## Change Log

- v379, 2026-09: lifts `traitmech:000502 Metis system` into the
  `METPO:1045600` placeholder block.
