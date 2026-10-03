# METPO Proposal v452: Hachiman Type I System

## Context

Payne et al. (DOI:10.1093/nar/gkab883) distinguish the original HamAB
architecture from HamC-containing type II. Cui et al.
(DOI:10.1038/s41467-025-57851-1) explicitly retain the HamAB-only type-I
classification and experimentally study subtypes I-A and I-B. This cohort
adds an organism-level possession class, not a protein or detector row.

## Scope

| Scope | Rows | Parent | Purpose |
|---|---:|---|---|
| A | 1 | Hachiman system | HamAB architecture without HamC |
| B | 0 | None | No new predicates |
| C | 0 | None | No schema vocabulary |

`traitmech:000575` was minted on 2026-10-03 because the mirrored METPO has
no exact class. It is used by one new trait record and linked from the
existing family and type-II discussions. A fresh seed emitted 399 records:
344 exact IDs already occur in the 969-record pre-addition corpus; the 55
absent IDs remain discovery leads, not automatically accepted additions.

## Novelty and Hierarchy

Ignored-and-hidden whole-repository searches covered Hachiman, HamABC,
type-I aliases, AbpA/AbpB, the two DOI sources, U00096.3, and proposed/local
identifiers. Neither METPO nor the live records has an exact type-I class.
v96/v451 represent the family and v451 also represents type II, not type I.
The broad family remains stable; the two discussion updates do not change
definitions, graphs, examples or hierarchy.

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1052900 | traitmech:000575 | Hachiman type I system | METPO:1052800 |

The parent is v451's corrected family placeholder for `traitmech:000219`,
not the superseded v96 placeholder METPO:1017300. No prior cohort is edited.
Type I is not synonymous with I-A or I-B, a particular effector domain,
a fixed phage spectrum, or a missing detector hit. A genome can possess
both type-I and type-II loci, so no disjointness axiom is proposed.

## Evidence Boundaries

Cui et al. supply the type-I-B source coordinates U00096.3:2761204-2765368.
NCBI GenBank and Taxonomy independently resolve them to NCBITaxon:511145,
Escherichia coli str. K-12 substr. MG1655. The record uses this natural source
as a possession example. Plasmid complementation in a hamAB-deleted MG1655
host is not an assay of the untouched native locus; BL21(DE3) was a separate
protein-expression host. HamC absence is supported by the paper's system
classification, not inferred from a cropped GenBank interval.

PADLOC at `9e380165633a8d6aef93b5a164cea0f3359bd33f` requires HamA1/HamB1
and prohibits HamC2 in its type-I model. DefenseFinder at
`afb0e5a8b466be53586b13266f5d38d98c3ac268` requires HamA/HamB but has no
forbidden HamC entry in its Hachiman XML. Neither model proves biological
absence, native activity or component essentiality. No raw detector key is
promoted to an exact synonym. No shifted external xref or SSSOM is proposed.

The parent already retains source-qualified I-A/I-B mechanism evidence.
No duplicate or universal mechanism graph is added. Other HamA-domain subtype
classes remain leads requiring their own evidence and novelty review.

## ID Space and Subset

Live allocation found v451 as the last cohort, using METPO:1052800-1052801
within its reserved hundred block. v452 reserves the next fresh block,
METPO:1052900-1052999, using one row and `metpo_traitmech_2026_10`.
Ignored-and-hidden searches found no prior reservation. This does not overlap
CommunityMech v1's 1007100-1007220 block.

## Files

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 class plus 2 headers |
| proposal.md | This narrative |

No property template or mappings file is emitted: scopes B/C and equivalent
external classes are absent from this proposal.

## Verification

The maintained proposal verifier passed with zero failures. ROBOT template,
merge and ELK validation passed with no UNSAT (23,329 merged lines and 23,335
reasoned lines). Cross-cohort coverage found all 575 local IDs represented.
All 28 focused writer tests passed, covering controlled preimages, dry run,
replay, preservation, output drift, all-record prevalidation, evidence scope
and the v451 parent replacement. The four snippets exactly match full-text
XML or pinned detector files; abstract-only checks are inconclusive for the
two full-text paper excerpts. NCBI resolved all 692 canonical examples with
zero errors and 24 existing label-drift warnings.

## Upstream Path

After TraitMech review, consolidate this row into berkeleybop/metpo#535 along
with v451's explicit replacement of the old family proposal. Proposed METPO
IDs remain placeholders, not production identifiers.

## Round-Trip Plan

Once real METPO IDs are minted, refresh the mirror, re-seed only relevant
records, migrate the identifier and parent links, and preserve
`traitmech:000575` for traceability. Retain earlier proposal artifacts rather
than reusing their blocks.

## Change Log

- v452, 2026-10-03: add HamC-lacking Hachiman type I with a source-strain
  example, component-detection caveats and linked discovery discussions.
