# METPO ROBOT Template Proposal - Rst_Hydrolase-3Tm System (v279, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v278 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst_Hydrolase-3Tm
system, the genome-level possession trait for a two-gene
hydrolase/transmembrane phage-defense locus. The pinned DefenseFinder wiki
describes the system as a two-protein Hydrolase/Hydrolase-Tm system.
DefenseFinder maps the `Rst_Hydrolase-3Tm` key in the pinned rule table to a
two-required-profile `Rst_Hydrolase-Tm` system,
`Rst_Hydrolase-Tm__Hydrolase` and `Rst_Hydrolase-Tm__Hydrolase-Tm`, with two
associated HMM rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_Hydrolase-3Tm |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035600` is reserved for this one-row class cohort. The v278 cohort used
`METPO:1035500`, so v279 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_Hydrolase-3Tm system record,
`rst_hydrolase_3tm_system` slug, validation or RefSeq source protein
accessions, `traitmech:000402`, `metpo_traitmech_v279`, or `METPO:1035600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035600` | Rst_Hydrolase-3Tm system | `METPO:1016300` phage defense system |

Rst_Hydrolase-3Tm system captures genome-level possession of a two-protein
hydrolase/transmembrane locus represented by DefenseFinder as a two-profile
`Rst_Hydrolase-Tm` model requiring `Rst_Hydrolase-Tm__Hydrolase` and
`Rst_Hydrolase-Tm__Hydrolase-Tm` and experimentally linked to T7 protection
when expressed in *Escherichia coli*. It excludes individual Hydrolase or
Hydrolase-Tm proteins, DefenseFinder HMM profiles, the source keys
`Rst_Hydrolase-3Tm` and `Rst_Hydrolase-Tm`, unvalidated RefSeq examples, and
other Rst or phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Hydrolase or Hydrolase-Tm
proteins, DefenseFinder HMM profiles, source database rows naming one Rousset
et al. system model, and candidate RefSeq genomic examples are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Rousset et al. citation, no exact synonyms, no exact external xrefs,
  and five related source-key, HMM-profile, or component synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000402` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000402` as traceability during the migration.

## Change Log

- v279, 2026-09: lifts `traitmech:000402 Rst_Hydrolase-3Tm system` into the
  `METPO:1035600` block.
