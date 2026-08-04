# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** urease activity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000077
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces urease, which hydrolyzes urea to ammonia and carbon dioxide, typically raising local pH; it is the basis of the diagnostic urease test.
- **Parent traits:** METPO:1000059
- **Synonyms:** urease-positive
- **Existing evidence:** DOI:10.1128/mr.59.3.451-480.1995:  (Mobley, Island & Hausinger review the molecular biology of microbial ureases that hydrolyze urea to ammonia and carbon dioxide.) | DOI:10.1128/mr.53.1.85-108.1989:  (Mobley & Hausinger review the significance and regulation of microbial ureases.)
- **Existing causal graph summary:** urease_activity_urea_hydrolysis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **urease activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/urease_activity.yaml`.

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
**Generated:** 2026-08-04T12:12:38.225087

1. nim2019thematurationpathway pages 1-3
2. burne2000bacterialureasesin pages 4-6
3. stabnikov2024microbialproducerof pages 1-3
4. farrugia2013biosynthesisofthe pages 1-1
5. nim2019thematurationpathway pages 8-10
6. szczerbiec2024antibacterialpropertiesand pages 5-7
7. szczerbiec2024antibacterialpropertiesand pages 1-2
8. szczerbiec2024antibacterialpropertiesand pages 7-8
9. szczerbiec2024antibacterialpropertiesand pages 8-11
10. szczerbiec2024antibacterialpropertiesand pages 2-3
11. 10.3390/inorganics7070085
12. 10.1074/jbc.R112.446526
13. 10.1016/S1286-4579(00)00312-9
14. 10.1038/s41598-024-51323-0
15. 10.24263/2304-974X-2024-13-2-10
16. 10.1128/MR.53.1.85-108.1989
17. 10.1128/MR.59.3.451-480.1995
18. https://doi.org/10.3390/inorganics7070085
19. https://doi.org/10.1074/jbc.R112.446526
20. https://doi.org/10.1016/S1286-4579(00
21. https://doi.org/10.1038/s41598-024-51323-0
22. https://doi.org/10.24263/2304-974X-2024-13-2-10
23. https://doi.org/10.1128/MR.53.1.85-108.1989
24. https://doi.org/10.1128/MR.59.3.451-480.1995
25. https://doi.org/10.3390/inorganics7070085,
26. https://doi.org/10.1074/jbc.r112.446526,
27. https://doi.org/10.1016/s1286-4579(00
28. https://doi.org/10.1038/s41598-024-51323-0,
29. https://doi.org/10.24263/2304-974x-2024-13-2-10,