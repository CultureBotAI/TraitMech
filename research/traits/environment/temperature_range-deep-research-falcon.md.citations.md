# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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
**Generated:** 2026-08-04T04:23:20.286926

1. rosso1995convenientmodelto pages 1-2
2. damico2006psychrophilicmicroorganismschallenges pages 1-2
3. hoogerland2024atemperaturesensitivemetabolic pages 7-8
4. giles2005cryptococcusneoformansmitochondrial pages 1-2
5. hoogerland2024atemperaturesensitivemetabolic pages 1-2
6. hoogerland2024atemperaturesensitivemetabolic pages 3-4
7. christina2024mechanismsofanammox pages 1-5
8. berdejo2024evolutionarytradeoffbetween pages 8-10
9. chen2015adaptationoflactococcus pages 1-2
10. rodrigues2008architectureofthermal pages 1-2
11. noll2020modelingandexploiting pages 22-23
12. maiti2024extrememakeoverthe pages 1-2
13. lehmann2023adaptivelaboratoryevolution pages 6-7
14. lehmann2023adaptivelaboratoryevolution pages 7-8
15. berdejo2024evolutionarytradeoffbetween pages 1-2
16. chiu2023membranelipidand pages 1-2
17. chiu2023membranelipidand pages 13-14
18. hurtadobautista2024thermalplasticityand pages 1-2
19. hurtadobautista2024thermalplasticityand pages 16-17
20. hurtadobautista2024thermalplasticityand pages 2-3
21. kik2024anadaptivebiomolecular pages 1-2
22. kik2024anadaptivebiomolecular pages 5-6
23. lehmann2023adaptivelaboratoryevolution pages 2-3
24. noll2020modelingandexploiting pages 6-8
25. DOI, published February 1995
26. DOI, published October 2023
27. DOI, published 13 February 2024
28. DOI, published April 2006
29. DOI, published October 2024
30. 10.1038/sj.embor.7400662
31. 10.1038/s41467-024-53677-5
32. 10.3389/fmicb.2023.1219779
33. 10.1101/2024.07.23.604647
34. 10.1128/mbio.03105-23
35. 10.1038/srep14199
36. 10.1128/EC.4.1.46-54.2005
37. 10.1038/s41467-024-47355-9
38. 10.1128/mbio.02753-24
39. 10.3390/biology13121088
40. DOI, accepted 17 October 2024
41. DOI, published December 2024
42. DOI, published 15 August 2023
43. DOI, accepted 27 March 2024
44. DOI, published 18 November 2008
45. DOI, published 21 September 2015
46. Preprint DOI, posted July 2024
47. DOI, published January 2020
48. last edge inferred; mark uncertain until direct boundary perturbation
49. direct in *C. neoformans*
50. mechanism strong; direct boundary edge usually uncertain
51. 10.1039/D4CC03114H
52. 10.3389/fmicb.2023.1265216
53. 10.1128/AEM.61.2.610-616.1995
54. 10.1186/1471-2164-9-547
55. 10.3390/pr8010121
56. 10.1016/S0300-9629(97)00003-0
57. https://doi.org/10.1128/aem.61.2.610-616.1995
58. https://doi.org/10.3389/fmicb.2023.1265216
59. https://doi.org/10.1128/mbio.03105-23
60. https://doi.org/10.1038/sj.embor.7400662
61. https://doi.org/10.1038/s41467-024-53046-2
62. https://doi.org/10.1038/s41467-024-53677-5
63. https://doi.org/10.3389/fmicb.2023.1219779
64. https://doi.org/10.1101/2024.07.23.604647
65. https://doi.org/10.1038/srep14199
66. https://doi.org/10.1128/EC.4.1.46-54.2005
67. https://doi.org/10.1038/s41467-024-47355-9
68. https://doi.org/10.1128/mbio.02753-24
69. https://doi.org/10.3390/biology13121088
70. https://doi.org/10.1186/1471-2164-9-547
71. https://doi.org/10.3390/pr8010121
72. https://doi.org/10.1039/D4CC03114H
73. https://doi.org/10.1128/AEM.61.2.610-616.1995
74. https://doi.org/10.1016/S0300-9629(97
75. https://doi.org/10.1128/aem.61.2.610-616.1995,
76. https://doi.org/10.3389/fmicb.2023.1265216,
77. https://doi.org/10.1128/mbio.03105-23,
78. https://doi.org/10.1038/sj.embor.7400662,
79. https://doi.org/10.1038/s41467-024-53677-5,
80. https://doi.org/10.1128/ec.4.1.46-54.2005,
81. https://doi.org/10.3389/fmicb.2023.1219779,
82. https://doi.org/10.1128/mbio.02753-24,
83. https://doi.org/10.3390/biology13121088,
84. https://doi.org/10.1038/srep14199,
85. https://doi.org/10.1038/s41467-024-47355-9,
86. https://doi.org/10.1101/2024.07.23.604647,
87. https://doi.org/10.1186/1471-2164-9-547,
88. https://doi.org/10.3390/pr8010121,
89. https://doi.org/10.1039/d4cc03114h,