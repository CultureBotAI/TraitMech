# Nucleophagy: METPO Proposal v519

## Context

Add `traitmech:000643 nucleophagy`, a PROPOSED PHYSIOLOGY class, on base
`26760c825a9fc41206477e6749b9b4c46fec1b6c`. Nuclear-cargo degradation through
autophagy is a microbial phenotype, not a sequence feature, gene inventory,
generic DNA-degradation observation or nuclear structure.

Whole-tree novelty searches included ignored and hidden files, CommunityMech
proposals, label/slug variants, nuclear autophagy/degradation/turnover,
piecemeal microautophagy, the DOI/PMID/PMC bundles, GO:0044804/0044805,
local identifier and the complete 1059600-1059699 block. ER-phagy's existing
mentions explicitly deny equivalence and are not unresolved exact nodes.
The broad lexical search also matched ribophagy's nucleotide-catabolism
boundary, not nuclear degradation. No exact record, synonym, node or prior
allocation was found. All-state GitHub searches found only #1753's research
lead in TraitMech, and no upstream nucleophagy or 1059600 hit; results were
not marked incomplete. The subsequently read 2013 review's DOI/PMID search
found only this branch's new files.

An additional nuclear-degradation GitHub search found #1691 and this repair's
#1754. Direct inspection of heterokaryon incompatibility (`traitmech:000606`)
shows a nonself-recognition phenotype with nuclear DNA-degradation readouts,
not autophagic delivery or an unresolved exact nucleophagy node. It remains
unchanged. A multiline ignored/hidden alias search and upstream piecemeal-
microautophagy search found no additional exact proposal.

The pre-addition corpus had 1,037 records. A fresh 399-record seed shares
344 identifiers; the 55 absent terms are 38 supporting-field terms and
17 reviewed duplicates. All 38 formerly unselected classes are live.
The complete 1,546-row release delta, 153-row active review and 12,617-triple
pinned METPO graph contain no candidate or prospective-block hit.
These checks establish local novelty, not exhaustion of microbial traits.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| A: existing parent correction | 0 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Nucleophagy narrows autophagy by nuclear cargo, including nuclear portions
or entire nuclei. It includes micro and macro routes without imposing a
universal gene, trigger, selectivity criterion or lethal outcome. ER-phagy
can overlap nuclear-envelope turnover without being equivalent. Mitophagy,
pexophagy and ribophagy are other cargo-specific siblings, not parents.

The 2013 review explicitly describes nucleophagy as selective. The 2024
study's Discussion also uses the name for the 2012 nonselective Magnaporthe
route. This cargo-defined phenotype preserves that broader attributed usage
and an OPEN discussion rather than silently treating one convention as
universal. Current, nonobsolete
[GO:0044804](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044804)
includes nuclear parts and entire nuclei without an explicit selectivity
restriction. Its process scope is not an exact organismal-phenotype mapping.
No exact synonym, xref or SSSOM alignment is asserted.

## Relationship to v514-v518

Issue #1754 identifies an overly narrow word in the autophagy definition:
cytoplasmic excludes nuclear cargo. The existing concept and local/proposed
identifiers are retained, while intracellular corrects the wording. Prior
self/non-self evidence, catabolic endpoints and route limits remain intact;
whole-nucleus evidence is added with a new per-record and repository history.
Current GO:0006914 scope was independently resolved at QuickGO and is
consistent with inclusion of cellular materials; it is not used as an exact
phenotype xref or substituted for experimental evidence.

The v519 TSV includes the corrected `METPO:1059100` dependency context,
not a second allocation or a new autophagy term. Its updated definition,
source list and observation supersede that parent row's narrow wording in
v514-v518. All five old TSVs remain byte-identical as historical artifacts,
and their narratives point to this correction. Their child rows stay valid.
When combining cohorts, select the v519 parent row and do not union both
old and corrected definition annotations. This is an evidence-backed
definition repair, not retraction, renumbering or semantic repurposing of
the parent. The new child receives the fresh v519 ID block.

The writer guards the complete parent preimage, recognizes only its exact
postimage for replay, and guards the full historical v514 template. Both
records validate before any production write. Older writers and their
production preimage guards remain unchanged; their controlled-fixture tests
must continue to pass independently of later parent curation.

## Evidence and Limits

