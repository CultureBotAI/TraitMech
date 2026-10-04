# Chemotropism: METPO Proposal v474

## Context

TraitMech mints `traitmech:000597 chemotropism` as a PROPOSED PHYSIOLOGY
class for chemical-gradient-directed polarized growth. It is distinct from
the existing chemotaxis, thigmotropism and galvanotropism records.

A fresh temporary seed emitted 399 identifiers, 344 present and 55 absent
from the pre-change 991-record corpus. Both frozen release-review tables
and their narrative were checked against live records. The remaining
absences are 38 supporting-field terms and 17 reviewed duplicates, not an
automatic addition queue. Structured OWL inspection found chemotrophic
energy-source terms but no chemotropism term. The whole-repository novelty
search included ignored and hidden files, synonyms, citations and IDs.
The only exact chemical-growth mention is contrasting evidence in the
thigmotropism record and its derived copies; it is not an unresolved node,
synonym or parent-gap TODO. No older trait YAML needs changing. An all-state
upstream METPO issue search returned no chemotropism entry.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new local identity. No predicates or schema enums are
lifted. This is a reusable phenotype, not a substrate-use pair or gene.

## Hierarchy And Boundaries

`METPO:1000059` resolves in the pinned OWL to phenotype, below
`METPO:1000188`. Growth orientation does not entail whole-cell locomotion,
so motile is not an appropriate parent. The definition is polarity-neutral:
toward and away responses are both within scope. Growth-rate or biomass
differences alone are insufficient. No unverified synonym, xref or SSSOM
alignment is asserted; the two OPEN discussions retain source, strain and
mechanistic-grounding limitations. Human signoff is required before promotion
from PROPOSED.

## Evidence And Access

The record carries two primary sources, each with a contiguous full-text
snippet: DOI:10.1371/journal.pbio.3002726 (PMID:39078817, PMC11288418)
and DOI:10.1038/s41598-020-67597-z (PMID:32612109, PMC7329813).
Evidence notes identify the inspected passages and limits. Aspergillus
Figure 3 and the S1 strain-table PDF were visually inspected; the stable
supplement DOI is `10.1371/journal.pbio.3002726.s002`. Other supplements
and movies were not inspected, nor were the Fusarium figures visually
inspected. No natural canonical strain, protein accession or causal graph
is inferred from laboratory-strain labels or ungrounded mechanisms.

Raw JATS substring checks confirm both snippets (18 and 20 words). The
first check caught an omitted figure pointer in the uncommitted draft (#1670);
the guarded writer restores it and retains a correction event. The
maintained abstract resolver returns NOT_IN_ABSTRACT for both full-text
quotes. These verdicts are not relabeled VERIFIED.

## ID Space And Files

Reserve `METPO:1055100` in block 1055100-1055199, following v473's
1055000-1055099 block. Ignored-and-hidden collision searches found no
identifier or block use; numeric hits in a git timestamp and certificate
bytes were unrelated. The block is disjoint from CommunityMech v1.
The live identity remains `traitmech:000597`, not the proposed METPO
placeholder. Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Property and SSSOM files are omitted because neither is proposed. The
11-column class header matches the canonical upstream template, including
empty trailing directive cells. Upstream guidance was read from the verified
`master` branch because the older local KG-Microbe checkout lacks it. The
TraitMech wrapper's real `https://w3id.org/metpo/` prefix supersedes the
legacy prefix in that upstream example.

## Verification

Eight focused writer tests pass: identity/polarity, evidence limits, TSV
parity, dry run and replay, record/proposal drift refusal, schema rejection,
and exact-draft correction with history preservation. Full pytest passed
1,981 tests with two dependency warnings in 1037.43s; all 45 README,
priority and QC-dashboard artifact tests passed in 441.54s. Full QC exited
zero with no new blocking findings and two existing ENIGMA source-license
warnings. LinkML, strict corpus validation, history (1,029 valid), products,
proposal verification/coverage, Biolink coverage and graph-artifact
verification passed. Canonical auditing checked shape only; NCBI resolution
was skipped and no canonical example was added.

ROBOT/ELK passed without UNSAT. The reasoned graph has 12,632 triples and
the exact new definition, with the real labeled w3id phenotype parent and
its quality ancestor, not a legacy METPO stub. Merged/reasoned OWL has
23,322/23,326 lines. ROBOT scratch artifacts remain ignored.

Desktop/mobile browser checks at 1440px and 390px passed with two evidence
items, zero canonical examples, correct local-ID provenance, no page errors
or document overflow, and a loaded dashboard image. Screenshots were
visually inspected. Comparing all 991 older trait pages found 990 footer-only
changes and the phenotype child link/count update (113 to 114). Existing
source YAMLs, including the protected record, are unchanged. Both exact
configured embedding sources were absent, so embeddings were not regenerated.
The shared generator's 139 source files matched the reviewed claw archive
before dashboard/discussion regeneration.

## Upstream And Round Trip

After review, submit the TSV to berkeleybop/metpo or the KG-Microbe proposal
pipeline. This reserved placeholder is not a released ontology term.
After acceptance, refresh the ontology, seed a temporary tree, migrate
to the accepted CURIE, retain the local ID in traceability metadata, and
reconcile references and proposal status in a reviewed change.

## Change Log

- v474, 2026-10-04: one chemical-directed growth class, curated by codex;
  guarded snippet correction and add-trait guidance on growth controls and
  contradictory summaries included before PR submission.
