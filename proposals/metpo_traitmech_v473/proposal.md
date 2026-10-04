# Durotaxis: METPO Proposal v473

## Context

TraitMech mints `traitmech:000596 durotaxis` as a PROPOSED PHYSIOLOGY
class for directional active migration in a substrate stiffness gradient. Independent studies
in Dictyostelium and Physarum support microbial applicability.

A fresh seed emitted 399 identifiers: 344 present and 55 absent from the
pre-change 990-record corpus. Both frozen release-review tables and the
active-review narrative were checked against live records. The 55 absences
comprise 38 supporting-field terms and 17 reviewed duplicates, not an
automatic addition queue. Structured OWL search found no exact durotaxis,
mechanotaxis, stiffness or rigidity term. Whole-repository searches included
ignored and hidden files, lexical variants, citations, identifiers and the
entire reserved block. Existing mentions are research leads under motile
and a contrast with thigmotropism, not an exact synonym, ungrounded causal
node or parent-gap discussion requiring repair. No existing curated YAML
is changed. The all-state upstream METPO issue search returned no durotaxis
entry.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or schema enum is lifted.

## Hierarchy And Boundaries

The pinned OWL resolves `METPO:1000702` to motile, below motility
(`METPO:1000701`). Directional active migration entails motility;
contact-guided polarized growth in `traitmech:000594 thigmotropism` does not
define this trait. Following review issue #1669, the definition is
polarity-neutral, consistent with primary terminology distinguishing positive
and negative durotaxis. Both microbial studies report stiff-side migration;
no opposite microbial response is inferred. Neither every microbe nor every
response to mechanics is asserted to exhibit durotaxis.

Speed changes, passive displacement and differential growth alone are
insufficient. Friction gradients, topography and remote substrate deformation
must not be substituted for measured stiffness-directed migration.
Mechanotaxis is broader, not an exact synonym. QuickGO's durotaxis search
returned zero hits on 2026-10-04; that is not exhaustive absence across
ontologies. No synonym, xref or SSSOM alignment is asserted.

## Evidence And Limits