| DOI | PMID | Quote Words | Role |
| --- | --- | ---: | --- |
| 10.1091/mbc.e02-08-0483 | 12529432 | 19 | Nuclear-parts microautophagy and degradation |
| 10.1091/mbc.e08-04-0363 | 18701704 | 20 | Revised PMN dependence and terminal-stage distinction |
| 10.1007/s00284-024-03838-y | 39162852 | 23 | Whole-nucleus vacuolar degradation and parent scope |
| 10.1371/journal.pone.0033270 | 22448240 | 18 | Nonselective route boundary |
| 10.1242/jcs.133090 | 24013549 | 18 | Review terminology, not experimental replication |

All quotes are contiguous scientific-abstract spans directly retrieved from
Europe PMC with matching DOIs. The live resolver reports five VERIFIED rows
for the new record and five for its updated parent. Manual section identity
and exact-substring checks were separate from resolver matching.

The early yeast papers were read as abstracts; failed full-text access is
not a biological negative. The 2008 assay conclusions revise the 2003
dependence claim. Blebs and inhibited bodies alone do not establish flux.
Selected 2024 XML Methods/Results/Discussion and 2012 PLOS Results were read.
Their assay, complementation, strain/reporter and unpublished-data limits
are retained in evidence notes. Actual figures and supplements were not
inspected; no panel-level or numerical experimental claims are curated.
The 2013 review's full text/poster was not inspected.

Canonical examples and causal graphs remain unset pending natural-strain
provenance and native taxon-paired protein evidence. Two OPEN child discussions
and the retained parent discussions preserve unresolved questions. Passing
source matching does not promote PROPOSED records to human REVIEWED status.

## ID Space and Files

Reserve `METPO:1059600` in fresh 1059600-1059699, following v518.
The local identifier is `traitmech:000643`; subset `metpo_traitmech_2026_10`.
`METPO:1059100` remains v514's parent allocation. No block collision was
found in ignored/hidden whole-tree, CommunityMech or upstream checks.
The upstream kg-microbe contract and canonical templates were fetched at
`1408e7099d039026d7611c240938d8e177753406`: class headers have 11 columns;
canonical properties have 13. METPO IRIs use w3id, not legacy purl stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 corrected parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer dry run, optimized-Python replay dry run and 36
controlled-fixture tests pass, covering replay, parent/target/template drift
refusal and validation-before-write. Both records' live snippet checks pass.
The focused README/priority/QC-dashboard and five older sibling-writer tests
passed 152 tests in 308.82 seconds. No older writer, test or baseline changed.
LinkML/strict validation, history, product-label checks, `just qc`, Ruff and
staged PR sanity pass. Product labels retain 123 SKIPPED_NO_ADAPTER rows;
the two existing source-license warnings remain explicit.

ROBOT/ELK and parsed RDF pass: classes/merged/reasoned have 25/12,638/12,642
triples, one corrected autophagy definition and the expected labeled w3id
child -> autophagy -> phenotype -> quality hierarchy. All 1,036 unrelated
old YAMLs and old page bodies are unchanged except page footers. Autophagy
has exactly the guarded repair and its expected child count changes 4 -> 5.
All five historical TSVs and shared discussion templates remain byte-identical.
The corpus has 1,038 records, 523 PROPOSED, 157 PHYSIOLOGY and 578 discussions
across 509 records. The protected record is unchanged.

Playwright and inspected screenshots at 1440/390 pixels confirm local identity
provenance, five quotes, two OPEN child discussions, corrected parent wording,
hierarchy navigation, dashboard counts and a loaded coverage image, without
horizontal overflow or page errors. Both configured embedding inputs are
absent, so embeddings were not regenerated. The scratch artifact audit's
first invocation lacked PYTHONPATH and failed to import the local package;
the explicit PYTHONPATH=src retry passed without changing production code.

Ordinary staged whitespace checking flags only the required three trailing
empty ROBOT directive cells. Exact-template scoped checks pass after header
width/directive inspection. Full-suite, committed-history, review, CI and
landing outcomes are tracked separately: the full local suite passed 2,597
tests in 586.36 seconds with two dependency warnings. Committed-history,
exact-head review, CI and landing outcomes will be recorded on the PR after
completion; local self-review is not independent approval.

## Upstream and Round Trip

Submit the child and corrected parent context for METPO review with #1754's
scope rationale. After acceptance, refresh the ontology, migrate identifiers
and parent links to accepted IDs, retain minting/history provenance and
regenerate without duplicate records. Preserve the independent OPEN source-
scope and exemplar/mechanism questions until separately resolved.

## Change Log

- v519, 2026-10-06: propose nuclear-cargo autophagy and repair the existing
  autophagy parent's cytoplasmic-only wording, with five cited snippets.
