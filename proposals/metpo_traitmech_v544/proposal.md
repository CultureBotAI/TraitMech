# Fungal Root Mantle Formation: METPO Proposal v544

## Context and Scope

Propose `traitmech:000668 fungal root mantle formation`, a PROPOSED
MORPHOLOGY class for formation of an external hyphal sheath around a plant
root. It is not a bare anatomical structure or a nutrient-transfer claim.
Work began from tested Hartig-net head
`2526a905a19d02667a928e40f18e5f93b2f3d5ad`, including peloton #1791 and
BAS #1788. BAS subsequently merged as
`64b0ec7fa9a0da69da695428533f89134ff62249`, with reconstructed-tree integrity
verified. Dependent PRs must incorporate actual main before becoming ready.

Concurrent pathway-context PR #1734 then landed as
`f7112cf664c9a54e05ab5e771b2d0366dae9f0b1`. This branch incorporates that
actual main, preserving its schema, renderer, contextual links, source pin
and append-only histories. Initial mantle validation passed through QC,
taxonomy and Ruff; its focused run was deliberately interrupted before
completion to restart all gates on the combined code. No full-suite pass
is claimed for that superseded checkpoint.

| Scope | Count | Parent |
| --- | ---: | --- |
| A: synthetic trait class | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

The novelty search included ignored and hidden files in all eight existing
worktrees, complete pending curation artifacts and CommunityMech proposals:
94,081 files and 2,179,501,531 bytes, with no search errors. The 59 matching
lines (76 matches in 25 files) were the Hartig record's explicit mantle
boundary and its generated/writer copies, plus unrelated Amazon Bedrock
Mantle dependencies. Additional sheath searches found bacterial coats,
spirochete outer membranes and phage sheaths, not this root architecture.
No same-scope graph node, synonym or parent-gap TODO needs migration.

A structured METPO search found no exact mantle/sheath class among 12,617
triples. The 399-record temporary seed, 1,546-row release delta and 153-row
active-review table were checked. The 55 non-live seed IDs remain 17
reviewed duplicates and 38 supporting relations/fields, not new traits.
This is a specific coverage gap, not evidence of global exhaustion.

## Hierarchy and Meaning

Use active `METPO:1000059 phenotype` under `METPO:1000188 quality`.
`METPO:1000198 mycorrhization` is obsolete. The root qualifier excludes
unrelated senses of mantle or sheath. Hartig-net formation `000667` is
intercellular within roots; arbuscules `000664` and pelotons `000666` are
intracellular; BAS `000665` branch from extraradical runner hyphae.
Bacterial mycelial growth `000074`, cell capsules `000063`, colony outline,
cell shape and ecological symbiosis outcomes are not this architecture.
No organism-level disjointness or fixed thickness, color, host range or
nutrient-transfer outcome is asserted. A closer morphology parent remains
an OPEN curation question. Bare structure names are not exact phenotype
synonyms; no xrefs or SSSOM equivalences are proposed.

## Evidence and Example

