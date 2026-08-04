# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level
- **METPO identifier:** METPO:1001101
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that categorizes biological agents according to their hazard level and required containment measures.
- **Parent traits:** METPO:1000188
- **Synonyms:** Safety information.risk assessment.biosafety level
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports pathogen virulence characteristics (transmissibility, severity, treatability) as the biological inputs underlying biosafety-level classification.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector-mediated host damage as a virulence axis informing hazard assessment.)
- **Existing causal graph summary:** biosafety_level_hazard_classification: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **biosafety level** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level.yaml`.

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
**Generated:** 2026-08-03T22:54:40.013881

1. kaufer2020laboratorybiosafetymeasures pages 3-4
2. kaufer2020laboratorybiosafetymeasures pages 4-5
3. pavone2024biologicalcontainmentfor pages 1-2
4. yu2024navigatingeskapepathogens pages 6-8
5. khairullah2024avianpathogenicescherichia pages 3-5
6. alhadlaq2024overviewofpathogenic pages 1-3
7. reem2024pseudomonasaeruginosaand pages 1-2
8. filipic2024evaluationofnovel pages 1-2
9. hartig2024influenceofenvironmental pages 1-3
10. blacksell2023thebiosafetyresearch pages 1-2
11. payne2024amethodologyfor pages 7-8
12. nguyen2024ageneticsafeguard pages 1-3
13. gomeztatay2024xenobiologyforthe pages 1-2
14. tang2024enhancinglaboratorybiosafety pages 1-2
15. george2024abumpyroad pages 1-2
16. shempela2024asituationanalysis pages 1-2
17. blacksell2023thebiosafetyresearch pages 4-5
18. payne2024amethodologyfor pages 5-7
19. blacksell2023thebiosafetyresearch pages 2-4
20. blacksell2023thebiosafetyresearch pages 7-8
21. blacksell2023thebiosafetyresearch pages 5-7
22. 10.1016/j.pathol.2020.09.006
23. 10.1089/apb.2022.0040
24. 10.1021/acsinfecdis.4c00007
25. 10.14202/vetworld.2024.2747-2762
26. 10.1186/s13099-024-00641-9
27. 10.1016/j.heliyon.2024.e29798
28. 10.3389/fcimb.2024.1370062
29. 10.1021/acs.est.4c10893
30. 10.1089/apb.2023.0025
31. 10.1101/2024.12.16.628630
32. 10.3390/life14080996
33. 10.1146/annurev.micro.62.081307.162938
34. 10.1038/s41467-023-44531-1
35. 10.3390/ani14030454
36. 10.3390/microorganisms12081697
37. 10.3389/fpubh.2024.1439051
38. https://doi.org/10.1016/j.pathol.2020.09.006
39. https://doi.org/10.1089/apb.2022.0040
40. https://doi.org/10.1021/acsinfecdis.4c00007
41. https://doi.org/10.14202/vetworld.2024.2747-2762
42. https://doi.org/10.1186/s13099-024-00641-9
43. https://doi.org/10.1016/j.heliyon.2024.e29798
44. https://doi.org/10.3389/fcimb.2024.1370062
45. https://doi.org/10.1021/acs.est.4c10893
46. https://doi.org/10.1089/apb.2023.0025
47. https://doi.org/10.1101/2024.12.16.628630
48. https://doi.org/10.3390/life14080996
49. https://doi.org/10.1146/annurev.micro.62.081307.162938
50. https://doi.org/10.1038/s41467-023-44531-1
51. https://doi.org/10.3390/ani14030454
52. https://doi.org/10.3390/microorganisms12081697
53. https://doi.org/10.3389/fpubh.2024.1439051
54. https://doi.org/10.1016/j.pathol.2020.09.006,
55. https://doi.org/10.1089/apb.2022.0040,
56. https://doi.org/10.3390/ani14030454,
57. https://doi.org/10.1021/acsinfecdis.4c00007,
58. https://doi.org/10.14202/vetworld.2024.2747-2762,
59. https://doi.org/10.1186/s13099-024-00641-9,
60. https://doi.org/10.1016/j.heliyon.2024.e29798,
61. https://doi.org/10.3389/fcimb.2024.1370062,
62. https://doi.org/10.1021/acs.est.4c10893,
63. https://doi.org/10.1089/apb.2023.0025,
64. https://doi.org/10.3390/life14080996,
65. https://doi.org/10.1101/2024.12.16.628630,
66. https://doi.org/10.3389/fpubh.2024.1439051,
67. https://doi.org/10.1038/s41467-023-44531-1,
68. https://doi.org/10.3390/microorganisms12081697,