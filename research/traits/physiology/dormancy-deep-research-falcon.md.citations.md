# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dormancy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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
**Generated:** 2026-08-04T11:20:11.470259

1. carvalho2024aquaticenvironmentdrives pages 1-2
2. dhaouadi2024persistenceandculturability pages 1-2
3. blattman2024identificationandgenetic pages 1-2
4. yang2024resuscitationofviable pages 1-2
5. sexton2020rolesoflysm pages 1-2
6. gou2024viablebutnonculturable pages 1-2
7. carvalho2024aquaticenvironmentdrives pages 3-4
8. imminger2024survivalandrapid pages 3-4
9. carvalho2024aquaticenvironmentdrives pages 2-3
10. imminger2024survivalandrapid pages 1-2
11. yang2024resuscitationofviable pages 2-4
12. blattman2024identificationandgenetic pages 3-4
13. imminger2024survivalandrapid pages 2-3
14. li2024resuscitationpromotionfactor pages 1-3
15. keep2006bacterialresuscitationfactors pages 1-2
16. carvalho2024aquaticenvironmentdrives pages 15-16
17. sexton2020rolesoflysm pages 10-11
18. gou2024viablebutnonculturable pages 2-3
19. blattman2024identificationandgenetic pages 2-3
20. blattman2024identificationandgenetic pages 4-5
21. dhaouadi2024persistenceandculturability pages 2-4
22. li2024resuscitationpromotionfactor pages 3-6
23. dhaouadi2024persistenceandculturability pages 15-16
24. yang2024resuscitationofviable pages 13-13
25. with
26. 10.1038/s41467-024-52633-7
27. 10.1038/s41586-024-08124-2
28. 10.1016/j.jare.2023.08.002
29. 10.1038/s41467-024-46920-6
30. 10.3389/fcimb.2024.1486426
31. 10.3390/antibiotics13090863
32. 10.3390/microorganisms12081528
33. 10.1038/s41392-024-01866-5
34. 10.1186/s12866-024-03628-3
35. 10.1093/ismejo/wrae179
36. 10.1074/jbc.ra120.013994
37. 10.1007/s00018-006-6188-2
38. 10.3390/foods12010082
39. 10.1007/s12088-011-0202-6
40. 10.1093/femsre/fux001
41. 10.1038/nrmicro.2016.107
42. 10.3389/fmicb.2020.601417
43. 10.3390/microorganisms10122334
44. 10.1111/j.1574-6976.2012.00331.x
45. 10.1128/jb.00307-19
46. https://doi.org/10.1038/s41467-024-52633-7
47. https://doi.org/10.1038/s41586-024-08124-2
48. https://doi.org/10.1016/j.jare.2023.08.002
49. https://doi.org/10.1038/s41467-024-46920-6
50. https://doi.org/10.3389/fcimb.2024.1486426
51. https://doi.org/10.3390/antibiotics13090863
52. https://doi.org/10.3390/microorganisms12081528
53. https://doi.org/10.1038/s41392-024-01866-5
54. https://doi.org/10.1186/s12866-024-03628-3
55. https://doi.org/10.1093/ismejo/wrae179
56. https://doi.org/10.1074/jbc.ra120.013994
57. https://doi.org/10.1007/s00018-006-6188-2
58. https://doi.org/10.3390/foods12010082
59. https://doi.org/10.1007/s12088-011-0202-6
60. https://doi.org/10.1093/femsre/fux001
61. https://doi.org/10.1038/nrmicro.2016.107
62. https://doi.org/10.3389/fmicb.2020.601417
63. https://doi.org/10.3390/microorganisms10122334
64. https://doi.org/10.1111/j.1574-6976.2012.00331.x
65. https://doi.org/10.1128/jb.00307-19
66. https://doi.org/10.1038/s41467-024-52633-7,
67. https://doi.org/10.1038/s41586-024-08124-2,
68. https://doi.org/10.1016/j.jare.2023.08.002,
69. https://doi.org/10.1038/s41467-024-46920-6,
70. https://doi.org/10.3389/fcimb.2024.1486426,
71. https://doi.org/10.1007/s00018-006-6188-2,
72. https://doi.org/10.1074/jbc.ra120.013994,
73. https://doi.org/10.3390/antibiotics13090863,
74. https://doi.org/10.3390/microorganisms12081528,