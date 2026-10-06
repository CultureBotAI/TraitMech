# Aggrephagy: METPO Proposal v522

## Context

Add `traitmech:000646 aggrephagy`, a PROPOSED PHYSIOLOGY class, on base
`70989f6c627deef1626e9012aa364358f53d0f09`. The phenotype is selective
macroautophagic protein-aggregate degradation by a microbial cell, not
protein aggregation, a gene inventory or a heterologous cargo sequence.

Whole-tree searches included ignored and hidden files, exact and variant
labels, multiline protein-aggregate/autophagy wording, the four DOI/PMID
bundles, PMC accessions, GO:0035973 and the prospective local/METPO block.
There was no exact record or prior local proposal. A first unbounded
IBophagy spelling search also matched ribophagy; boundary-aware reruns
removed that lexical false positive. The known #1757 landing comment was
read separately and names aggrephagy only as a research lead. GitHub
all-state searches in TraitMech and METPO returned no indexed aggrephagy
item, and the prospective ID search upstream was empty; none was marked
incomplete. Index silence does not override the known lead comment.

The pre-addition corpus has 1,040 records. A fresh 399-record METPO seed
shares 344 identifiers; 55 absent terms comprise 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are now
live. The full 1,546-row release delta, 153-row active review and
12,617-triple pinned METPO graph contain no candidate or block hit.
These checks establish candidate novelty, not discovery exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Selective aggregate cargo and the macroautophagic route narrow the existing
autophagy phenotype. No universal receptor, trigger, ubiquitination state
or aggregate reporter is imposed. The sibling proteaphagy record concerns
proteasomes as cargo, not the proteolytic disposal of unrelated aggregates.

[GO:0035973](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035973)
was directly resolved as a nonobsolete biological process for selective
protein-aggregate degradation by macroautophagy. It is not an exact
organismal phenotype. No exact xrefs, synonyms or SSSOM mapping is asserted.
IBophagy remains a source-attributed neighboring term, not an exact synonym
or a newly allocated child; its scope relationship requires human review.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.1080/15548627.2026.2724473 | 42647820 | Definition and yeast heat-induced aggregate degradation |
| 10.1038/s44319-024-00275-7 | 39322741 | Conditional solid-aggrephagy mechanism; PMC11549370 |
| 10.1016/j.cell.2014.05.048 | 25042851 | Yeast CUET evidence, distinct from human rescue |
| 10.1080/27694127.2023.2236407 | 37680383 | IBophagy boundary evidence; PMC10482306 |

All four snippets are exact spans from directly retrieved DOI-matched
scientific abstracts, not search extracts. The 2026 Abbreviations and 2024
Synopsis are separate sections, not scientific-abstract authorities. Three
papers supply positive aggregate-turnover evidence; the fourth informs a
terminological boundary. Linked commentaries are not counted as independent
experimental replication. Source-specific access and assay limits are
preserved in the YAML notes.

The 2024 XML Introduction, Results Sec3-Sec7, Discussion Sec9 and yeast
Methods Sec11 and Sec14-Sec16 were read. Its Synopsis residue discrepancy
is explicit. Reporter processing, maturation and localization are not
interchangeable measures of complete cargo destruction. Actual figures and
supplements remain uninspected. The 2026 autophagy-independent vacuolar
turnover finding is not generalized to every condition. Natural-strain
provenance and native protein accessions remain unverified; no canonical
examples or protein-level graph is added. Two OPEN discussions retain
these limits and the qualified mapping/IBophagy questions.

## Relationship to v521

The TSV copies the corrected `METPO:1059100` autophagy context from v521
unchanged. It is dependency context, not another allocation. The parent YAML
and historical proposals remain unchanged. v519 corrected the former
cytoplasmic-only parent definition under #1754; the superseded wording is
not reintroduced when combining cohorts.

The writer defaults to dry run and guards the complete parent semantic
preimage plus the full v521 template hash. It rejects existing target or
proposal drift and validates the record before production writes. It never
writes the parent or older template. Tests use isolated preimages and
distinct fixture hashes while retaining production-guard checks.

## ID Space and Files

Reserve `METPO:1059900` in fresh block 1059900-1059999, following v521.
Local identifier: `traitmech:000646`; subset: `metpo_traitmech_2026_10`.
Current upstream contract and templates were retrieved at
`1408e7099d039026d7611c240938d8e177753406`. The class header has 11 columns;
the canonical property header has 13. CommunityMech v1's three reference
files were read end-to-end. Local, CommunityMech and pinned upstream
checks found no candidate/block collision. METPO IRIs use w3id, not legacy
OBO METPO stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The production writer dry run and 43 focused tests passed before applying
the record. The full suite passed 2,726 tests with two dependency warnings;
a separate generated-artifact suite passed 45 tests. All four scientific-
abstract snippets passed the maintained resolver as VERIFIED. LinkML,
strict validation, history, products, QC, Ruff, proposal verification and
ROBOT validation passed. Both graph grounders made no changes. The
canonical-example audit passed offline; live NCBI taxonomy resolution was
not run, and no examples changed.

Artifact checks confirmed all 1,040 existing YAML records and historical
proposal TSVs unchanged. Existing trait-page bodies are unchanged except
for the parent's new child link; other page churn is footer count/coverage
regeneration. RDF checks confirmed the w3id child-parent ancestry and the
single corrected parent definition. Browser checks and inspected screenshots
at 1,440 and 390 pixels confirmed readable pages, evidence, discussions,
parent navigation and the dashboard, without overflow or page errors.

Embedding coordinates were not regenerated because both configured input
files are absent. Coverage falls from 45.9% to 45.8% as the record denominator
increases. Staged PR sanity passed. Whitespace checking passed except for
the canonical ROBOT directive row's three required empty trailing cells;
that TSV also passed with only blank-at-EOL checking disabled.

## Upstream and Round Trip

Submit the child plus unchanged corrected parent context and scope notes
to upstream METPO after review. After acceptance, refresh the ontology,
migrate local identity and parent references to accepted identifiers while
preserving the local identifier's provenance and history, and regenerate
derived products without creating duplicate records. Upstream minting does
not resolve the independent scientific discussions. No separate upstream
issue has been opened by this branch.

## Change Log

- v522, 2026-10-06: propose microbial aggrephagy with four source-matched
  snippets, selective macroautophagy scope and explicit IBophagy limits.
