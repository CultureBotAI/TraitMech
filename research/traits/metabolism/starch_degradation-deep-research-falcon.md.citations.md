# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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
**Generated:** 2026-06-18T06:09:33.144987

1. brown2024acarboseimpairsgut pages 3-5
2. pickens2024clostridiumbutyricumprazmowski pages 11-13
3. albright2025developmentofa pages 9-12
4. brown2024acarboseimpairsgut pages 5-7
5. dong2024extracellularoverexpressionof pages 8-10
6. brown2024acarboseimpairsgut pages 1-3
7. brown2024acarboseimpairsgut pages 7-9
8. lui2023characterizingtheeffect pages 1-2
9. sanchezgallardo2024unveilingmetabolicpathways pages 3-6
10. lui2023characterizingtheeffect pages 3-5
11. bhandari2023transportandutilization pages 4-7
12. bhandari2023transportandutilization pages 1-2
13. dong2024extracellularoverexpressionof pages 1-2
14. brown2024acarboseimpairsgut pages 27-27
15. bhandari2023elucidatingthemechanisms pages 90-94
16. bhandari2023elucidatingthemechanismsa pages 76-82
17. dong2024extracellularoverexpressionof pages 6-8
18. Sus
19. https://doi.org/10.1128/mbio.01506-24
20. https://doi.org/10.1007/s00018-023-04812-w
21. https://doi.org/10.1021/acschembio.2c00791
22. https://doi.org/10.1128/spectrum.04435-22
23. https://doi.org/10.1128/msphere.00566-23
24. https://doi.org/10.3390/bioengineering11070661
25. https://doi.org/10.3389/fmicb.2024.1414471
26. https://doi.org/10.1128/mbio.01506-24,
27. https://doi.org/10.1128/msphere.00566-23,
28. https://doi.org/10.1128/spectrum.04435-22,
29. https://doi.org/10.1101/2025.07.04.663206,
30. https://doi.org/10.3390/bioengineering11070661,
31. https://doi.org/10.1021/acschembio.2c00791,
32. https://doi.org/10.3389/fmicb.2024.1414471,