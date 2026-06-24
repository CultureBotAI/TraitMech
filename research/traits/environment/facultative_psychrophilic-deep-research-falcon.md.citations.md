# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative psychrophilic
- **METPO identifier:** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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
**Generated:** 2026-06-17T22:33:28.701682

1. ramon2023ageneraloverview pages 1-2
2. moyer2017psychrophilesandpsychrotrophs pages 1-2
3. purwar2024adaptationsofpsychrophilic pages 8-10
4. xiong2023wholegenomeanalysis pages 2-3
5. moyer2017psychrophilesandpsychrotrophs pages 3-5
6. ramon2023ageneraloverview pages 10-12
7. yasser2024psychrotrophicbacteriain pages 34-40
8. ramasamy2023comprehensiveinsightson pages 3-4
9. xiong2023wholegenomeanalysis pages 1-2
10. otur2024comprehensivecharacterizationand pages 1-3
11. purwar2024adaptationsofpsychrophilic pages 6-7
12. xiong2023wholegenomeanalysis pages 6-9
13. shaffer2023genomicandphenotypic pages 1-2
14. licciardello2025twoantarcticendophytic pages 1-2
15. ramasamy2023comprehensiveinsightson pages 1-2
16. label-only
17. candidate
18. broad
19. extracellular space, broad
20. candidate ice binding label-only
21. label
22. ice binding label-only if needed
23. https://doi.org/10.1007/s42770-023-01057-4
24. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
25. https://doi.org/10.37256/amtt.5220244537
26. https://doi.org/10.1038/s41598-023-41323-x
27. https://doi.org/10.1007/s11274-024-04153-1
28. https://doi.org/10.3389/fmicb.2023.1197797
29. https://doi.org/10.1007/s42770-023-01057-4,
30. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
31. https://doi.org/10.37256/amtt.5220244537,
32. https://doi.org/10.1038/s41598-023-41323-x,
33. https://doi.org/10.3389/fmicb.2023.1197797,
34. https://doi.org/10.1007/s11274-024-04153-1,
35. https://doi.org/10.3389/fmicb.2023.1156033,
36. https://doi.org/10.1007/s00300-025-03367-9,