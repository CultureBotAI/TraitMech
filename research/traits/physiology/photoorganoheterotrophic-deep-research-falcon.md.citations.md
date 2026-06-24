# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoorganoheterotrophic
- **METPO identifier:** METPO:1000659
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-809633-8.20672-9: light-induced redox chemistry (Phototrophy chapter supports light-driven reaction-center electron transfer.) | DOI:10.1021/acsomega.3c02205: photoorganoheterotrophic (Review table classifies photoorganoheterotrophy by light with organic electron and carbon sources.)
- **Existing causal graph summary:** photoorganoheterotrophic_light_organic_electrons: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoorganoheterotrophic.yaml`.

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
**Generated:** 2026-06-18T12:33:40.726251

1. tinguely2023diurnalcyclesdrive pages 1-2
2. stebegg2023heterotrophyamongcyanobacteria pages 2-4
3. stebegg2023heterotrophyamongcyanobacteria pages 1-2
4. stebegg2023heterotrophyamongcyanobacteria pages 2-2
5. mujakic2023multienvironmentecogenomicsanalysis pages 9-11
6. mujakic2023multienvironmentecogenomicsanalysis pages 1-2
7. kopejtka2024minimaltranscriptionalregulation pages 1-2
8. oh2024effectoflight pages 1-2
9. oh2024effectoflight pages 13-14
10. lee2024effectsoflight pages 1-2
11. niederman2024whatweare pages 1-2
12. niederman2024whatweare pages 5-7
13. kopejtka2024minimaltranscriptionalregulation pages 8-10
14. oh2024effectoflight pages 10-11
15. deng2025theroleof pages 47-51
16. oh2024effectoflight pages 12-13
17. oh2024effectoflight pages 8-9
18. niederman2024whatweare pages 9-11
19. oh2024effectoflight pages 6-8
20. niederman2024whatweare pages 20-22
21. stebegg2023heterotrophyamongcyanobacteria pages 13-14
22. mujakic2023multienvironmentecogenomicsanalysis pages 11-13
23. mujakic2023multienvironmentecogenomicsanalysis pages 15-17
24. niederman2024whatweare pages 11-13
25. niederman2024whatweare pages 4-5
26. niederman2024whatweare pages 22-23
27. niederman2024whatweare pages 7-9
28. oh2024effectoflight pages 2-3
29. 4Fe-4S
30. s
31. https://doi.org/10.3390/biom14030311
32. https://doi.org/10.1038/s43705-023-00334-5
33. https://doi.org/10.4014/jmb.2410.10034
34. https://doi.org/10.1021/acsomega.3c02205
35. https://doi.org/10.1128/spectrum.01112-23
36. https://doi.org/10.1128/msystems.00706-24
37. https://doi.org/10.1007/s12275-024-00125-0
38. https://doi.org/10.1038/s43705-023-00334-5,
39. https://doi.org/10.1021/acsomega.3c02205,
40. https://doi.org/10.1128/spectrum.01112-23,
41. https://doi.org/10.1128/msystems.00706-24,
42. https://doi.org/10.4014/jmb.2410.10034,
43. https://doi.org/10.1007/s12275-024-00125-0,
44. https://doi.org/10.3390/biom14030311,