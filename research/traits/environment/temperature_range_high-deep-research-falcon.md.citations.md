# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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
**Generated:** 2026-08-04T04:24:22.828778

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. zhou2021acoldshock pages 5-6
3. ezemaduka2014asmallheat pages 3-4
4. ezemaduka2014asmallheat pages 6-7
5. sato2024effectsofsmall pages 1-2
6. baes2023transcriptionalandtranslational pages 15-17
7. grunberger2023uncoveringthetemporal pages 2-4
8. chong2024archaeamembranesin pages 2-3
9. chong2024archaeamembranesin pages 1-2
10. borges2010thermococcuskodakarensis pages 5-6
11. esteves2014mannosylglycerateanddi pages 9-12
12. chiu2023membranelipidand pages 1-2
13. lipscomb2017reversegyraseis pages 1-2
14. atomi2004reversegyraseis pages 3-5
15. zhou2021acoldshock pages 1-2
16. ezemaduka2014asmallheat pages 1-2
17. borges2010thermococcuskodakarensis pages 1-2
18. esteves2014mannosylglycerateanddi pages 1-5
19. siliakus2017adaptationsofarchaeal pages 8-10
20. mondal2024aquificaeovercomescompetition pages 1-2
21. mondal2024aquificaeovercomescompetition pages 23-24
22. lipscomb2017reversegyraseis pages 2-4
23. lipscomb2017reversegyraseis pages 4-5
24. zhou2021acoldshock pages 2-5
25. ezemaduka2014asmallheat pages 5-6
26. esteves2014mannosylglycerateanddi pages 20-28
27. esteves2014mannosylglycerateanddi pages 16-20
28. esteves2014mannosylglycerateanddi pages 12-16
29. chong2024archaeamembranesin pages 3-4
30. atomi2004reversegyraseis pages 1-2
31. borges2010thermococcuskodakarensis pages 3-4
32. mondal2024aquificaeovercomescompetition pages 24-26
33. mondal2024aquificaeovercomescompetition pages 26-28
34. 10.1007/s00792-017-0929-z
35. 10.1128/JB.186.14.4829-4833.2004
36. 10.1038/s41421-021-00246-5
37. 10.1128/JB.01473-14
38. 10.1007/s00792-023-01326-y
39. 10.1128/mbio.03593-22
40. 10.1128/mbio.02174-23
41. 10.3389/frbis.2023.1338019
42. 10.1128/JB.01115-09
43. 10.1128/AEM.00559-14
44. 10.3389/fmicb.2023.1265216
45. 10.3389/fmicb.2023.1219779
46. 10.1007/s00792-017-0939-x
47. 10.1371/journal.pone.0310595
48. https://doi.org/10.1007/s00792-017-0929-z
49. https://doi.org/10.1128/JB.186.14.4829-4833.2004
50. https://doi.org/10.1038/s41421-021-00246-5
51. https://doi.org/10.1128/JB.01473-14
52. https://doi.org/10.1007/s00792-023-01326-y
53. https://doi.org/10.1128/mbio.03593-22
54. https://doi.org/10.1128/mbio.02174-23
55. https://doi.org/10.3389/frbis.2023.1338019
56. https://doi.org/10.1128/JB.01115-09
57. https://doi.org/10.1128/AEM.00559-14
58. https://doi.org/10.3389/fmicb.2023.1265216
59. https://doi.org/10.3389/fmicb.2023.1219779
60. https://doi.org/10.1007/s00792-017-0939-x
61. https://doi.org/10.1371/journal.pone.0310595
62. https://doi.org/10.3389/fmicb.2023.1265216,
63. https://doi.org/10.1371/journal.pone.0310595,
64. https://doi.org/10.1007/s00792-017-0929-z,
65. https://doi.org/10.1038/s41421-021-00246-5,
66. https://doi.org/10.1128/jb.01473-14,
67. https://doi.org/10.1128/aem.00559-14,
68. https://doi.org/10.3389/frbis.2023.1338019,
69. https://doi.org/10.1128/jb.186.14.4829-4833.2004,
70. https://doi.org/10.1007/s00792-023-01326-y,
71. https://doi.org/10.1128/mbio.03593-22,
72. https://doi.org/10.1128/mbio.02174-23,
73. https://doi.org/10.1128/jb.01115-09,
74. https://doi.org/10.3389/fmicb.2023.1219779,
75. https://doi.org/10.1007/s00792-017-0939-x,
76. https://doi.org/10.1101/2023.07.10.548480,