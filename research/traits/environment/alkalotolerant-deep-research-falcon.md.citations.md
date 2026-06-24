# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkalotolerant
- **METPO identifier:** METPO:1003009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkalitolerant
- **Existing evidence:** DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis phenotype.)
- **Existing causal graph summary:** alkalotolerant_alkaline_stress_homeostasis: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **alkalotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkalotolerant.yaml`.

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
**Generated:** 2026-06-17T21:46:25.290132

1. chia2025roleofextremophiles pages 6-8
2. xing2024thepolyextremophilenatranaerobius pages 1-2
3. horikoshi1999alkaliphilessomeapplications pages 4-5
4. foreman2021geneticandbiochemical pages 12-13
5. wang2023characterizationoftwo pages 16-16
6. horikoshi2016alkaliphiles pages 2-5
7. sawatari2007diversityandmechanisms pages 3-5
8. sawatari2007diversityandmechanisms pages 6-7
9. he2025coinoculationofbacillus pages 1-2
10. horikoshi1999alkaliphilessomeapplications pages 1-3
11. gondal2021adaptabilityofsoil pages 3-4
12. horikoshi2016alkaliphiles pages 1-2
13. wang2023salinealkalisoilproperty pages 1-2
14. sawatari2007diversityandmechanisms pages 1-1
15. xing2024thepolyextremophilenatranaerobius pages 10-14
16. thompson2023insightsintothe pages 5-7
17. H+
18. https://doi.org/10.1128/MMBR.63.4.735-750.1999
19. https://doi.org/10.1007/978-4-431-55408-0_4
20. https://doi.org/10.18488/journal.68.2021.82.71.79
21. https://doi.org/10.1128/AEM.02834-06
22. https://doi.org/10.1007/s11244-024-01919-7
23. https://doi.org/10.1128/AEM.00145-24
24. https://doi.org/10.3390/ijms23169156
25. https://doi.org/10.1128/JB.00284-21
26. https://doi.org/10.3390/ijms241310786
27. https://doi.org/10.3390/ijms24097737
28. https://doi.org/10.3389/fmicb.2023.1179857
29. https://doi.org/10.3390/ijms23169156;
30. https://doi.org/10.1128/JB.00284-21;
31. https://doi.org/10.1128/MMBR.63.4.735-750.1999;
32. https://doi.org/10.1007/978-4-431-55408-0_4;
33. https://doi.org/10.1128/AEM.02834-06;
34. https://doi.org/10.1128/AEM.00145-24;
35. https://doi.org/10.1007/s11244-024-01919-7;
36. https://doi.org/10.1128/aem.00145-24
37. https://doi.org/10.1128/jb.00284-21
38. https://doi.org/10.1128/aem.02834-06
39. https://doi.org/10.1128/mmbr.63.4.735-750.1999
40. https://doi.org/10.3389/fpls.2025.1677763
41. https://doi.org/10.3390/ijms25115785
42. https://doi.org/10.1128/mmbr.63.4.735-750.1999,
43. https://doi.org/10.18488/journal.68.2021.82.71.79,
44. https://doi.org/10.1007/978-4-431-55408-0\_4,
45. https://doi.org/10.3389/fmicb.2023.1179857,
46. https://doi.org/10.1128/aem.02834-06,
47. https://doi.org/10.3390/ijms23169156,
48. https://doi.org/10.1128/jb.00284-21,
49. https://doi.org/10.1007/s11244-024-01919-7,
50. https://doi.org/10.1128/aem.00145-24,
51. https://doi.org/10.3390/ijms241310786,
52. https://doi.org/10.3390/ijms24097737,
53. https://doi.org/10.3389/fpls.2025.1677763,
54. https://doi.org/10.3390/ijms25115785,