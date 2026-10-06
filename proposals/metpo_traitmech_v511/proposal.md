# Pinocytosis: METPO Proposal v511

## Context

Add `traitmech:000635 pinocytosis`, a PROPOSED PHYSIOLOGY class for
vesicular uptake of surrounding fluid by a microbial organism. This is
an organismal phenotype, not a sequence feature or host-cell response.
Base: `a43f95d63ab2659c1bfaa80966ec6874d8a783d2`.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
covered pinocytosis/pinocytotic, cell drinking, endocytosis, fluid-uptake
variants, source identifiers, the local ID and prospective METPO block.
Existing macropinocytosis and phagocytosis scope contrasts, myzocytosis's
endocytosis discussion and raw Biolink process terminology are not an
exact primary record. All-state TraitMech and METPO PR searches found
no pinocytosis or 1058800 proposal. No exact record or reservation was found.

A fresh seed contains 399 records, sharing 344 IDs with the 1,029-record
pre-addition corpus. All 55 absent IDs reconcile to 38 supporting-field
terms and 17 reviewed duplicates. The complete 1,546-row release delta
and 153-row active review were parsed; all 38 formerly unselected
classes are live. All 12,617 pinned METPO triples were searched for
pinocytosis/cell-drinking/fluid-phase-endocytosis terms and the prospective
block, with no match. This does not establish literature exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Pinocytosis requires fluid internalization into membrane-bound compartments;
transport across the membrane, surface adsorption, open invaginations and
membrane recycling alone are insufficient. No fixed vesicle size, ruffle,
nutritional requirement, rate or universally nonconcentrative mechanism
is imposed. Particle engulfment, nutritional phagotrophy and prey-content
aspiration remain distinct concepts, without organismal disjointness axioms.
No synonyms, process-level equivalence, protein accessions or causal graph
are asserted. Phenotype remains the parent pending a broader hierarchy.

The definition of macropinocytosis `traitmech:000634` entails this broader
phenotype. Its direct local parent becomes `traitmech:000635`; the temporary
parent-gap discussion is resolved with its historical rationale preserved.
Its definition, evidence, DdB example, other discussion and prior history
are unchanged. This is a definition-based hierarchy inference, not a new
experimental claim about the child.

**Additional upstream axiom on adoption:**
`METPO:1058700 SubClassOf METPO:1058800`.
The v510 `METPO:1000059` superclass is still true and is preserved in that
historical cohort. Following v447/v449, the old ID is not re-emitted in the
new reservation template; the child refinement is an explicit upstream
curation request, not an axiom emitted by the v511-only ROBOT template.

## Evidence and Example

- `DOI:10.1083/jcb.53.3.681`, `PMID:5028259`, `PMC2108769`:
  Bowers and Olszewski (1972), definition authority. The 17-word scientific
  Abstract snippet is exact. Introduction, Methods, Results and Discussion
  were read from full-text OCR in the authoritative Europe PMC XML:
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2108769/fullTextXML.
  Tracer uptake and author-reported intracellular HRP support fluid uptake
  in Neff cells. The PDF/figures were unavailable and were not visually
  audited. Nonrandom vesicle sampling, estimated membrane turnover, tracer
  loss/metabolism and uncertain uptake routes limit interpretation.
- `DOI:10.1099/00221287-92-2-246`, `PMID:1255130`:
  Chambers and Thompson (1976), independent experimental study. The 12-word
  scientific Abstract snippet was read at the publisher and in NCBI PubMed
  XML. Stationary-phase inulin uptake decreases while bead phagocytosis
  essentially ceases. Full text and figures were unavailable; no unread
  methods, strain accession or native protein is inferred.
  https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-92-2-246

Both studies concern Acanthamoeba, not independent taxon replication. HRP
is an external tracer, not a native microbial protein. Respiratory-inhibitor
sensitivity does not identify a molecular dependency. Nonconcentrative
uptake in the first study is not imposed on the entire trait.

