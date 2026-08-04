# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sporulation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000870
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's ability to form dormant, stress-resistant endospores.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Physiology and metabolism.spore formation.spore formation
- **Existing evidence:** DOI:10.1146/annurev.genet.30.1.297: conversion of a growing cell into a two-cell-chamber sporangium (Supports sporulation as a developmental morphogenesis process producing a spore within a sporangium.)
- **Existing causal graph summary:** sporulation_spo0a_sigma_morphogenesis: 19 nodes, 13 edges

## Research Objective

Research the microbial trait **sporulation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sporulation.yaml`.

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
**Generated:** 2026-08-04T10:16:53.262802

1. beskrovnaya2021structuralmetabolicand pages 2-3
2. meeske2016highthroughputgeneticscreens pages 18-20
3. meeske2016highthroughputgeneticscreens pages 16-18
4. updegrove2024altruisticfeedingand pages 1-2
5. shrestha2023diversificationofdivision pages 1-2
6. gohari2024theimpactof pages 1-2
7. jun2023timecoursetranscriptomeanalysis pages 17-18
8. bidnenko2024complexsporulationspecificexpression pages 3-4
9. bidnenko2024complexsporulationspecificexpression pages 6-7
10. hasan2024roleofglycogen pages 1-3
11. updegrove2024altruisticfeedingand pages 3-4
12. gohari2024theimpactof pages 5-6
13. hasan2024roleofglycogen pages 10-13
14. hasan2024roleofglycogen pages 5-7
15. 10.1126/sciadv.adq0791
16. 10.3389/fmicb.2021.630573
17. 10.1128/mbio.02248-23
18. into
19. 10.3390/microorganisms11081928
20. 10.1371/journal.pbio.1002341
21. 10.3390/microbiolres14020035
22. 10.1038/s41467-023-43595-3
23. 10.1016/j.jbc.2024.107905
24. 10.1128/msphere.00310-24
25. 10.1146/annurev.genet.30.1.297
26. https://doi.org/10.1126/sciadv.adq0791
27. https://doi.org/10.3389/fmicb.2021.630573
28. https://doi.org/10.1128/mbio.02248-23
29. https://doi.org/10.3390/microorganisms11081928
30. https://doi.org/10.1371/journal.pbio.1002341
31. https://doi.org/10.3390/microbiolres14020035
32. https://doi.org/10.1038/s41467-023-43595-3
33. https://doi.org/10.1016/j.jbc.2024.107905
34. https://doi.org/10.1128/msphere.00310-24
35. https://doi.org/10.1146/annurev.genet.30.1.297
36. https://doi.org/10.3390/microbiolres14020035,
37. https://doi.org/10.1126/sciadv.adq0791,
38. https://doi.org/10.3389/fmicb.2021.630573,
39. https://doi.org/10.1128/mbio.02248-23,
40. https://doi.org/10.3390/microorganisms11081928,
41. https://doi.org/10.1371/journal.pbio.1002341,
42. https://doi.org/10.1038/s41467-023-43595-3,
43. https://doi.org/10.1016/j.jbc.2024.107905,
44. https://doi.org/10.1128/msphere.00310-24,