# METPO proposal v558: rapid axopodial contraction

## Context and scope

Lift `traitmech:000682` as `METPO:1063500`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
This is rapid shortening of microtubule-supported cellular projections,
not organismal locomotion. Existing motile `METPO:1000702` is curated
around locomotion and is not adopted automatically. Re-elongation, slow
structural loss, generic pseudopod extension, stalk contraction and
drug-induced microtubule disassembly do not alone establish this response.
No universal speed cutoff, exact synonym, xref, SSSOM equivalence or
organism-level disjointness is asserted. A closer parent remains open.

## Evidence and limits

- [Khan et al. 2003](https://doi.org/10.2108/zsj.20.1367), PMID:14624035:
  scientific abstract retrieved directly through Europe PMC. Stimulation
  experiments and axopodial ultrastructure support the definition.
- [Kinoshita et al. 2001](https://doi.org/10.1111/j.1550-7408.2001.tb00187.x),
  PMID:11596916: scientific abstract read directly through PubMed and
  Europe PMC. Food-uptake observations support the rapid response.

Both snippets are contiguous scientific-abstract spans, not search-result
text. Full Methods and figures were not inspected. Keep calcium dependence
and tubule observations source-qualified; do not combine them into a
universal mechanism. The record documents the inference limits. Natural
culture provenance and current taxonomy are unresolved, so there are no
canonical examples. A protein-resolved graph is deferred pending direct
perturbation evidence and taxon-paired accessions, not claimed impossible.

## Allocation and novelty

Reserve **traitmech:000682**, cohort **v558**, and the entire
**METPO:1063500-1063599** block; only 1063500 is populated. This follows
v557's 1063400-1063499 block without overlapping CommunityMech v1 or its
extensions. Subset: `metpo_traitmech_2026_10`.

Allocation main: `77c408b95a12cec7e876c74c8768861160bd2ed2`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout and a complete fresh open-PR snapshot:
22 roots. Queries included axopodial terminology, source taxa and alternate
name stems, DOIs, PMIDs, local ID, cohort and full block. Two novelty hits
were CommunityMech cached Actinophrys figure text, not a contraction trait.
All 31 allocation hits were unrelated numbers, not reservations. Wrapped
contraction/pseudopodial/motility context was also reviewed. Parsed pinned
METPO has no exact class. Fresh seeding emitted 399 records; 55 exact IDs
are absent from the 1,076-record corpus. That is not a missing-work queue
or evidence that discovery is exhausted.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file counts, immutable curation blobs and head stability checked.
Recheck main and reservations before publishing.

## Artifacts and verification

One class TSV has two 11-column headers and one class row. No property or
SSSOM file is needed. Preserve three empty trailing directive cells.
Upstream skill and templates are pinned at
`1408e7099d039026d7611c240938d8e177753406`. Verified class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 provides the worked cohort convention. Use maintained
w3id METPO expansion, not the upstream legacy OBO example.

Required checks: proposal verifier, ROBOT/ELK and parsed OWL identities,
LinkML/strict/history/QC/products, snippet resolver and direct-source
checks, focused/full tests and desktop/mobile browser QA. Record actual
results in the PR receipt, not a claim of success before execution.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. Do not emit this placeholder as a released ID.

## Change log

- v558, 2026-10-08: initial proposal.
