# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 13 nodes, 8 edges

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
**Generated:** 2026-08-04T04:26:11.093625

1. purwar2024adaptationsofpsychrophilic pages 8-10
2. ogawa2020bioconversionfromdocosahexaenoic pages 1-2
3. sidarta2024lipidphaseseparation pages 1-2
4. liu2023psychrophilicyeastsinsights pages 4-5
5. ogawa2020bioconversionfromdocosahexaenoic pages 9-11
6. purwar2024adaptationsofpsychrophilic pages 4-6
7. ramon2023ageneraloverview pages 21-22
8. ramasamy2023comprehensiveinsightson pages 3-4
9. purwar2024adaptationsofpsychrophilic pages 3-4
10. yoshida2016bacteriallongchainpolyunsaturated pages 9-10
11. garcialopez2021identificationofbiomolecules pages 4-6
12. pathania2021adaptationtocold pages 220-223
13. purwar2024adaptationsofpsychrophilic pages 10-11
14. sidarta2024lipidphaseseparation pages 5-9
15. sidarta2024lipidphaseseparation pages 14-16
16. liu2023psychrophilicyeastsinsights pages 1-2
17. liu2023psychrophilicyeastsinsights pages 5-7
18. ramon2023ageneraloverview pages 12-14
19. purwar2024adaptationsofpsychrophilic pages 13-15
20. 10.1128/spectrum.03925-23
21. 10.37256/amtt.5220244537
22. 10.3390/genes14010158
23. 10.1007/s42770-023-01057-4
24. 10.3389/fmicb.2023.1197797
25. 10.3389/fmicb.2020.01104
26. 10.3390/md14050094
27. 10.1111/gtc.12002
28. 10.3390/biom11081155
29. 10.1007/978-981-16-2625-8_4
30. https://doi.org/10.1128/spectrum.03925-23
31. https://doi.org/10.37256/amtt.5220244537
32. https://doi.org/10.3390/genes14010158
33. https://doi.org/10.1007/s42770-023-01057-4
34. https://doi.org/10.3389/fmicb.2023.1197797
35. https://doi.org/10.3389/fmicb.2020.01104
36. https://doi.org/10.3390/md14050094
37. https://doi.org/10.1111/gtc.12002
38. https://doi.org/10.3390/biom11081155
39. https://doi.org/10.1007/978-981-16-2625-8_4
40. https://doi.org/10.37256/amtt.5220244537,
41. https://doi.org/10.1007/s42770-023-01057-4,
42. https://doi.org/10.1128/spectrum.03925-23,
43. https://doi.org/10.3389/fmicb.2020.01104,
44. https://doi.org/10.3390/md14050094,
45. https://doi.org/10.3390/genes14010158,
46. https://doi.org/10.1111/gtc.12002,
47. https://doi.org/10.3389/fmicb.2023.1197797,
48. https://doi.org/10.1007/978-981-16-2625-8\_4,
49. https://doi.org/10.3390/biom11081155,