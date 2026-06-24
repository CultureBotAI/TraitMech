# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methylotrophic
- **METPO identifier:** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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
**Generated:** 2026-06-18T12:16:03.074915

1. samanta2024fromgenometo pages 18-20
2. orsi2023synergisticinvestigationof pages 1-2
3. schmider2024physiologicalbasisfor pages 6-7
4. mitic2023theoxygentolerantreductive pages 1-2
5. gorniak2024changesingrowth pages 1-2
6. samanta2024fromgenometo pages 12-14
7. zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2
8. schann2024designconstructionand pages 1-2
9. li2024aeukaryotefeaturedmembrane pages 1-2
10. ahmadi2024recentfindingsin pages 7-9
11. rasmussen2024diverseandunconventional pages 1-2
12. wu2023engineeringasynthetic pages 1-2
13. wang2024metabolicengineeringof pages 2-4
14. samanta2024fromgenometo pages 16-18
15. phi2024assessinglanthanidedependentmethanol pages 21-24
16. warters2024widespreadbacterialuse pages 9-13
17. kamachi2025switchingbetweenmethanol pages 1-2
18. voutsinos2024weatheredgranitesand pages 1-2
19. tucci2024directmethaneoxidation pages 38-40
20. ahmadi2024recentfindingsin pages 1-2
21. voutsinos2024weatheredgranitesand pages 4-7
22. voutsinos2024weatheredgranitesand pages 2-4
23. voutsinos2024weatheredgranitesand pages 12-14
24. orsi2023synergisticinvestigationof pages 2-4
25. orsi2023synergisticinvestigationof pages 5-6
26. shao2024transcriptomicdatareveals pages 1-2
27. schann2024theserineshunt pages 1-6
28. orsi2023synergisticinvestigationof pages 4-4
29. shao2024transcriptomicdatareveals pages 2-4
30. kamachi2025switchingbetweenmethanol pages 10-10
31. voutsinos2024weatheredgranitesand pages 17-18
32. voutsinos2024weatheredgranitesand pages 16-17
33. warters2024widespreadbacterialuse pages 39-41
34. voutsinos2024weatheredgranitesand pages 10-12
35. sun2023engineeringandadaptive pages 12-12
36. https://doi.org/10.1128/msystems.00248-24
37. https://doi.org/10.1128/msystems.00314-24
38. https://doi.org/10.1038/s41467-023-43610-7
39. https://doi.org/10.1038/s41467-023-43610-7;
40. https://doi.org/10.1186/s12934-024-02475-1
41. https://doi.org/10.1128/aem.02090-23;
42. https://doi.org/10.1038/s41467-024-48197-1
43. https://doi.org/10.1007/s00284-022-03141-8
44. https://doi.org/10.5282/edoc.33507
45. https://doi.org/10.1128/msphere.00685-24
46. https://doi.org/10.1016/b978-0-443-13307-7.00014-1
47. https://doi.org/10.1186/s12915-024-01841-0
48. https://doi.org/10.1021/acssynbio.4c00499
49. https://doi.org/10.1111/1751-7915.14527
50. https://doi.org/10.1007/s00253-023-12978-3
51. https://doi.org/10.1038/s41467-023-42166-w
52. https://doi.org/10.1038/s41467-023-44247-2
53. https://doi.org/10.1038/s41467-024-50342-9
54. https://doi.org/10.1021/acs.chemrev.3c00727
55. https://doi.org/10.1128/msystems.00248-24,
56. https://doi.org/10.1007/s00253-023-12978-3,
57. https://doi.org/10.1038/s41467-024-48197-1,
58. https://doi.org/10.1038/s41467-023-42166-w,
59. https://doi.org/10.1038/s41467-023-43610-7,
60. https://doi.org/10.1128/msphere.00685-24,
61. https://doi.org/10.1186/s12915-024-01841-0,
62. https://doi.org/10.1038/s41467-024-50342-9,
63. https://doi.org/10.1111/1751-7915.14527,
64. https://doi.org/10.1021/acssynbio.4c00499,
65. https://doi.org/10.1128/msystems.00314-24,
66. https://doi.org/10.1186/s12864-024-10923-w,
67. https://doi.org/10.1038/s41467-023-44247-2,
68. https://doi.org/10.1101/2024.07.31.605843,
69. https://doi.org/10.1186/s12934-024-02475-1,
70. https://doi.org/10.1007/s00284-022-03141-8,
71. https://doi.org/10.1016/b978-0-443-13307-7.00014-1,
72. https://doi.org/10.1021/acs.chemrev.3c00727,
73. https://doi.org/10.3389/fbioe.2022.1089639,