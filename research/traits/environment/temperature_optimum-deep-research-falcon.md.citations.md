# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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
**Generated:** 2026-08-04T04:06:55.681460

1. siliakus2017adaptationsofarchaeal pages 8-10
2. colette2025machinelearningfor pages 1-4
3. liang2024interactionsbetweenchaperone pages 16-17
4. mendoza2014temperaturesensingby pages 1-2
5. mendoza2014temperaturesensingby pages 5-6
6. knapp2025metabolicrearrangementenables pages 1-2
7. moon2023temperaturemattersbacterial pages 3-5
8. lehmann2023adaptivelaboratoryevolution pages 1-2
9. barnum2024predictingmicrobialgrowth pages 1-3
10. barnum2024predictingmicrobialgrowth pages 3-6
11. ernst2016homeoviscousadaptationand pages 1-2
12. colette2025machinelearningfor pages 4-7
13. grunberger2023uncoveringthetemporal pages 1-2
14. grunberger2023uncoveringthetemporal pages 23-24
15. hoffmann2024temperaturedependenttrnamodifications pages 13-14
16. hoffmann2024temperaturedependenttrnamodifications pages 9-10
17. hoffmann2024temperaturedependenttrnamodifications pages 17-19
18. hoffmann2024temperaturedependenttrnamodifications pages 1-2
19. barnum2024predictingmicrobialgrowth pages 6-9
20. barnum2024predictingmicrobialgrowth pages 22-24
21. moon2023temperaturemattersbacterial pages 1-3
22. *B. subtilis*
23. 10.1038/s41564-024-01841-4
24. 10.3390/ijms25168823
25. 10.1101/2024.03.22.586313
26. 10.7717/peerj.17197
27. 10.3389/fmicb.2023.1265216
28. 10.1128/mbio.02174-23
29. 10.1007/s12275-023-00031-x
30. 10.1007/s00792-017-0939-x
31. 10.1016/j.jmb.2016.08.013
32. 10.1146/annurev-micro-091313-103612
33. https://doi.org/10.1038/s41564-024-01841-4
34. https://doi.org/10.3390/ijms25168823
35. https://doi.org/10.1101/2024.03.22.586313
36. https://doi.org/10.7717/peerj.17197
37. https://doi.org/10.3389/fmicb.2023.1265216
38. https://doi.org/10.1128/mbio.02174-23
39. https://doi.org/10.1007/s12275-023-00031-x
40. https://doi.org/10.1007/s00792-017-0939-x
41. https://doi.org/10.1016/j.jmb.2016.08.013
42. https://doi.org/10.1146/annurev-micro-091313-103612
43. https://doi.org/10.1101/2025.03.03.640802,
44. https://doi.org/10.1007/s00792-017-0939-x,
45. https://doi.org/10.7717/peerj.17197,
46. https://doi.org/10.1146/annurev-micro-091313-103612,
47. https://doi.org/10.1038/s41564-024-01841-4,
48. https://doi.org/10.1007/s12275-023-00031-x,
49. https://doi.org/10.1128/mbio.02174-23,
50. https://doi.org/10.3390/ijms25168823,
51. https://doi.org/10.3389/fmicb.2023.1265216,
52. https://doi.org/10.1101/2024.03.22.586313,
53. https://doi.org/10.1016/j.jmb.2016.08.013,