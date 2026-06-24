# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum very low
- **METPO identifier:** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 4 nodes, 3 edges

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
**Generated:** 2026-06-18T02:23:45.177225

1. moyer2017psychrophilesandpsychrotrophs pages 1-2
2. cavicchioli2016ontheconcept pages 1-2
3. siddiqui2013psychrophiles pages 9-11
4. purwar2024adaptationsofpsychrophilic pages 6-7
5. bao2023miningofkey pages 1-2
6. ramon2023ageneraloverview pages 1-2
7. hamdan2018psychrophilesecologicalsignificance pages 2-2
8. yang2023insightintothe pages 1-2
9. purwar2024adaptationsofpsychrophilic pages 8-10
10. damico2006psychrophilicmicroorganismschallenges pages 2-3
11. ramon2023ageneraloverview pages 12-14
12. zerouki2023wholegenomesequenceand pages 10-12
13. buschi2024resistancetofreezing pages 1-2
14. bao2023miningofkey pages 6-7
15. purwar2024adaptationsofpsychrophilic pages 3-4
16. hamdan2018psychrophilesecologicalsignificance pages 1-2
17. moyer2017psychrophilesandpsychrotrophs pages 2-3
18. purwar2024adaptationsofpsychrophilic pages 1-3
19. damico2006psychrophilicmicroorganismschallenges pages 1-2
20. https://doi.org/10.3389/fmicb.2023.1215837
21. https://doi.org/10.1007/s42770-023-01057-4
22. https://doi.org/10.17159/sajs.2018/20170254
23. https://doi.org/10.1128/AEM.01928-22
24. https://doi.org/10.37256/amtt.5220244537
25. https://doi.org/10.1146/annurev-earth-040610-133514
26. https://doi.org/10.1038/sj.embor.7400662
27. https://doi.org/10.1007/s00438-023-02073-7
28. https://doi.org/10.1126/sciadv.adk9117
29. https://doi.org/10.1007/s12275-023-00031-x
30. https://doi.org/10.1128/aem.01928-22
31. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
32. https://doi.org/10.1038/ismej.2015.160
33. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
34. https://doi.org/10.17159/sajs.2018/20170254,
35. https://doi.org/10.1007/s42770-023-01057-4,
36. https://doi.org/10.1038/ismej.2015.160,
37. https://doi.org/10.1038/sj.embor.7400662,
38. https://doi.org/10.1146/annurev-earth-040610-133514,
39. https://doi.org/10.37256/amtt.5220244537,
40. https://doi.org/10.3389/fmicb.2023.1215837,
41. https://doi.org/10.1128/aem.01928-22,
42. https://doi.org/10.1007/s00438-023-02073-7,
43. https://doi.org/10.1126/sciadv.adk9117,