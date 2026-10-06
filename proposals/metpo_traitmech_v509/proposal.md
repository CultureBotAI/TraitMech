# Trogocytosis: METPO Proposal v509

## Context

Add `traitmech:000633 trogocytosis`, a PROPOSED PHYSIOLOGY class for a
microbe taking discrete portions of another living cell during contact.
This is an organismal phenotype, not a literal sequence feature or a host
immune cell's attack on the microbe.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
covered trogocytosis, cell nibbling, both DOIs, the local identifier and
the entire prospective METPO block. The existing myzocytosis discussion
contains a source-attributed contrast, not an exact unresolved node.
No exact record, prior proposal or ID collision was found. All-state
TraitMech/METPO PR searches found no trogocytosis or 1058600 reservation.
The pre-addition base is `411f7fc8f3fb117b6f264fcaaf0af863373a37c1`.

A fresh seed contains 399 records, sharing 344 IDs with the 1,027-record
live corpus. All 55 absent IDs reconcile to 38 supporting-field terms
and 17 reviewed duplicates. The complete 1,546-row release delta and
153-row active review were parsed; all 38 formerly unselected classes
are live. All 12,617 pinned METPO triples were inspected programmatically
for the candidate and reserved block, with no matches. This does not
establish exhaustion of the microbial trait literature.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Retain phenotype pending a closer uptake hierarchy. Phagocytosis
`traitmech:000627` includes particle enclosure and internalization;
phagotrophy `traitmech:000628` additionally requires nutrition.
Myzocytosis `traitmech:000631` is prey-content aspiration through a
localized connection; pallium feeding `traitmech:000632` uses a feeding
veil. The source's whole-cell phagocytosis contrast is operational and
does not establish disjoint organismal capabilities or a complete hierarchy.
Existing YAML requires no exact-mention repair.

Do not require killing, nutrition, serum protection, a human target or
a fixed fragment size. No exact synonyms, ontology xrefs, protein
accessions, SSSOM equivalences or causal graph are asserted.

## Evidence and Example

- `DOI:10.1038/nature13242`, `PMID:24717428`, `PMC4006097`: definition
  authority. The snippet is from the final scientific Abstract, directly
  checked at Nature/PubMed, not the differently worded author manuscript.
  The PMC manuscript's Results/Discussion, relevant Methods and actual
  Figures 1-2 were inspected. Other figures and movies were not visually
  audited. https://pubmed.ncbi.nlm.nih.gov/24717428/
- `DOI:10.1128/mBio.00068-19`, `PMID:31040235`, `PMC6495370`: follow-up
  evidence. The snippet is from the scientific Abstract, not the distinct
  Importance/precis block. Relevant Results, cell-culture Methods,
  Discussion and actual Figures 1, 6 and 8 were inspected. Remaining
  figures and supplements were not visually audited.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6495370/

The two papers are not independent taxon replication. The canonical
example is species-level `NCBITaxon:5759 Entamoeba histolytica`, qualified
to parental HM1:IMSS cultures in the 2019 study. NCBI ESearch/EFetch
verified its name and rank. The paper names ATCC but no catalog/lot number;
https://www.atcc.org/products/30459 documents the matching strain's natural
clinical provenance, not an exact experimental lot or clone. Engineered
knockdowns and vector controls are not the canonical example.

## ID Space and Files

Reserve `METPO:1058600` in 1058600-1058699, following v508's 1058500 block.
The next local identifier is `traitmech:000633`; subset is
`metpo_traitmech_2026_10`. The kg-microbe contract and template headers
were read at `1408e7099d039026d7611c240938d8e177753406`. The class template
has 11 columns; the upstream 13-column property template does not affect
this class-only cohort. CommunityMech v1's class/property blocks do not
overlap. Use the pinned ontology's w3id METPO namespace.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

Definition provenance combines the local minting record and both DOIs,
not ontology mappings. Both header rows preserve 11 cells.

## Verification

The guarded writer dry run and 12 focused tests passed before application.
The tests cover dry-run immutability, exact replay, parent preservation,
preimage drift refusal, source scope and proposal consistency.

- LinkML and strict validation passed for the new record; corpus strict
  validation found zero errors across 1,028 records. `just qc`,
  `just validate-history`, `just validate-products` and Ruff passed.
  The full-suite outcome is reported in the PR validation receipt.
- Both snippets returned `VERIFIED` with similarity 1.00. Direct section
  checks independently identify them as scientific-abstract quotes.
  The NCBI audit resolved 725 examples across 540 records, with zero
  errors and 24 existing label-drift warnings.
- Proposal verification and ROBOT/ELK passed. RDF parsing measured 15
  triples in classes.owl, 12,628 in merged.owl and 12,632 in reasoned.owl.
  The new w3id class has phenotype as its parent, preserving the pinned
  phenotype label and quality hierarchy without legacy METPO stubs.
- Graph findings remain 74 baselined, zero new or blocking; snippet
  findings remain 2,419 baselined, zero new or blocking. No baseline,
  existing trait, previous history or protected record was changed.
- Maintained generators produced 1,028 trait pages, 557 discussions,
  current priority data and a 1,028-record QC dashboard with no failing
  slots. The isolated reviewed claw source matched all 139 archive
  source files byte-for-byte. All 1,026 non-parent existing trait pages
  changed only in footer counts; phenotype additionally gained one
  child. Its child count (140 to 141) is the only changed existing
  priority row. The regenerated coverage image is included.
- Chromium checks at 1440 and 390 pixels passed identity, both snippets,
  qualified example, parent navigation, dashboard counts, image loading
  and document-overflow checks, with no page errors. Screenshots were
  inspected. Both exact configured embedding source paths are absent;
  embedding artifacts were not regenerated.
- Ordinary staged whitespace checking flags only the ROBOT directive
  row's three required trailing tabs. All rows parse as 11 cells. The
  documented exact-TSV exception and normal checks on other paths pass;
  no global Git whitespace setting was changed.

These checks do not replace exact-head review or the native merge queue.

## Upstream and Round Trip

Submit the cohort to METPO review after TraitMech signoff. After inclusion
in a release, refresh the pinned ontology, migrate the local identifier
and its references to the accepted METPO term, retain minting provenance
and append-only history, and regenerate artifacts without a duplicate
primary record. Uptake hierarchy and native molecular mechanism remain
open discussions. PROPOSED status awaits human curator signoff.

## Change Log

- v509, 2026-10-06: propose trogocytosis with two DOI-backed snippets
  and a natural-strain-qualified example.
