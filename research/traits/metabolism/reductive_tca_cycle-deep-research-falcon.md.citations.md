# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** reductive tricarboxylic acid cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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
**Generated:** 2026-08-04T07:01:15.514931

1. garritano2022carbonfixationpathways pages 2-3
2. sokolskyi2023roleofhorizontal pages 1-6
3. berg2011ecologicalaspectsof pages 5-6
4. scott2024widespreaddissolvedinorganic pages 13-15
5. rubinblum2019geneticevidencefor pages 1-2
6. peng2025carbonfluxesrewiring pages 1-2
7. sokolskyi2023roleofhorizontal pages 12-18
8. dogan2024seasonalgeneprofiling pages 5-6
9. sokolskyi2023roleofhorizontal pages 18-23
10. berg2011ecologicalaspectsof pages 4-5
11. berg2011ecologicalaspectsof pages 1-2
12. rubinblum2019geneticevidencefor pages 2-3
13. sokolskyi2023roleofhorizontal pages 6-12
14. tommasi2024thebiochemistryof pages 4-6
15. tommasi2024thebiochemistryof pages 2-4
16. s
17. ATP-citrate lyase
18. citryl-CoA synthetase
19. citryl-CoA lyase
20. 10.1128/AEM.01557-23
21. 10.18016/ksutarimdoga.vi.1212062
22. 10.3390/catal14100679
23. 10.1101/2022.10.25.513756
24. 10.1038/s41559-023-02147-0
25. 10.1093/pnasnexus/pgac226
26. 10.1128/AEM.02473-10
27. 10.1111/j.1462-2920.2006.01118.x
28. 10.1128/JB.00523-06
29. 10.1128/JB.179.15.4859-4867.1997
30. 10.1128/mSphere.00394-18
31. 10.1186/s13036-025-00489-w
32. https://doi.org/10.1128/AEM.01557-23
33. https://doi.org/10.18016/ksutarimdoga.vi.1212062
34. https://doi.org/10.3390/catal14100679
35. https://doi.org/10.1101/2022.10.25.513756
36. https://doi.org/10.1038/s41559-023-02147-0
37. https://doi.org/10.1093/pnasnexus/pgac226
38. https://doi.org/10.1128/AEM.02473-10
39. https://doi.org/10.1111/j.1462-2920.2006.01118.x
40. https://doi.org/10.1128/JB.00523-06
41. https://doi.org/10.1128/JB.179.15.4859-4867.1997
42. https://doi.org/10.1128/mSphere.00394-18
43. https://doi.org/10.1186/s13036-025-00489-w
44. https://doi.org/10.1128/aem.02473-10,
45. https://doi.org/10.1128/msphere.00394-18,
46. https://doi.org/10.1093/pnasnexus/pgac226,
47. https://doi.org/10.1101/2022.10.25.513756,
48. https://doi.org/10.1128/aem.01557-23,
49. https://doi.org/10.1186/s13036-025-00489-w,
50. https://doi.org/10.18016/ksutarimdoga.vi.1212062,
51. https://doi.org/10.3390/catal14100679,