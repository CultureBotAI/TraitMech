# Fungal Mycelial Cord Formation: METPO Proposal v545

## Context and Scope

Propose `traitmech:000669 fungal mycelial cord formation`, a PROPOSED
MORPHOLOGY class. This is a developmental phenotype, not a bare structure,
network-analysis variable or inferred nutrient-transport capability.
The branch starts from actual main `4e7e8cd1ceaf7e74f9cfce18f8174c3edfe9b4dd`.
Hartig #1794 and mantle #1796 remain pending but are not included in this
branch. Their identifier reservations remain occupied.

| Scope | Count | Parent |
| --- | ---: | --- |
| A: synthetic trait class | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

Ignored-and-hidden searches covered the whole original repository and all
nine other existing worktrees, the complete pending-PR curation snapshot,
and CommunityMech proposals. Queries included mycelial/hyphal cord and
strand variants plus the primary DOIs. Existing matches were the rhizomorph
scope discussion and the fusion paper's individual hyphal-strand wording,
plus their scripts and generated copies, not an exact cord-formation record.
The two records were read before accepting this target. The parsed pinned
METPO graph has 12,617 triples and no exact cord/strand class; active-release
review tables were also searched. This establishes a specific gap, not
exhaustion of microbial-trait discovery.

## Hierarchy and Meaning

Use active phenotype `METPO:1000059`, under quality `METPO:1000188`.
The operational definition adopts the diffuse-front developmental sense
specified by Boddy et al., not every historical use of cord or strand.
The existing rhizomorph definition (`traitmech:000662`) is broader in wording
and retains the source-attributed Koch/Oliveira terminology conflict. Its
OPEN discussion gains a link to this record; no existing definition,
evidence, example, synonym or parent changes. No exact equivalence,
subclass or organism-level disjointness between the two traits is asserted.

Bacterial mycelial growth (`000074`), completed hyphal fusion (`000605`),
filament-shaped cells (`METPO:1000674`) and filamentous/rhizoid colony
outlines (`1007066`/`1007068`) differ in scope. No exact synonyms, xrefs,
SSSOM mappings, universal pigment/rind requirements or molecular causal
graph are proposed. Closer fungal hierarchy and historical terminology
remain explicit curation questions.

## Evidence and Example

