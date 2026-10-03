# METPO Proposal v451: Hachiman Type II and Family Scope

## Context

Payne et al. (DOI:10.1093/nar/gkab883) define Hachiman type II by HamAB plus
HamC (DUF3223); Cui et al. (DOI:10.1038/s41467-025-57851-1) retain that
classification, citing Payne rather than independently testing type II.
This is an organism-level system-possession trait, not a gene or detector row.
Issue #1630 corrects the broad family definition's unsupported universal
DNA-cleavage requirement before adding the child.

## Scope

| Scope | Rows | Parent | Purpose |
|---|---:|---|---|
| A | 2 | phage defense system; Hachiman system | One corrected family proposal and one new child |
| B | 0 | None | No new predicates |
| C | 0 | None | No schema vocabulary |

`traitmech:000574` was minted on 2026-10-03 because the mirrored METPO has
no exact class; it denotes one new trait record. `traitmech:000219` retains
the existing family identity, with its mechanistic overstatement corrected.
The fresh seeder emitted 399 records: 344 exact IDs already occur in the live
968-record pre-addition corpus, and 55 are only discovery leads. No Hachiman
seed exists. Ignored-and-hidden whole-repository searches covered labels,
aliases, identifiers, HamC, source citations and source accession; v96 was
the broad-family proposal, not an exact type-II child.

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1052800 | traitmech:000219 | Hachiman system | METPO:1016300 phage defense system (v86) |
| METPO:1052801 | traitmech:000574 | Hachiman type II system | METPO:1052800 |

The child requires the HamABC biological architecture. DefenseFinder XML at
`afb0e5a8b466be53586b13266f5d38d98c3ac268` marks three components mandatory
but sets both minimum counts to two; PADLOC at
`9e380165633a8d6aef93b5a164cea0f3359bd33f` requires three core components.
Neither raw detector names nor missing hits establish complete architecture,
biological absence or experimental component essentiality. No detector key is
promoted to an exact synonym, and no shifted external mapping is proposed.

DSM 14551 (NCBITaxon:173675, Sphingopyxis witflariensis) supplied the natural
locus on NZ_NISJ01000011.1. Phage assays were in engineered E. coli BL21-AI,
not the source strain. GenBank and NCBI Taxonomy independently resolve the
source. No species-wide possession, universal phage range or type-II DNA
cleavage mechanism is asserted. Type-I mechanism evidence stays on the family
record with its original restricted graph scope. HamC function remains open.

## Relationship to v96

This is Path C of the proposal update policy. `METPO:1052800` replaces the
unminted v96 placeholder `METPO:1017300` for the same stable local family
`traitmech:000219`; the old definition overgeneralized type-I DNA cleavage.
Do not submit both family rows as separate biological classes. The v96 TSV
remains byte-for-byte historical, with a supersession notice in its narrative.
No local trait identifier is retired. The new child points only to the
replacement family placeholder. This is not an assertion that the old and new
placeholder IDs have been minted upstream.

## ID Space and Subset

The live highest cohort was v450, reserving METPO:1052700. This cohort reserves
the fresh METPO:1052800-1052899 block, using two rows and subset
`metpo_traitmech_2026_10` (v96 used `metpo_traitmech_2026_09`). Collision
searches included ignored and hidden files. The block does not overlap
CommunityMech v1's 1007100-1007220 range.

## Files

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 2 classes plus 2 headers |
| proposal.md | This narrative |

No property template or SSSOM is emitted because there are no new predicates
or verified equivalent external classes.

## Verification

`scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v451` passed
with zero failures. `scripts/robot_validate_proposal.py` passed template,
merge and ELK reasoning with no UNSAT (23,348 merged lines, 23,354 reasoned).
`scripts/verify_metpo_proposal.py --coverage` found all 574 local IDs covered.
The 19 focused writer tests passed. Writer tests
check header width, local-to-proposed IDs, the corrected family definition,
parent linkage, preimage refusal, dry run, replay and preservation.

## Upstream Path

After TraitMech review, consolidate the two rows into berkeleybop/metpo#535
with the explicit v96 replacement instruction. Do not emit unminted METPO
placeholders as production trait identifiers.

## Round-Trip Plan

After real IDs are minted, update the METPO mirror, re-seed only the relevant
records, migrate their identifiers and parent links, and preserve both stable
local IDs for traceability. Retain old proposal artifacts as history rather
than reusing their placeholder blocks.

## Change Log

- v451, 2026-10-03: add HamABC type-II possession and replace v96's
  overgeneralized family definition; retain type-I mechanism evidence.
