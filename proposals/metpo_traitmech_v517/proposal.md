# Ribophagy: METPO Proposal v517

## Context

Add `traitmech:000641 ribophagy`, a PROPOSED PHYSIOLOGY class, on base
`d4cf4735a0b401dc230186a241c7e8e71436be92`. The record denotes selective
macroautophagic degradation of mature ribosomes or their subunits by a
microbial cell, not a gene, sequence motif, ribosome-presence record,
bulk RNA-decay assay or host response elicited by a microbe.

Whole-repository novelty searches included ignored and hidden files,
ribosome-turnover variants, the source identifier bundles, GO:0034517,
the local identifier and prospective 1059400-1059499 block. CommunityMech
proposals were included. Related dormancy evidence concerns protection
against ribosome degradation, not ribophagy. No exact record, synonym,
causal node or earlier reservation needs repair. Complete all-state
GitHub queries for ribophagy in TraitMech and METPO, and 1059400 upstream,
returned zero hits without incomplete-results flags.

The pre-addition corpus contains 1,035 records. A fresh 399-record seed
shares 344 identifiers; the 55 absent terms are 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are live.
The complete 1,546-row release delta, 153-row active review and 12,617
pinned METPO triples contain no exact candidate or prospective-block hit.
This establishes local novelty, not exhaustion of microbial traits.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Selective mature-ribosome or subunit degradation narrows autophagy.
Mitophagy and pexophagy are cargo-specific siblings, not parents. Dormancy,
rRNA operon copy number, extracellular proteolysis and ribosome biogenesis
are not equivalent or closer parents. Delivery, free-protein turnover,
bulk RNA catabolism and marker accumulation alone do not show this phenotype.

The 2008 paper names selective mature-ribosome turnover ribophagy; the
2014 paper explicitly includes 60S subunits and separates their targeting
from 40S turnover. The 2025 Rsa1 study distinguishes its selective pathway
from previously named Ubp3/Ufd3/Cdc48-dependent ribophagy and discusses
different mammalian usage. Preserve this attribution as an OPEN terminology
question: the study is boundary evidence, not an unqualified canonical
ribophagy assignment. Do not split organismal traits solely by protein
names or impose a universal Ubp3 requirement.

Issuing [GO:0034517](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0034517)
is nonobsolete and specifies selective mature-ribosome degradation by
macroautophagy. Preserve that route qualifier, but do not equate a biological
process with this organismal phenotype. No xrefs, synonyms or SSSOM mapping
are asserted.

The TSV retains v514's complete unchanged autophagy row as dependency
context, not a new allocation. The writer guards the live parent's eight
identity/scope fields and the complete v514 template. Existing trait YAMLs
and v514 are not edited. When combining cohorts upstream, deduplicate the
identical parent row; standalone ancestry is autophagy -> phenotype -> quality.

## Evidence and Limits

| DOI | PMID | Quote Words | Role |
| --- | --- | ---: | --- |
| 10.1038/ncb1723 | 18391941 | 17 | Original selective-ribophagy study |
| 10.1083/jcb.201308139 | 24616224 | 20 | 60S subunit turnover and Ltn1/Ubp3 dependence |
| 10.15252/embj.201489083 | 25468960 | 13 | Bulk RNA-catabolism boundary |
| 10.1016/j.jbc.2025.108554 | 40294649 | 20 | Rsa1 mechanism and terminology boundary |

All four short snippets exactly match directly retrieved Europe PMC core
scientific abstracts with matching DOIs. The maintained resolver reports
four VERIFIED rows. For the 2014 paper, the XML scientific abstract was
distinguished from its precis; Introduction, the LTN1-deletion Results,
strain/culture Methods and Table 1 were read. Reporter cleavage and
localization support vacuolar degradation; loss of LTN1 rescues the delayed
reporter cleavage in ubp3 mutants. This is not an unconditional gene-presence
criterion. BY4741 has listed auxotrophic deletions, not independently
verified natural-exemplar provenance.

For the 2025 paper, XML Results sec1.1-sec1.3, Discussion sec2 and Methods
sec3.1/sec3.7-sec3.11/sec3.13 were read. Rpl25-GFP processing, Atg2 controls
and RNA measurements support degradation; RNA accumulation alone does not.
Residual turnover in rsa1 mutants remains. The Discussion's nascent nuclear
cargo hypothesis is not established by the mature-rRNA measurements.
Rpl8 contact and Atg8-binding motifs are modeled, not experimentally mapped.
Actual figures and supplements were not inspected, despite directly read
captions. Full Methods and independent strain provenance were not audited.
The 2008 and 2015 sources were read as scientific abstracts only; the latter's
full-text endpoint returned HTTP 500. Search-index text was not substituted.

No canonical examples or causal graph are added. Two OPEN discussions
retain terminology, strain-provenance and subunit-specific mechanism limits.
The phenotype belongs to the yeast, not an E. coli protein-expression host.
PROPOSED status requires human signoff; source matching or green tests are
not biological approval.

## ID Space and Files

Reserve `METPO:1059400` in the fresh 1059400-1059499 block following v516;
local identifier `traitmech:000641`, subset `metpo_traitmech_2026_10`.
Parent `METPO:1059100` remains v514's allocation. Ignored-and-hidden searches
found no block collision in TraitMech or CommunityMech proposals.
The upstream kg-microbe contract remains at
`1408e7099d039026d7611c240938d8e177753406`; use its 11-column class headers
and w3id METPO IRIs, not legacy purl stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The writer dry run and 22 controlled-fixture tests pass, covering identity,
evidence boundaries, parent/context parity, replay, drift refusal and
validation before writes. Direct abstract matching and the maintained
snippet resolver pass (four VERIFIED rows, similarity 1.00). The 45 focused
artifact tests passed in 272.41 seconds. Direct LinkML/strict validation,
history/products, `just qc`, Ruff and staged PR sanity pass. ROBOT/ELK and
parsed RDF checks pass: classes/merged/reasoned have 25/12,638/12,642 triples
with the expected w3id ancestry. All 1,035 old YAMLs and v514 remain unchanged;
1,034 old page bodies have footer-only changes, while autophagy gains a child
link. Its only priority-row change is children 2 -> 3. Desktop/mobile
Playwright checks and screenshot inspection pass at 1440/390 pixels.
The live corpus has 1,036 records, 521 PROPOSED and 155 PHYSIOLOGY.
Both configured embedding sources are absent, so embeddings are not rebuilt.
The ordinary staged whitespace check flags only the required trailing empty
ROBOT header cells; inspected exact-TSV scoped checks pass. The full suite
passed 2,539 tests with two dependency deprecation warnings in 626.16 seconds.
Committed-history, exact-head CI, review and native-queue receipts will be
recorded on the PR; they are not inferred from local test success.

## Upstream and Round Trip

Submit the new class and unchanged autophagy dependency for METPO review.
After acceptance, refresh the ontology, migrate identifiers and parent links
to accepted METPO IDs, preserve minting provenance and append-only history,
and regenerate without duplicate primary records. The terminology and
exemplar/mechanism discussions remain OPEN.

## Change Log

- v517, 2026-10-06: propose microbial ribophagy with four DOI-backed snippets,
  explicit subunit, selectivity and terminology limits, and unchanged parent context.
