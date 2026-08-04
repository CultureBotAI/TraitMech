# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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
**Generated:** 2026-06-30T00:55:43.685549

1. brown2024acarboseimpairsgut pages 16-18
2. foley2016thesusoperon pages 2-3
3. mokhtari2013enterococcusfaecalisutilizes pages 1-2
4. dippel2005themaltodextrinsystem pages 4-5
5. dippel2005themaltodextrinsystem pages 2-2
6. foley2016thesusoperon pages 5-7
7. sidar2020carbohydratebindingmodules pages 2-3
8. mascelli2024geneticandenzymatic pages 7-8
9. dippel2005themaltodextrinsystem pages 1-2
10. davidson2010bindingproteindependentuptake pages 2-4
11. grondin2017polysaccharideutilizationloci pages 3-5
12. foley2016thesusoperon pages 8-10
13. brown2024acarboseimpairsgut pages 9-12
14. mokhtari2013enterococcusfaecalisutilizes pages 4-5
15. foley2016thesusoperon pages 1-2
16. mascelli2024geneticandenzymatic pages 12-13
17. dippel2005themaltodextrinsystem pages 7-8
18. mokhtari2013enterococcusfaecalisutilizes pages 2-4
19. mascelli2024geneticandenzymatic pages 8-10
20. davidson2010bindingproteindependentuptake pages 1-2
21. foley2016thesusoperon pages 10-12
22. foley2016thesusoperon pages 7-8
23. brown2024acarboseimpairsgut pages 1-3
24. glucose
25. is
26. 10.1007/s00018-016-2242-x
27. 10.1128/jb.00860-16
28. 10.3389/fbioe.2020.00871
29. 10.1128/jb.187.24.8322-8331.2005
30. 10.1111/mmi.12183
31. 10.1128/aem.01521-23
32. 10.1128/mbio.01506-24
33. 10.1007/s00018-023-04812-w
34. 10.1128/mbio.02599-23
35. 10.1128/msphere.00566-23
36. 10.1128/ecosalplus.3.3.3
37. 10.1016/s1369-5274(99)80034-4
38. 10.1186/1471-2164-14-873
39. 10.1016/j.jbc.2023.103038
40. 10.1016/S0168-1656(01)00407-2
41. 10.1093/nar/gkt1178
42. https://doi.org/10.1007/s00018-016-2242-x
43. https://doi.org/10.1128/jb.00860-16
44. https://doi.org/10.3389/fbioe.2020.00871
45. https://doi.org/10.1128/jb.187.24.8322-8331.2005
46. https://doi.org/10.1111/mmi.12183
47. https://doi.org/10.1128/aem.01521-23
48. https://doi.org/10.1128/mbio.01506-24
49. https://doi.org/10.1007/s00018-023-04812-w
50. https://doi.org/10.1128/mbio.02599-23
51. https://doi.org/10.1128/msphere.00566-23
52. https://doi.org/10.1128/ecosalplus.3.3.3
53. https://doi.org/10.1016/s1369-5274(99
54. https://doi.org/10.1186/1471-2164-14-873
55. https://doi.org/10.1016/j.jbc.2023.103038
56. https://doi.org/10.1016/S0168-1656(01
57. https://doi.org/10.1093/nar/gkt1178
58. https://doi.org/10.1007/s00018-016-2242-x,
59. https://doi.org/10.3389/fbioe.2020.00871,
60. https://doi.org/10.1128/mbio.01506-24,
61. https://doi.org/10.1128/jb.187.24.8322-8331.2005,
62. https://doi.org/10.1128/aem.01521-23,
63. https://doi.org/10.1111/mmi.12183,
64. https://doi.org/10.1128/jb.00860-16,
65. https://doi.org/10.1128/ecosalplus.3.3.3,