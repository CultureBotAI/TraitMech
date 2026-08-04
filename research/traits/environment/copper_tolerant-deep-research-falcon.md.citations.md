# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copper tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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
**Generated:** 2026-08-04T00:39:31.808199

1. andrei2020cuhomeostasisin pages 16-19
2. virieuxpetit2022fromcoppertolerance pages 8-9
3. wong2023coppereffluxsystem pages 10-12
4. hirth2023fullcopperresistance pages 16-18
5. rebelo2023unravelingtherole pages 6-8
6. giachino2020coppertolerancein pages 3-5
7. bittner2017thecopperefflux pages 1-2
8. hyre2021copperhomeostaticmechanisms pages 2-4
9. virieuxpetit2022fromcoppertolerance pages 5-7
10. rismondo2023thesensoryhistidine pages 8-10
11. rismondo2023thesensoryhistidine pages 1-2
12. rismondo2023thesensoryhistidine pages 5-8
13. yu2024isolationofhighly pages 4-6
14. yu2024isolationofhighly pages 1-2
15. gillieatt2024unravellingthemechanisms pages 10-11
16. gillieatt2024unravellingthemechanisms pages 11-13
17. hirth2023fullcopperresistance pages 14-16
18. hirth2023fullcopperresistance pages 1-3
19. arguello2013mechanismsofcopper pages 3-4
20. hirth2023fullcopperresistance pages 7-9
21. andrei2020cuhomeostasisin pages 19-21
22. gautam2023linkingcopperassociatedsignal pages 3-5
23. andrei2020cuhomeostasisin pages 10-12
24. chaturvedi2014pathogenicadaptationsto pages 6-7
25. andrei2020cuhomeostasisin pages 21-23
26. rismondo2023thesensoryhistidine pages 2-5
27. hirth2023fullcopperresistance pages 11-12
28. yu2024isolationofhighly pages 2-3
29. hirth2023fullcopperresistance pages 4-6
30. hirth2023fullcopperresistance pages 9-11
31. hirth2023fullcopperresistance pages 3-4
32. virieuxpetit2022fromcoppertolerance pages 4-5
33. gillieatt2024unravellingthemechanisms pages 9-10
34. 10.3389/fmolb.2017.00009
35. 10.1128/ecosalplus.esp-0014-2020
36. 10.3390/genes13020301
37. 10.3390/membranes10090242
38. 10.1128/aem.00567-23
39. 10.1128/spectrum.00291-23
40. 10.3389/fmicb.2024.1390451
41. 10.1128/iai.00091-23
42. https://doi.org/10.1128/aem.00567-23
43. https://doi.org/10.1128/spectrum.00291-23
44. https://doi.org/10.1128/iai.00091-23
45. https://doi.org/10.3389/fmicb.2024.1390451
46. https://doi.org/10.1093/femsre/fuae017
47. https://doi.org/10.3390/antibiotics12091474
48. https://doi.org/10.1111/mmi.14522
49. https://doi.org/10.3390/membranes10090242
50. https://doi.org/10.1128/ecosalplus.esp-0014-2020
51. https://doi.org/10.3389/fcimb.2013.00073
52. https://doi.org/10.3390/genes13020301
53. https://doi.org/10.3389/fmolb.2017.00009
54. https://doi.org/10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23
55. https://doi.org/10.1128/spectrum.00291-23](https://doi.org/10.1128/spectrum.00291-23
56. https://doi.org/10.1128/iai.00091-23](https://doi.org/10.1128/iai.00091-23
57. https://doi.org/10.3389/fmicb.2024.1390451](https://doi.org/10.3389/fmicb.2024.1390451
58. https://doi.org/10.1093/femsre/fuae017](https://doi.org/10.1093/femsre/fuae017
59. https://doi.org/10.3390/antibiotics12091474](https://doi.org/10.3390/antibiotics12091474
60. https://doi.org/10.1111/mmi.14522](https://doi.org/10.1111/mmi.14522
61. https://doi.org/10.3390/membranes10090242](https://doi.org/10.3390/membranes10090242
62. https://doi.org/10.1128/ecosalplus.esp-0014-2020](https://doi.org/10.1128/ecosalplus.esp-0014-2020
63. https://doi.org/10.3389/fcimb.2013.00073](https://doi.org/10.3389/fcimb.2013.00073
64. https://doi.org/10.3390/genes13020301](https://doi.org/10.3390/genes13020301
65. https://doi.org/10.3389/fmolb.2017.00009](https://doi.org/10.3389/fmolb.2017.00009
66. https://doi.org/10.1128/aem.00567-23,
67. https://doi.org/10.3390/membranes10090242,
68. https://doi.org/10.3390/genes13020301,
69. https://doi.org/10.1128/spectrum.00291-23,
70. https://doi.org/10.3389/fmicb.2024.1390451,
71. https://doi.org/10.3390/antibiotics12091474,
72. https://doi.org/10.1128/ecosalplus.esp-0014-2020,
73. https://doi.org/10.3389/fmolb.2017.00009,
74. https://doi.org/10.13016/m2gdm3-y5hr,
75. https://doi.org/10.1111/mmi.14522,
76. https://doi.org/10.3389/fcimb.2014.00003,
77. https://doi.org/10.1128/iai.00091-23,
78. https://doi.org/10.1093/femsre/fuae017,
79. https://doi.org/10.3389/fcimb.2013.00073,