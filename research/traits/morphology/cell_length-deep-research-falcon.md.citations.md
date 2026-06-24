# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length
- **METPO identifier:** METPO:1000881
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its longer dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.cub.2014.07.022: cell size is tightly controlled (Review establishes cell size as an actively regulated phenotype, supporting length as a controlled cellular dimension.) | DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports an inter-divisional length increment underlying cell-length distributions.)
- **Existing causal graph summary:** cell_length_division_growth_control: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **cell length** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length.yaml`.

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
**Generated:** 2026-06-18T07:09:33.310433

1. chung2024singlecellimagingof pages 7-8
2. tian2023cellsortingdirectedselection pages 4-7
3. harpring2023plasticityinthe pages 1-2
4. lakey2023theroleof pages 1-2
5. hayashi2024septalwallsynthesis pages 1-2
6. vashistha2023bacterialcellsizechanges pages 1-2
7. chung2024singlecellimagingof pages 1-2
8. cameron2024insightsintothe pages 1-3
9. lakey2023theroleof pages 18-19
10. lakey2023theroleof pages 2-4
11. vashistha2023bacterialcellsizechanges pages 8-9
12. kalia2024manipulatingmicrobialcell pages 1-2
13. thiermann2024toolsandmethods pages 1-3
14. tian2023cellsortingdirectedselection pages 1-2
15. sichangi2023geneticeventsresponsible pages 28-32
16. thiermann2024toolsandmethodsa pages 14-16
17. kalia2024manipulatingmicrobialcell pages 7-8
18. kalia2024manipulatingmicrobialcell pages 5-7
19. kalia2024manipulatingmicrobialcell pages 9-11
20. battaje2023modelsversuspathogens pages 1-3
21. biswas2024universalityofphenotypic pages 1-2
22. elgamel2023multigenerationalmemoryin pages 1-2
23. castanheira2023evidenceoftwo pages 1-2
24. nieto2024mechanismsofcell pages 1-2
25. kalia2024manipulatingmicrobialcell pages 4-5
26. thiermann2024toolsandmethodsa pages 10-11
27. thiermann2024toolsandmethods pages 10-11
28. nieto2024mechanismsofcell pages 6-7
29. sichangi2023geneticeventsresponsible pages 45-49
30. s
31. es
32. https://doi.org/10.1038/s42003-024-07279-y
33. https://doi.org/10.1038/s41467-023-41487-0
34. https://doi.org/10.1128/mbio.00631-23
35. https://doi.org/10.3390/ijms24043243
36. https://doi.org/10.1038/s41564-024-01846-z
37. https://doi.org/10.3389/fcimb.2023.1205488
38. https://doi.org/10.1038/s41579-023-00942-x
39. https://doi.org/10.3390/polym16030410
40. https://doi.org/10.7554/elife.88463
41. https://doi.org/10.1038/s42003-023-05308-w
42. https://doi.org/10.1038/s41540-024-00383-z
43. https://doi.org/10.1103/physrevresearch.6.l022043
44. https://doi.org/10.1103/physreve.108.l032401
45. https://doi.org/10.1042/bsr20221664
46. https://doi.org/10.1038/s41564-024-01846-z,
47. https://doi.org/10.3389/fcimb.2023.1205488,
48. https://doi.org/10.1038/s41579-023-00942-x,
49. https://doi.org/10.1038/s42003-024-07279-y,
50. https://doi.org/10.1038/s41467-023-41487-0,
51. https://doi.org/10.7554/elife.88463,
52. https://doi.org/10.3390/ijms24043243,
53. https://doi.org/10.1128/mbio.00631-23,
54. https://doi.org/10.3390/polym16030410,
55. https://doi.org/10.7554/elife.88463.4,
56. https://doi.org/10.1042/bsr20221664,
57. https://doi.org/10.1103/physrevresearch.6.l022043,
58. https://doi.org/10.1103/physreve.108.l032401,
59. https://doi.org/10.1038/s41540-024-00383-z,
60. https://doi.org/10.1038/s42003-023-05308-w,