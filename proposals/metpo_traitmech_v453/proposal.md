# METPO Proposal v453: Zorya Type III System

## Context and Scope

Payne et al. (DOI:10.1093/nar/gkab883) define and test the ZorA/B/F/G
architecture named Zorya type III. Mariano et al.
(DOI:10.1038/s41467-025-57397-2) retain that classification while studying
type-I/II mechanisms. This cohort adds an organism-level possession class,
not a protein, domain or detector-output row.

| Scope | Rows | Purpose |
|---|---:|---|
| A | 1 | ZorA/B/F/G Zorya architecture |
| B | 0 | No new predicates |
| C | 0 | No schema vocabulary |

`traitmech:000576` was minted on 2026-10-03 because the mirrored METPO has
no exact class. The new record and the parent's open subtype discussion use
that identifier. A fresh seed emitted 399 records: 344 exact IDs already
occur in the 970-record pre-addition corpus; 55 absent IDs remain discovery
leads, not automatically accepted additions.

## Novelty and Hierarchy

Ignored-and-hidden whole-repository searches covered Zorya, type-III aliases,
ZorF/ZorG, the source accession, citations, slug and reserved identifiers.
The family record and type-I/II children are distinct from the four-component
type-III class; no exact live or METPO class or prior reservation was found.

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053000 | traitmech:000576 | Zorya type III system | METPO:1017100 |

The parent is v94's family placeholder for `traitmech:000217`. No prior
proposal, sibling definition or family hierarchy is changed. Multiple
subtype loci can coexist in one genome; no organism-level disjointness
axiom is proposed. No external xref or SSSOM equivalence is asserted.

## Evidence Decisions

Payne's Results refer to a different core pair than its Figure 2C and
Discussion. The figure was directly inspected: type III is depicted as
ZorF, ZorA, ZorB and ZorG. The Discussion and Mariano's later Introduction
agree with that architecture. The discrepancy is documented explicitly;
the definition does not silently depend on the conflicting Results text.

Payne's Methods identify the natural source as Stenotrophomonas nitritireducens
DSM 12575, NZ_LDJG01000021.1. GenBank independently resolves that contig to
strain DSM 12575 and species taxon NCBITaxon:83617; NCBI Taxonomy confirms
the species label. The canonical example is strain-limited possession,
not a species-wide assertion. The paper's Figure 3 activity experiments
used the cloned system in E. coli BL21-AI, not native-host defense assays.

PADLOC commit `9e380165633a8d6aef93b5a164cea0f3359bd33f` requires all four
core profiles, with both minimum counts 4 and maximum separation 0.
DefenseFinder commit `afb0e5a8b466be53586b13266f5d38d98c3ac268` lists four
mandatory slots but sets both minimum counts to 3 and inter-gene space to 5;
ZorA2 is exchangeable with ZorA. The executable YAML/XML were parsed
structurally. Neither rule establishes component essentiality or defense
by every prediction. An incomplete call does not replace the biological
definition, and missing hits do not prove absence.

ZorF/ZorG regulation of ZorAB is a hypothesis in Payne. Mariano's experiments
on types I/II do not establish type-III ion usage, DNA targets, triggers or
cell-death mechanisms. The record leaves those questions open and adds no
protein-resolved mechanism graph. The parent graph remains explicitly
limited to its characterized type-I/II outputs.

## ID Space and Artifacts

v452 used METPO:1052900 within its reserved hundred block. v453 reserves
METPO:1053000-1053099 with subset `metpo_traitmech_2026_10`. Live allocation
and ignored-and-hidden searches found no collision. This does not overlap
the CommunityMech v1 ranges.

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 class plus 2 headers |
| proposal.md | This narrative |

No property template or SSSOM file is emitted because scopes B/C and exact
external alignments are absent.

## Verification

All four evidence snippets were exact-matched against freshly retrieved
primary full text or pinned raw model files. The primary publisher HTML
was used for Mariano after the Europe PMC XML endpoint returned 503.
The original Payne figure and NCBI source/taxon records were also checked.
All 17 focused writer tests passed, covering controlled preimages, refusal,
dry run, apply/replay, preservation and all-record prevalidation. LinkML and
the proposal verifier passed. ROBOT template/merge/ELK passed with no UNSAT
(23,329 merged lines, 23,335 reasoned). The NCBI audit resolved all 693
canonical examples with zero errors and 24 existing label warnings. History
validation found 993 records and zero invalid records. Full-suite results
and independent review will be recorded in the PR.

## Upstream and Round Trip

Consolidate the reviewed class into berkeleybop/metpo#535. The proposed ID
is a placeholder, not a production METPO identifier. Once upstream mints
the real term, refresh the mirror, re-seed only relevant records, migrate
identifier/parent links, and retain the local ID for traceability. Do not
reuse old proposal blocks or rewrite earlier proposal history.

## Change Log

- v453, 2026-10-03: add Zorya type III with source-strain possession evidence,
  an explicit paper discrepancy, and separate model-threshold caveats.
