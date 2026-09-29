# METPO ROBOT Template Proposal - PD-T2-1 System (v353, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T2-1 system, the
genome-level possession trait for the two-gene phage-defense operon described
by Goedecke et al. The final article reports that the ECOR03 operon disrupted
in a T7 gp17 transposon screen was renamed phage defense against T2 system 1
(PD-T2-1), and the pinned DefenseFinder article registry maps PD-T2-1 to the
Goedecke et al. preprint. The pinned DefenseFinder HMM inventory and rules
table checked in this curation pass have no PD-T2-1 rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T2-1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043000` is reserved for this one-row class cohort. The v352 cohort used
`METPO:1042900`, so v353 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T2-1 TraitMech, METPO,
history, or prior proposal record; no `pd_t2_1_system` slug; no final
`DOI:10.1038/s41564-025-02239-6`, `PMC12875140`, or preprint
`10.1101/2025.07.02.662641` mention; no `traitmech:000476`; no
`metpo_traitmech_v353`; and no `METPO:1043000` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043000` | PD-T2-1 system | `METPO:1016300` phage defense system |

PD-T2-1 system captures genome-level possession of the two-gene operon linked
to antiphage protection by Goedecke et al. It excludes the ECOR03 `geneAB`
placeholder, individual PD-T2-1A and PD-T2-1B proteins, the ECOR03
`QOWO01000016` coordinate range, absent pinned DefenseFinder HMM-profile rows,
the absent pinned DefenseFinder rule row, exact detection criteria, native host
breadth, the direct sensor or output mechanism, and other phage-defense
systems.

`traitmech:000476` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `PD-T2-1` synonym, the exact en-dash `PD-T2–1` typographic variant,
  and the related `geneAB operon` placeholder label used before renaming.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000476` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000476` as traceability during the migration.

## Change Log

- v353, 2026-09: lifts `traitmech:000476 PD-T2-1 system` into the
  `METPO:1043000` placeholder block.
