# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** triangular shaped
- **METPO identifier:** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **triangular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/triangular_shaped.yaml`.

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
**Generated:** 2026-06-18T10:35:07.026884

1. gambelli2021thepolygonalcell pages 9-10
2. du2023evolutionarydevelopmentalbiology pages 7-14
3. schiller2024identificationofstructural pages 1-2
4. gambelli2021thepolygonalcell pages 13-14
5. schiller2024identificationofstructural pages 3-5
6. schiller2024identificationofstructural pages 6-7
7. gambelli2021thepolygonalcell pages 1-2
8. gambelli2021thepolygonalcell pages 10-11
9. bondocnaumovitz2023methodsandmeasures pages 8-9
10. du2023evolutionarydevelopmentalbiology pages 31-33
11. schiller2024identificationofstructural pages 9-9
12. du2023evolutionarydevelopmentalbiology pages 26-31
13. schiller2024identificationofstructural pages 11-12
14. https://doi.org/10.3389/fmicb.2021.766527
15. https://doi.org/10.1038/s41467-024-45196-0
16. https://doi.org/10.48617/etd.674
17. https://doi.org/10.3389/fmicb.2023.1270665
18. https://doi.org/10.3389/fmicb.2024.1474570
19. https://doi.org/10.48550/arxiv.2303.00068
20. https://doi.org/10.3389/fmicb.2023.1270665,
21. https://doi.org/10.48617/etd.674,
22. https://doi.org/10.1038/s41467-024-45196-0,
23. https://doi.org/10.3389/fmicb.2021.766527,
24. https://doi.org/10.3389/fmicb.2024.1474570,
25. https://doi.org/10.48550/arxiv.2303.00068,