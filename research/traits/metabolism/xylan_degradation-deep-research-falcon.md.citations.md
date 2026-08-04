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
- **Existing causal graph summary:** xylan_degradation_xylanase: 8 nodes, 5 edges

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
**Generated:** 2026-06-30T00:22:33.708871

1. liu2022selfishuptakeversus pages 9-12
2. liu2024intracellularremovalof pages 1-2
3. liu2023theweimbergpathway pages 1-3
4. leschonski2024structuredependentstimulationof pages 2-4
5. panwar2025transcriptionaldelineationof pages 5-7
6. novak2024currentmodelsin pages 4-5
7. novak2024currentmodelsin pages 2-4
8. lindic2025structuralandfunctional pages 9-10
9. zhang2014xylanutilizationin pages 2-2
10. novak2024currentmodelsin pages 1-2
11. kerkaert2023regulationofnutrient pages 5-6
12. liu2022selfishuptakeversus pages 1-2
13. christov1993esterasesofxylandegrading pages 1-2
14. liu2022selfishuptakeversus pages 6-9
15. kerkaert2023regulationofnutrient pages 36-38
16. park2025xylosemetabolismand pages 2-3
17. zhang2014xylanutilizationin pages 6-7
18. martin2025metabolismofhemicelluloses pages 3-5
19. liu2022selfishuptakeversus pages 2-4
20. novak2024currentmodelsin pages 15-16
21. dvorak2024syntheticallyprimedadaptationof pages 3-4
22. christov1993esterasesofxylandegrading pages 6-7
23. zhang2014xylanutilizationin pages 2-3
24. leschonski2024structuredependentstimulationof pages 28-29
25. novak2024currentmodelsin pages 12-13
26. novak2024currentmodelsin pages 11-12
27. dvorak2024syntheticallyprimedadaptationof pages 5-6
28. zhang2014xylanutilizationin pages 1-2
29. https://doi.org/10.1016/0141-0229(93
30. https://doi.org/10.1080/19490976.2024.2430419,
31. https://doi.org/10.1186/s12934-024-02423-z,
32. https://doi.org/10.3389/fmicb.2025.1638551,
33. https://doi.org/10.1186/s13068-022-02225-8,
34. https://doi.org/10.1186/s13068-023-02266-7,
35. https://doi.org/10.4014/jmb.2504.04021,
36. https://doi.org/10.1128/aem.01759-24,
37. https://doi.org/10.1073/pnas.1406156111,
38. https://doi.org/10.1093/ismejo/wraf022,
39. https://doi.org/10.1007/s00253-023-12977-4,
40. https://doi.org/10.1007/s00253-023-12680-4,
41. https://doi.org/10.1038/s41467-024-46812-9,