# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anaerobic oxidation of methane
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **anaerobic oxidation of methane** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_oxidation_of_methane.yaml`.

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
**Generated:** 2026-08-04T05:30:59.309088

1. scheller2020catabolicpathwaysand pages 45-48
2. gao2017anaerobicoxidationof pages 6-7
3. scheller2020catabolicpathwaysand pages 48-51
4. timmers2017reversemethanogenesisand pages 1-2
5. zhang2021anaerobicoxidationof pages 8-9
6. zhang2021anaerobicoxidationof pages 5-5
7. li2023phylogeneticandmetabolic pages 9-9
8. timmers2017reversemethanogenesisand pages 12-14
9. chauhan2024chemistryofcoenzyme pages 10-11
10. 10.1007/978-3-319-50391-2_3
11. 10.1155/2017/1654237
12. 10.1111/1758-2229.13008
13. 10.1038/s41598-017-05180-9
14. 10.1126/sciadv.abe4939
15. 10.1128/AEM.01832-18
16. 10.1038/s43705-023-00246-4
17. 10.1021/acs.accounts.4c00413
18. 10.1101/2023.07.24.550278
19. 10.3390/microorganisms12112259
20. https://doi.org/10.1038/35036572
21. https://doi.org/10.1155/2017/1654237
22. https://doi.org/10.1038/s41598-017-05180-9
23. https://doi.org/10.1007/978-3-319-50391-2_3
24. https://doi.org/10.1111/1758-2229.13008
25. https://doi.org/10.1126/sciadv.abe4939
26. https://doi.org/10.1038/s43705-023-00246-4
27. https://doi.org/10.1021/acs.accounts.4c00413
28. https://doi.org/10.1101/2023.07.24.550278
29. https://doi.org/10.3390/microorganisms12112259
30. https://doi.org/10.1128/AEM.01832-18
31. https://doi.org/10.1038/35036572](https://doi.org/10.1038/35036572
32. https://doi.org/10.1155/2017/1654237](https://doi.org/10.1155/2017/1654237
33. https://doi.org/10.1038/s41598-017-05180-9](https://doi.org/10.1038/s41598-017-05180-9
34. https://doi.org/10.1007/978-3-319-50391-2_3](https://doi.org/10.1007/978-3-319-50391-2_3
35. https://doi.org/10.1111/1758-2229.13008](https://doi.org/10.1111/1758-2229.13008
36. https://doi.org/10.1126/sciadv.abe4939](https://doi.org/10.1126/sciadv.abe4939
37. https://doi.org/10.1038/s43705-023-00246-4](https://doi.org/10.1038/s43705-023-00246-4
38. https://doi.org/10.1021/acs.accounts.4c00413](https://doi.org/10.1021/acs.accounts.4c00413
39. https://doi.org/10.1101/2023.07.24.550278](https://doi.org/10.1101/2023.07.24.550278
40. https://doi.org/10.3390/microorganisms12112259](https://doi.org/10.3390/microorganisms12112259
41. https://doi.org/10.1007/978-3-319-50391-2\_3,
42. https://doi.org/10.1155/2017/1654237,
43. https://doi.org/10.1111/1758-2229.13008,
44. https://doi.org/10.1038/s41598-017-05180-9,
45. https://doi.org/10.62110/sciencein.jmc.2024.696,
46. https://doi.org/10.1038/s43705-023-00246-4,