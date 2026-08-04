# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** brown pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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
**Generated:** 2026-08-04T07:28:30.974281

1. schmalerripcke2009productionofpyomelanin pages 1-2
2. elzawawy2024bioproductionandoptimization pages 1-2
3. hunter2010aputativeabc pages 5-6
4. ahmad2016geneticdeterminantsfor pages 1-2
5. qin2024melanininfungi pages 2-4
6. urbaniak2023invitroand pages 1-2
7. wang2015identificationandmolecular pages 1-2
8. moustafa2024mutationofhmga pages 1-2
9. hunter2010aputativeabc pages 1-2
10. jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2
11. pavan2020melaninbiosynthesisin pages 3-4
12. lorquin2022newinsightsand pages 19-19
13. wang2015identificationandmolecular pages 9-11
14. moustafa2024mutationofhmga pages 4-7
15. moustafa2024mutationofhmga pages 9-11
16. moustafa2024mutationofhmga pages 2-4
17. moustafa2024mutationofhmga pages 7-9
18. 10.1128/spectrum.00410-24
19. 10.1186/s12934-024-02614-8
20. 10.1186/s12934-023-02276-y
21. 10.3390/ijms24097846
22. 10.1093/jimb/kuac013
23. 10.3389/fmicb.2021.733612
24. 10.1007/s00253-019-10245-y
25. 10.1371/journal.pone.0160845
26. 10.1371/journal.pone.0120923
27. 10.1128/JB.01021-10
28. 10.1128/AEM.02077-08
29. 10.1128/AEM.67.8.3463-3468.2001
30. https://doi.org/10.1128/spectrum.00410-24
31. https://doi.org/10.1186/s12934-024-02614-8
32. https://doi.org/10.1186/s12934-023-02276-y
33. https://doi.org/10.3390/ijms24097846
34. https://doi.org/10.1093/jimb/kuac013
35. https://doi.org/10.3389/fmicb.2021.733612
36. https://doi.org/10.1007/s00253-019-10245-y
37. https://doi.org/10.1371/journal.pone.0160845
38. https://doi.org/10.1371/journal.pone.0120923
39. https://doi.org/10.1128/JB.01021-10
40. https://doi.org/10.1128/AEM.02077-08
41. https://doi.org/10.1128/AEM.67.8.3463-3468.2001
42. https://doi.org/10.1371/journal.pone.0120923,
43. https://doi.org/10.1007/s00253-019-10245-y,
44. https://doi.org/10.1128/aem.02077-08,
45. https://doi.org/10.1128/jb.01021-10,
46. https://doi.org/10.3390/ijms24097846,
47. https://doi.org/10.1371/journal.pone.0160845,
48. https://doi.org/10.1128/spectrum.00410-24,
49. https://doi.org/10.3389/fmicb.2021.733612,
50. https://doi.org/10.1186/s12934-023-02276-y,
51. https://doi.org/10.1186/s12934-024-02614-8,
52. https://doi.org/10.1101/2024.04.11.589128,
53. https://doi.org/10.1093/jimb/kuac013,