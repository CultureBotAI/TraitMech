# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory manganese reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.

**Provider:** falcon
**Generated:** 2026-08-04T06:04:42.345438

1. richter2012dissimilatoryreductionof pages 4-5
2. richter2012dissimilatoryreductionof pages 2-4
3. wunder2024manganesereductionand pages 6-7
4. beblawy2018extracellularreductionof pages 4-6
5. wunder2024manganesereductionand pages 3-4
6. wunder2024manganesereductionand pages 1-2
7. wunder2024manganesereductionand pages 4-6
8. wunder2024manganesereductionand pages 7-9
9. d
10. 10.1128/mr.55.2.259-287.1991
11. 10.3389/fmicb.2024.1398021
12. 10.1128/AEM.06803-11
13. 10.1111/mmi.14067
14. https://doi.org/10.1128/mr.55.2.259-287.1991
15. https://doi.org/10.3389/fmicb.2024.1398021
16. https://doi.org/10.1128/AEM.06803-11
17. https://doi.org/10.1111/mmi.14067
18. https://doi.org/10.1128/mr.55.2.259-287.1991,
19. https://doi.org/10.3389/fmicb.2024.1398021,
20. https://doi.org/10.1128/aem.06803-11,
21. https://doi.org/10.1111/mmi.14067,