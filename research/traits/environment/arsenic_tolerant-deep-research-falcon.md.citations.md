# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** arsenic tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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
**Generated:** 2026-08-04T00:14:22.848801

1. dunivin2019aglobalsurvey pages 1-2
2. naiel2024thearsenicbioremediation pages 6-7
3. yan2019geneticmechanismsof pages 2-4
4. yang2016newmechanismsof pages 1-2
5. fekih2018distributionofarsenic pages 3-4
6. li2016theorganoarsenicalbiocycle pages 1-3
7. rueangmongkolrat2024theroleof pages 1-2
8. haghi2023arsenicpollutionand pages 1-2
9. hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2
10. preetha2023biotechnologyadvancesin pages 2-4
11. william2023arsenicandmicroorganisms pages 4-6
12. garbinski2020bacterialmechanismsof pages 32-35
13. rueangmongkolrat2024theroleof pages 8-10
14. william2023arsenicandmicroorganisms pages 8-9
15. william2023arsenicandmicroorganisms pages 11-12
16. As(V)
17. As(III)
18. 10.3389/fenvs.2023.1195643
19. 10.7717/peerj.18383
20. 10.1186/s12866-024-03676-9
21. 10.1186/s12915-019-0661-5
22. 10.3389/fmicb.2018.02473
23. 10.3390/microorganisms12010074
24. 10.1016/j.heliyon.2024.e36314
25. 10.3390/molecules28031474
26. 10.1007/s00294-018-0894-9
27. 10.1039/C6MT00168H
28. 10.1016/j.bj.2015.08.003
29. https://doi.org/10.3389/fenvs.2023.1195643
30. https://doi.org/10.7717/peerj.18383
31. https://doi.org/10.1186/s12866-024-03676-9
32. https://doi.org/10.1186/s12915-019-0661-5
33. https://doi.org/10.3389/fmicb.2018.02473
34. https://doi.org/10.3390/microorganisms12010074
35. https://doi.org/10.1016/j.heliyon.2024.e36314
36. https://doi.org/10.3390/molecules28031474
37. https://doi.org/10.1007/s00294-018-0894-9
38. https://doi.org/10.1039/C6MT00168H
39. https://doi.org/10.1016/j.bj.2015.08.003
40. https://doi.org/10.3390/microorganisms12010074,
41. https://doi.org/10.1186/s12915-019-0661-5,
42. https://doi.org/10.1007/s00294-018-0894-9,
43. https://doi.org/10.1186/s12866-024-03676-9,
44. https://doi.org/10.7717/peerj.18383,
45. https://doi.org/10.1016/j.heliyon.2024.e36314,
46. https://doi.org/10.3389/fenvs.2023.1195643,
47. https://doi.org/10.1016/j.bj.2015.08.003,
48. https://doi.org/10.3390/molecules28031474,
49. https://doi.org/10.1039/c6mt00168h,
50. https://doi.org/10.25148/etd.fidc009238,
51. https://doi.org/10.3389/fmicb.2018.02473,