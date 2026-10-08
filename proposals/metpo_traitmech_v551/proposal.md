# METPO proposal v551: false branching

## Context and scope

Lift `traitmech:000675`, cyanobacterial false branching, as `METPO:1062800`.
This reusable morphological phenotype is used in one new TraitRecord and
remains `PROPOSED` pending human review.

| Scope | New terms | Parent |
| --- | ---: | --- |
| A: local trait class | 1 | phenotype, METPO:1000059 |
| B: causal predicates | 0 | mechanism deferred |
| C: schema enums | 0 | not applicable |

## Hierarchy and evidence

Use active phenotype below quality (`METPO:1000188`). Branched shaped
(`METPO:1000687`) describes cell shape, not necessarily this trichome
arrangement. Necridium formation (`traitmech:000674`) and hormogonium formation
(`traitmech:000651`) describe distinct developmental features, not all false
branching. Obsolete cell-arrangement classes redirect to flagellar arrangement,
which is not an appropriate parent. The closer-parent question remains open.
No same-scope existing node, synonym or discussion needs repair.

The definition follows [Golubic et al. 1996](https://doi.org/10.1127/algol_stud/83/1996/303),
whose scientific abstract was retrieved directly from the publisher and whose
identity was cross-checked in Crossref. Both bundle partitioning and lateral
trichome protrusion are included. The branch-point distinction is local to
the junction, not an organism-level exclusion of true branching elsewhere.
The full 1996 article and its figures were not inspected.

[Tawong et al. 2022](https://doi.org/10.5507/fot.2021.017) supplies directly
inspected microscopy and the natural NUACC06 example. The record preserves
the Results/figure-pointer discrepancy and the species-rank NCBI identity
(`NCBITaxon:2929979`) rather than inventing a strain accession.
[Masumoto and Sanders 2022](https://doi.org/10.1111/jpy.13256), scientific
abstract directly read, supports variability of developmental routes and
coexistence of branching modes. Its full text, figures and supplements were
not inspected. Each citation has one short contiguous verbatim snippet.
Provenance-only taxonomy evidence is not counted as a fourth trait study.

Neither necridia nor heterocytes define the whole class. The pseudo-branch
attachment usage in the Rhizonema paper is not accepted as an exact synonym.
No xrefs, SSSOM equivalences or organism-level disjointness are asserted.
No causal graph is proposed: taxonomic marker sequences do not establish a
protein-resolved branching mechanism. This is an explicit knowledge gap.

## ID space and novelty

Reserve **traitmech:000675**, cohort **v551**, and the full
**METPO:1062800-1062899** block. Only 1062800 is used; this follows v550's
1062700-1062799 block. Subset: `metpo_traitmech_2026_10`.

Allocation main: `dd73175ca7de21360cdac73daa1ac04a472bb2e9`.
Ignored-and-hidden searches covered all 18 then-existing TraitMech worktrees,
the complete CommunityMech checkout and a fresh complete open-PR curation
snapshot: 20 roots. Queries included false-branch/ramification/pseudo-branch
variants, bundle partitioning, lateral protrusion, source DOIs, taxon and
strain labels, the local ID, cohort and all values in the hundred block.
Only software/cache text and unrelated numeric substrings matched; none
reserved this biology or identifier space. RDF inspection of the pinned
12,617-triple METPO ontology found no exact class. Related cell-shape,
arrangement, necridium and hormogonium records were inspected for scope.
CommunityMech v1 and its extensions do not overlap this block.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Curation reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu record; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

The publication recheck retained the same main SHA and all five open heads.
A fresh paginated inventory again checked file counts, immutable blobs and
head stability. The ignored-and-hidden scan now covered 21 roots including
this worktree. New matches were confined to this branch's artifacts and Git
metadata; no competing reservation or biological duplicate was found.

## Files and verification

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 class |
| proposal.md | this narrative |
| properties / SSSOM | omitted; no predicates or mappings |

Upstream kg-microbe contract at `1408e7099d039026d7611c240938d8e177753406`
was read. Pinned class blob `b590cf303dc2fbdd57bed021668641cd0c32396d`
and property blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` were retrieved
and their 11/13-column headers checked. Preserve the three empty trailing
class-directive cells. Use the maintained w3id METPO prefix, not a legacy stub.

Required validation before merge:

```bash
just verify-proposal metpo_traitmech_v551
just robot-validate-proposal metpo_traitmech_v551
just qc
```

Inspect emitted RDF for the child and phenotype/quality hierarchy. Run the
maintained snippet resolver without changing its verdicts, live NCBI taxonomy
audit, focused writer tests, full pytest, committed-history audit and browser
checks of generated identity, evidence, example, discussions and history.

Local proposal verification and ROBOT template/merge/ELK validation passed.
RDF inspection found 15 class-template, 12,628 merged and 12,632 reasoned
triples, with the expected w3id child and phenotype/quality ancestry and no
legacy METPO stub. The live NCBI audit resolved all 752 examples with zero
errors and 24 pre-existing label warnings. The snippet resolver returned
`VERIFIED` for the Rhizonema scientific abstract and `UNRESOLVED` for the
1996 and Fottea references; the latter were directly verified at the recorded
publisher-abstract and figure-caption locations. Resolver verdicts and frozen
baselines were not changed.

Desktop/mobile browser checks passed at 1440/390 pixels: three quotes, the
qualified example, two open discussions, history, identifier provenance,
hierarchy/browse navigation and loaded dashboard image, without horizontal
overflow or JavaScript errors. All 1,069 existing YAML records, prior proposal
templates, histories and embedding files are byte-preserved. The 1,068 existing
non-parent trait pages differ only in their footer; phenotype also gains the
new child link. Embedding regeneration was skipped because both configured
source paths are absent in the worktree and primary checkout. Committed-tree
QC, full pytest and CI remain merge gates.

## Upstream and round trip

Submit the template and narrative to berkeleybop/metpo or the kg-microbe
proposal pipeline after review. No upstream issue or accepted METPO ID is
claimed. After acceptance, refresh the ontology, re-seed and migrate the
record to the accepted identifier while preserving local-ID traceability
and both history trails. Keep unresolved parent and mechanism discussions.

## Change log

- v551, 2026-10-08: source-qualified false branching with both developmental modes.
