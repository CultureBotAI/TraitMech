# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately piezophilic
- **METPO identifier:** traitmech:000002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).
- **Parent traits:** traitmech:000001
- **Synonyms:** obligate piezophile
- **Existing evidence:** DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii is an obligate piezophile that requires high hydrostatic pressure for growth.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high pressure (80-140 MPa) and does not grow near atmospheric pressure.)
- **Existing causal graph summary:** obligate_piezophily_high_pressure_requirement: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **obligately piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_piezophilic.yaml`.

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
**Generated:** 2026-06-18T00:05:52.652616

1. scoma2021functionalgroupsin pages 5-6
2. roumagnac2020responsestothe pages 1-2
3. peoples2020distinctivegeneand pages 1-2
4. scheffer2023themysteryof pages 7-9
5. scheffer2023themysteryof pages 9-10
6. scheffer2023themysteryof pages 6-7
7. malas2024biologicalfunctionsat pages 1-2
8. scoma2021functionalgroupsin pages 1-2
9. qiu2024metabolicadaptationsof pages 5-7
10. tamby2023microbialmembranelipid pages 2-4
11. qiu2024metabolicadaptationsof pages 1-2
12. peoples2020distinctivegeneand pages 7-9
13. tamby2023microbialmembranelipid pages 1-2
14. peoples2020distinctivegeneand pages 5-7
15. michoud2016highhydrostaticpressure pages 1-2
16. scoma2021functionalgroupsin pages 2-3
17. scheffer2023themysteryof pages 10-12
18. malas2024biologicalfunctionsat pages 12-13
19. malas2024biologicalfunctionsat pages 2-3
20. peoples2020distinctivegeneand pages 4-5
21. peoples2020distinctivegeneand pages 9-11
22. are
23. https://doi.org/10.3389/fmolb.2022.1058381
24. https://doi.org/10.3390/microorganisms11071629
25. https://doi.org/10.1186/s12864-020-07102-y
26. https://doi.org/10.1007/s00253-023-12906-5
27. https://doi.org/10.3389/fmicb.2020.588771
28. https://doi.org/10.3389/fmicb.2024.1293928
29. https://doi.org/10.1038/s41396-021-00930-0
30. https://doi.org/10.1038/srep27289
31. https://doi.org/10.1038/s41396-021-00930-0,
32. https://doi.org/10.3389/fmicb.2020.588771,
33. https://doi.org/10.1186/s12864-020-07102-y,
34. https://doi.org/10.1038/srep27289,
35. https://doi.org/10.3389/fmolb.2022.1058381,
36. https://doi.org/10.3390/microorganisms11071629,
37. https://doi.org/10.3389/fmicb.2024.1293928,
38. https://doi.org/10.1007/s00253-023-12906-5,