- [Krause 2015](https://doi.org/10.1128/AEM.01991-15), directly read publisher
  Introduction, first paragraph: definition authority and a 17-word
  contiguous clause. Main text and captions were read; actual figure
  images and supplementary contents were not inspected. The clause
  separates the external mantle from the intraradical Hartig net.
- [Pena 2014](https://doi.org/10.3389/fpls.2014.00229), Figure 1 caption:
  complete 15-word sentence, exact-matched in primary full-text XML and
  visually checked on p. 3 of the [publisher PDF](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2014.00229/pdf).
  The actual composite combines root and section images with schematic
  infrared arrows; it is not an experimental image of radiation penetration.
  Main Results separately describe multilayered field-root mantles. Other
  figure images and Table S1 remain unread; no numerical thickness,
  spectral function or additional taxon exemplar is inferred.
- [Ruytinx 2021](https://doi.org/10.3390/microorganisms9122612), Results 3.3:
  complete 11-word sentence, exact-matched in primary full-text XML. Main
  text and actual Figure 2 on p. 8 of the [author PDF](https://pure.mpg.de/rest/items/item_3375108_1/component/file_3400121/content)
  were inspected. The 21-day thinner, denser mantle follows a thick,
  dense 14-day state; it does not mean sheath loss. Methods 2.6 names
  WGA-Alexa 488 while the caption names WGA-oregon green. The discrepancy
  remains explicit. Other figure images and supplements were not inspected.

The maintained Europe PMC verifier returned `NOT_IN_ABSTRACT` for all
three full-text quotations. Their direct checks do not change that verdict
to `VERIFIED`; no snippet-baseline exception was added.

Canonical example: `NCBITaxon:29883 Laccaria bicolor`, specifically S238N
in Populus tremula x alba 717-1B4 P20 sandwich coculture, including the
14- and 21-day mantle states (Ruytinx Methods 2.1/2.3, Results 3.3,
Figure 2B-C). The [laboratory provenance page](https://mycor.iam.inrae.fr/IAM/?page_id=4555)
traces the culture to a 1976 Crater Lake, Oregon fruitbody collected under
Tsuga mertensiana. Fresh NCBI EFetch resolves species 29883 and its separate
child strain 486041 S238N-H82. That progeny is not substituted for the
experimental culture. Provenance is not counted as independent trait
evidence, and the example is not an all-strain claim or reidentification.

A protein-resolved graph is deferred pending verified protein identities,
sequence-to-culture links and the relevant perturbation images, not assumed
biologically absent. Krause's native ald1 overexpression and thicker mantle
do not establish a universal necessary pathway. Its mte1 assay is
heterologous yeast growth rescue, not native mantle-formation knockout.
Keep first formation, sheath thickness, branching and plant responses
separate. Ruytinx's EcM transcriptomic sample includes all fungal and mixed
plant-fungal material within 0.5 cm of the root; bulk expression does not
localize or functionally validate mantle proteins. Its models explicitly
remain hypotheses for future experiments.

## ID Space and Templates

Reserve `traitmech:000668`, v544 and `METPO:1062100` within the entire
`1062100-1062199` block; subset `metpo_traitmech_2026_10`.
At allocation, main `8e9a7b7c121e41e595c6161e6c0e925b6b42ec17` had maximum
local ID 664. Pending BAS #1788, peloton #1791 and Hartig #1794 reserved
665/v541/1061800-1061899, 666/v542/1061900-1061999 and
667/v543/1062000-1062099 respectively. These reservations stay occupied.

All eight then-open PRs, including drafts, were checked using complete
paginated changed-file lists and immutable Git-blob-verified curation files:

| PR | Head | Curation artifacts |
| --- | --- | ---: |
| #1794 | 2526a905a19d02667a928e40f18e5f93b2f3d5ad | 12 |
| #1791 | 8e830c82e7eb1dab968e33314ee42a1860997036 | 8 |
| #1788 | 7117fa563b54d61be07e3f1b6ead785794926506 | 4 |
| #1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 0 |
| #1734 | 23ddabfdd5db2c2b401a51a8b525d658ec3cbc54 | 15 |
| #1476 | a138e46f803b5af9d48969217b86cf7c9a3b61bd | 0 |
| #973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 0 |
| #924 | e61ce120b8da953da097b9f94bfed7f292e5675a | 0 |

Main and the open-head set were refreshed before branch creation. The
ignored-and-hidden ID/cohort/full-block search found 11 unrelated numeric
matches: seven embedding similarity values, one historical workflow run,
one Swagger numeric array and two SciPy fixtures. Their contexts were read;
none reserves an identifier. CommunityMech v1 and extensions were read and
do not overlap this block. Recheck concurrent reservations before publishing.

The prepublication refresh after BAS and #1734 landed covered all six
remaining open PRs. Hartig #1794 remains at `2526a905a19d02667a928e40f18e5f93b2f3d5ad`
and peloton #1791 was at `55b5523f7f6f48584a40bb4cfc53cc8cebd27121`;
the other four heads above were unchanged. Complete paginated file lists
and immutable curation blobs were checked again. The refreshed
ignored-and-hidden search of all other worktrees, actual main, pending
artifacts and CommunityMech searched 104,059 files / 2,262,739,703 bytes.
Its 12 matches were eight embedding values, the same workflow ID, the
Swagger array and two SciPy fixtures; none is a competing reservation.
The current branch was excluded from this non-self reservation search.

The upstream skill and both template headers were read at kg-microbe
`1408e7099d039026d7611c240938d8e177753406`: 11-column classes and
13-column properties. Retain the class directive row's three trailing empty
cells and use w3id.org METPO IRIs, not legacy purl stubs.

## Files and Verification

| File | Rows | Purpose |
| --- | ---: | --- |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 class | Scope A lift |
| proposal.md | Not applicable | Evidence and allocation narrative |
| Properties / SSSOM | 0, not emitted | No predicate or equivalence claim |

The guarded writer checks the parent projection, target and template replay,
and prevalidates before writing. Its 20 tests and dry run passed before
application. It uses `record_curation_event` and `write_validated_trait`.
Repository history records the actual Codex actor and is append-only.
Corpus counts are derived from live records; validation results will be
recorded after the maintained gates finish.

The current-main preservation audit overlays `f7112cf` on the tested
Hartig/peloton stack. All 1,062 expected prior YAMLs are preserved exactly,
including main's 11 updated records; older histories, proposal narratives,
548 TSVs (537 class, six property, five SSSOM), embedding products and
discussion templates are unchanged. Existing trait pages differ only in
their global-count footer except phenotype's expected added children.
Relative to main, phenotype has three extra children from peloton, Hartig
and mantle; no other priority row changes. The protected YAML is unchanged.

ROBOT output was parsed rather than counted by physical lines: classes,
merged and reasoned graphs contain 15, 12,628 and 12,632 triples. Assertions
verify label, definition, source annotation, phenotype parent, quality
ancestry and w3id.org IRIs. Desktop/mobile browser checks at 1,440/390
passed with three snippets, one qualified example, two discussions, history,
hierarchy and search navigation, a loaded coverage image and the live
1,063-record count. Screenshots were inspected. No overflow or browser
errors were observed. Both exact configured embedding input paths are
absent in the worktree and original workspace; no embedding rebuild is
claimed. Online NCBI resolved 745 canonical examples with zero errors and
24 existing warnings. All 20 governed artifacts match the immutable pin.

## Upstream Round Trip

After review, submit the template and hierarchy question to METPO or the
kg-microbe proposal pipeline. The placeholder is not a released METPO term
or the record's live identifier. Following upstream acceptance, refresh
the pinned ontology, seed a temporary tree, compare meanings and migrate
references, retaining the local ID as provenance rather than a synonym.
Append history, regenerate products and revalidate. Use the native merge
queue and verify actual MERGED state and reconstructed landed-tree integrity
before deleting the feature branch.

## Change Log

- v544, 2026-10-07: one root-external fungal sheath phenotype, three
  primary DOI snippets, a culture-qualified example and explicit boundaries.
