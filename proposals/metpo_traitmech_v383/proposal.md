# METPO ROBOT Template Proposal - GmrSD System (v383, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GmrSD system, the
genome-level possession trait for a GmrSD type IV modification-dependent
restriction system targeting glucosylated hydroxymethylcytosine-containing DNA.
Bair and Black support the Escherichia coli CT596 split `gmrS`/`gmrD` genes as
encoding a Type IV modification-dependent restriction nuclease whose activity
requires both protein products. Machnicka et al. support GmrSD systems as a
family that can be encoded either by split GmrS/GmrD components or by fused
double-domain homologs. The pinned DefenseFinder article registry maps
`GmrSD_RM_Type_IV` to the Bair and Black DOI, while the pinned HMM inventory and
rules table have no exact GmrSD or `GmrSD_RM_Type_IV` row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GmrSD system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046000` is reserved for this one-row class cohort. The v382 cohort used
`METPO:1045900`, so v383 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope GmrSD system record,
`gmrsd_system` slug, `traitmech:000506`, `METPO:1046000`, or
`metpo_traitmech_v383`; it also found no prior local use of the Machnicka DOI
`10.1186/s12859-015-0773-z` or PMID `26493560`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046000` | GmrSD system | `METPO:1045000` type IV modification-dependent restriction system |

GmrSD system captures genome-level possession of a GmrSD locus encoding separate
GmrS/GmrD components or a fused double-domain GmrSD-family homolog that targets
glucosylated hydroxymethylcytosine-containing DNA. It excludes individual GmrS
or GmrD proteins, individual `gmrS` or `gmrD` genes, phage IPI inhibitor
proteins, TgvAB, HEC-05, HEC-06, McrA, McrBC, MspJI, PvuRts1I, EcoKMcrA,
ScoMcrA, TagI, VcaM4I, broad `RM_Type_IV` and `Other_Type_IV` source keys, the
`GmrSD_RM_Type_IV` source key outside a complete organism-level system, and
individual glucosylated hydroxymethylcytosine DNA substrate classes.

`traitmech:000506` is a direct local child of `traitmech:000496` type IV
modification-dependent restriction system. This proposal uses `METPO:1045000`,
the v373 placeholder for `traitmech:000496`.

## External Mappings

No exact external mapping is proposed. Individual GmrS or GmrD proteins,
individual `gmrS` or `gmrD` loci, Escherichia coli strains, glucosylated HMC
substrates, and the DefenseFinder article-registry key are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000506` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000506` as traceability during the migration.

## Change Log

- v383, 2026-10: lifts `traitmech:000506 GmrSD system` into the
  `METPO:1046000` placeholder block.
