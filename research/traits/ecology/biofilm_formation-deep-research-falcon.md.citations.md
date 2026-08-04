# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biofilm formation
- **METPO identifier:** traitmech:000053
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which cells form surface-attached, matrix-enclosed multicellular communities (biofilms) held together by extracellular polymeric substances — a widespread mode of microbial life.
- **Parent traits:** METPO:1000059
- **Synonyms:** biofilm-forming
- **Existing evidence:** DOI:10.1038/nrmicro.2016.94:  (Flemming et al. describe matrix-enclosed, surface-associated communities (biofilms) as an emergent, distinct mode of bacterial life.) | DOI:10.1038/s41579-019-0162-0:  (Flemming & Wuertz support the global ubiquity of the biofilm lifestyle across microbial habitats.)
- **Existing causal graph summary:** biofilm_eps_matrix_community: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **biofilm formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biofilm_formation.yaml`.

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
**Generated:** 2026-08-03T22:59:21.897353

1. goltermann2024microbialprimerthe pages 1-3
2. bohning2024theroleof pages 1-2
3. kovacs2019evolvedbiofilmreview pages 1-3
4. yang2024classicalandmodern pages 1-2
5. whitfield2020pelpolysaccharidebiosynthesis pages 1-2
6. yaeger2024ageneticscreen pages 1-2
7. wang2023biofilmformationmechanistic pages 10-11
8. saunders2020extracellulardnapromotes pages 1-3
9. bancucerzan2025persistentthreatsa pages 2-4
10. park2022controllingbiofilmdevelopment pages 1-2
11. park2022controllingbiofilmdevelopment pages 7-9
12. valentini2016biofilmsandcyclic pages 1-2
13. mishra2024medicaldeviceassociatedinfections pages 1-2
14. shineh2023biofilmformationand pages 1-2
15. sahoo2024biofilmformationin pages 2-3
16. 10.1007/978-3-031-08491-1_3
17. 10.1074/jbc.R115.711507
18. 10.1042/BCJ20210301
19. 10.1038/s41522-024-00496-7
20. 10.1128/JB.00684-19
21. 10.1186/s43556-023-00164-w
22. 10.3390/antibiotics13070623
23. 10.1016/j.jmb.2019.02.005
24. 10.1016/j.cell.2020.07.006
25. 10.1099/mic.0.001497
26. 10.3390/antibiotics13121228
27. 10.3390/applmicrobiol3030044
28. 10.1016/j.cell.2021.10.010
29. https://doi.org/10.1007/978-3-031-08491-1_3
30. https://doi.org/10.1074/jbc.R115.711507
31. https://doi.org/10.1042/BCJ20210301
32. https://doi.org/10.1038/s41522-024-00496-7
33. https://doi.org/10.1128/JB.00684-19
34. https://doi.org/10.1186/s43556-023-00164-w
35. https://doi.org/10.3390/antibiotics13070623
36. https://doi.org/10.1016/j.jmb.2019.02.005
37. https://doi.org/10.1016/j.cell.2020.07.006
38. https://doi.org/10.1099/mic.0.001497
39. https://doi.org/10.3390/antibiotics13121228
40. https://doi.org/10.3390/applmicrobiol3030044
41. https://doi.org/10.1016/j.cell.2021.10.010
42. https://doi.org/10.1099/mic.0.001497,
43. https://doi.org/10.1042/bcj20210301,
44. https://doi.org/10.1007/978-3-031-08491-1\_3,
45. https://doi.org/10.7759/cureus.70629,
46. https://doi.org/10.1016/j.jmb.2019.02.005,
47. https://doi.org/10.3390/antibiotics13121228,
48. https://doi.org/10.1074/jbc.r115.711507,
49. https://doi.org/10.1186/s43556-023-00164-w,
50. https://doi.org/10.1128/jb.00684-19,
51. https://doi.org/10.1038/s41522-024-00496-7,
52. https://doi.org/10.1016/j.cell.2020.07.006,
53. https://doi.org/10.3390/microorganisms13081805,
54. https://doi.org/10.3390/antibiotics13070623,
55. https://doi.org/10.3390/applmicrobiol3030044,