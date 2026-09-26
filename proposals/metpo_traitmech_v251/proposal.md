# METPO ROBOT Template Proposal - Rst_DUF4238 System (v251, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v250 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst_DUF4238 system, the
genome-level possession trait for a single-gene DUF4238 phage-defense locus.
Rousset et al. support a one-protein DUF4238 P2-hotspot system that provides
strong resistance against phage T7, and the DefenseFinder wiki describes
Rst_DUF4238 as a single-gene system whose molecular mechanism is unknown.
DefenseFinder maps the `Rst_DUF4238` key to the Rousset et al. preprint in its
article registry and models the system in the pinned rule and HMM tables with
one `Rst_DUF4238__DUF4238_Pers` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_DUF4238 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032800` is reserved for this one-row class cohort. The v250 cohort used
`METPO:1032700`, so v251 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_DUF4238 system record,
`rst_duf4238_system` slug, Rousset preprint DOI, `traitmech:000374`,
`metpo_traitmech_v251`, or `METPO:1032800`; the Rousset final DOI was already
used by the distinct PARIS system record.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032800` | Rst_DUF4238 system | `METPO:1016300` phage defense system |

Rst_DUF4238 system captures genome-level possession of a single-gene DUF4238
locus represented by DefenseFinder as a single Rst_DUF4238__DUF4238_Pers
profile and experimentally linked to strong resistance against phage T7. It
excludes individual DUF4238 or DUF4238_Pers proteins, the
`Rst_DUF4238__DUF4238_Pers` HMM profile, the source key `Rst_DUF4238`, T7
resistance outside a complete Rst_DUF4238 locus, unvalidated RefSeq examples,
and other Rst or phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual DUF4238 proteins,
DefenseFinder HMM profiles, source database rows naming one Rousset et al.
system model, and candidate RefSeq genomic examples are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms, no exact external xrefs, and three related source-key or
  HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000374` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000374` as traceability during the migration.

## Change Log

- v251, 2026-09: lifts `traitmech:000374 Rst_DUF4238 system` into the
  `METPO:1032800` block.
