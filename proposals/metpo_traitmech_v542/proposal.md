# Fungal Peloton Formation: METPO Proposal v542

## Context and Scope

Propose `traitmech:000666 fungal peloton formation`, a PROPOSED MORPHOLOGY
class, initially developed from main
`8e9a7b7c121e41e595c6161e6c0e925b6b42ec17`. It denotes a
fungal morphological phenotype, not a plant observation, a bare structure,
a sequence feature, or a nutrient-transfer assertion.

| Scope | Count | Parent |
| --- | ---: | --- |
| A: synthetic trait class | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

The whole-repository novelty search included ignored and hidden files,
peloton/coil terminology, orchid/ericoid usage, culture aliases and relevant
DOIs. It found no matches across 38,978 searched files (1,327,497,004 bytes).
The additional ignored-and-hidden search of all other worktrees and pending
curation artifacts also returned no match. Neighboring definitions were
read separately; lexical absence alone is not semantic novelty.

The pinned METPO RDF has 12,617 triples and no exact peloton class. A fresh
temporary seed yielded 399 records, 344 already live. The remaining 55
reconcile to 17 reviewed duplicates and 38 supporting-field terms, checked
against the 1,546-row release delta and 153-row active-review table. These
figures are discovery checks, not evidence of global trait exhaustion.

## Hierarchy and Meaning

Use the active phenotype parent `METPO:1000059`, below quality
`METPO:1000188`. Spiral, branched and filament shapes (`1000684`, `1000687`,
`1000674`) classify cell shape, not this intracellular fungal architecture.
Mycelial growth `traitmech:000074` is explicitly bacterial. Arbuscule
formation `000664` concerns branched intracellular structures; anastomosis
`000605` concerns fusion, pseudohyphal growth `000653` budding-cell chains,
and haustorium formation `000663` specialized host interfaces. BAS formation
in pending #1788 (`000665`) concerns extraradical dichotomous branches.
None is an exact duplicate or a settled closer parent.

The unqualified name includes the orchid usage in Fochi et al. and the
explicit ericoid usage in Meyers et al. The definition is not orchid-only.
Perotto and Balestrini compare Paris-type AM coils with orchid pelotons and
describe a continuum with arbusculate coils; resemblance does not establish
exact synonyms or disjoint organism-level traits. Liverwort comparisons
remain a qualified abstract-only follow-up. No exact synonyms, structure
xrefs or SSSOM equivalences are proposed. A closer parent remains OPEN.

## Evidence and Example

