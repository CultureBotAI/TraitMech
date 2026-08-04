# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 15 nodes, 8 edges

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
**Generated:** 2026-08-04T04:33:36.833193

1. wang2024genomicinsightsinto pages 11-12
2. moyer2017psychrophilesandpsychrotrophs pages 2-3
3. son2023morphologicalandphysiological pages 1-2
4. riccardi2023metabolicrobustnessto pages 1-2
5. li2024mechanismsunderlyingthe pages 12-13
6. li2024mechanismsunderlyingthe pages 5-7
7. bao2023miningofkey pages 1-2
8. ramon2023ageneraloverview pages 4-5
9. purwar2024adaptationsofpsychrophilic pages 1-3
10. ramon2023ageneraloverview pages 1-2
11. li2024mechanismsunderlyingthe pages 1-3
12. son2023morphologicalandphysiological pages 3-4
13. moyer2017psychrophilesandpsychrotrophs pages 3-5
14. 10.3389/fmicb.2024.1465627
15. 10.1007/s42770-023-01057-4
16. 10.1128/JB.01377-08
17. 10.1128/msystems.01124-22
18. 10.1038/s41598-023-42179-x
19. 10.3389/fmicb.2023.1215837
20. 10.3389/fmicb.2024.1459716
21. 10.1016/B978-0-12-809633-8.02282-2
22. 10.1038/sj.embor.7400662
23. https://doi.org/10.3389/fmicb.2024.1465627
24. https://doi.org/10.1007/s42770-023-01057-4
25. https://doi.org/10.1128/JB.01377-08
26. https://doi.org/10.1128/msystems.01124-22
27. https://doi.org/10.1038/s41598-023-42179-x
28. https://doi.org/10.3389/fmicb.2023.1215837
29. https://doi.org/10.3389/fmicb.2024.1459716
30. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
31. https://doi.org/10.1038/sj.embor.7400662
32. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
33. https://doi.org/10.37256/amtt.5220244537,
34. https://doi.org/10.1007/s42770-023-01057-4,
35. https://doi.org/10.3389/fmicb.2024.1459716,
36. https://doi.org/10.1038/s41598-023-42179-x,
37. https://doi.org/10.1128/msystems.01124-22,
38. https://doi.org/10.3389/fmicb.2023.1215837,
39. https://doi.org/10.1128/jb.01377-08,
40. https://doi.org/10.3389/fmicb.2024.1465627,