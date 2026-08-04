# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000881
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its longer dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.cub.2014.07.022: cell size is tightly controlled (Review establishes cell size as an actively regulated phenotype, supporting length as a controlled cellular dimension.) | DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports an inter-divisional length increment underlying cell-length distributions.)
- **Existing causal graph summary:** cell_length_division_growth_control: 12 nodes, 12 edges

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
**Generated:** 2026-08-04T07:38:23.297539

1. ojkic2021bacterialcellshape pages 1-2
2. meier2017ftsexmediatedregulationof pages 1-2
3. lee2024comprehensiveunderstandingof pages 1-2
4. lee2023theuniquenterminal pages 1-2
5. hill2018anutrientdependentdivision pages 1-2
6. hill2013amoonlightingenzyme pages 1-2
7. weart2007ametabolicsensor pages 1-2
8. heinrich2019molecularbasisand pages 1-2
9. heinrich2019molecularbasisand pages 5-6
10. mahone2023integrationofcell pages 1-2
11. mogerreischer2023evolutionofa pages 1-2
12. gulsoy2024divisomeminimizationshows pages 1-4
13. jun2018fundamentalprinciplesin pages 54-55
14. vadia2015growthrateand pages 6-7
15. lee2024comprehensiveunderstandingof pages 9-10
16. 10.3389/fpls.2024.1369976
17. 10.1083/jcb.202211026
18. 10.1101/2024.01.12.575403
19. 10.1038/s41586-023-06288-x
20. 10.1128/jb.00092-23
21. 10.1128/mBio.01557-19
22. 10.1186/s12866-018-1155-2
23. 10.1088/1361-6633/aaa628
24. 10.1371/journal.pgen.1006999
25. 10.1016/j.mib.2015.01.011
26. 10.1371/journal.pgen.1003663
27. 10.1016/j.cell.2007.05.043
28. https://doi.org/10.3389/fpls.2024.1369976
29. https://doi.org/10.1083/jcb.202211026
30. https://doi.org/10.1101/2024.01.12.575403
31. https://doi.org/10.1038/s41586-023-06288-x
32. https://doi.org/10.1128/jb.00092-23
33. https://doi.org/10.1128/mBio.01557-19
34. https://doi.org/10.1186/s12866-018-1155-2
35. https://doi.org/10.1088/1361-6633/aaa628
36. https://doi.org/10.1371/journal.pgen.1006999
37. https://doi.org/10.1016/j.mib.2015.01.011
38. https://doi.org/10.1371/journal.pgen.1003663
39. https://doi.org/10.1016/j.cell.2007.05.043
40. https://doi.org/10.1101/2021.03.25.436990,
41. https://doi.org/10.1371/journal.pgen.1006999,
42. https://doi.org/10.3389/fpls.2024.1369976,
43. https://doi.org/10.1128/jb.00092-23,
44. https://doi.org/10.1186/s12866-018-1155-2,
45. https://doi.org/10.1371/journal.pgen.1003663,
46. https://doi.org/10.1016/j.cell.2007.05.043,
47. https://doi.org/10.1128/mbio.01557-19,
48. https://doi.org/10.1083/jcb.202211026,
49. https://doi.org/10.1038/s41586-023-06288-x,
50. https://doi.org/10.1101/2024.01.12.575403,
51. https://doi.org/10.1016/j.mib.2015.01.011,
52. https://doi.org/10.1088/1361-6633/aaa628,