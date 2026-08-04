# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_very_low.yaml`.

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
**Generated:** 2026-08-04T04:10:37.773506

1. ramon2023ageneraloverview pages 1-2
2. moyer2017psychrophilesandpsychrotrophs pages 1-2
3. bao2023miningofkey pages 1-2
4. li2024mechanismsunderlyingthe pages 12-13
5. moyer2017psychrophilesandpsychrotrophs pages 2-3
6. moyer2017psychrophilesandpsychrotrophs pages 3-5
7. purwar2024adaptationsofpsychrophilic pages 3-4
8. purwar2024adaptationsofpsychrophilic pages 6-7
9. purwar2024adaptationsofpsychrophilic pages 8-10
10. li2024mechanismsunderlyingthe pages 10-12
11. bao2023miningofkey pages 6-7
12. label-only
13. GO:0016020
14. GO:0009409
15. CHEBI label-only
16. GO:0006810
17. GO:0022900
18. GO:0003824
19. CHEBI:26220
20. GO:0061077
21. GO:0016070
22. EC 1.11.1.6
23. EC 1.15.1.1
24. CHEBI:26523
25. UniProt family label-only
26. GO:0006457
27. GO:0042254
28. GO:0006412
29. 10.3389/fmicb.2024.1465627
30. 10.37256/amtt.5220244537
31. 10.3389/fmicb.2023.1215837
32. 10.1007/s42770-023-01057-4
33. 10.1016/B978-0-12-809633-8.02282-2
34. 10.1038/sj.embor.7400662
35. https://doi.org/10.3389/fmicb.2024.1465627
36. https://doi.org/10.37256/amtt.5220244537
37. https://doi.org/10.3389/fmicb.2023.1215837
38. https://doi.org/10.1007/s42770-023-01057-4
39. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
40. https://doi.org/10.1038/sj.embor.7400662
41. https://doi.org/10.1007/s42770-023-01057-4,
42. https://doi.org/10.3389/fmicb.2023.1215837,
43. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
44. https://doi.org/10.37256/amtt.5220244537,
45. https://doi.org/10.3389/fmicb.2024.1465627,