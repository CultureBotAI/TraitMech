# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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
**Generated:** 2026-08-04T03:55:42.916910

1. purwar2024adaptationsofpsychrophilic pages 3-4
2. moyer2017psychrophilesandpsychrotrophs pages 3-5
3. bao2023miningofkey pages 9-11
4. bao2023miningofkey pages 1-2
5. li2024mechanismsunderlyingthe pages 12-13
6. moyer2017psychrophilesandpsychrotrophs pages 2-3
7. gupta2023psychrophilesasa pages 9-10
8. ramon2023ageneraloverview pages 1-2
9. bao2023miningofkey pages 6-7
10. xiong2023wholegenomeanalysis pages 9-10
11. purwar2024adaptationsofpsychrophilic pages 6-7
12. bao2023miningofkey pages 11-13
13. grigorov2023dynamictranscriptionallandscape pages 15-16
14. purwar2024adaptationsofpsychrophilic pages 8-10
15. 10.1016/B978-0-12-809633-8.02282-2
16. 10.3389/fmicb.2023.1215837
17. 10.52679/tabcj.2023.0006
18. 10.3389/fmicb.2024.1465627
19. 10.1111/1751-7915.14467
20. 10.1038/s41598-023-41323-x
21. 10.37256/amtt.5220244537
22. 10.1007/s42770-023-01057-4
23. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
24. https://doi.org/10.3389/fmicb.2023.1215837
25. https://doi.org/10.52679/tabcj.2023.0006
26. https://doi.org/10.3389/fmicb.2024.1465627
27. https://doi.org/10.1111/1751-7915.14467
28. https://doi.org/10.1038/s41598-023-41323-x
29. https://doi.org/10.37256/amtt.5220244537
30. https://doi.org/10.1007/s42770-023-01057-4
31. https://doi.org/10.1007/s42770-023-01057-4,
32. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
33. https://doi.org/10.37256/amtt.5220244537,
34. https://doi.org/10.3389/fmicb.2023.1215837,
35. https://doi.org/10.1111/1751-7915.14467,
36. https://doi.org/10.3390/ijms241612706,
37. https://doi.org/10.3389/fmicb.2024.1465627,
38. https://doi.org/10.52679/tabcj.2023.0006,
39. https://doi.org/10.1038/s41598-023-41323-x,