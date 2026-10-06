# Pexophagy: METPO Proposal v516

## Context

Add `traitmech:000640 pexophagy`, a PROPOSED PHYSIOLOGY class, on base
`82a5fb3b02254fd7981bd3a9eaa32a3e79979196`. This is selective peroxisome
degradation by a microbial cell, not an ATG gene, protein, sequence feature,
organelle-presence record or animal-host response induced by a microbe.

Whole-repository searches included ignored and hidden files, candidate
labels, peroxisome-turnover variants, all four source identifier bundles,
GO terms, the local identifier and prospective 1059300-1059399 block.
CommunityMech proposals were included. The only relevant prior mention is
broader autophagy evidence and its generated copies, plus v514's earlier
search narrative; there is no exact record, synonym or graph to repair.
Complete all-state GitHub queries for pexophagy in TraitMech and METPO,
and 1059300 upstream, returned zero results with no incomplete-results flag.

The pre-addition corpus has 1,034 records. A fresh 399-record seed shares
344 identifiers; its 55 absent identifiers are 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are live.
The full 1,546-row release delta and 153-row active review were parsed.
All 12,617 pinned METPO triples were checked for candidate terminology and
the new block, without a hit. These checks establish local novelty,
not exhaustion of the microbial-trait frontier.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Selective peroxisome degradation narrows the broad autophagy phenotype.
Mitophagy is a sibling with different cargo, not a parent. Uptake/feeding,
extracellular proteolysis, secretion and organelle presence are not equivalent
or better parents. Incidental bulk capture and cytosolic peroxisomal-protein
turnover are not sufficient; neither starvation nor damaged cargo is universal.

The 2008 PpAtg30 scientific abstract explicitly uses pexophagy for both
micropexophagy and macropexophagy. Its opening nonselective characterization
of autophagy is not imposed on the route-inclusive local parent. In contrast,
the issuing [GO records](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000425,GO%3A0000426,GO%3A0030242)
use GO:0000425 pexophagy specifically for selective macroautophagy, with
macropexophagy exact; GO:0000426 micropexophagy is its sibling under
GO:0030242 autophagy of peroxisome, which lists pexophagy as related.
All three are nonobsolete biological-process terms. This source-attributed
scope mismatch remains OPEN for human review; no exact phenotype xref,
synonym or SSSOM mapping is asserted.

The TSV carries v514's unchanged autophagy row as dependency context,
not a second allocation or newly minted class. The guarded writer checks
the live parent's eight-field projection and complete original template.
This preserves standalone autophagy -> phenotype -> quality ancestry.
No existing trait YAML or v514 proposal changes. Upstream should deduplicate
the identical context row when combining cohorts.

## Evidence and Limits

| DOI | PMID | Quote Words | Source and Role |
| --- | --- | ---: | --- |
| 10.1038/emboj.2012.151 | 22643220 | 20 | Scientific Abstract; definition and Atg36 study |
| 10.1016/j.devcel.2007.12.011 | 18331717 | 14 | Scientific Abstract; selectivity and route-inclusive terminology |
| 10.1242/jcs.108.1.25 | 7738102 | 19 | Scientific Abstract; vacuolar degradation and route diversity |
| 10.1080/15548627.2019.1603546 | 31007124 | 20 | Scientific Abstract; cytosolic-protein boundary, not positive organelle turnover |

All four snippets exactly match directly retrieved Europe PMC core scientific
abstracts with matching DOIs. The maintained resolver reports four VERIFIED
rows. Snippet matching is not proof of every biological interpretation.

For the Atg36 study, Results sec3/sec4 and Methods sec16/sec20/sec23 were
also directly read in PMC3395097 XML. Peroxisomal reporters, Pex11-GFP
processing and Atg1/vacuolar-protease controls support degradation; Cvt,
mitophagy and bulk-autophagy assays bound selectivity. Pex14 deletion retains
pexophagy in this species, and engineered mitochondrial Pex3 redirection is
not native Atg36 mitophagy evidence. Figure 1/2 captions were read; actual
figures could not be retrieved, and supplements, complete Methods and natural
strain provenance were not inspected. Putative BLAST orthologues are not
functional protein examples. The other studies have directly read scientific
abstracts only; full methods, actual figures and strain provenance were not
audited. Failed full-text access is not replaced by search-index snippets.

No canonical examples or causal graph are added: natural strain provenance,
historical Pichia taxonomy and accession-level native taxon-paired mechanisms
remain unresolved. Two OPEN discussions retain these limits. Atg30/Atg36
are not a universal receptor inventory. PROPOSED status still needs human
signoff; passing tests or resolver checks does not supply it.

## ID Space and Files

Reserve `METPO:1059300` in the fresh 1059300-1059399 block following v515;
local identifier `traitmech:000640`, subset `metpo_traitmech_2026_10`.
The parent `METPO:1059100` remains v514's allocation. No collision with
CommunityMech proposals was found, including ignored files. The upstream
kg-microbe contract was rechecked at
`1408e7099d039026d7611c240938d8e177753406`; the 11-column template headers
use its contract. Use w3id METPO IRIs, not legacy purl stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The writer dry run and 22 controlled-fixture tests passed. Tests cover
scope, source sections, cytosolic-protein boundaries, parent/context parity,
dry-run immutability, replay, drift refusal and validation before writes.
Direct scientific-abstract matching and the maintained snippet resolver passed.
The 45 focused artifact tests passed in 309.08 seconds. ROBOT/ELK and the
RDF hierarchy audit passed: classes/merged/reasoned graphs contain
25/12,638/12,642 triples. All 1,034 prior YAMLs, v514 and shared discussion
templates remain byte-identical. Existing pages have footer-only changes
except autophagy's child link; its only priority-row change is children 1 -> 2.
Desktop/mobile Playwright checks and screenshot inspection passed at 1440/390
pixels. Both configured embedding sources are absent, so embeddings were not
regenerated. Corpus totals are 1,035 records, 520 PROPOSED and 154 PHYSIOLOGY.

The requested skill review reproduced #1749: the verifier and guidance rejected
the canonical upstream 13-column property template. The same branch adds
backward-compatible 12/13-column validation and layout-specific guidance;
this class-only cohort's template is unchanged. All 28 verifier tests pass,
including 15 new end-to-end cases; the six existing legacy property cohorts
pass, and a canonical-header ROBOT smoke test retains two separate aliases
and the shifted subset. The add-trait skill passes its generic validator.
That validator rejects the companion skill's pre-existing legacy frontmatter
keys, which were confirmed unchanged rather than removed as unrelated churn.
Strict validation, history/products, `just qc`, Ruff and staged PR sanity pass.
The full suite passed 2,517 tests with two dependency deprecation warnings in
617.14 seconds. The combined writer/verifier focused suite passed 50 tests in
2.86 seconds. The ordinary staged whitespace check flags only three required
trailing empty ROBOT header cells; the documented exact-file scoped checks pass.
Committed-history validation, exact-head CI, review and native-queue receipts
will be recorded on the PR; they are not inferred from local test success.

## Upstream and Round Trip

Submit the new class with the existing autophagy dependency for METPO review.
After acceptance, refresh the ontology, migrate identifiers and parent links
to accepted METPO IDs, preserve minting provenance and append-only history,
and regenerate without duplicate primary records. The route-scope and
exemplar/mechanism discussions remain OPEN.

## Change Log

- v516, 2026-10-06: propose microbial pexophagy with four DOI-backed snippets,
  explicit source/route/endpoint limits and unchanged autophagy context.