- [Boddy et al. 2009](https://doi.org/10.1007/s10267-008-0450-4): a directly
  read review supplies the adopted terminology, not experimental replication.
  The short Introduction clause was visually checked on printed p. 10 in
  the [author PDF](https://markfricker.org/wp-content/uploads/2015/12/boddy_et_al-2009-mycoscience-50-9.pdf).
- [Dowson et al. 1986](https://doi.org/10.1099/00221287-132-1-203): primary
  formation evidence and canonical-isolate provenance. All nine pages of
  text and actual Figures 1 and 3 were read in the
  [original-paper reprint](https://www.davidmoore.org.uk/21st_century_guidebook_to_fungi_platinum/REPRINT_collection/Dowson_etal_mycelia_cord-forming_basidiomycetes.pdf).
- [Wood et al. 2006](https://doi.org/10.1016/j.mycres.2006.05.013),
  [PMID:16891104](https://pubmed.ncbi.nlm.nih.gov/16891104/): a separately
  retrieved scientific abstract reports cord production and remodeling.
  Full text, images and isolate provenance remain unread.

The example is `NCBITaxon:194680 Phanerochaete velutina`, verified by NCBI
EFetch and limited to the natural, unnumbered UK isolate and experimental
conditions recorded in the YAML. No later collection strain is substituted.
Formation does not establish a universal transport or sensing mechanism.
The maintained snippet resolver returned `NOT_IN_ABSTRACT` for the 2009
full-text clause, `UNRESOLVED` for 1986 and `VERIFIED` for the 2006 scientific
abstract. Exact-DOI Europe PMC retrieval returned no 1986 record; Crossref
confirmed its title, authors, year and pages, and the paper itself was read.
These direct checks do not overwrite the automated resolver verdicts.

## ID Space and Templates

Reserve `traitmech:000669`, v545 and the complete `METPO:1062200-1062299`
block, using row `METPO:1062200` and subset `metpo_traitmech_2026_10`.
No reservation for the ID, cohort or full block occurred in ignored-and-hidden
searches of main, all local worktrees, pending artifacts or CommunityMech.
The broader bare-number check also inspected six dependency-file matches:
floating-point sample data and a web-archive timestamp, not reservations.
CommunityMech v1/v1.1/v1.2 blocks do not overlap.

The complete paginated open-PR snapshot was checked at immutable heads,
including drafts; every selected artifact's Git blob was verified and the
head set rechecked at the end:

| PR | Head | Curation artifacts |
| --- | --- | ---: |
| #1796 | d058d9e1e546e7549fdc2085860fc47524f60c23 | 8 |
| #1794 | 7b10b76e22fa48cd82cdf4a52b78955e95f25b1b | 4 |
| #1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 0 |
| #1476 | a138e46f803b5af9d48969217b86cf7c9a3b61bd | 0 |
| #973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 0 |
| #924 | e61ce120b8da953da097b9f94bfed7f292e5675a | 0 |

Pending Hartig reserves 000667/v543/1062000-1062099; mantle reserves
000668/v544/1062100-1062199. Recheck before publishing and merging.
The upstream skill and canonical headers at kg-microbe
`1408e7099d039026d7611c240938d8e177753406` were rechecked: 11 columns for
classes, 13 for properties. The class directive retains three trailing
empty cells. Use w3id.org METPO IRIs, not the legacy purl example.

## Files and Verification

| File | Rows | Purpose |
| --- | ---: | --- |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 class | Scope A lift |
| proposal.md | Not applicable | Evidence, boundaries and allocation |
| Properties / SSSOM | 0, not emitted | No new predicate or equivalence |

The writer defaults to dry run, guards the full semantic rhizomorph
preimage, parent projection and target/template replay, and prevalidates
both records before writing. Thirty-five tests and a production dry run
passed before application. Each changed record receives its own curation
event and scaffolded repository history. Corpus validation, generated
artifacts and committed-tree QC now pass. Exact-head CI and published-PR
review remain pending.

Local verification receipts:

- LinkML and strict validation passed for both touched records; all 3,227
  full-suite tests (693.37 seconds), all 100 focused tests, Ruff,
  proposal verification, ROBOT, history, products,
  committed-history audit, `just qc` and PR sanity passed.
- Online taxonomy resolved all 744 examples with zero errors and 24 existing
  label warnings. The three snippet resolver outcomes above are retained.
- Parsed OWL contains 15 class-template, 12,628 merged and 12,632 reasoned
  triples. The proposed class and both parent levels use the correct w3id
  IRIs; its definition and citation annotation match the TSV and YAML.
- Preservation checks compare against actual main `4e7e8cd`: 1,060 prior
  trait YAMLs are byte-identical, with the rhizomorph discussion/history
  append checked separately. All old proposal templates, narratives,
  histories, embedding products and shared discussion templates are intact.
  Of the prior trait pages, 1,059 differ only in their corpus footer; the
  phenotype child list and rhizomorph scope note are the expected exceptions.
- Desktop/mobile browser checks at 1,440/390 pixels passed for evidence,
  canonical example, discussions, history, navigation and the regenerated
  dashboard image, without horizontal overflow or JavaScript errors. The
  corresponding screenshots were inspected.
- Neither configured embedding source path exists; existing embedding
  artifacts were preserved, not regenerated. The only ordinary whitespace
  finding is the TSV directive's three required trailing empty cells;
  exact-path-scoped whitespace checks pass without changing Git settings.
- The prepublication reservation snapshot rechecked all six pending heads
  above and their complete paginated files at immutable blob hashes. Fresh
  ignored-and-hidden allocation searches covered the original main checkout,
  all nine other worktrees and CommunityMech, with no competing reservation.
  Main remains `4e7e8cd1ceaf7e74f9cfce18f8174c3edfe9b4dd`.

The author adversarial pass tested the operational definition against broader
rhizomorph usage, the distinction between review terminology and primary
experiments, isolate provenance, snippet fidelity, ontology scope and writer
drift safeguards. No actionable curation defect was found in that pass.
This is an author review, not independent approval; existing OPEN scientific
questions remain explicit rather than being represented as solved.

## Dependency Reconciliation

The preceding validation receipts refer to the original independent branch.
Hartig #1794 subsequently landed as
`f9bd6b23517bc85f27af8dfdaae7d1d14a0e0454`, with exact landed-tree
reconstruction before branch cleanup. This draft incorporates that main
through reconciled mantle head `8538ab496c051fe7d4dac89a478dda381fd8544e`
and remains dependent on mantle #1796's actual landing. Generated conflicts
are resolved with the separate citation audit and four maintained product
generators; README counts are derived from the combined corpus. A fresh full
suite validates the combined data rather than relabeling the old independent
branch's run. Final exact-head validation and review receipts are recorded
on PR #1798. Reconcile actual landed main again and reduce the final scope
to cord and its coupled rhizomorph discussion before queue admission.

## Upstream Round Trip

After TraitMech sign-off, submit the class template and terminology question
to METPO or the kg-microbe proposal pipeline. The reserved METPO ID is not
a released identifier. After upstream acceptance, refresh the ontology,
seed to a temporary directory, verify semantic correspondence and migrate
references while retaining the old local identifier as provenance, not
a lexical synonym. Append history and regenerate all affected products.
Use the native merge queue and reconstruct the actual landed tree before
deleting this branch.

## Change Log

- v545, 2026-10-07: one source-qualified cord-formation phenotype and a
  tightly coupled link in the existing rhizomorph scope discussion.
