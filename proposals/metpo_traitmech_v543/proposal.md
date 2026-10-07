# Fungal Hartig Net Formation: METPO Proposal v543

## Context and Scope

Propose `traitmech:000667 fungal Hartig net formation`, a PROPOSED
MORPHOLOGY class for the fungal intercellular network within a plant root.
It is neither a bare anatomical structure nor a nutrient-transfer assertion.
This draft starts from tested combined head
`8e830c82e7eb1dab968e33314ee42a1860997036` of peloton #1791, including
reviewed BAS #1788. Both earlier PRs remain unmerged at allocation time;
the draft must incorporate their actual main commits before becoming ready.

| Scope | Count | Parent |
| --- | ---: | --- |
| A: synthetic trait class | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

The ignored-and-hidden novelty search covered the original workspace, all
five other existing worktrees, complete pending curation artifacts and
CommunityMech proposals: 57,781 files, 1,720,283,201 bytes, zero matches for
Hartig-net variants, intraradical-network names and the primary DOIs.
Broader root-colonization matches were bacterial ecological mechanisms,
not exact mentions to migrate. Neighbor definitions were read separately.

The parsed pinned METPO graph has 12,617 triples with no exact class found.
A temporary seed has 399 records; its 55 non-live IDs remain the previously
reviewed 17 class duplicates and 38 supporting relations/fields, not 55 new
trait candidates. The 1,546-row release delta and 153-row active-review
table were checked. This establishes a specific gap, not global exhaustion.

## Hierarchy and Meaning

Use active phenotype `METPO:1000059` under quality `METPO:1000188`.
Mycorrhization `METPO:1000198` is explicitly obsolete. Branched cell shape
`METPO:1000687`, bacterial mycelial growth `traitmech:000074`, intracellular
arbuscules `000664`, intracellular pelotons `000666`, and extraradical BAS
`000665` do not denote this architecture. Symbiosis and mutualism classify
associations and outcomes, not the network. No exact, broader or disjoint
relationship to haustorium formation `000663` is asserted.

