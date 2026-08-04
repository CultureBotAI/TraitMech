# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory metal reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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
**Generated:** 2026-08-04T06:07:37.865426

1. lloyd2003microbialreductionof pages 1-2
2. shi2012molecularunderpinningsof pages 1-2
3. zavarzina2023ironorsulfur pages 1-2
4. zavarzina2023ironorsulfur pages 7-8
5. norman2023acysteinepair pages 1-2
6. shi2012molecularunderpinningsof pages 2-3
7. zavarzina2023ironorsulfur pages 12-13
8. schwarz2024lackofphysiological pages 8-11
9. jiang2023thevariedroles pages 1-2
10. schwarz2024lackofphysiological pages 1-2
11. jiang2023thevariedroles pages 3-5
12. ueki2021cytochromesinextracellular pages 10-12
13. hazzan2023strategiesforenhancing pages 2-3
14. conley2020ahybridextracellular pages 29-31
15. zacharoff2017redoxconductionin pages 6-7
16. lloyd2003microbialreductionof pages 3-5
17. philipp2025identificationoffactors pages 14-16
18. norman2023acysteinepair pages 5-7
19. hazzan2023strategiesforenhancing pages 23-24
20. Fe(III)
21. 10.3389/fmicb.2012.00050
22. 10.3389/fmicb.2023.1251346
23. 10.1128/mbio.02589-22
24. 10.3389/fmicb.2023.1108245
25. 10.1128/mbio.00690-24
26. 10.1128/AEM.03109-20
27. 10.1016/S0168-6445(03)00044-5
28. 10.3390/app132312760
29. 10.1128/AEM.01253-20
30. 10.1016/j.coelec.2017.09.003
31. https://doi.org/10.3389/fmicb.2012.00050
32. https://doi.org/10.3389/fmicb.2023.1251346
33. https://doi.org/10.1128/mbio.02589-22
34. https://doi.org/10.3389/fmicb.2023.1108245
35. https://doi.org/10.1128/mbio.00690-24
36. https://doi.org/10.1128/AEM.03109-20
37. https://doi.org/10.1016/S0168-6445(03
38. https://doi.org/10.3390/app132312760
39. https://doi.org/10.1128/AEM.01253-20
40. https://doi.org/10.1016/j.coelec.2017.09.003
41. https://doi.org/10.1016/s0168-6445(03
42. https://doi.org/10.3389/fmicb.2012.00050,
43. https://doi.org/10.3389/fmicb.2023.1251346,
44. https://doi.org/10.3389/fmicb.2023.1108245,
45. https://doi.org/10.1128/aem.00685-25,
46. https://doi.org/10.1128/mbio.00690-24,
47. https://doi.org/10.1128/mbio.02589-22,
48. https://doi.org/10.3390/app132312760,
49. https://doi.org/10.1128/aem.03109-20,
50. https://doi.org/10.1128/aem.01253-20,
51. https://doi.org/10.1016/j.coelec.2017.09.003,