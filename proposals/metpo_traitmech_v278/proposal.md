# METPO ROBOT Template Proposal - Rst_HelicaseDUF2290 System (v278, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v277 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for
Rst_HelicaseDUF2290 system, the genome-level possession trait for a two-gene
phage-defense locus. The pinned DefenseFinder wiki maps the
`Rst_HelicaseDUF2290` key to Rousset et al. 2022 and describes the system as a
two-protein helicase/DUF2290 system. DefenseFinder models
Rst_HelicaseDUF2290 in the pinned rule table as a two-required-profile system,
`Rst_HelicaseDUF2290__DUF2290` and `Rst_HelicaseDUF2290__Helicase`, with
three associated HMM rows for DUF2290, DUF2290_Pers, and Helicase.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_HelicaseDUF2290 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035500` is reserved for this one-row class cohort. The v277 cohort used
`METPO:1035400`, so v278 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_HelicaseDUF2290 system
record, `rst_helicaseduf2290_system` slug, validation or RefSeq source protein
accessions, `traitmech:000401`, `metpo_traitmech_v278`, or `METPO:1035500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035500` | Rst_HelicaseDUF2290 system | `METPO:1016300` phage defense system |

Rst_HelicaseDUF2290 system captures genome-level possession of a two-protein
helicase/DUF2290 locus represented by DefenseFinder as a two-profile model
requiring `Rst_HelicaseDUF2290__DUF2290` and
`Rst_HelicaseDUF2290__Helicase` and experimentally linked to T7 protection
when expressed in *Escherichia coli*. It excludes individual helicase or
DUF2290 proteins, DefenseFinder HMM profiles, the additional
`Rst_HelicaseDUF2290__DUF2290_Pers` HMM row, the source key
`Rst_HelicaseDUF2290`, unvalidated RefSeq examples, and other Rst or
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual DUF2290 or helicase proteins,
DefenseFinder HMM profiles, source database rows naming one Rousset et al.
system model, and candidate RefSeq genomic examples are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Rousset et al. citation, no exact synonyms, no exact external xrefs,
  and five related source-key, HMM-profile, or component synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000401` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000401` as traceability during the migration.

## Change Log

- v278, 2026-09: lifts `traitmech:000401 Rst_HelicaseDUF2290 system` into the
  `METPO:1035500` block.
