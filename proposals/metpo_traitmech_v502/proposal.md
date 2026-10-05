# Bacterial Cannibalism: METPO Proposal v502

## Context

Add `traitmech:000626 bacterial cannibalism`, a PROPOSED ECOLOGY class
for the classical nutritional sense: killing conspecific cells and obtaining
nutrients from them. This is an organismal phenotype, not possession or
expression of toxin genes. The record deliberately preserves uncertainty in
the feeding interpretation and newer contrary evidence.

Whole-repository novelty searches included ignored and hidden files, labels,
slugs, fratricide and conspecific/sibling-killing terminology, DOI/PMID/PMC
identifiers, the local identifier and the complete proposed hundred block.
The only cannibalism-name matches were unrelated NetworkX dependency code.
Structured examination of the pinned METPO found no exact class. The fresh
399-record seed shares 344 identifiers with the 1,020-record pre-addition
corpus; the 55 absent seed IDs are not treated as a missing-work queue.
The 1,546-row release delta and 153-row active-review inventory had no matching
candidate. This is not a claim that microbial trait discovery is exhausted.

An all-state upstream issue search returned no cannibalism/fratricide proposal
on 2026-10-05. Full file inventories of the four open TraitMech PRs and four
open METPO PRs showed no competing trait or proposal allocation.

## Scope and Hierarchy

| Scope | New Classes | Existing Classes Reused | Parent |
| --- | ---: | ---: | --- |
| A: synthetic trait | 1 | 1 | METPO:1007653 predatory bacterium |
| B: predicates | 0 | 0 | Not applicable |
| C: schema enums | 0 | 0 | Not applicable |

The existing predatory bacterium definition includes killing and nutrient
consumption, without restricting prey to another species. Conspecific prey
therefore supplies the differentia. The template repeats its existing v5 ID
`METPO:1007653`, definition and phenotype parent so standalone ROBOT validation
has a real labeled parent. Its TraitRecord is not edited and its ID is not
reallocated. v5 remains valid; these parent assertions agree.

Bacteriocin production does not require feeding or conspecific killing.
Saprotrophy need not kill the consumed material. Natural competence concerns
DNA uptake. No exact synonymy with those traits, fratricide, programmed cell
death, sporulation delay or biofilm formation is asserted.

The 2026 study also uses cannibalism for a broader toxin-dependent developmental
program. That source-attributed usage is retained in an OPEN scope discussion;
the nutritional class and its predation parent do not classify every phenotype
that paper calls cannibalism. A toxin-expression signature is insufficient to
assign this trait.

## Evidence and Limits

- `DOI:10.1126/science.1086462`, `PMID:12817086`: classical identity source;
  directly retrieved scientific abstract and author-posted main text read.
  The feeding explanation is inferred, not a traced uptake measurement.
- `DOI:10.1111/j.1365-2958.2009.06882.x`, `PMID:19775247`, `PMC2983100`:
  NCBI BioC full text directly read, including Results and Methods. Distinguish
  the NCIB3610 background from engineered hypercannibal derivatives.
- `DOI:10.1128/mbio.00525-26`, `PMID:42294941`, `PMC13343845.1`:
  2026-06-15 publication; full-text XML and PMC HTML directly read. The short
  counterevidence quote is from IMPORTANCE, not the scientific Abstract.

All three evidence items have contiguous snippets. Actual figures and
supplements were not inspected; no figure-specific numerical claim is imported.
No canonical example, protein accession, causal graph, synonym, xref or SSSOM
mapping is added. Direct conspecific feeding measurements and natural strain
provenance remain explicit prerequisites for exemplar curation. Gene presence,
expression and developmental or membrane-integrity readouts are not substituted
for those measurements. The record stays PROPOSED pending human review.

## ID Space and Artifacts

Reserve new block `1057900-1057999` and class `METPO:1057900`, following v501;
subset `metpo_traitmech_2026_10`. This does not overlap CommunityMech v1.
The template follows the pinned kg-microbe contract at
`ea1c5f15e6c4dba6c72165367162b354e215f018` with w3id METPO expansion.
Citation fields contain source references, not external ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 2, including the unchanged existing parent |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

LinkML and strict validation, `just validate-history`, `just validate-products`
and `just qc` passed. All 626 local identifiers have proposal coverage and
all 506 PROPOSED records passed the citation gate. The guarded writer passed
10 focused tests; README/priority checks passed 44 tests and the QC-dashboard
check passed. Existing audit baselines were not changed.
The full Python 3.13 suite passed: 2,262 tests, with two dependency deprecation
warnings, in 1,137.75 seconds.

The maintained snippet verifier returned three VERIFIED verdicts against its
retrieved Europe PMC text. Separately, all three snippets were checked as exact
contiguous text in directly retrieved source material. This does not turn the
2026 IMPORTANCE passage into a scientific Abstract or into positive feeding
evidence. The versioned PMC URL returned the actual article with the expected
DOI and passage.

`just verify-proposal proposals/metpo_traitmech_v502` and
`just robot-validate-proposal proposals/metpo_traitmech_v502` passed, with no
unsatisfiable classes. Direct RDF checks confirmed the child-to-predation-to-
phenotype hierarchy, definitions, labels and w3id IRIs. The merged file contains
12,638 RDF triples (23,339 physical lines); the reasoned file contains 12,642
triples (23,343 lines). Line counts are not triple counts.

Generated pages, discussions and dashboards reflect 1,021 records. Comparing
every existing trait page with the base after removing the footer found 1,019
footer-only changes and just one substantive existing-page change: the new
child link on predatory bacterium. Both configured embedding-input paths were
absent; embeddings were not rebuilt.

Playwright checks at 1,440px and 390px verified identity, local-ID provenance,
three evidence items and snippets, reciprocal parent/child links, dashboard
counts and image loading, with no horizontal overflow or JavaScript errors.
Screenshots were inspected. The existing floating theme button can overlap
mobile text; this shared-template limitation is not a new trait-data defect.

Whitespace checks passed outside the ROBOT TSV and on that exact TSV with
blank-at-EOL checking disabled. The ordinary check flags only its three
required empty trailing template-header cells; all four TSV rows have exactly
11 parsed columns. These cells were preserved, not trimmed.

## Upstream and Round Trip

Submit this cohort for METPO review. After accepted identifiers appear in a
release, refresh the pinned ontology, migrate the local identifier and parent
references to accepted METPO IDs, preserve local-ID provenance in migration
artifacts and append-only history, and regenerate products without duplicate
primary records. The reused predation parent must migrate consistently too.

## Change Log

- v502, 2026-10-05: propose nutritional bacterial cannibalism with explicit
  inferential limits and contrary developmental evidence.
