# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range low
- **METPO identifier:** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_low.yaml`.

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
**Generated:** 2026-06-18T02:38:33.314668

1. ramon2023ageneraloverview pages 1-2
2. purwar2024adaptationsofpsychrophilic pages 1-3
3. son2023morphologicalandphysiological pages 2-3
4. hu2023comparativegenomicanalysis pages 8-11
5. yang2023insightintothe pages 2-4
6. purwar2024adaptationsofpsychrophilic pages 8-10
7. purwar2024adaptationsofpsychrophilic pages 10-11
8. son2023morphologicalandphysiological pages 1-2
9. son2023morphologicalandphysiological pages 7-7
10. yang2023insightintothe pages 4-7
11. liu2023psychrophilicyeastsinsights pages 4-5
12. ramasamy2023comprehensiveinsightson pages 3-4
13. purwar2024adaptationsofpsychrophilic pages 6-7
14. yang2023insightintothe pages 1-2
15. son2023morphologicalandphysiological pages 3-4
16. gupta2023psychrophilesasa pages 9-10
17. hu2023comparativegenomicanalysis pages 7-8
18. son2023morphologicalandphysiological pages 4-7
19. hu2023comparativegenomicanalysis pages 12-14
20. https://doi.org/10.37256/amtt.5220244537;
21. https://doi.org/10.1007/s42770-023-01057-4
22. https://doi.org/10.3390/genes14010158
23. https://doi.org/10.37256/amtt.5220244537
24. https://doi.org/10.1128/aem.01928-22
25. https://doi.org/10.1186/s12864-023-09638-1;
26. https://doi.org/10.3389/fmicb.2023.1197797;
27. https://doi.org/10.1038/s41598-023-42179-x
28. https://doi.org/10.1186/s12864-023-09638-1
29. https://doi.org/10.3389/fmicb.2023.1197797
30. https://doi.org/10.1111/1751-7915.14467
31. https://doi.org/10.1007/s42770-023-01057-4,
32. https://doi.org/10.37256/amtt.5220244537,
33. https://doi.org/10.1038/s41598-023-42179-x,
34. https://doi.org/10.3389/fmicb.2023.1197797,
35. https://doi.org/10.1186/s12864-023-09638-1,
36. https://doi.org/10.1128/aem.01928-22,
37. https://doi.org/10.1111/1751-7915.14467,
38. https://doi.org/10.3390/genes14010158,
39. https://doi.org/10.52679/tabcj.2023.0006,