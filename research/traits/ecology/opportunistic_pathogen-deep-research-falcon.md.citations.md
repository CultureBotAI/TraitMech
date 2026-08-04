# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** opportunistic pathogen
- **METPO identifier:** traitmech:000046
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A host-association lifestyle in which a normally commensal or environmental microorganism causes disease only when host defenses are compromised or it reaches a normally sterile site.
- **Parent traits:** METPO:1004000
- **Synonyms:** opportunistic infection
- **Existing evidence:** DOI:10.1016/j.tim.2012.04.005:  (Brown, Cornforth & Mideo, "Evolution of virulence in opportunistic pathogens", support context-dependent virulence maintained by advantages outside the host.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. support facultative shifts toward parasitism/pathogenicity along the parasite-mutualist continuum, the basis of opportunistic disease.)
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **opportunistic pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/opportunistic_pathogen.yaml`.

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
**Generated:** 2026-08-03T23:38:28.554545

1. froismartins2024candidaalbicansvirulence pages 4-5
2. burke2024thepathogenicityand pages 19-20
3. uberoi2024thewoundmicrobiota pages 1-2
4. valentine2024nanobodymediatedneutralizationof pages 1-2
5. sebastian2024leafmicrobiomedysbiosis pages 1-2
6. sebastian2024leafmicrobiomedysbiosis pages 4-5
7. chen2024combinatorialcontrolof pages 1-2
8. shahzad2024pseudomonasaeruginosaheme pages 1-2
9. bouhrour2024medicaldeviceassociatedbiofilm pages 1-2
10. jandl2024intestinalbiofilmspathophysiological pages 7-8
11. katsipoulaki2024candidaalbicansand pages 43-47
12. wang2023biofilmformationmechanistic pages 1-2
13. dekker2024withinhostevolutionof pages 12-14
14. lucidi2024pathogenicityandvirulence pages 1-2
15. sangiorgio2024theimpactof pages 1-2
16. chen2024combinatorialcontrolof pages 15-17
17. jensen2024controllingcandida pages 10-12
18. mikhailovich2024stenotrophomonasmaltophiliavirulence pages 1-2
19. 10.1007/s40588-024-00235-8
20. 10.1128/cmr.00133-23
21. 10.1128/mbio.03409-23
22. 10.1128/mmbr.00021-23
23. 10.1186/s43556-023-00164-w
24. 10.1146/annurev-pathmechdis-051122-111408
25. 10.1128/mbio.02763-23
26. 10.1080/21505594.2023.2289769
27. 10.1038/s41564-023-01555-z
28. 10.1128/msystems.00372-24
29. 10.1128/iai.00516-23
30. 10.1080/21505594.2024.2359483
31. 10.3390/pathogens13050409
32. 10.1038/s41579-024-01035-z
33. 10.3390/pathogens13050393
34. 10.3389/fmicb.2024.1385631
35. 10.1038/s41579-021-00550-7
36. 10.1016/j.tim.2012.04.005
37. https://doi.org/10.1007/s40588-024-00235-8
38. https://doi.org/10.1128/cmr.00133-23
39. https://doi.org/10.1128/mbio.03409-23
40. https://doi.org/10.1128/mmbr.00021-23
41. https://doi.org/10.1186/s43556-023-00164-w
42. https://doi.org/10.1146/annurev-pathmechdis-051122-111408
43. https://doi.org/10.1128/mbio.02763-23
44. https://doi.org/10.1080/21505594.2023.2289769
45. https://doi.org/10.1038/s41564-023-01555-z
46. https://doi.org/10.1128/msystems.00372-24
47. https://doi.org/10.1128/iai.00516-23
48. https://doi.org/10.1080/21505594.2024.2359483
49. https://doi.org/10.3390/pathogens13050409
50. https://doi.org/10.1038/s41579-024-01035-z
51. https://doi.org/10.3390/pathogens13050393
52. https://doi.org/10.3389/fmicb.2024.1385631
53. https://doi.org/10.1038/s41579-021-00550-7
54. https://doi.org/10.1016/j.tim.2012.04.005
55. https://doi.org/10.1007/s40588-024-00235-8,
56. https://doi.org/10.1080/21505594.2024.2359483,
57. https://doi.org/10.1038/s41579-024-01035-z,
58. https://doi.org/10.1128/mbio.03409-23,
59. https://doi.org/10.1128/cmr.00133-23,
60. https://doi.org/10.3389/fmicb.2024.1385631,
61. https://doi.org/10.1038/s41564-023-01555-z,
62. https://doi.org/10.1128/msystems.00372-24,
63. https://doi.org/10.1128/mbio.02763-23,
64. https://doi.org/10.3390/pathogens13050393,
65. https://doi.org/10.1128/mmbr.00021-23,
66. https://doi.org/10.1186/s43556-023-00164-w,
67. https://doi.org/10.1146/annurev-pathmechdis-051122-111408,
68. https://doi.org/10.1080/21505594.2023.2289769,
69. https://doi.org/10.3390/pathogens13050409,
70. https://doi.org/10.1128/iai.00516-23,