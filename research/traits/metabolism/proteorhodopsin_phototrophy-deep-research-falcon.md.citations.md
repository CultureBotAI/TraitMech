# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteorhodopsin phototrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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
**Generated:** 2026-08-04T07:01:18.412210

1. dupont2012genomicinsightsto pages 8-9
2. needham2019adistinctlineage pages 10-10
3. feng2023isproteorhodopsina pages 17-23
4. feng2023isproteorhodopsina pages 34-38
5. feng2023isproteorhodopsina pages 28-34
6. fujiwara2024carotenoidpigmentsenhance pages 9-12
7. feng2023isproteorhodopsina pages 95-101
8. johnson2010enhancementofsurvival pages 1-2
9. feng2023isproteorhodopsina pages 89-95
10. bukhdruker2025proteorhodopsininsightsinto pages 18-19
11. cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3
12. cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6
13. johnson2010enhancementofsurvival pages 6-7
14. feng2023isproteorhodopsina pages 131-136
15. retinal
16. ed
17. 10.1126/science.289.5486.1902
18. 10.1038/35081051
19. 10.1038/nature05381
20. 10.1073/pnas.0712027105
21. 10.1074/jbc.M109.002618
22. 10.1128/AEM.02425-09
23. 10.1038/ismej.2011.189
24. 10.1128/mSphere.00525-21
25. 10.1111/1462-2920.16243
26. 10.25959/23241740
27. 10.4014/jmb.2410.10034
28. 10.1101/2024.11.08.622755
29. https://doi.org/10.1126/science.289.5486.1902
30. https://doi.org/10.1038/35081051
31. https://doi.org/10.1038/nature05381
32. https://doi.org/10.1073/pnas.0712027105
33. https://doi.org/10.1074/jbc.M109.002618
34. https://doi.org/10.1128/AEM.02425-09
35. https://doi.org/10.1038/ismej.2011.189
36. https://doi.org/10.1128/mSphere.00525-21
37. https://doi.org/10.1111/1462-2920.16243
38. https://doi.org/10.25959/23241740
39. https://doi.org/10.4014/jmb.2410.10034
40. https://doi.org/10.1101/2024.11.08.622755
41. https://doi.org/10.25959/23241740,
42. https://doi.org/10.1038/ismej.2011.189,
43. https://doi.org/10.1073/pnas.1907517116,
44. https://doi.org/10.1128/aem.02425-09,
45. https://doi.org/10.1126/sciadv.adu5303,
46. https://doi.org/10.1128/msphere.00525-21,
47. https://doi.org/10.1101/2024.11.08.622755,