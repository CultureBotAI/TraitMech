# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** helical shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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
**Generated:** 2026-08-04T09:00:10.146343

1. charon2012theuniqueparadigm pages 2-4
2. lin2021peptidoglycanbindingby pages 46-51
3. sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6
4. salama2020cellmorphologyas pages 1-2
5. sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4
6. sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8
7. salama2020cellmorphologyas pages 2-4
8. blair2018thehelicobacterpylori pages 1-3
9. salama2020cellmorphologyas pages 4-5
10. frirdich2023multiplecampylobacterjejuni pages 2-3
11. charon2012theuniqueparadigm pages 4-5
12. wolgemuth2015flagellarmotilityof pages 4-6
13. nakamura2020spirocheteflagellaand pages 1-3
14. blair2018thehelicobacterpylori pages 23-27
15. sycuro2010peptidoglycancrosslinkingrelaxation pages 6-7
16. sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10
17. wolgemuth2015flagellarmotilityof pages 6-7
18. liu2010cellulararchitectureof pages 8-9
19. liu2010cellulararchitectureof pages 7-8
20. 10.1016/j.cell.2010.03.046
21. 10.1016/j.mib.2019.12.002
22. 10.1111/mmi.14087
23. 10.3389/fmicb.2023.1162806
24. 10.1371/journal.ppat.1002602
25. 10.1038/s41467-019-13934-4
26. 10.1111/mmi.14482
27. 10.7554/eLife.86577.2
28. 10.1038/s41467-024-54806-w
29. 10.1101/2024.06.08.598065
30. 10.3390/biom10040550
31. activity unresolved through 2024
32. https://doi.org/10.1016/j.cell.2010.03.046
33. https://doi.org/10.3389/fmicb.2023.1162806
34. https://doi.org/10.1111/mmi.14087
35. https://doi.org/10.1016/j.mib.2019.12.002
36. https://doi.org/10.1371/journal.ppat.1002602
37. https://doi.org/10.1038/s41467-019-13934-4
38. https://doi.org/10.1146/annurev-micro-092611-150145
39. https://doi.org/10.1016/j.jmb.2010.09.020
40. https://doi.org/10.1016/j.semcdb.2015.10.015
41. https://doi.org/10.3390/biom10040550
42. https://doi.org/10.1111/mmi.14482
43. https://doi.org/10.7554/eLife.86577.2
44. https://doi.org/10.1038/s41467-024-54806-w
45. https://doi.org/10.1101/2024.06.08.598065
46. https://doi.org/10.1016/j.cell.2010.03.046](https://doi.org/10.1016/j.cell.2010.03.046
47. https://doi.org/10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806
48. https://doi.org/10.1111/mmi.14087](https://doi.org/10.1111/mmi.14087
49. https://doi.org/10.1016/j.mib.2019.12.002](https://doi.org/10.1016/j.mib.2019.12.002
50. https://doi.org/10.1371/journal.ppat.1002602](https://doi.org/10.1371/journal.ppat.1002602
51. https://doi.org/10.1038/s41467-019-13934-4](https://doi.org/10.1038/s41467-019-13934-4
52. https://doi.org/10.1146/annurev-micro-092611-150145](https://doi.org/10.1146/annurev-micro-092611-150145
53. https://doi.org/10.1016/j.jmb.2010.09.020](https://doi.org/10.1016/j.jmb.2010.09.020
54. https://doi.org/10.1016/j.semcdb.2015.10.015](https://doi.org/10.1016/j.semcdb.2015.10.015
55. https://doi.org/10.3390/biom10040550](https://doi.org/10.3390/biom10040550
56. https://doi.org/10.1111/mmi.14482](https://doi.org/10.1111/mmi.14482
57. https://doi.org/10.7554/eLife.86577.2](https://doi.org/10.7554/eLife.86577.2
58. https://doi.org/10.1038/s41467-024-54806-w](https://doi.org/10.1038/s41467-024-54806-w
59. https://doi.org/10.1101/2024.06.08.598065](https://doi.org/10.1101/2024.06.08.598065
60. https://doi.org/10.1146/annurev-micro-092611-150145,
61. https://doi.org/10.3390/biom10040550,
62. https://doi.org/10.1016/j.cell.2010.03.046,
63. https://doi.org/10.3389/fmicb.2023.1162806,
64. https://doi.org/10.1016/j.mib.2019.12.002,
65. https://doi.org/10.14288/1.0401780,
66. https://doi.org/10.1371/journal.ppat.1002602,
67. https://doi.org/10.1111/mmi.14087,
68. https://doi.org/10.1016/j.semcdb.2015.10.015,
69. https://doi.org/10.1016/j.jmb.2010.09.020,