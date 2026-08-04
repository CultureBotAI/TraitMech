# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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
**Generated:** 2026-08-04T03:14:48.132540

1. tamby2023microbialmembranelipid pages 1-2
2. roumagnac2020responsestothe pages 1-2
3. malas2024biologicalfunctionsat pages 1-2
4. zhao2024pressuretolerantsurvivalmechanism pages 1-2
5. qiu2024metabolicadaptationsofa pages 1-2
6. zhao2024pressuretolerantsurvivalmechanism pages 6-8
7. qiu2024metabolicadaptationsofa pages 8-11
8. coffin2024responseandadaptation pages 1-2
9. duru2021highpressureprocessinginducedtranscriptome pages 1-2
10. zhong2024insightintothe pages 15-17
11. li2023strategyforthe pages 2-4
12. coffin2024responseandadaptation pages 11-12
13. malas2024biologicalfunctionsat pages 9-10
14. tamby2023microbialmembranelipid pages 7-9
15. li2023strategyforthe pages 1-2
16. tamby2024exploringrobustnessof pages 1-2
17. scheffer2023themysteryof pages 7-9
18. scoma2021functionalgroupsin pages 1-2
19. scoma2021functionalgroupsin pages 5-6
20. li2023strategyforthe pages 10-12
21. duru2021highpressureprocessinginducedtranscriptome pages 13-14
22. tamby2024exploringrobustnessof pages 8-9
23. 10.3389/fmolb.2022.1058381
24. 10.3389/fmicb.2024.1467153
25. 10.3389/fmars.2024.1471465
26. 10.1128/AEM.01304-22
27. 10.1128/msystems.01085-23
28. 10.3389/fmicb.2024.1470617
29. 10.3389/fmicb.2024.1293928
30. 10.3389/fmicb.2024.1470844
31. 10.3390/microorganisms11071629
32. 10.1038/s41396-021-00930-0
33. 10.3389/fmicb.2020.588771
34. 10.1186/s12864-021-07407-6
35. https://doi.org/10.3389/fmolb.2022.1058381
36. https://doi.org/10.3389/fmicb.2024.1467153
37. https://doi.org/10.3389/fmars.2024.1471465
38. https://doi.org/10.1128/AEM.01304-22
39. https://doi.org/10.1128/msystems.01085-23
40. https://doi.org/10.3389/fmicb.2024.1470617
41. https://doi.org/10.3389/fmicb.2024.1293928
42. https://doi.org/10.3389/fmicb.2024.1470844
43. https://doi.org/10.3390/microorganisms11071629
44. https://doi.org/10.1038/s41396-021-00930-0
45. https://doi.org/10.3389/fmicb.2020.588771
46. https://doi.org/10.1186/s12864-021-07407-6
47. https://doi.org/10.3389/fmolb.2022.1058381,
48. https://doi.org/10.1038/s41396-021-00930-0,
49. https://doi.org/10.3389/fmicb.2020.588771,
50. https://doi.org/10.1128/aem.01304-22,
51. https://doi.org/10.3389/fmicb.2024.1293928,
52. https://doi.org/10.1186/s12864-021-07407-6,
53. https://doi.org/10.3389/fmars.2024.1471465,
54. https://doi.org/10.3389/fmicb.2024.1467153,
55. https://doi.org/10.3389/fmicb.2024.1470844,
56. https://doi.org/10.3389/fmicb.2024.1470617,
57. https://doi.org/10.1128/msystems.01085-23,
58. https://doi.org/10.3390/microorganisms11071629,