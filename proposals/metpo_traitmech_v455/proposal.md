# METPO Proposal v455: Druantia Type I

## Context

This Scope-A cohort proposes `traitmech:000578 Druantia type I system`
as an organism-level locus-possession class, not a gene, HMM hit or detector
output. The definition follows the literature's DruB/C/D/E architecture
with optional DruA.

A fresh METPO seed emitted 399 identifiers: 344 present and 55 absent from
the live corpus. Those absences are leads, not evidence of novelty. Searches
across the whole repository, including ignored and hidden files, found no
exact record or METPO term. The family discussion, original family writer
and type-III proposal mention type I but do not represent its exact scope.
The broader family and existing III and IV children have distinct meanings.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | Druantia system | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

## Hierarchy Decisions

| Proposed ID | Stable local ID | Label | Parent |
|---|---|---|---|
| METPO:1053200 | traitmech:000578 | Druantia type I system | METPO:1053100 |

The local parent is `traitmech:000234 Druantia system`. The proposal uses
the corrected family placeholder from v454, not superseded v111
`METPO:1018800`. Keep v454's replacement instructions when consolidating
upstream; do not submit both family placeholders as separate classes.

Doron et al. (DOI:10.1126/science.aar4120), The Druantia system and Table 1,
describe the three type-I partner genes alongside DruE, with an additional
DUF4338 component in some cases. The accepted manuscript is available from
[Weizmann's repository](https://weizmann.elsevierpure.com/ws/portalfiles/portal/80086469/rs_Science_SystematicDiscoveryofAntiPhage_AM2018.pdf).
The comparative-genomics study DOI:10.3389/fmicb.2020.00961 maps DUF4338 to
DruA and describes a five-gene type-I form. Together these support optional
DruA, rather than a universal five-gene requirement. The second paper's
UW163 functionality claim is a prediction, not a measured infection outcome.

Adversarial recheck: Doron Figure 2C (manuscript page 19, PDF page 21)
labels the DUF-bearing partner DruA within a five-gene DruA/B/C/D/E
arrangement. The main text counts three variable partners beside DruE,
then adds DUF4338 in some cases. Thus the optional component is the fifth
member, consistent with DruA naming, not a sixth gene preceding five
otherwise required genes.

The canonical example is natural possession by E. coli UMEA 4076-1,
grounded to the independently resolved species NCBITaxon:562. Doron's
functional assay transferred that locus into E. coli MG1655. Neither
species-wide possession nor native-host resistance is inferred.

The pinned DefenseFinder model at
`afb0e5a8b466be53586b13266f5d38d98c3ac268` requires one mandatory DruE
slot and three total matches; DruA/B/C/D are accessory slots. The DruE
slot permits three exchangeable profiles, including a type-IV profile.
PADLOC at `9e380165633a8d6aef93b5a164cea0f3359bd33f` instead requires
all five DruA1/B1/C1/D1/E1 profiles. These are different operational
criteria, not equivalent definitions or evidence of universal essentiality.
Complete locus review is needed; unmatched profiles and engineered
deletions do not establish a naturally absent component.

No causal graph, protein examples, exact external mappings or organism-level
disjointness are proposed. Type-III mechanistic results do not establish
type-I partner functions, activation or biochemical output. The family
discussion now resolves the architecture lead while retaining these gaps
and the separate type-II lead. Its definition and evidence are unchanged.

## ID Space and Subset

Live pre-allocation checks found highest local ID 577, cohort v454 and
proposed class METPO:1053101. v455 reserves the fresh
METPO:1053200-1053299 block and subset `metpo_traitmech_2026_10`.
The ignored-and-hidden collision search found no use of this block or
traitmech:000578. It does not overlap CommunityMech v1's 1007100-1007220.

## Files

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 class plus 2 headers |
| proposal.md | This narrative |

No property template or SSSOM is needed. The class header follows the
canonical kg-microbe `master` contract, including empty trailing ROBOT cells.

## Verification

The guarded writer passes 17 focused tests covering biological scope,
proposal parity, controlled preimages, dry-run, replay and preservation.
Template verification passes with zero failures; both 11-column headers
match upstream. ROBOT template/merge/ELK passes with no UNSAT: 23,329 merged
lines and 23,335 reasoned lines. Cross-cohort coverage includes all 578
local IDs. Both changed records pass LinkML and strict validation.
The four snippets were checked against primary full text or pinned raw
models; the abstract-only check is inconclusive for both full-text quotes.
NCBI resolves all 694 examples with zero errors and 24 baseline warnings.
Final full-corpus results are recorded on the reviewed PR.

## Upstream Path

After TraitMech review, consolidate this row with the corrected v454 parent
under [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535).
The reserved METPO placeholder is not a minted production identifier.

## Round-Trip Plan

After upstream minting, update the METPO mirror, re-seed the affected
records, migrate local identifiers and parent links to the real METPO IDs,
and preserve the local IDs for traceability. Retain historical proposal
artifacts and never reuse their allocated blocks.

## Change Log

- v455, 2026-10-03: add Druantia I possession with optional DruA and explicit
  detector-versus-biological scope.