The definition does not fix the host, root cell layer or mycorrhizal category.
The arbutoid study below supplies direct anatomical support. The directly
retrieved [Massicotte abstract](https://pubmed.ncbi.nlm.nih.gov/15490255/),
DOI `10.1007/s00572-004-0305-6`, also reports paraepidermal nets in two
monotropoid hosts. That abstract-only usage is qualified in a discussion;
its full text and images have not been inspected. The name is not limited
to the familiar ectomycorrhizal example. A closer parent remains OPEN.
No exact synonyms, structure xrefs or SSSOM equivalences are proposed.

## Evidence and Example

- [Zhang 2022](https://doi.org/10.1111/nph.17940), directly read publisher
  Introduction: definition authority and a 15-word contiguous snippet.
  Main text and captions were inspected, not actual images or supplements.
- [Zhang 2018](https://doi.org/10.1111/nph.15113), public
  [author PDF](https://ri.conicet.gov.ar/bitstream/handle/11336/117651/CONICET_Digital_Nro.2f10e756-314d-4409-8829-81a4798588b0_A.pdf?isAllowed=y&sequence=2):
  21-word Introduction snippet, exact-matched after PDF line joining and
  visually inspected. Actual Figure 2d supports the wild-type S238N
  example. Other figure images and supplementary contents remain unread.
- [Kuehdorf 2015](https://doi.org/10.1007/s00572-014-0590-7), public
  [publisher PDF](https://d-nb.info/1192098684/34): the 14-word descriptive
  sentence at printed p. 112 / physical p. 4 was exact-matched and visually
  checked. Main text and actual Figure 3 were inspected. The anatomy is
  restricted to subgroup e and does not identify every sequenced Leotia
  sample or the separately observed fruit bodies.

The maintained Europe PMC resolver returned `NOT_IN_ABSTRACT` for all
three full-text snippets. Direct manual verification does not change those
verdicts to `VERIFIED`.

Canonical example: `NCBITaxon:29883 Laccaria bicolor`, explicitly wild-type
S238N, in INRA 717-1-B4 poplar roots. The [laboratory provenance page](https://mycor.iam.inrae.fr/IAM/?page_id=4555)
supports natural collection provenance. NCBI EFetch confirms species 29883
and strain 486041 S238N-H82; that progeny is not substituted for S238N.
The example is culture-qualified, not an all-strain assertion.

The record defers a protein-resolved graph until sequence and authority
anchors are checked. Partial perturbation effects do not establish loss of
formation. The directly read [Chowdhury study](https://doi.org/10.1111/nph.18358)
further separates net depth from overall colonization frequency; its T89
host is not INRA 717-1-B4. The [2026 strain paper](https://doi.org/10.7150/jgen.130158)
and older laboratory history use conflicting S238O/S238-O provenance;
the discussion preserves this ambiguity rather than equating aliases.

## ID Space and Templates

Reserve `traitmech:000667`, v543 and `METPO:1062000` within the entire
`1062000-1062099` block. Subset: `metpo_traitmech_2026_10`.
Main `8e9a7b7c121e41e595c6161e6c0e925b6b42ec17` has maximum local ID
664. Pending BAS #1788 reserves 665/v541/1061800-1061899; peloton #1791
reserves 666/v542/1061900-1061999. Their published reservations remain
occupied before merge.

All seven open PRs, including drafts, were inspected by complete paginated
changed-file lists and immutable, Git-blob-checked curation artifacts:

| PR | Head | Curation artifacts |
| --- | --- | ---: |
| #1791 | 8e830c82e7eb1dab968e33314ee42a1860997036 | 8, BAS and peloton |
| #1788 | 7117fa563b54d61be07e3f1b6ead785794926506 | 4, BAS |
| #1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 0 |
| #1734 | ca9b337ec3d24806baf16b42b8f384087701280e | 14, existing records/history |
| #1476 | a138e46f803b5af9d48969217b86cf7c9a3b61bd | 0 |
| #973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 0 |
| #924 | e61ce120b8da953da097b9f94bfed7f292e5675a | 0 |

Main and the open-head set were refreshed before branch creation. The
ignored-and-hidden ID/cohort/full-block search covered all these sources
and historical records. Its five numeric matches were the identical
setuptools wheel byte size `1062021` in dependency locks, not reservations.
CommunityMech v1 and its extensions were read and do not overlap the block.
Recheck concurrent reservations immediately before publication and merge.

The upstream skill and two template headers were retrieved at kg-microbe
`1408e7099d039026d7611c240938d8e177753406`: 11-column classes and
13-column properties. The class directive row retains three trailing
empty cells. Use maintained w3id.org METPO expansion, not the legacy
upstream example's purl stub.

## Files and Verification

| File | Rows | Purpose |
| --- | ---: | --- |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 class | Scope A lift |
| proposal.md | Not applicable | Evidence and allocation narrative |
| Properties / SSSOM | 0, not emitted | No predicate or equivalence claim |

The guarded writer defaults to a dry run, checks the reviewed parent and
target/template replay, and prevalidates before writing. It passed its
20 tests and dry run before application. The new record uses
`record_curation_event` and `write_validated_trait`; repository history is
scaffolded with the actual Codex actor and remains append-only.

Local validation completed on 2026-10-07: LinkML and strict validation,
all four maintained product generators, predicate/node grounding, Biolink
coverage, proposal verification, ROBOT ELK, history and products, corpus
QC, local taxonomy and Ruff all passed. Focused tests passed (65 tests,
323.42 seconds), followed by the full suite (3,193 tests, 901.33 seconds).
Online NCBI validation resolved 744 examples with no errors and 24 existing
warnings. All 20 governed files match the pinned source. The final writer
dry run passed. RDF inspection confirmed the proposed label, definition,
parent, quality ancestry and citation annotation using w3id.org IRIs.

Preservation checks against the tested peloton/BAS base `8e830c8` found
all 1,061 prior trait YAML files, prior history, proposal narratives and
547 proposal TSVs (536 class, six property and five SSSOM files) unchanged.
Existing trait pages have only the generated global-count footer change,
except phenotype's expected new child. Existing priority rows are unchanged
except phenotype's child count. The protected spore-germination YAML is
unchanged. Both configured embedding sources are absent at their exact
worktree and original-workspace paths; existing embedding products and
discussion templates remain byte-identical.

Browser checks passed at 1,440- and 390-pixel widths: three snippets, one
qualified example, two open discussions, history and navigation, and the
1,062-record dashboard with a loaded coverage image. No horizontal overflow
or browser errors were observed; five screenshots were visually inspected.
Scoped whitespace checks passed, preserving the class template's required
three empty trailing directive cells as the sole exception.

### Current Main Integration

After BAS #1788 and pathway-context #1734 actually merged, the branch
incorporated main `f7112cf664c9a54e05ab5e771b2d0366dae9f0b1` and regenerated
all four maintained products. On integration head
`7495b092be3c96285b64e39fc87588ffc26a9186`, all 18 local validation steps
passed, including committed QC, 65 focused tests (529.45 seconds) and
3,212 full-suite tests (1,203.93 seconds). This supersedes the earlier
integration result above, not its historical provenance.

The preservation audit overlays actual main on the tested peloton stack:
1,061 prior YAMLs and 547 TSVs (536 class, six property, five SSSOM) remain
exact, including main's 11 updated records. Its schema, renderer, pathway
context index/pin, tests and protein-taxon report are preserved. Old history,
proposal narratives, embedding products, discussion templates and the
protected spore-germination record are unchanged. Existing-page differences
are limited to the count footer and phenotype's expected children; no other
priority row changes. Desktop/mobile checks passed again at 1,440/390 with
the complete qualified example, snippets, discussions and loaded dashboard.

Peloton #1791 remains a pending dependency. The main-based committed-history
gate therefore reports two traits/two history records, not a standalone
Hartig addition. Keep this PR draft until peloton actually lands, incorporate
its actual main commit, regenerate affected products and recheck the final
scope. Author adversarial review is not independent approval. Actual merge
and reconstructed landed-tree verification precede branch deletion.

## Upstream Round Trip

After TraitMech review, submit the template and hierarchy question to METPO
or the kg-microbe proposal pipeline. This placeholder is not a released
METPO term or the record's live identifier. Following upstream acceptance,
refresh the pinned ontology, seed a temporary tree and compare meanings,
then migrate references while retaining the local ID as provenance, not
a lexical synonym. Append history, regenerate products and revalidate.
Merge through the native queue; confirm actual MERGED state and reconstructed
landed-tree integrity before deleting the feature branch.

## Change Log

- v543, 2026-10-07: one intercellular root-network phenotype with three
  primary citations, qualified strain evidence and explicit scope limits.
