# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows optimally at hydrostatic pressures substantially above atmospheric pressure (0.1 MPa), characteristic of deep-sea and deep-subsurface microorganisms.
- **Parent traits:** METPO:1000059
- **Synonyms:** barophilic, piezophile
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Membrane-lipid adaptation review supports the definition of piezophiles as high-hydrostatic-pressure-adapted organisms, with adaptation involving unsaturated and branched-chain fatty acids.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae strain MTCD1, the most piezophilic organism described, grows optimally at 120 MPa.)
- **Existing causal graph summary:** piezophilic_hhp_membrane_adaptation: 8 nodes, 10 edges

## Research Objective

Research the microbial trait **piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezophilic.yaml`.

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
**Generated:** 2026-08-04T03:10:01.179324

1. tamby2023microbialmembranelipid pages 1-2
2. peoples2020distinctivegeneand pages 1-2
3. qiu2024metabolicadaptationsof pages 1-2
4. malas2024biologicalfunctionsat pages 1-2
5. li2023strategyforthe pages 10-12
6. scheffer2023themysteryof pages 6-7
7. cui2024nterminusgtpasedomain pages 1-2
8. liu2023thetorrstwo pages 1-2
9. liu2023thetorrstwo pages 6-8
10. peoples2020distinctivegeneand pages 9-11
11. cui2024nterminusgtpasedomain pages 7-9
12. cui2024nterminusgtpasedomain pages 9-10
13. scheffer2023themysteryof pages 9-10
14. scheffer2023themysteryof pages 7-9
15. malas2024biologicalfunctionsat pages 9-10
16. liu2023thetorrstwo pages 8-10
17. tamby2023microbialmembranelipid pages 4-6
18. qiu2024metabolicadaptationsof pages 6-8
19. qiu2024metabolicadaptationsof pages 11-12
20. tamby2023microbialmembranelipid pages 7-9
21. 10.3389/fmicb.2024.1441398
22. 10.3389/fmicb.2024.1467153
23. 10.3389/fmicb.2024.1293928
24. 10.3389/fmicb.2023.1291578
25. 10.1128/aem.01304-22
26. 10.3389/fmolb.2022.1058381
27. 10.3390/microorganisms11071629
28. 10.1186/s12864-020-07102-y
29. 10.1099/ijsem.0.001671
30. https://doi.org/10.3389/fmicb.2024.1441398
31. https://doi.org/10.3389/fmicb.2024.1467153
32. https://doi.org/10.3389/fmicb.2024.1293928
33. https://doi.org/10.3389/fmicb.2023.1291578
34. https://doi.org/10.1128/aem.01304-22
35. https://doi.org/10.3389/fmolb.2022.1058381
36. https://doi.org/10.3390/microorganisms11071629
37. https://doi.org/10.1186/s12864-020-07102-y
38. https://doi.org/10.1099/ijsem.0.001671
39. https://doi.org/10.3389/fmolb.2022.1058381,
40. https://doi.org/10.1186/s12864-020-07102-y,
41. https://doi.org/10.3389/fmicb.2024.1467153,
42. https://doi.org/10.3389/fmicb.2024.1293928,
43. https://doi.org/10.3389/fmicb.2023.1291578,
44. https://doi.org/10.3389/fmicb.2024.1441398,
45. https://doi.org/10.3390/microorganisms11071629,
46. https://doi.org/10.1128/aem.01304-22,