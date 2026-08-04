# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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
**Generated:** 2026-08-04T04:18:38.487677

1. berdejo2024evolutionarytradeoffbetween pages 8-10
2. lehmann2023adaptivelaboratoryevolution pages 1-2
3. lehmann2023adaptivelaboratoryevolution pages 8-9
4. hoogerland2024atemperaturesensitivemetabolic pages 1-2
5. hoogerland2024atemperaturesensitivemetabolic pages 7-8
6. pathania2021adaptationtocold pages 220-223
7. purwar2024adaptationsofpsychrophilic pages 10-11
8. purwar2024adaptationsofpsychrophilic pages 6-7
9. murata2011molecularstrategyfor pages 1-2
10. noll2020modelingandexploiting pages 6-8
11. mohammed2023potentialsandlimitations pages 5-6
12. schaum2022evolutionofthermal pages 5-6
13. engqvist2018correlatingenzymeannotations pages 2-4
14. ramon2023ageneraloverview pages 1-2
15. noll2020modelingandexploiting pages 19-20
16. lehmann2023adaptivelaboratoryevolution pages 2-3
17. engqvist2018correlatingenzymeannotations pages 4-6
18. engqvist2018correlatingenzymeannotations pages 9-10
19. hoogerland2024atemperaturesensitivemetabolic pages 5-6
20. hoogerland2024atemperaturesensitivemetabolic pages 3-4
21. hoogerland2024atemperaturesensitivemetabolic pages 6-7
22. hoogerland2024atemperaturesensitivemetabolic pages 2-3
23. lipscomb2017reversegyraseis pages 2-4
24. lipscomb2017reversegyraseis pages 1-2
25. pathania2021adaptationtocold pages 192-195
26. murata2011molecularstrategyfor pages 5-6
27. hoogerland2024atemperaturesensitivemetabolic pages 4-5
28. engqvist2018correlatingenzymeannotations pages 1-2
29. engqvist2018correlatingenzymeannotations pages 6-9
30. engqvist2018correlatingenzymeannotations pages 10-11
31. 10.1038/s41467-024-53677-5
32. 10.1007/978-981-16-2625-8_4
33. 10.37256/amtt.5220244537
34. 10.1371/journal.pone.0020063
35. 10.1128/aem.01928-22
36. 10.3389/fmicb.2023.1197797
37. 10.4314/ajcem.v24i3.1
38. 10.1098/rspb.2022.0834
39. 10.1128/mbio.03105-23
40. 10.3389/fmicb.2023.1265216
41. 10.1007/s42770-023-01057-4
42. 10.1007/s12275-023-00031-x
43. 10.1128/msystems.01124-22
44. 10.1007/s00792-017-0929-z
45. 10.1186/s12866-018-1320-7
46. 10.3390/pr8010121
47. 10.3389/fmicb.2020.00824
48. https://doi.org/10.1038/s41467-024-53677-5
49. https://doi.org/10.1007/978-981-16-2625-8_4
50. https://doi.org/10.37256/amtt.5220244537
51. https://doi.org/10.1371/journal.pone.0020063
52. https://doi.org/10.1128/aem.01928-22
53. https://doi.org/10.3389/fmicb.2023.1197797
54. https://doi.org/10.4314/ajcem.v24i3.1
55. https://doi.org/10.1098/rspb.2022.0834
56. https://doi.org/10.1128/mbio.03105-23
57. https://doi.org/10.3389/fmicb.2023.1265216
58. https://doi.org/10.1007/s42770-023-01057-4
59. https://doi.org/10.1007/s12275-023-00031-x
60. https://doi.org/10.1128/msystems.01124-22
61. https://doi.org/10.1007/s00792-017-0929-z
62. https://doi.org/10.1186/s12866-018-1320-7
63. https://doi.org/10.3390/pr8010121
64. https://doi.org/10.3389/fmicb.2020.00824
65. https://doi.org/10.3390/pr8010121,
66. https://doi.org/10.3389/fmicb.2023.1265216,
67. https://doi.org/10.1128/mbio.03105-23,
68. https://doi.org/10.1186/s12866-018-1320-7,
69. https://doi.org/10.1038/s41467-024-53677-5,
70. https://doi.org/10.1007/s00792-017-0929-z,
71. https://doi.org/10.1007/978-981-16-2625-8\_4,
72. https://doi.org/10.37256/amtt.5220244537,
73. https://doi.org/10.1371/journal.pone.0020063,
74. https://doi.org/10.4314/ajcem.v24i3.1,
75. https://doi.org/10.1098/rspb.2022.0834,
76. https://doi.org/10.1007/s42770-023-01057-4,