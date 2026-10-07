# Macropinocytosis: METPO Proposal v510

## Context

Add `traitmech:000634 macropinocytosis`, a PROPOSED PHYSIOLOGY class
for microbial bulk-fluid uptake through membrane-ruffle closure. This
is an organismal capability, not a literal sequence feature, assay column
or host cell's response to a microbe.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
covered the label, macropinocytic/macropinosome variants, fluid-uptake
phrases, both DOIs/PMIDs, local ID and prospective METPO block. No exact
record or reservation was found. The phagocytosis discussion's broader
pinocytosis contrast does not require a same-scope repair. All-state PR
searches in TraitMech and METPO found no candidate or 1058700 proposal.
The base is `fb85fb13a1dd9d369577034447c788adba46d2bc`.

A fresh seed contains 399 records, sharing 344 IDs with the 1,028-record
pre-addition corpus. All 55 absent IDs reconcile to 38 supporting-field
terms and 17 reviewed duplicates. The complete 1,546-row release delta
and 153-row active review were parsed; all 38 formerly unselected
classes are live. All 12,617 pinned METPO triples were checked for the
candidate, endocytosis/pinocytosis hierarchy and prospective block.
No matching term or occupied block was found. This is not evidence that
the microbial trait literature is exhausted.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Retain phenotype pending a closer endocytic-capability hierarchy.
Phagocytosis `traitmech:000627`, phagotrophy `traitmech:000628` and
trogocytosis `traitmech:000633` differ in particle uptake, nutritional
assimilation and living-cell nibbling, respectively. These are not
asserted equivalent or disjoint. Generic pinocytosis is broader.

Ruffling alone, transporter-mediated solute entry and small-vesicle
uptake are insufficient. No fixed diameter, axenic-growth requirement,
enhanced rate or nutritional endpoint is asserted. No existing trait,
protein accession, synonym, process-level xref or causal graph is changed.

## Evidence and Example

- `DOI:10.1242/jcs.213736`, `PMID:29440238`, `PMC5897714`:
  definition authority, with a scientific ABSTRACT snippet. Relevant
  Results, Methods, Discussion and actual Figure 2 were inspected.
  The record preserves the P=0.057 formation-rate limit and distinguishes
  reporter-based diameters from dextran assays.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5897714/
- `DOI:10.7554/eLife.04940`, `PMID:25815683`, `PMC4374526`:
  Introduction snippet, not Abstract or eLife digest. Relevant Results,
  confocal Methods, Discussion, Table 2 and actual Figure 3 were read.
  The record distinguishes formation events from single-section images.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC4374526/

These papers share a group and organism; they are not independent taxon
replication. Other figures, movies and supplements were not visually
audited. The example is parental DdB, not axenic mutants or reporter
transformants. Species-level `NCBITaxon:44689 Dictyostelium discoideum`
was verified with NCBI EFetch. The primary genealogy source documents
laboratory selection and copy-number differences in this NC4-derived
clone, not an unchanged wild isolate:
https://link.springer.com/article/10.1186/gb-2008-9-4-r75.
This provenance-only source is not counted as independent trait evidence.

## ID Space and Files

Reserve `METPO:1058700` in 1058700-1058799, following v509's 1058600
block. Local identifier: `traitmech:000634`; subset:
`metpo_traitmech_2026_10`. The Knowledge-Graph-Hub/kg-microbe contract
and headers were read at `1408e7099d039026d7611c240938d8e177753406`.
Use its 11-column class template and the pinned ontology's w3id namespace,
not the old purl METPO example. The upstream 13-column property template
does not affect this class-only cohort. CommunityMech v1 does not overlap.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

Definition provenance combines the local minting record and both DOIs.
Both header rows preserve 11 cells, including the required trailing tabs.

## Verification

The guarded dry run and 12 focused tests passed before application.
Tests cover native-versus-mutant scope, quote sections, measurement limits,
proposal consistency, dry-run immutability, exact replay and drift refusal.
The append-only CREATE record accurately distinguishes these completed
checks from subsequent corpus, artifact and CI validation.

- LinkML and strict new-record validation passed. The taxonomy audit
  resolved 726 examples across 541 records with zero errors and 24
  existing label-drift warnings.
- `just qc`, `just validate-history`, `just validate-products` and Ruff
  passed. Corpus strict validation found zero errors across 1,029
  records; graph and snippet findings remain fully baselined with zero
  new or blocking findings.
- The 2018 abstract quote returned `VERIFIED`, similarity 1.00. The 2015
  Introduction quote returned `NOT_IN_ABSTRACT`, similarity 0.40;
  direct section-level matching independently confirmed its exact span.
  It is not relabeled as a resolver verification.
- Proposal verification and ROBOT/ELK passed. Parsed RDF measured 15
  triples in classes.owl, 12,628 in merged.owl and 12,632 in reasoned.owl.
  The w3id child/phenotype/quality hierarchy is intact, without legacy
  purl METPO stubs. All 634 local IDs have proposal coverage and all
  514 PROPOSED records pass the two-citation gate.
- Maintained generators produced 1,029 trait pages, 559 discussions
  across 500 records and a 1,029-record QC dashboard with no failing
  slots. All 139 reviewed claw source files match their archive.
  All 1,027 non-parent existing trait pages changed only in footers;
  phenotype gained one child, from 141 to 142. This child count is the
  sole changed existing priority row. The coverage image is included.
- Chromium checks at 1440 and 390 pixels passed identity, both quotes,
  qualified example, parent navigation, dashboard counts/image loading
  and document overflow checks, with no page errors. Screenshots were
  inspected. Both exact embedding source paths are absent, so embedding
  artifacts were not regenerated.
- Ordinary staged whitespace checking flags only the ROBOT directive
  row's three required trailing tabs. All rows parse as 11 cells; the
  documented exact-TSV exception and normal checks elsewhere pass.
  No global whitespace setting, existing trait, prior history, schema,
  baseline or protected record was changed.

The full local test suite and exact-head CI outcomes are recorded in the
PR validation receipt. No unrun check is claimed passed here.

## Upstream and Round Trip

Submit the cohort to METPO review after TraitMech signoff. After upstream
acceptance, refresh the pinned ontology, migrate this local identifier and
references to the accepted METPO term, retain minting provenance and
append-only history, and regenerate without a duplicate primary record.
Hierarchy and native molecular mechanism remain open discussions;
PROPOSED status awaits human curator signoff.

## Change Log

- v510, 2026-10-06: propose macropinocytosis with two source-checked
  DOI snippets and a parental DdB-qualified example.
