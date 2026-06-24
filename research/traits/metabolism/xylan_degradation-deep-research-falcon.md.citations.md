# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xylan degradation
- **METPO identifier:** traitmech:000113
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes xylan, the most abundant hemicellulose, into xylose and xylo-oligosaccharides using xylanases and accessory enzymes.
- **Parent traits:** traitmech:000110
- **Synonyms:** xylanolytic, hemicellulose degradation
- **Existing evidence:** DOI:10.1111/j.1757-1707.2009.01004.x:  (Dodd & Cann review the enzymatic deconstruction of xylan, the major hemicellulosic polysaccharide.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. include hemicellulose (xylan) degradation within lignocellulose breakdown across organisms.)
- **Existing causal graph summary:** xylan_degradation_xylanase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xylan degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/xylan_degradation.yaml`.

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
**Generated:** 2026-06-18T06:30:20.096364

1. rakitin2024verrucomicrobiaofthe pages 2-3
2. hinkley2025investigatingthemechanism pages 101-106
3. liu2024intracellularremovalof pages 1-2
4. novak2024currentmodelsin pages 2-4
5. pentari2025exploringthesynergy pages 1-2
6. novak2024currentmodelsin pages 1-2
7. mukherjee2023comprehensivegenomeanalysis pages 10-12
8. mukherjee2023comprehensivegenomeanalysis pages 2-4
9. rakitin2024verrucomicrobiaofthe pages 5-7
10. rakitin2024verrucomicrobiaofthe pages 1-2
11. xia2024clusteredsurfaceamino pages 2-4
12. xia2024clusteredsurfaceamino pages 1-2
13. mukherjee2023comprehensivegenomeanalysis pages 1-2
14. pentari2025exploringthesynergy pages 5-6
15. pentari2025exploringthesynergy pages 7-9
16. hinkley2025investigatingthemechanisma pages 30-36
17. ed
18. https://doi.org/10.1186/s12934-024-02423-z
19. https://doi.org/10.1007/s00253-023-12977-4
20. https://doi.org/10.1128/spectrum.05028-22
21. https://doi.org/10.1038/s41598-024-74787-6
22. https://doi.org/10.3390/microorganisms12112271
23. https://doi.org/10.1007/s00253-024-13045-1
24. https://doi.org/10.1186/s13068-025-02639-0
25. https://doi.org/10.3390/microorganisms12112271,
26. https://doi.org/10.1111/1541-4337.70391,
27. https://doi.org/10.1186/s12934-024-02423-z,
28. https://doi.org/10.1128/spectrum.05028-22,
29. https://doi.org/10.1038/s41598-024-74787-6,
30. https://doi.org/10.1007/s00253-023-12977-4,
31. https://doi.org/10.1186/s13068-025-02639-0,
32. https://doi.org/10.1080/19490976.2024.2353229,
33. https://doi.org/10.1007/s00253-024-13045-1,