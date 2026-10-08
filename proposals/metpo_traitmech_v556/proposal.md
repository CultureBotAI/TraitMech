# METPO proposal v556: fungal nonconstricting-ring trap formation

## Context and scope

Lift `traitmech:000680` as `METPO:1063300`: one morphological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
This three-cell hyphal trap is not individual-cell ring shape, an immature
constricting trap, a loop within an adhesive net, a unicellular knob,
an adhesive column or an intracellular cytokinetic ring. Existing mycelial
growth is explicitly bacterial, and hyphal anastomosis denotes fusion,
not trap identity. No exact synonym, xref, SSSOM equivalence or
organism-level disjointness is asserted. Nearby records mention this
class only as a scope exclusion, not an unresolved exact grounding;
adding it does not resolve their closer-parent questions.

## Evidence and limits

- [Saikawa and Takahashi 2002](https://doi.org/10.1007/s102670200061):
  all three primary PDF pages and Figures 1-20 inspected. The Figure 8
  caption provides the snippet; body observations support the distinction
  from inflation-based trapping. The paper's adhesive ultrastructure
  discussion attributes earlier work, not new electron microscopy.
- [Li et al. 2006](https://doi.org/10.1016/j.mycres.2006.04.011):
  scientific Abstract directly retrieved through NCBI XML, PMID:16876699.
  Full Methods and figures were not retrieved. Independent taxa from
  China show co-occurring knobs and nonconstricting rings; phylogenetic
  sequence analyses are not phenotype predictions.

Canonical example: `NCBITaxon:430499`, **Dactylellina leptospora** at
species rank, with source synonym Dactylella leptospora verified live at
NCBI. The example is qualified to the natural TGU isolate and reported
conditions, not a strain accession or a universal species assertion.

Formation does not guarantee capture in every condition. A protein graph
is deferred pending direct molecular evidence and accession review;
no inflation mechanism from constricting rings or adhesion protein from
knobs/nets is transferred. Closer hierarchy and mechanism remain open.

## Allocation and novelty

Reserve **traitmech:000680**, cohort **v556**, and the entire
**METPO:1063300-1063399** block; only 1063300 is populated. This follows
v555's 1063200-1063299 block without overlap with CommunityMech v1 or its
extensions. Subset: `metpo_traitmech_2026_10`.

Allocation main: `d211b7d163c40c2152e859b7cea30c34596e1aa5`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout, and the fresh complete open-PR curation
snapshot: 22 roots. Queries included nonconstricting/noncontracting,
passive/adhesive-ring forms, historical/current taxon names, both DOIs,
PMID, taxid, primary PDF identifier, the local ID, cohort and entire block.
All 32 novelty matches were scope exclusions or unrelated dependency
wording, not an exact record. All 83 allocation matches were unrelated
DOI/PMC numbers or numeric data, not reservations. Parsed pinned METPO
has no exact class. Fresh seeding emitted 399 records; 55 exact IDs are
absent from the 1,074-record corpus. That is not a missing-work queue or
evidence that discovery is exhausted.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file counts, immutable curation blobs and head stability checked;
both Shedu artifacts read. Recheck main and reservations before publishing.

## Artifacts and verification

One class TSV has two 11-column headers and one class row. No property or
SSSOM file is needed. Preserve the three empty trailing directive cells.
The upstream skill and templates at
`1408e7099d039026d7611c240938d8e177753406` were read and verified against
immutable GitHub blobs: class `b590cf303dc2fbdd57bed021668641cd0c32396d`,
property `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1's three files were read end to end. Use the maintained
w3id METPO expansion, not the upstream legacy OBO example.

Required checks: proposal verifier, ROBOT/ELK and parsed OWL identities,
LinkML/strict/history/QC/products, snippet resolver and direct-source
checks, live NCBI, focused/full tests and desktop/mobile browser QA.
Record actual outcomes in the PR receipt, including any unresolved
abstract-resolver result for the directly read full-text caption.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream
issue or accepted term is claimed. Following release, refresh the pinned
ontology, seed the accepted term and migrate the local identifier while
retaining provenance. Do not emit this placeholder as a released ID.

## Change log

- v556, 2026-10-08: initial proposal.
