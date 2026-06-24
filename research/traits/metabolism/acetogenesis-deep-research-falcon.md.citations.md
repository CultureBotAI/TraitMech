# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Acetogenesis
- **METPO identifier:** METPO:1000845
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that produces acetate as the primary end product through the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl pathway, typically performed by acetogenic bacteria under anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Acetate fermentation
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA (Supports acetyl-CoA formation from CO2 and CO in acetogens.)
- **Existing causal graph summary:** acetogenesis_wood_ljungdahl: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Acetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/acetogenesis.yaml`.

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
**Generated:** 2026-06-18T04:03:05.841953

1. jezernik2024designofmicrobial pages 17-20
2. zwerger2024aceticacidbioproduction pages 13-17
3. zhang2024engineeredacetogenicbacteria pages 2-3
4. zhang2024engineeredacetogenicbacteria pages 1-2
5. moon2024redirectingelectronflow pages 1-2
6. allaart2023overflowmetabolismat pages 2-4
7. quintela2024influenceofhydrogen pages 4-5
8. robazza2024acetateshockloads pages 1-2
9. wang2024codrivenelectronand pages 1-3
10. cheng2024explorationofbiogasb pages 41-45
11. yu2023genomicpotentialand pages 1-2
12. zwerger2024aceticacidbioproduction pages 64-67
13. basen2023editorialacetogens pages 1-2
14. katsyv2023molecularbasisof pages 1-2
15. bae2024harnessingacetogenicbacteria pages 8-9
16. baum2024theenergyconvertinghydrogenase pages 1-2
17. elisiario2023aceticacidgrowth pages 1-3
18. ahuja2023aminireviewon pages 10-11
19. cheng2024explorationofbiogas pages 41-45
20. baum2024theenergyconvertinghydrogenase pages 2-5
21. elisiario2023aceticacidgrowth pages 4-6
22. elisiario2023aceticacidgrowth pages 10-11
23. allaart2023overflowmetabolismat pages 1-2
24. jezernik2024designofmicrobial pages 71-74
25. moon2024redirectingelectronflow pages 4-6
26. moon2024redirectingelectronflow pages 2-3
27. FeFe
28. is reduced by FDH/HDCR to
29. donates electrons to
30. is converted by Fhs to
31. is converted by FolD/FTC-MDH activities to
32. is reduced by MTHFR (MetF/MetV) to
33. transfers methyl group via MT to
34. is reduced by CODH to
35. are condensed by ACS to form
36. is converted by PTA to
37. is converted by ACK to
38. oxidizes H2 and reduces
39. drives Rnf to reduce
40. translocates
41. drives
42. couples ferredoxin/H+ interconversion to
43. rebalances
44. has net
45. enables growth on
46. increases
47. is detoxified/oxidized by
48. causes
49. shifts metabolism toward
50. increases specificity toward
51. suppresses
52. provides acetate/H2 that supports
53. lack complete
54. fefe
55. https://doi.org/10.3389/fbioe.2024.1395540;
56. https://doi.org/10.34726/hss.2024.114566
57. https://doi.org/10.3389/fbioe.2024.1395540
58. https://doi.org/10.1038/s41467-024-49680-5;
59. https://doi.org/10.1021/jacs.2c11683
60. https://doi.org/10.1128/spectrum.03380-23
61. https://doi.org/10.3389/fmicb.2023.1186930
62. https://doi.org/10.1038/s41467-024-49680-5
63. https://doi.org/10.1111/1751-7915.14212
64. https://doi.org/10.1007/s00253-023-12670-6
65. https://doi.org/10.3390/molecules29235653
66. https://doi.org/10.1111/1751-7915.70063
67. https://doi.org/10.1186/s40168-024-01869-y
68. https://doi.org/10.1039/d4cb00099d
69. https://doi.org/10.3389/fmicb.2023.1279544
70. https://doi.org/10.3390/su15043765
71. https://doi.org/10.3389/fbioe.2024.1395540,
72. https://doi.org/10.34726/hss.2024.114566,
73. https://doi.org/10.3389/fmicb.2023.1186930,
74. https://doi.org/10.1021/jacs.2c11683,
75. https://doi.org/10.1128/spectrum.03380-23,
76. https://doi.org/10.1038/s41467-024-49680-5,
77. https://doi.org/10.1007/s00253-023-12670-6,
78. https://doi.org/10.1111/1751-7915.14212,
79. https://doi.org/10.1111/1751-7915.70063,
80. https://doi.org/10.3390/molecules29235653,
81. https://doi.org/10.1186/s40168-024-01869-y,
82. https://doi.org/10.3389/fmicb.2023.1279544,
83. https://doi.org/10.3390/su15043765,
84. https://doi.org/10.1039/d4cb00099d,