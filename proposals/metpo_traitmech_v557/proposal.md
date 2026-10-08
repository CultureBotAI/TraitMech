# METPO proposal v557: fungal adhesive-column trap formation

## Context and scope

Lift `traitmech:000681` as `METPO:1063400`: one morphological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
Serially arranged adhesive hyphal cells form the column trap. Distinguish
unicellular knobs, interconnected net loops, nonconstricting rings and
mechanically constricting rings. Existing mycelial growth is explicitly
bacterial; hyphal anastomosis denotes fusion, not trap identity. Generic
branching or individual-cell shape does not establish the phenotype.
No exact synonyms, xrefs, SSSOM equivalences or organism-level disjointness
are asserted. Adhesive-branch terminology needs usage review before any
equivalence. Neighboring scope exclusions are not unresolved groundings;
their closer-parent questions remain open.

## Evidence and limits

- [Ji et al. 2020](https://doi.org/10.1016/j.isci.2020.101057): primary
  full-text XML from Europe PMC, PMC7186526, and actual Figure 1 inspected.
  The Introduction provides the contiguous snippet. Figure 1C shows a
  source-named Dactylellina cionopagum column; 1G shows capture by columns.
  Gene-family expansion and expression correlations do not establish a
  protein requirement for column formation. The paper's cited adhesion-gene
  disruption experiment concerns A. oligospora, not the column-forming
  organism. Supplemental Methods downloads were incomplete; no strain or
  universal culture condition is inferred from this source.
- [Su et al. 2016](https://doi.org/10.1111/lam.12557): scientific Abstract
  retrieved directly through NCBI XML, PMID:26928264. Full Methods and
  figures were not retrieved. The abstract names D. cionopaga YMF1.01472
  as column-producing in its ammonia-induction context. The initial
  eleven-bacterium assay concerns A. oligospora; it is not eleven column
  phenotypes. No universal ammonia requirement or molecular pathway is
  inferred. The snippet preserves the source's middle-dot strain notation.

No canonical example is asserted. Live NCBI `47266` resolves Dactylellina
cionopaga at species rank and records Monacrosporium cionopagum and
Dactylella cionopaga synonyms. That does not resolve YMF1.01472 provenance
or identify the 2020 experimental strain. Do not conflate these cultures.
Formation, adhesion, capture, penetration and digestion remain distinct;
formation alone does not guarantee capture under every condition. A
column-specific protein graph, natural exemplar and closer parent remain
open, not claimed nonexistent.

## Allocation and novelty

Reserve **traitmech:000681**, cohort **v557**, and the entire
**METPO:1063400-1063499** block; only 1063400 is populated. This follows
v556's 1063300-1063399 block without overlapping CommunityMech v1 or its
extensions. Subset: `metpo_traitmech_2026_10`.

Allocation main: `ee39eccd3ee721a9b8bb9b96b117666885447bf6`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout and a complete fresh open-PR curation
snapshot: 22 roots. Queries covered column/branch trap terminology,
cionopaga/cionopagum and other historical-name stems, both DOIs, PMID/PMC
identifiers, taxid, local ID, cohort and whole block. All 390 novelty hits
were scope exclusions or unrelated numeric/dependency references, not an
exact record. All 80 allocation hits were unrelated numbers, not reservations.
Wrapped neighboring definitions/discussions were also read. Parsed pinned
METPO has no exact class. Fresh seeding emitted 399 records; 55 exact IDs
are absent from the 1,075-record corpus. This is not a missing-work queue
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
SSSOM file is needed. Preserve three empty trailing directive cells. The
upstream skill and templates at `1408e7099d039026d7611c240938d8e177753406`
were read and verified against immutable GitHub blobs: class
`b590cf303dc2fbdd57bed021668641cd0c32396d`, property
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1's three files were read end to end. Use maintained w3id
METPO expansion, not the upstream legacy OBO example.

Required checks: proposal verifier, ROBOT/ELK and parsed OWL identities,
LinkML/strict/history/QC/products, snippet resolver and direct-source
checks, focused/full tests and desktop/mobile browser QA. Record actual
results in the PR receipt, distinguishing abstract-resolver limitations
from the directly verified full-text snippet.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. Do not emit this placeholder as a released ID.

## Change log

- v557, 2026-10-08: initial proposal.
