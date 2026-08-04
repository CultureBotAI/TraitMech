# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** viable but nonculturable state
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **viable but nonculturable state** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/viable_but_nonculturable_state.yaml`.

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
**Generated:** 2026-08-04T12:27:56.859410

1. prosdocimi2023cellphenotypechanges pages 1-2
2. pazosrojas2023theviablebut pages 11-13
3. pazosrojas2023theviablebut pages 1-2
4. yang2024resuscitationofviable pages 13-13
5. nystrom2003nonculturablebacteriaprogrammed pages 1-2
6. santos2023rolesofviable pages 4-7
7. cantlay2024phenotypicandtranscriptional pages 5-6
8. zhang2023currentperspectiveson pages 4-5
9. zhang2023currentperspectiveson pages 10-12
10. pazosrojas2023theviablebut pages 21-21
11. yang2024resuscitationofviable pages 1-2
12. yang2024resuscitationofviable pages 9-10
13. pazosrojas2023theviablebut pages 13-14
14. yang2024resuscitationofviable pages 10-13
15. pazosrojas2023theviablebut pages 4-5
16. santos2023rolesofviable pages 7-9
17. cantlay2024phenotypicandtranscriptional pages 9-10
18. cantlay2024phenotypicandtranscriptional pages 10-12
19. pazosrojas2023theviablebut pages 15-17
20. pazosrojas2023theviablebut pages 7-8
21. zhang2023currentperspectiveson pages 14-15
22. zhang2023currentperspectiveson pages 5-7
23. prosdocimi2023cellphenotypechanges pages 5-7
24. zhang2023currentperspectiveson pages 7-9
25. pazosrojas2023theviablebut pages 10-11
26. zhang2023currentperspectiveson pages 13-14
27. 10.1016/j.jare.2023.08.002
28. 10.3389/fmicb.2024.1347488
29. 10.3390/microorganisms12010039
30. 10.3390/foods12061179
31. 10.1186/s13213-022-01703-6
32. 10.3389/fcimb.2023.1122450
33. 10.3389/fcimb.2023.1185571
34. 10.1128/spectrum.03388-23
35. 10.1002/bies.10233
36. 10.3390/molecules21060790
37. 10.1016/j.molcel.2020.05.028
38. 10.1186/1745-6150-4-19
39. 10.1093/femsre/fuaf007
40. https://doi.org/10.3390/microorganisms12010039;
41. https://doi.org/10.1186/s13213-022-01703-6.
42. https://doi.org/10.1002/bies.10233.
43. https://doi.org/10.3389/fcimb.2023.1122450;
44. https://doi.org/10.3389/fmicb.2024.1347488.
45. https://doi.org/10.1016/j.jare.2023.08.002.
46. https://doi.org/10.3389/fcimb.2023.1122450.
47. https://doi.org/10.3390/foods12061179.
48. https://doi.org/10.3390/microorganisms12010039.
49. https://doi.org/10.3390/foods12061179;
50. https://doi.org/10.1016/j.jare.2023.08.002
51. https://doi.org/10.3389/fmicb.2024.1347488
52. https://doi.org/10.3390/microorganisms12010039
53. https://doi.org/10.3390/foods12061179
54. https://doi.org/10.1186/s13213-022-01703-6
55. https://doi.org/10.3389/fcimb.2023.1122450
56. https://doi.org/10.3389/fcimb.2023.1185571
57. https://doi.org/10.1128/spectrum.03388-23
58. https://doi.org/10.1002/bies.10233
59. https://doi.org/10.3390/molecules21060790
60. https://doi.org/10.1016/j.molcel.2020.05.028
61. https://doi.org/10.1186/1745-6150-4-19
62. https://doi.org/10.1093/femsre/fuaf007
63. https://doi.org/10.3390/microorganisms12010039,
64. https://doi.org/10.1186/s13213-022-01703-6,
65. https://doi.org/10.1016/j.jare.2023.08.002,
66. https://doi.org/10.1002/bies.10233,
67. https://doi.org/10.3389/fcimb.2023.1122450,
68. https://doi.org/10.3389/fmicb.2024.1347488,
69. https://doi.org/10.3390/foods12061179,