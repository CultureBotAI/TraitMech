# METPO proposal v552: cyanobacterial multiseriate trichome formation

## Scope and hierarchy

Lift `traitmech:000676` as `METPO:1062900`: one reusable morphological
phenotype, used in one new record and kept `PROPOSED` pending human review.
Scope A: one class. Scope B: zero predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
The differentia concerns more than one adjacent cell row in a trichome,
including two rows, produced by division in multiple planes. It does not
denote independent uniseriate trichomes bundled inside a shared sheath or
every loose cell cluster. It is not equivalent to branched shaped
`METPO:1000687`, generic filament-shaped cell morphology, hormogonium
formation `traitmech:000651`, or cyanobacterial false branching
`traitmech:000675`. No exact existing node, synonym or TODO needs repair.
Obsolete cell-arrangement terms redirect to flagellar arrangement, not a
suitable multicellular parent. The closer-parent question stays open.

Do not add a separate cyanobacterial true-branching wrapper merely because
the broad branched-shaped class lacks that phrase. That candidate remains
unaccepted here; this proposal instead distinguishes a different cellular
organization. Multiseriality and branching can coexist in one organism.
No synonyms, xrefs, SSSOM equivalences or disjointness axioms are proposed.

## Evidence and limits

- [Springstein et al. 2020](https://doi.org/10.1002/2211-5463.13016): directly
  read primary XML and Figure 2E support multiplanar division and the mature
  multiseriate morphology. The paper's parenthetical wording refers to
  trichomes in a row; its developmental context and the other sources support
  the cell-row definition. The record preserves this terminology distinction.
- [Koch et al. 2017](https://doi.org/10.1186/s12862-017-1053-5): inspected
  main Results, supplementary text and actual Figures S1/S6. S6 distinguishes
  multiseriate BG11-grown filaments from salt-associated aseriate clusters.
  Responses differ between taxa; salt is not a universal defining trigger.
- [Halder 2016](https://doi.org/10.3126/on.v14i1.16445): inspected field-study
  Methods/Results, Conclusions and Figure 1. The canonical example is
  morphology-identified NH-1260 from a rice field, not an invented PCC strain
  match. `NCBITaxon:1124` is the live-resolved species accession, not a
  collection-specific identity or a fourth independent phenotype study.

All three sources have short, source-checked contiguous snippets. The example
is stage-qualified. Molecular identification of the field material is not
claimed. Gene overexpression and transcript correlations are not promoted to
a universal native mechanism; a causal graph is explicitly deferred.

## Allocation and novelty

Reserve local **traitmech:000676**, cohort **v552**, and the entire
**METPO:1062900-1062999** block; only 1062900 is populated. This follows
v551's 1062800-1062899 block. Subset: `metpo_traitmech_2026_10`.

Allocation main: `4bd399d54559939f53b55e9bce058d4914724043`.
Ignored-and-hidden searches covered all 19 then-existing TraitMech worktrees,
the complete CommunityMech checkout and a fresh open-PR curation snapshot:
21 roots. Searches included multiseriate/biseriate/row/trichome variants,
true branching, source DOIs, Chlorogloeopsis, the local ID, cohort and every
value in the reserved hundred block. Numerical cache/log coincidences were
inspected and are not reservations. No exact record or reservation was found.
RDF inspection of the pinned 12,617-triple ontology found no exact class.
Existing branching records only provide neighboring scope, not this trait.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

File counts, selected immutable curation blobs and before/after head stability
were checked. Recheck main and reservations immediately before publication.

Publication snapshot again found the same main and five open heads, with
complete paginated file lists and immutable selected blobs verified. The
current branch is the sole new reservation in this cohort.

## Artifacts and validation

The class TSV has two 11-column headers and one class row. No properties or
SSSOM file is needed. Preserve the three empty trailing directive cells.
Upstream contract `1408e7099d039026d7611c240938d8e177753406` and class blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` / property blob
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` were inspected in this curation
session. The canonical class/property widths are 11/13, respectively.
Use the maintained w3id METPO prefix, not the legacy OBO stub.

Before merge: LinkML/strict validation, proposal coverage/ROBOT, RDF hierarchy
inspection, snippet resolver plus direct checks, live NCBI taxonomy audit,
focused writer tests, committed-history audit, full QC and pytest, generated
artifact review and desktop/mobile browser checks. Preserve actual resolver
verdicts and frozen baselines. Refresh generated pages, discussions, QC and
priority dashboards; regenerate embeddings only if a configured source exists.

Local LinkML/strict, proposal and ROBOT checks passed. Parsed RDF counts are
15 template, 12,628 merged and 12,632 reasoned triples; w3id phenotype/quality
ancestry is intact with no legacy METPO stub. The live NCBI audit resolved
753 examples with zero errors and 24 pre-existing label warnings. The snippet
resolver returned two `NOT_IN_ABSTRACT` rows (2020/2017) and one `UNRESOLVED`
row (2016); all three stored spans match directly retrieved full-text or
supplementary sources. No resolver verdict or frozen baseline was changed.

All 1,070 previous YAMLs, proposal files, histories and embedding files are
byte-preserved. All 1,069 non-parent existing trait pages are footer-only
changes; phenotype gains one child, 170 to 171. Both configured embedding
source paths are absent in the primary checkout and worktree, so embeddings
were not regenerated. Shared generators ran from a newly materialized copy
of the same reviewed commit `6d0a6fbbaeec47f42c6f999233b460e3f56bae89`, after
the older temporary copy was found missing its source files. Generated
discussion navigation/templates remain unchanged. Browser checks and actual
screenshots at 1440/390 pixels passed for evidence, provenance, example,
discussions/history, hierarchy/browse navigation and the loaded QC image.
Committed-tree QC, full pytest and required CI remain mandatory merge gates.

## Upstream path

Submit this template through the METPO or kg-microbe proposal pipeline after
review. No upstream issue or accepted METPO allocation is claimed. After
acceptance, refresh METPO, re-seed and migrate the record to the accepted ID
while preserving local-ID traceability and both history trails. Keep the
parent and mechanism discussions until supported resolutions exist.

## Change log

- v552, 2026-10-08: evidence-backed multiseriate trichome phenotype.
