# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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
**Generated:** 2026-08-04T09:12:31.700100

1. alexandre2025movementofbacteria pages 1-2
2. wheeler2024individualbacterialcells pages 1-2
3. nakamura2024structureanddynamics pages 1-3
4. hendrix2024plzrregulatestype pages 1-2
5. ohara2024surfacehydrophilicitypromotes pages 1-2
6. hendrix2024plzrregulatestype pages 2-3
7. nakamura2024structureanddynamics pages 12-14
8. nakamura2024structureanddynamics pages 6-8
9. matilla2023targetingmotilityand pages 1-2
10. antani2024reassessingthestandard pages 1-3
11. wong2021roadmaponemerging pages 48-49
12. nakamura2024structureanddynamics pages 3-4
13. https://doi.org/10.1128/aem.00246-25
14. https://doi.org/10.1038/s41564-024-01729-3
15. https://doi.org/10.3390/biom14121488
16. https://doi.org/10.1038/s41467-024-52732-5
17. https://doi.org/10.1128/msphere.00390-24
18. https://doi.org/10.1038/s41467-024-52732-5.
19. https://doi.org/10.1038/s41467-024-53638-y
20. https://doi.org/10.1111/mpp.70001
21. https://doi.org/10.1111/1751-7915.14306
22. https://doi.org/10.3390/biom14121488.
23. https://doi.org/10.1038/s41467-024-53638-y.
24. https://doi.org/10.1128/msphere.00390-24.
25. https://doi.org/10.1038/s41564-024-01729-3.
26. https://doi.org/10.1111/mpp.70001.
27. https://doi.org/10.1146/annurev-chembioeng-100722-114625.
28. https://doi.org/10.1111/1751-7915.14306.
29. https://doi.org/10.1088/1478-3975/abdc0e.
30. https://doi.org/10.1128/aem.00246-25.
31. https://doi.org/10.1128/aem.00246-25,
32. https://doi.org/10.1038/s41564-024-01729-3,
33. https://doi.org/10.3390/biom14121488,
34. https://doi.org/10.1038/s41467-024-52732-5,
35. https://doi.org/10.1128/msphere.00390-24,
36. https://doi.org/10.1146/annurev-chembioeng-100722-114625,
37. https://doi.org/10.1038/s41467-024-53638-y,
38. https://doi.org/10.1111/mpp.70001,
39. https://doi.org/10.1111/1751-7915.14306,
40. https://doi.org/10.1088/1478-3975/abdc0e,