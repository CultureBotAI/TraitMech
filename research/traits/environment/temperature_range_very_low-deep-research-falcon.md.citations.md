# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range very low
- **METPO identifier:** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_very_low.yaml`.

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
**Generated:** 2026-06-18T02:52:57.312932

1. ramon2023ageneraloverview pages 1-2
2. purwar2024adaptationsofpsychrophilic pages 8-10
3. damico2006psychrophilicmicroorganismschallenges pages 1-2
4. jing2024transcriptomeresponseof pages 8-10
5. gupta2023psychrophilesasa pages 9-10
6. purwar2024adaptationsofpsychrophilic pages 6-7
7. li2024mechanismsunderlyingthe pages 7-9
8. ramasamy2023comprehensiveinsightson pages 3-4
9. li2024mechanismsunderlyingthe pages 5-7
10. li2024mechanismsunderlyingthe pages 9-10
11. ramasamy2023comprehensiveinsightson pages 6-7
12. wu2025applicationofantifreeze pages 5-6
13. damico2006psychrophilicmicroorganismschallenges pages 3-4
14. purwar2024adaptationsofpsychrophilic pages 1-3
15. li2024mechanismsunderlyingthe pages 1-3
16. jing2024transcriptomeresponseof pages 1-2
17. ramasamy2023comprehensiveinsightson pages 1-2
18. ramasamy2023comprehensiveinsightson pages 2-3
19. ramasamy2023comprehensiveinsightson pages 4-6
20. li2024mechanismsunderlyingthe pages 4-5
21. jing2024transcriptomeresponseof pages 4-7
22. jing2024transcriptomeresponseof pages 2-4
23. microorganisms
24. act
25. the
26. is
27. https://doi.org/10.1007/s42770-023-01057-4
28. https://doi.org/10.3389/fmicb.2023.1197797
29. https://doi.org/10.52679/tabcj.2023.0006
30. https://doi.org/10.37256/amtt.5220244537
31. https://doi.org/10.3389/fmicb.2024.1465627
32. https://doi.org/10.1007/s00227-024-04434-1
33. https://doi.org/10.1038/sj.embor.7400662
34. https://doi.org/10.3390/foods14122089
35. https://doi.org/10.1007/s42770-023-01057-4,
36. https://doi.org/10.1038/sj.embor.7400662,
37. https://doi.org/10.37256/amtt.5220244537,
38. https://doi.org/10.3389/fmicb.2023.1197797,
39. https://doi.org/10.1007/s00227-024-04434-1,
40. https://doi.org/10.3389/fmicb.2024.1465627,
41. https://doi.org/10.52679/tabcj.2023.0006,
42. https://doi.org/10.3390/foods14122089,