- Kang et al., DOI:10.7554/eLife.96821, PMID:39671466, PMCID:PMC11643633:
  the inspected full text is the 2024-12-13 Version of Record, version 4
  (https://doi.org/10.7554/eLife.96821.4). The exact snippet comes from
  Results, "Amoeboid durotaxis is evolutionarily conserved". Figure 4,
  not Figure 6, contains the Dictyostelium experiments. Visual inspection
  confirms greater directional migration on gradient versus uniform gels,
  with no significant speed difference. Pharmacological effects on both
  direction and speed do not isolate a stiffness sensor. Supplementary
  file 1 contains simulation parameters; the MDAR checklist refers back
  to cell-culture methods. Both supplement documents were inspected as
  structured OOXML; their layout was not rendered. No mathematical symbol
  is quoted from them. The paper's mammalian NMIIA experiments are not
  microbial accession-level evidence.
- Filipinas and Confesor, DOI:10.1088/1361-6463/adb6b8, published online
  2025-02-27: the publisher-deposited Crossref abstract reports directed
  Physarum polycephalum plasmodial-node migration on agar stiffness
  gradients. Its snippet was exact-matched to that deposited abstract.
  Full methods, figures and supplements were not inspected. The gradient
  controls, strain identity and migration/growth distinction remain open.
- Isomursu et al., DOI:10.1038/s41563-022-01294-2, PMID:35817964,
  published 2022-07-11: the final abstract sentence explicitly distinguishes
  positive and negative durotaxis. Its exact snippet was checked against
  the Europe PMC MED abstract; publisher wording corroborates the polarity
  usage. This is mammalian terminology evidence only, not an additional
  microbial observation or a transferable microbial mechanism. Full methods,
  figures and supplements were not inspected for this scope check.

Each of the three evidence citations has a contiguous snippet under 25 words.
Kang's culture-method citation, DOI:10.3389/fcell.2022.835185, was also
inspected: it describes Ax2-derived cells and expression constructs but
does not uniquely identify Kang's assayed cells. It is provenance context,
not a third independent demonstration of durotaxis. No canonical taxon,
protein accession or causal graph is inferred. Two OPEN discussions retain
the boundary, strain and mechanistic-grounding questions. Human review is
required before promotion from PROPOSED.

## ID Space And Artifacts

Reserve `METPO:1055000` in block 1055000-1055099, following v472's
1054900-1054999 block. Ignored-and-hidden collision searches found the new
block unoccupied; CommunityMech v1 ranges are disjoint. The live identity
remains `traitmech:000596`. Subset: `metpo_traitmech_2026_10`.

The class TSV contains one row and the canonical 11-column two-row header,
including three empty trailing ROBOT directive cells. Property and SSSOM
files are omitted because no property or verified alignment is proposed.

## Verification

Eight focused writer tests pass after the polarity correction, covering
identity and source boundaries, TSV parity, dry run, idempotent replay,
schema rejection, exact reviewed-preimage upgrade and preimage-drift refusal.
Before that correction, full pytest passed 1,972 tests with two dependency warnings in
1100.67s; all 45 artifact/priority tests passed in 656.14s. Direct LinkML,
strict validation, full QC, history (1,027 records), products, proposal
coverage, Biolink coverage and graph-artifact verification passed. QC
retains existing baselined findings and two source-license warnings, with
no new blocking findings.

ROBOT/ELK passed with no UNSAT; merged/reasoned outputs have 23,322/23,326
lines and 12,628/12,632 RDF triples. Both use the real labeled w3id motile
parent and its motility ancestor, without legacy METPO stubs. The TSV header
matches the canonical upstream 11-column header, including empty cells.

The microbial snippets were exact-matched to raw source text: Kang's full JATS
paragraph and the publisher-deposited Crossref abstract. The maintained
abstract resolver reports NOT_IN_ABSTRACT and UNRESOLVED, respectively;
these are not relabeled VERIFIED. An exact quoted-DOI Europe PMC query
returned zero Physarum results, while Crossref resolves the citation.
Offline canonical auditing skipped NCBI identity resolution; no canonical
example was added.

Before the correction, desktop/mobile rendering passed at 1440px and 390px with correct local-ID
provenance, two evidence items, no page errors or document overflow, and a
loaded dashboard coverage image. Screenshots were visually inspected.
All 990 existing pages were compared: 989 footer-only changes, plus the
motile child link/count (19 to 20). Both configured embedding sources were
absent, so embeddings were not regenerated. Protected source YAML remains
unchanged and ROBOT scratch outputs remain untracked.

## Upstream And Round Trip

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. The reserved placeholder is not a released METPO term.
After acceptance, refresh the ontology and seed a temporary tree; migrate
to the accepted CURIE, retain the local identifier in traceability metadata,
and reconcile references and proposal status in a reviewed change.

## Change Log

- v473, 2026-10-04: one evidence-backed durotaxis class, curated by codex.
- Review correction #1669: polarity-neutral definition and bounded terminology
  citation; the original two microbial observations remain stiff-side only.
  The writer retains the initial curation event and appends the correction,
  accepting only the exact reviewed record/proposal preimages or current output.
  Post-correction full pytest passed 1,973 tests with two dependency warnings
  in 888.89s; full QC exited 0 with no new blocking findings. LinkML, strict
  validation, history (1,028 valid), proposal verification and ROBOT/ELK pass.
  All three snippets match raw source text; the new abstract quote is VERIFIED
  by the maintained resolver, without relabeling the two earlier verdicts.
  The reasoned ontology retains the real w3id motile hierarchy and matches the
  polarity-neutral definition. Desktop/mobile browser checks and visual
  screenshot review passed again with three evidence items. Regeneration
  leaves the coverage image and priority outputs unchanged; the published
  dashboard and listing-page timestamps reflect the correction event.
