# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately anaerobic
- **METPO identifier:** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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
**Generated:** 2026-06-18T00:04:37.011940

1. dyksma2024growthofsulfatereducing pages 1-2
2. lu2021whenanaerobesencounter pages 22-27
3. silva2024methodsforcultivation pages 1-3
4. silva2024methodsforcultivation pages 3-5
5. morais2024effectofmicroaeration pages 1-2
6. caulat2024physiologicalroleand pages 2-5
7. caulat2024physiologicalroleand pages 15-17
8. caulat2024physiologicalroleand pages 1-2
9. lu2021whenanaerobesencounter pages 1-3
10. bystrom2024couplingbutyrylcoenzymea pages 17-21
11. lu2021whenanaerobesencounter pages 11-13
12. lu2021whenanaerobesencounter pages 4-6
13. silva2024methodsforcultivation pages 5-6
14. muller2024highthroughputanaerobicscreening pages 2-4
15. li2024acomprehensivereview pages 11-13
16. lu2021whenanaerobesencounter pages 3-4
17. caulat2024physiologicalroleand pages 5-7
18. lu2021whenanaerobesencounter pages 13-15
19. muller2024highthroughputanaerobicscreening pages 15-18
20. li2024acomprehensivereview pages 1-2
21. dyksma2024growthofsulfatereducing pages 5-6
22. morais2024effectofmicroaeration pages 2-4
23. FeFe
24. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
25. https://doi.org/10.1038/s41579-021-00583-y
26. https://doi.org/10.1186/s40168-024-01909-7
27. https://doi.org/10.14288/1.0447284
28. https://doi.org/10.1128/mbio.01591-24
29. https://doi.org/10.1007/978-1-0716-4043-2_7
30. https://doi.org/10.1007/s00253-023-12969-4
31. https://doi.org/10.1038/s41596-023-00926-4
32. https://doi.org/10.3390/methane3020014
33. https://doi.org/10.1038/s41579-021-00583-y,
34. https://doi.org/10.1128/mbio.01591-24,
35. https://doi.org/10.1186/s40168-024-01909-7,
36. https://doi.org/10.14288/1.0447284,
37. https://doi.org/10.1007/978-1-0716-4043-2\_7,
38. https://doi.org/10.1038/s41596-023-00926-4,
39. https://doi.org/10.1007/s00253-023-12969-4,
40. https://doi.org/10.3390/methane3020014,