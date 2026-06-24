# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flask shaped
- **METPO identifier:** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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
**Generated:** 2026-06-18T07:56:05.550102

1. kysela2016diversitytakesshape pages 5-7
2. pohl2024adynamicbactofilin pages 1-2
3. pohl2024adynamicbactofilin pages 19-21
4. chen2025unravelingtherole pages 4-7
5. schwab2022characterizationofputative pages 7-10
6. schwab2022characterizationofputative pages 1-7
7. delaby2024phenotypicplasticityin pages 35-38
8. richter2023interactingbactofilinsimpact pages 1-2
9. delaby2025phenotypicplasticityin pages 10-10
10. schwab2022characterizationofputativea pages 7-10
11. delaby2025phenotypicplasticityin pages 1-2
12. richter2023interactingbactofilinsimpact pages 26-27
13. richter2023interactingbactofilinsimpact pages 15-16
14. https://doi.org/10.1186/s12866-025-04320-w
15. https://doi.org/10.1371/journal.pbio.1002565
16. https://doi.org/10.7554/elife.86577.2
17. https://doi.org/10.1371/journal.pgen.1010788
18. https://doi.org/10.1101/2024.11.07.622495
19. https://doi.org/10.1038/s41467-025-60005-y
20. https://doi.org/10.1186/s12866-025-04320-w,
21. https://doi.org/10.1371/journal.pbio.1002565,
22. https://doi.org/10.7554/elife.86577.2,
23. https://doi.org/10.1371/journal.pgen.1010788,
24. https://doi.org/10.1101/2024.11.07.622495,
25. https://doi.org/10.1038/s41467-025-60005-y,