The canonical example is strain-qualified Neff, not either species as a
whole. NCBI EFetch verified `NCBITaxon:1257118`, strain rank and exact label
`Acanthamoeba castellanii str. Neff` on 2026-10-06. ATCC documents Neff's
soil origin in Pacific Grove, California: https://www.atcc.org/products/30010.
The 1972 paper supplies no collection accession. This does not establish
vial/genome identity with ATCC 30010 or an unchanged wild isolate.

An OPEN discussion records the authority-name conflict with the 2024 transfer
of Neff to A. terricola: `DOI:10.1016/j.ejop.2024.126091`, `PMID:38772052`.
Its 20-word scientific Abstract snippet was directly checked in NCBI PubMed
XML; the full phylogenetic data were not audited. This is taxonomy evidence,
not a third pinocytosis experiment. The issuing-authority strain label is
retained with this qualification, without silent species reassignment.

## ID Space and Files

Reserve `METPO:1058800` in 1058800-1058899, following v510's 1058700
block. Local identifier: `traitmech:000635`; subset:
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

Definition provenance combines the local minting record and both experimental
DOIs. Both header rows retain 11 cells, including required trailing tabs.

## Verification

The guarded dry run and 26 focused tests passed before application. Tests
cover scope, source limits, taxonomy, proposal consistency, coupled changes,
unchanged child evidence/history, dry-run immutability, exact replay,
prevalidation and drift refusal. Each touched TraitRecord receives its own
curation event and append-only repository history. Broader validation and
exact-head CI outcomes will be recorded in the PR receipt; no unrun check
is claimed passed here.

- Direct LinkML and strict checks passed for both records. All three
  snippets returned `VERIFIED`, similarity 1.00, separately confirmed as
  scientific-abstract spans. The live taxonomy audit resolved 727 examples
  across 542 records, with zero errors and 24 existing name-drift warnings.
- Proposal verification and ROBOT/ELK passed. Parsed RDF measured 15
  triples in classes.owl, 12,628 in merged.owl and 12,632 in reasoned.owl.
  The new w3id class points to labeled phenotype and its quality parent;
  there are no legacy purl METPO stubs. All 635 local IDs have proposal
  coverage and all 515 PROPOSED records meet the two-citation gate.
- Maintained generators produced 1,030 trait pages, 562 discussions
  across 501 records, and a 1,030-record QC dashboard with no failing
  slots. All 139 reviewed claw source files match their archive.
  All 1,027 non-coupled existing trait pages changed only in footers;
  phenotype exchanged the old direct child for pinocytosis. No existing
  priority row changed; the new row has one child. Shared browser/dashboard
  navigation and accessibility templates are unchanged.
- Chromium checks at 1440 and 390 pixels passed identity, experimental
  quotes, qualified example, child resolution, hierarchy round trip,
  dashboard counts/image loading and overflow checks, without page errors.
  Screenshots were inspected. Both exact embedding source paths are absent,
  so embedding artifacts were not regenerated.
- Semantic comparison confirms that the child's definition, evidence,
  example, other discussion and prior history are preserved. The v510
  template and protected spore-germination record are byte-identical to base.
- The complete local pipeline exited zero: `just qc`, history/products,
  Ruff and all 2,380 tests passed (two dependency deprecation warnings;
  pytest 700.32 seconds). Strict corpus validation found zero errors across
  1,030 records; existing graph/snippet findings remain fully baselined
  with zero new or blocking findings. Exact-head CI is recorded separately.
- Ordinary staged whitespace checking flags only the ROBOT directive row's
  three required trailing tabs. All rows parse as 11 cells; normal checks
  elsewhere and the documented exact-TSV exception pass. No global Git
  whitespace setting was changed.

## Upstream and Round Trip

Submit the cohort and explicit child axiom to METPO review after TraitMech
signoff. After upstream acceptance, refresh the pinned ontology, migrate
the local ID and references to the accepted term, retain minting provenance
and append-only history, and regenerate without a duplicate primary record.
Pinocytosis scope/hierarchy, taxonomy and native mechanism remain OPEN;
PROPOSED status awaits human curator signoff. The child's separate native
mechanism discussion also remains OPEN.

## Change Log

- v511, 2026-10-06: propose pinocytosis with two DOI-backed experimental
  snippets, a qualified Neff example and the macropinocytosis parent refinement.
