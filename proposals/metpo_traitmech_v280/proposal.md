# METPO ROBOT Template Proposal - Rst_RT-nitrilase-Tm System (v280, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v279 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for
Rst_RT-nitrilase-Tm system, the genome-level possession trait for a two-gene
reverse-transcriptase/nitrilase plus transmembrane-protein phage-defense locus.
The pinned DefenseFinder wiki describes RT-nitrilase-Tm, also named UG5-large,
as a two-gene defense system. DefenseFinder maps the `Rst_RT-nitrilase-Tm`
key in the pinned rule table to a two-required-profile `Rst_RT-Tm` system,
`Rst_RT-Tm__RT` and `Rst_RT-Tm__RT-Tm`, with those two profiles and an
alternate `Rst_RT-Tm__RT2` row in the pinned HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_RT-nitrilase-Tm |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035700` is reserved for this one-row class cohort. The v279 cohort used
`METPO:1035600`, so v280 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_RT-nitrilase-Tm system
record, `rst_rt_nitrilase_tm_system` slug, validation or RefSeq source protein
accessions, `traitmech:000403`, `metpo_traitmech_v280`, or `METPO:1035700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035700` | Rst_RT-nitrilase-Tm system | `METPO:1016300` phage defense system |

Rst_RT-nitrilase-Tm system captures genome-level possession of a two-protein
reverse-transcriptase/nitrilase plus transmembrane locus represented by
DefenseFinder as a two-profile `Rst_RT-Tm` model requiring `Rst_RT-Tm__RT` and
`Rst_RT-Tm__RT-Tm` and experimentally linked to AL505_P2 protection when
expressed in *Escherichia coli*. It excludes individual RT, RT2, RT-Tm,
reverse-transcriptase, or nitrilase proteins, DefenseFinder HMM profiles, the
source keys `Rst_RT-nitrilase-Tm` and `Rst_RT-Tm`, UG5 reverse-transcriptase
groups without a complete Rst_RT-nitrilase-Tm locus, unvalidated RefSeq
examples, and other Rst, DRT, or Abi reverse-transcriptase-containing
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual RT, RT2, RT-Tm, reverse
transcriptase, or nitrilase proteins, DefenseFinder HMM profiles, source
database rows naming one Rousset et al. system model, and candidate RefSeq
genomic examples are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Rousset et al. citation, no exact synonyms, no exact external xrefs,
  and eight related source-key, HMM-profile, or component synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000403` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000403` as traceability during the migration.

## Change Log

- v280, 2026-09: lifts `traitmech:000403 Rst_RT-nitrilase-Tm system` into the
  `METPO:1035700` block.
