# METPO Proposal v446: Lamassu-SMEK System

## Context and Scope

Reserve `METPO:1052300` for `traitmech:000569`, a GENOMICS possession
trait for a Lamassu locus with SMEK-domain LmuA, LmuB and LmuC. This is a
literature-recognized architecture, not an individual protein or profile row.

| Scope | Classes | Parent | Reason |
|---|---:|---|---|
| A | 1 | METPO:1018600 | Lamassu system, reserved for traitmech:000232 in v109 |
| B | 0 | Not applicable | No new predicates |
| C | 0 | Not applicable | No schema vocabulary lift |

## Evidence and Hierarchy

- [Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122) identify SMEK
  as an LmuA effector type and describe its association with short Lamassu.
- [Dataset S1](https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx)
  contains 125 unique SMEK-system IDs, not 377 systems: 377 is the component-row
  count. Of those calls, 124 contain short LmuB profiles and one contains two
  long LmuB-profile hits. The latter is one call, not two. These sets do not
  overlap. Its rows 6042-6045 require reconciliation with the short-specific
  prose before asserting a biological long-LmuB subtype. The definition
  therefore names the shared architecture without a length restriction.
- The canonical example uses `S3_Lamassu_Detection` rows 165-167 and
  `S2_Genomes` row 1383 to connect a complete three-component call to
  `GCF_021491935.1`, study replicon `ACJU001.0722.00009.C001`.
- [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_021491935.1/dataset_report)
  resolves this assembly to Acinetobacter junii WCO-9, `NCBITaxon:40215`.
  The example is computational genomic possession, not measured antiviral
  activity in WCO-9 or a species-wide assertion.
- The [pinned executable model](https://raw.githubusercontent.com/mdmparis/defense-finder-models/afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/Lamassu-Fam/Lamassu_SMEK.xml)
  requires SMEK-bearing LmuA, LmuB and LmuC; long and short LmuB are
  exchangeable. The model and SMEK profile exist despite missing entries
  in that commit's legacy summary TSV and HMM inventory.

The existing DS-27 record (`traitmech:000451`) denotes a single-gene
transcriptional unit also called SMEK in its source. It is not an exact
duplicate or parent of this three-component Lamassu architecture. No bare
SMEK synonym, DS-27 phenotype, molecular activity, or acronym expansion is
transferred. Model keys are related synonyms; no exact xref or SSSOM mapping
is proposed. Functional validation and protein-resolved mechanisms remain
explicit gaps; no causal graph is fabricated from computational calls.

## Identity, Files and Verification

Pre-write searches included ignored and hidden files across the whole
repository. They found no exact Lamassu-SMEK record or METPO term. The HNH
record quotes SMEK in a shared source passage but does not denote this
architecture. The local ID, v446 cohort and `METPO:1052300` block were
unused; v445 reserved the preceding `METPO:1052200` block. These IDs do not
overlap CommunityMech v1. Subset: `metpo_traitmech_2026_10`.

| File | Content |
|---|---|
| metpo_proposal_classes_robot.tsv | One Scope A class plus two header rows |
| proposal.md | Scope, evidence, identity and round-trip decisions |

`scripts/add_lamassu_smek_system_trait.py` generates the class template and
TraitRecord from the same definition and synonyms. Verify with
`verify_metpo_proposal.py`, its cross-cohort `--coverage` gate, and
`robot_validate_proposal.py` (template, merge and ELK reasoning). Primary
snippets are checked directly against XML, raw spreadsheet cells and NCBI
JSON, not only against an abstract cache.

## Upstream and Round Trip

Submit this class for upstream review through berkeleybop/metpo#535.
Following acceptance, update the METPO mirror, replace the local primary
identifier with the assigned METPO ID, and preserve `traitmech:000569` in
migration provenance. Until human review, the record remains `PROPOSED`.

## Change Log

- v446, 2026-10-03: propose the SMEK-bearing Lamassu architecture with a
  computational genome example and an explicit long-profile annotation gap.