- [Fochi et al.](https://doi.org/10.1111/nph.14279): the directly read
  [author manuscript](https://iris.unito.it/retrieve/e27ce429-fbc3-2581-e053-d805fe0acbaa/N_metabolism_ORM_rev10_4aperto.pdf)
  supplies the Discussion snippet at printed p. 15 / physical p. 17,
  line 465. Main text through Conclusions and actual Figure 5 were inspected.
  The title differs slightly from published metadata and the manuscript
  retains a GEO placeholder; neither is silently harmonized. Other images
  and supplementary contents were not inspected.
- [Meyers et al.](https://doi.org/10.1111/1365-2745.70188): Table 1, CCI
  row, p. 3681 / physical p. 4 explicitly calls ericoid coils pelotons.
  The actual table was inspected in the [institutional publisher PDF](https://freidok.uni-freiburg.de/data/273892),
  SHA256 `d98586c7a214142cf0fab46f8dbd7185984174cd3bd425204581e626ed21d6e9`,
  matching the repository checksum. CCI measures root intersects, not
  individual fungal cells or nutrient flux. Supplementary Figure S3 was not
  inspected; no named fungal exemplar is inferred from the host plant.
- [Perotto and Balestrini](https://doi.org/10.1111/nph.19338): directly
  read early-view PDF, main text and actual Figures 1-3. The p. 2 snippet
  supports terminology, not independent experimental replication. Its
  plant-driven-development interpretation is not a demonstrated mechanism.
  Inconsistent Figure 2 panel/scale labels are not used for measurements.

The canonical example is `NCBITaxon:156515 Tulasnella calospora`, explicitly
AL13/4D = MUT4182 in oat-medium Serapias vomeracea protocorm cultures at
20 C in darkness, with Figure 5 showing pelotons 30 days after sowing.
Fochi Methods reports isolation from Anacamptis laxiflora roots in northern
Italy and deposition as MUT4182; the cited original isolation paper was not
read. Direct NCBI EFetch confirmed the species and child strain 1051891 with
AL13/4D as equivalent name. This is not independent reidentification or
evidence for every strain. The engineered yeast transport assay is separate
from the fungal culture. SV6/MUT4178 in the later De Rose paper is not this
strain; AL13/4D there is a reference genome.

Formation is kept separate from nutrient transfer, universal lifespan,
exclusive mutualism and a proposed common developmental mechanism. No
protein-resolved causal graph is asserted without direct perturbation and
authority-verified protein evidence.

## ID Space and Templates

Reserve `traitmech:000666`, cohort v542, and `METPO:1061900` within the
whole block `1061900-1061999`, subset `metpo_traitmech_2026_10`. The
main maximum at that allocation checkpoint was 664; pending BAS #1788
reserved 665, v541 and the entire
1061800-1061899 block. These pending reservations are occupied even before
merge. Local main, all local worktrees, complete paginated open PR files
(including drafts), historical records and CommunityMech proposals were
searched with ignored and hidden files included. The only block-pattern
hits were unrelated Unix timestamps in Git reflogs, not ID reservations.

Immutable heads inspected: #1788 `7117fa563b54d61be07e3f1b6ead785794926506`,
#1782 `35099af2b7d5347f2ca6e418c4a139979071644d`, #1734
`ca9b337ec3d24806baf16b42b8f384087701280e`, #1476
`a138e46f803b5af9d48969217b86cf7c9a3b61bd`, #973
`331f9517bbdf4d2c9fa97b338ee59a8986f2f174`, and draft #924
`e61ce120b8da953da097b9f94bfed7f292e5675a`. Every downloaded curation
artifact was Git-blob-hash checked. #1788 adds the BAS trait, proposal and
history; #1734 modifies existing traits/history without a new allocation.
#1782, #1476, #973 and draft #924 have no curation artifact change. This
explicit partition corrects the ambiguous audit wording identified in #1790.
The head set and fetched main remained unchanged immediately before branch
creation. The final prepublication comparison again confirmed the same
remote main and all six open-head/draft states. An ignored-and-hidden
repeat across the original workspace, other worktrees, pending curation
artifacts and CommunityMech found no competing ID, cohort or block use.

The canonical upstream contract is pinned at kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Hash-checked class template
`b590cf303dc2fbdd57bed021668641cd0c32396d` has 11 columns; property template
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` has 13. The class directive row
retains its three required trailing empty cells. The maintained wrapper
uses actual `https://w3id.org/metpo/` IRIs, not legacy METPO stubs.
CommunityMech's inspected v1/extension blocks do not overlap this range.

## Files and Verification

| File | Rows | Purpose |
| --- | ---: | --- |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 class | Scope A lift |
| proposal.md | Not applicable | Evidence and allocation narrative |
| Properties / SSSOM | 0, not emitted | No predicate or equivalence claim |

The dry-run-first writer guards the reviewed phenotype projection and exact
target/template replay, uses `record_curation_event` and
`write_validated_trait`, and does not edit existing traits. Repository
history is scaffolded with the actual Codex actor and remains append-only.

Initial standalone-draft verification at `0893c2ca5cf8aa19bb291be4de5e2ef2d36c26f3`
passed: all 20 writer tests and the pre-application dry
run; direct LinkML/strict, proposal/ROBOT/ELK and RDF checks; full-tree Ruff;
history/products; corpus QC; and all 20 pinned vendored artifacts. The
focused suite passed 65 tests in 279.98 seconds and full pytest passed
3,153 tests in 693.25 seconds. Online NCBI validation resolved all 742
examples with zero errors and 24 existing warnings. Three PDF snippets
exact-matched and were visually checked; the maintained abstract resolver
returned two NOT_IN_ABSTRACT and one UNRESOLVED, not three VERIFIED results.

The preservation audit confirmed all 1,059 old trait YAMLs, previous history
and proposal narratives unchanged, along with 545 historical TSVs: 534 class
templates, six property templates and five SSSOM mappings. Of the old trait
pages, 1,058 changed only in their corpus footer; the phenotype page also
gained the new child. RDF graphs contain 15 proposal, 12,628 merged and
12,632 reasoned triples with the expected w3id.org labels and ancestry.
Playwright checks at 1,440/390 pixels passed evidence, example, discussion,
history, navigation, browse search and dashboard assertions without
overflow or browser errors; screenshots were visually inspected. Embedding
sources were unavailable, so existing embedding products were preserved.

Required before merge: writer/full tests, LinkML and strict validation,
proposal/ROBOT verification and RDF inspection, snippet verification,
online taxonomy, history/products, QC, derived-product preservation and
browser checks. Record actual outcomes on the PR; do not infer a pass from
the existence of this checklist.

### Combined Draft Refresh

While #1788 remained in the native queue with all required candidate checks
passing, its exact reviewed head
`7117fa563b54d61be07e3f1b6ead785794926506` was incorporated into this draft.
All 14 conflicts were generated HTML; no trait or history record conflicted.
The combined corpus contains 1,061 records, including 111 morphology records
with 19 PROPOSED entries. Shared products are regenerated through maintained
recipes, not resolved by choosing one side.

The combined 18-step validation run passed, including full QC, history,
products, LinkML/strict, proposal/ROBOT, RDF and Ruff. The focused suite passed
65 tests in 329.71 seconds; full pytest passed 3,173 tests in 653.56 seconds.
Online taxonomy resolved 743 examples with zero errors and 24 existing
warnings. All 20 governed artifacts match the pinned canonical source.

Against BAS's exact reviewed head, all 1,060 prior YAMLs, histories, proposal
narratives and 546 historical TSVs remain byte-identical (535 class, six
property, five SSSOM). Of the prior trait pages, 1,059 differ only in their
footer; the phenotype page also gains the peloton child (161 to 162).
Desktop/mobile browser checks at 1,440/390 pixels passed with live count
1,061, and the screenshots were inspected. The ordinary staged whitespace
check flags only the imported BAS template's three required empty header
cells; byte identity, 11-column widths and exact-path scoped checks passed.

A renewed complete seven-PR snapshot includes this draft at its previously
published head and all six other immutable heads listed above, unchanged.
An ignored-and-hidden search of other worktrees, non-self pending artifacts
and CommunityMech proposals found no competing ID, cohort or full-block use
across 51,396 searched files. This is a reservation check, not global trait
exhaustion.

The directly related skill/queue documentation fix for #1792 distinguishes
auto-merge from actual native queue membership, preserves the exact-head
guard, and requires landed-tree reconstruction before branch deletion.
After BAS actually lands, incorporate its published main commit and verify
the final tree and all affected products before marking this PR ready.

### Current Main Integration

BAS subsequently merged as `64b0ec7fa9a0da69da695428533f89134ff62249`.
Its landed tree was reconstructed successfully before its branch was deleted.
This branch also incorporates concurrent pathway-context main
`f7112cf664c9a54e05ab5e771b2d0366dae9f0b1`. All affected products were
regenerated. Main's schema, renderer, pathway index/pin, source manifest,
11 updated records and histories remain intact; no source or evidence change
was made to the peloton record.

Current integration validation passed: full pytest 3,192 tests in 1,211.09
seconds and focused 65 tests in 531.58 seconds, plus LinkML/strict, all
four product generators, grounding, Biolink, proposal verification,
ROBOT/ELK, parsed RDF, history/products, QC, taxonomy shape checks and Ruff.
The first QC run correctly found the pre-merge HEAD coverage report stale;
the local integration commit preserved the exact main report, and full QC
then passed. No baseline or gate was changed. The related add-trait guidance
fix for #1795 now distinguishes working-tree and committed comparison bases,
following the existing #560 guidance without a drifting static report list.

The preservation audit against actual main again confirms all 1,060 prior
YAMLs, histories, proposal narratives and 546 TSVs unchanged. Of old trait
pages, 1,059 differ only in the footer; phenotype gains the child, and its
child count is the only old priority-row change. Protected YAML and all
main pathway-context source files are byte-identical. Desktop/mobile checks
were repeated at 1,440/390 pixels, with the live 1,061-record dashboard,
evidence, example, discussions, history and navigation present and no
overflow or browser errors. The committed history gate now reports one
changed trait and one added history against main.

## Upstream Round Trip

After TraitMech review, submit the one-class template and hierarchy question
to METPO or the kg-microbe proposal pipeline. The placeholder is not a
released METPO identifier and is not the live record ID. On upstream
acceptance, refresh the pinned ontology and seed a temporary tree, check the
accepted meaning, then migrate references while preserving the local ID as
provenance rather than a lexical synonym. Append history, regenerate
products and repeat validation. Use the native merge queue and verify the
actual landed tree before deleting the branch.

## Change Log

- v542, 2026-10-07: one peloton-formation class with orchid and ericoid
  terminology, qualified culture evidence and explicit mechanism limits.
