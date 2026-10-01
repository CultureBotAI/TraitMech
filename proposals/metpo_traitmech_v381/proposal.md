# METPO ROBOT Template Proposal - AbiF System (v381, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiF system, the
genome-level possession trait for the pNP40-derived Lactococcus abortive
infection determinant cloned on pCG1 that inhibits bacteriophage phi 712 DNA
replication.
Garvey et al. localized the determinant to a pCG1 subclone, showed that a
frameshift inside the single complete open reading frame disrupted phage
resistance, and designated the resulting abortive-infection mechanism AbiF.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiF system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045800` is reserved for this one-row class cohort. The v380 cohort used
`METPO:1045700`, so v381 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope AbiF system record,
`abif_system` slug, `traitmech:000504`, `metpo_traitmech_v381`, or
`METPO:1045800`; the Garvey DOI `10.1128/AEM.61.12.4321-4328.1995`, `pCG1`,
`pNP40`, and AbiF text appeared only as shifted AbiE or AbiL evidence, generated
pages, or the scripts that produced those records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045800` | AbiF system | `METPO:1016800` abortive infection system |

AbiF system captures genome-level possession of the pNP40-derived
abortive-infection locus in which the AbiF open reading frame is required for
phage insensitivity and the determinant inhibits the rate of phage phi 712 DNA
replication. It excludes individual AbiF proteins, the abiF open reading frame
outside a complete AbiF system, AbiD/AbiD1 homologs, the pPG01 AbiE determinant,
generic pNP40 phage-insensitivity regions, generic abortive-infection systems,
and phage-DNA-replication inhibition outside the AbiF system.

`traitmech:000504` is a direct local child of `traitmech:000214` abortive
infection system. This proposal uses `METPO:1016800`, the v91 placeholder for
`traitmech:000214`.

## External Mappings

No exact external mapping is proposed. Individual AbiF proteins, abiF open
reading frames, pNP40 plasmid fragments, Lactococcus hosts, bacteriophage phi
712, and phage DNA replication are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000504` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000504` as traceability during the migration.

## Change Log

- v381, 2026-10: lifts `traitmech:000504 AbiF system` into the
  `METPO:1045800` placeholder block.
- v381 review, 2026-10: clarifies pNP40 as the AbiF source plasmid and pCG1
  as the recombinant plasmid clone.
