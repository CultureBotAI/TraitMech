# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkaphilic
- **METPO identifier:** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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
**Generated:** 2026-06-17T21:27:57.623546

1. khomyakova2023phenotypicandgenomic pages 1-2
2. krulwich2011molecularaspectsof pages 12-14
3. jong2024quantitativeproteomicsreveals pages 1-2
4. krulwich2011molecularaspectsof pages 6-8
5. wang2023characterizationoftwo pages 7-8
6. xing2024thepolyextremophilenatranaerobius pages 19-21
7. goto2022differencesinbioenergetic pages 1-2
8. thompson2023insightsintothe pages 1-2
9. xing2024thepolyextremophilenatranaerobius pages 1-2
10. wadhawan2024potentialofhalophiles pages 1-2
11. wadhawan2024potentialofhalophiles pages 7-8
12. wadhawan2024potentialofhalophiles pages 10-11
13. wadhawan2024potentialofhalophiles pages 6-7
14. wang2023salinealkalisoilproperty pages 1-2
15. adetunji2024unravelingthepotentials pages 19-20
16. krulwich2011molecularaspectsof pages 27-28
17. rekadwad2023extremophilesthespecies pages 8-10
18. krulwich2011molecularaspectsof pages 20-22
19. wang2023characterizationoftwo pages 10-12
20. thompson2023insightsintothe pages 2-3
21. https://doi.org/10.1038/nrmicro2549
22. https://doi.org/10.3390/ijms241310786
23. https://doi.org/10.1128/aem.00145-24
24. https://doi.org/10.3389/fmicb.2022.842785
25. https://doi.org/10.3389/fmicb.2023.1233691
26. https://doi.org/10.3389/fmicb.2023.1179857
27. https://doi.org/10.3389/fmicb.2024.1468929
28. https://doi.org/10.1007/s13205-024-04036-0
29. https://doi.org/10.3390/min14090861
30. https://doi.org/10.3390/ijms24097737
31. https://doi.org/10.1007/s13205-023-03733-6
32. https://doi.org/10.3389/fmicb.2023.1233691,
33. https://doi.org/10.1038/nrmicro2549,
34. https://doi.org/10.3389/fmicb.2024.1468929,
35. https://doi.org/10.1128/aem.00145-24,
36. https://doi.org/10.3390/ijms241310786,
37. https://doi.org/10.3389/fmicb.2022.842785,
38. https://doi.org/10.3389/fmicb.2023.1179857,
39. https://doi.org/10.1007/s13205-024-04036-0,
40. https://doi.org/10.3390/ijms24097737,
41. https://doi.org/10.3390/min14090861,
42. https://doi.org/10.1007/s13205-023-03733-6,