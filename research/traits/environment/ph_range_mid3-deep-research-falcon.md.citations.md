# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid3
- **METPO identifier:** METPO:1000463
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 8–10, characteristic of alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile, pHR_8_to_10
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile physiology growing across pH 8–10.)
- **Existing causal graph summary:** ph_range_mid3_alkaliphile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid3.yaml`.

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
**Generated:** 2026-06-18T01:08:31.366114

1. jong2023membraneproteomeof pages 1-2
2. krishna2021comparativegenomeanalysis pages 12-14
3. khomyakova2023phenotypicandgenomic pages 1-2
4. wang2023characterizationoftwo pages 7-8
5. xing2024thepolyextremophilenatranaerobius pages 1-2
6. krishna2021comparativegenomeanalysis pages 1-2
7. krishna2021comparativegenomeanalysis pages 11-12
8. rekadwad2023extremophilesthespecies pages 8-10
9. jong2023membraneproteomeof pages 9-10
10. lee2022iontransfermechanisms pages 1-2
11. kim2024lineagespecificevolutionof pages 1-2
12. jong2024quantitativeproteomicsreveals pages 1-2
13. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2
14. lee2022iontransfermechanisms pages 8-9
15. krishna2021comparativegenomeanalysis pages 15-17
16. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13
17. https://doi.org/10.1038/s41467-022-33640-y,
18. https://doi.org/10.3390/ijms241310786,
19. https://doi.org/10.1007/s13205-021-02938-x,
20. https://doi.org/10.1128/AEM.00145-24,
21. https://doi.org/10.3389/fmicb.2023.1228266,
22. https://doi.org/10.3389/fmicb.2023.1233691,
23. https://doi.org/10.1007/s13205-023-03733-6,
24. https://doi.org/10.3390/jof9060652,
25. https://doi.org/10.1038/s41467-022-33640-y
26. https://doi.org/10.3390/ijms241310786
27. https://doi.org/10.3389/fmicb.2023.1228266
28. https://doi.org/10.3389/fmicb.2023.1233691
29. https://doi.org/10.3390/jof9060652
30. https://doi.org/10.1007/s13205-023-03733-6
31. https://doi.org/10.1128/aem.00145-24
32. https://doi.org/10.1128/aem.02091-23
33. https://doi.org/10.3389/fmicb.2024.1468929
34. https://doi.org/10.1007/s13205-021-02938-x
35. https://doi.org/10.1128/aem.00145-24,
36. https://doi.org/10.3389/fmicb.2024.1468929,
37. https://doi.org/10.1128/aem.02091-23,