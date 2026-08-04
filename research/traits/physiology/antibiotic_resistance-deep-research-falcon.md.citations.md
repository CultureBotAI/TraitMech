# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** antibiotic resistance
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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
**Generated:** 2026-08-04T10:41:31.308462

1. maeda2024laboratoryevolutionof pages 1-2
2. xu2025epidemiologymechanismsand pages 1-2
3. zhu2022clinicalperspectiveof pages 2-4
4. nazir2025theglobalchallenge pages 1-2
5. zhu2022clinicalperspectiveof pages 4-5
6. schumann2024siteselectivemodificationsby pages 17-18
7. maeda2024laboratoryevolutionof pages 6-7
8. gaballa2023morethanmcr pages 1-2
9. naghavi2024globalburdenof pages 1-2
10. maeda2024laboratoryevolutionof pages 12-13
11. gajic2025acomprehensiveoverview pages 6-8
12. gao2016disseminationandmechanism pages 8-10
13. gao2016disseminationandmechanism pages 1-2
14. naghavi2024globalburdenof pages 17-18
15. naghavi2024globalburdenof pages 2-3
16. naghavi2024globalburdenof pages 3-4
17. 10.1016/S0140-6736(24)01867-1
18. 10.3390/antibiotics13010094
19. 10.1128/msphere.00731-24
20. 10.3389/fcimb.2023.1060519
21. 10.3390/ijms24065777
22. 10.2147/IDR.S345574
23. 10.1371/journal.ppat.1005957
24. 10.1038/nrmicro3380
25. 10.1038/s41579-022-00820-y
26. https://doi.org/10.1016/S0140-6736(24
27. https://doi.org/10.3390/antibiotics13010094
28. https://doi.org/10.1128/msphere.00731-24
29. https://doi.org/10.3389/fcimb.2023.1060519
30. https://doi.org/10.3390/ijms24065777
31. https://doi.org/10.2147/IDR.S345574
32. https://doi.org/10.1371/journal.ppat.1005957
33. https://doi.org/10.1038/nrmicro3380
34. https://doi.org/10.1038/s41579-022-00820-y
35. https://doi.org/10.3390/antibiotics13010094,
36. https://doi.org/10.2147/idr.s345574,
37. https://doi.org/10.1038/s44259-025-00076-5,
38. https://doi.org/10.3390/antibiotics14030221,
39. https://doi.org/10.1002/hsr2.71077,
40. https://doi.org/10.1371/journal.ppat.1005957,
41. https://doi.org/10.3389/fcimb.2023.1060519,
42. https://doi.org/10.1128/msphere.00731-24,
43. https://doi.org/10.1016/s0140-6736(24