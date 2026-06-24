# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
**Generated:** 2026-06-17T20:28:29.885887

1. meaney2025engineeringrhizobiaendosymbiontsa pages 67-70
2. ling2024acompletedna pages 10-11
3. song2024cellularinteractionsand pages 8-9
4. ling2024acompletedna pages 6-7
5. wierz2024intracellularsymbiontsymbiodolus pages 1-2
6. bai2024endosymbionttremblayaphenacola pages 1-2
7. isidraarellano2024understandingthecrucial pages 1-2
8. silva2024comparativetranscriptomicsof pages 19-21
9. ferrarini2023coordinationofhost pages 1-3
10. ferrarini2023coordinationofhost pages 10-13
11. ferrarini2023coordinationofhost pages 6-8
12. isidraarellano2024understandingthecrucial pages 5-6
13. isidraarellano2024understandingthecrucial pages 11-12
14. isidraarellano2024understandingthecrucial pages 3-5
15. silva2024comparativetranscriptomicsof pages 1-2
16. semenova2024autophagyandsymbiosis pages 7-8
17. isidraarellano2024understandingthecrucial pages 2-3
18. semenova2024autophagyandsymbiosis pages 1-2
19. ling2024acompletedna pages 9-10
20. ling2024acompletedna pages 7-9
21. meaney2025engineeringrhizobiaendosymbionts pages 63-67
22. ling2024acompletedna pages 1-2
23. semenova2024autophagyandsymbiosis pages 11-13
24. ferrarini2023coordinationofhost pages 17-18
25. silva2024comparativetranscriptomicsof pages 25-26
26. ing
27. METPO traitmech:000045
28. label
29. GO:0005622 broad host context only
30. ENVO candidate label
31. GO:0006310
32. GO:0007035 related vacuolar acidification
33. NCBITaxon candidate
34. GO:0009306 broad
35. GO:0046718 candidate broad host cell invasion
36. GO:0043655 candidate
37. UBERON:0000992
38. GO:0018995 candidate label
39. GO:1901607
40. GO:0051186
41. GO:0006520
42. PATO:0001914 candidate
43. CHEBI antibiotic class candidate
44. GO:0031929
45. UniProt host-specific not assigned
46. GO:0009253
47. UniProt family/GO molecular function label
48. CHEBI:73616
49. GO:0010468
50. protein label
51. CHEBI:16199
52. cell type label
53. GO:0006810
54. GO candidate label
55. CHEBI:18198
56. GO:0005385
57. CHEBI:29105
58. GO:0003795 candidate
59. GO:0051301
60. CHEBI:16412
61. GO:0006915
62. GO:0006914
63. GO:0004843
64. GO:0010507
65. CHEBI:18367
66. CHEBI:18248
67. PO:0005640 candidate
68. ENVO/label
69. GO:0009399
70. gene label
71. GO candidate
72. GO:0006826
73. gene labels
74. GO:0000045
75. gene set label
76. GO:0034976
77. GO:0042594
78. protein labels
79. GO:0006298
80. PATO/label
81. SO:0000167
82. GO:0007015
83. traitmech:000045
84. GO:0007040 candidate broad
85. GO:0005768
86. GO:0005764
87. GO:0000502
88. NCBITaxon:31969
89. https://doi.org/10.1093/ismejo/wrae117
90. https://doi.org/10.1093/ismejo/wrae099
91. https://doi.org/10.1093/ismejo/wrae052
92. https://doi.org/10.3390/ijms25084228
93. https://doi.org/10.1186/s40168-023-01714-8
94. https://doi.org/10.1093/pcp/pcae128
95. https://doi.org/10.3390/ijms25052918
96. https://doi.org/10.1073/pnas.2415651121
97. https://doi.org/10.1093/ismejo/wrae117,
98. https://doi.org/10.1186/s40168-023-01714-8,
99. https://doi.org/10.1073/pnas.2415651121,
100. https://doi.org/10.1093/ismejo/wrae052,
101. https://doi.org/10.3390/ijms25084228,
102. https://doi.org/10.1093/ismejo/wrae099,
103. https://doi.org/10.1093/pcp/pcae128,
104. https://doi.org/10.3390/ijms25052918,