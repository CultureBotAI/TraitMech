# METPO ROBOT Template Proposal - Rst_3HP System (v275, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v274 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst_3HP system, the
genome-level possession trait for a three-gene Hp1/Hp2/Hp3 P2-hotspot
phage-defense locus. Rousset et al. support an unnamed three-gene system that
has no clear predicted domains and protects against P1, and the DefenseFinder
wiki maps the `Rst_3HP` key to the Rousset et al. study. DefenseFinder models
Rst_3HP in the pinned rule and HMM tables with three required profiles,
`Rst_3HP__Hp1`, `Rst_3HP__Hp2`, and `Rst_3HP__Hp3`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst_3HP |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035200` is reserved for this one-row class cohort. The v274 cohort used
`METPO:1035100`, so v275 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst_3HP system record,
`rst_3hp_system` slug, Hp1/Hp2/Hp3 source protein accessions,
`traitmech:000398`, `metpo_traitmech_v275`, or `METPO:1035200`; the Rousset
final DOI was already used by the distinct PARIS, Rst_DUF4238, and
Rst_gop_beta_cll system records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035200` | Rst_3HP system | `METPO:1016300` phage defense system |

Rst_3HP system captures genome-level possession of a three-gene Hp1/Hp2/Hp3
locus represented by DefenseFinder as three required custom Rst_3HP profiles and
experimentally linked to P1 protection when expressed in *Escherichia coli*. It
excludes individual Hp1, Hp2, or Hp3 proteins, the DefenseFinder
`Rst_3HP__Hp1`, `Rst_3HP__Hp2`, and `Rst_3HP__Hp3` HMM profiles, the source key
`Rst_3HP`, P1 resistance outside a complete Rst_3HP locus, unvalidated RefSeq
examples, and other Rst or phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Hp proteins, DefenseFinder HMM
profiles, source database rows naming one Rousset et al. system model, and
candidate RefSeq genomic examples are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, no exact external xrefs, and four related source-key or
  HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000398` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000398` as traceability during the migration.

## Change Log

- v275, 2026-09: lifts `traitmech:000398 Rst_3HP system` into the
  `METPO:1035200` block.
