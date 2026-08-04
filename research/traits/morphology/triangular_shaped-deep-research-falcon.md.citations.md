# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** triangular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 7 nodes, 7 edges

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
**Generated:** 2026-08-04T10:30:23.474895

1. du2023evolutionarydevelopmentalbiology pages 1-7
2. brown2024archaealtubulinlikeproteins pages 1-5
3. wolferen2022thecellbiology pages 3-4
4. duggin2015cetztubulinlikeproteins pages 1-2
5. gambelli2021thepolygonalcell pages 7-9
6. liao2018archaealcellbiology pages 1-5
7. bissonfilho2018archaealimagingleading pages 2-3
8. schiller2024identificationofstructural pages 5-6
9. schiller2024identificationofstructural pages 9-10
10. gambelli2021thepolygonalcell pages 1-2
11. 10.1038/s41467-024-45196-0
12. 10.1101/2024.10.29.620987
13. 10.3389/fmicb.2023.1270665
14. 10.48617/etd.674
15. 10.1038/s41564-022-01215-8
16. 10.3389/fmicb.2021.766527
17. 10.1042/ETLS20180026
18. 10.1091/mbc.e17-10-0603
19. 10.1038/nature13983
20. 10.1016/S0723-2020(11)80165-7
21. 10.1016/0378-1097(92)90285-V
22. 10.1007/BF01955151
23. 10.1007/s007920050012
24. https://doi.org/10.1038/s41467-024-45196-0
25. https://doi.org/10.1101/2024.10.29.620987
26. https://doi.org/10.3389/fmicb.2023.1270665
27. https://doi.org/10.48617/etd.674
28. https://doi.org/10.1038/s41564-022-01215-8
29. https://doi.org/10.3389/fmicb.2021.766527
30. https://doi.org/10.1042/ETLS20180026
31. https://doi.org/10.1091/mbc.e17-10-0603
32. https://doi.org/10.1038/nature13983
33. https://doi.org/10.1016/S0723-2020(11
34. https://doi.org/10.1016/0378-1097(92
35. https://doi.org/10.1007/BF01955151
36. https://doi.org/10.1007/s007920050012
37. https://doi.org/10.1038/s41564-022-01215-8,
38. https://doi.org/10.48617/etd.674,
39. https://doi.org/10.1042/etls20180026,
40. https://doi.org/10.1091/mbc.e17-10-0603,
41. https://doi.org/10.1038/nature13983,
42. https://doi.org/10.1101/2024.10.29.620987,
43. https://doi.org/10.3389/fmicb.2023.1270665,
44. https://doi.org/10.1038/s41467-024-45196-0,
45. https://doi.org/10.3389/fmicb.2021.766527,