# Galvanotropism: METPO Proposal v472

## Context

TraitMech mints `traitmech:000595 galvanotropism` as a PROPOSED PHYSIOLOGY
class for electric-field-directed growth. Primary bacterial and fungal
studies support the trait without imposing a single electrode preference.

A fresh seed contained 399 identifiers: 344 present and 55 absent in the
pre-change 989-record corpus. Both frozen release-review tables and the
active-review narrative were checked against live records. The remaining
seed absences are supporting-field vocabulary or reviewed duplicates, not
an automatic addition queue. Structured OWL search found no exact
galvanotropism or electric-field growth class. Whole-repo searches included
ignored and hidden files, lexical variants, citations, local identifiers
and the entire proposed block. Earlier galvanotropism mentions are context
in thigmotropism, not an ungrounded exact node, synonym or mapping TODO.
No existing curated record requires replacement or repair. The all-state
upstream METPO issue search returned no galvanotropism entry.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the identity. No predicate or schema enum is lifted.

## Hierarchy And Boundaries

The pinned OWL resolves `METPO:1000059` to phenotype, below quality
(`METPO:1000188`). No narrower exact parent was identified. Growth
orientation does not entail whole-cell locomotion. Existing
`traitmech:000581 galvanotaxis` is a motile phenotype, whereas
`traitmech:000594 thigmotropism` is contact-directed polarized growth.
Neither is an exact duplicate or appropriate parent.

Passive displacement, bending, alignment and altered growth rates alone
do not establish galvanotropism. Electron uptake and current production
are different traits. QuickGO's galvanotropism search returned zero hits
on 2026-10-04, not proof that every external ontology lacks an equivalent.
No exact xref, SSSOM alignment or synonym is asserted. Electrotropism as a
lexical variant remains a separate authority/scope question.

## Evidence And Limits

- Rajnicek et al., DOI:10.1128/jb.176.3.702-713.1994, PMID:8300526,
  PMCID:PMC205108: the abstract defines the phenomenon and reports bacterial
  anodal curvature, polarity reversal and controls for passive bending and
  medium gradients. Its historical actin-absence premise is not adopted.
- Crombie et al., DOI:10.1099/00221287-136-2-311, PMID:2182770:
  the abstract reports cathodal growth of attached Candida albicans germ
  tubes. Field effects on emergence timing and extension rate are kept
  separate from directional growth.
- Brand et al., DOI:10.1016/j.cub.2006.12.043, PMID:17275302,
  PMCID:PMC1885950: full text, Figs. 1 and 2 and the supplement were
  inspected. Germ-tube emergence and later tip orientation differ in their
  calcium-related perturbation responses. The snippet is an exact full-text
  paragraph span, not an abstract quotation. Supplementary Table S1 and
  methods identify CAI4/CIp10 (NGY152) as the engineered isogenic control;
  no natural canonical exemplar is inferred.

The first two studies were checked at abstract level only. All three
sources have contiguous snippets of at most 25 words. The full-text snippet
requires direct source verification because the maintained resolver checks
abstracts. No protein accession, taxon ID or causal graph is inferred.
Two OPEN discussions retain field/growth boundaries and natural-strain,
stage-specific mechanism and accession-grounding work. Human curation is
still required for promotion from PROPOSED.

## ID Space And Artifacts

Reserve `METPO:1054900` in block 1054900-1054999, following v471's
1054800-1054899 block. Ignored-and-hidden collision searches found the new
block unoccupied; CommunityMech v1 ranges are disjoint. The live identifier
remains `traitmech:000595`. Subset: `metpo_traitmech_2026_10`.

The class TSV has one row and the canonical 11-column two-row header,
including three empty trailing ROBOT directive cells. Property and SSSOM
files are omitted because no property or verified alignment is proposed.

## Verification

Seven writer tests pass, covering scope, source limits, TSV parity, dry run,
idempotent application, schema rejection and preimage-drift refusal. Full
pytest passed 1,965 tests with two dependency warnings in 1006.57s; all 45
artifact/priority tests passed in 521.81s. Direct LinkML/strict validation,
full QC, history (1,026 records), products, Biolink coverage, graph-artifact
verification and ROBOT/ELK passed. Both merged and reasoned RDF retain the
actual labeled w3id phenotype-to-quality hierarchy without legacy stubs.

The live resolver reports two VERIFIED abstract quotes and one
NOT_IN_ABSTRACT. Direct raw-source checks confirm all three snippets,
including the full-text paragraph span. No NCBI identity was resolved in
the offline canonical audit; no example was added.

Desktop/mobile rendering passed at 1440px and 390px, with correct local-ID
provenance, three evidence items, no page errors or document overflow, and
a loaded coverage image. Screenshots were visually inspected. Of 989
existing trait pages, 988 have only record-count footer changes; phenotype
also adds the child link and changes its child count from 112 to 113.
Both configured embedding sources were absent, so embeddings were not
regenerated. The protected source YAML is unchanged; ROBOT scratch outputs
remain untracked.

The add-trait skill now explicitly distinguishes establishment from
maintenance readouts when a perturbation affects them differently.

## Upstream And Round Trip

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. The reserved placeholder is not a released METPO term.
After upstream acceptance, refresh the ontology and seed a temporary tree;
migrate to the accepted CURIE, retain the local identifier in traceability
metadata, and reconcile references and proposal status in a reviewed change.

## Change Log

- v472, 2026-10-04: one evidence-backed galvanotropism class, curated by codex.
