# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anaerobic oxidation of methane
- **METPO identifier:** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T04:08:07.736257

1. murali2023physiologicalpotentialand pages 1-2
2. ouboter2024mechanismsofextracellular pages 16-21
3. krause2024spatialevidenceof pages 1-6
4. zheng2023intermediatesproductionin pages 5-7
5. schnabel2024influenceofminor pages 17-20
6. wissink2024probingdenitrifyinganaerobic pages 1-2
7. yao2024methanedependentcompletedenitrification pages 1-3
8. sivan2024enigmaticfemnfueledanaerobic pages 1-4
9. slobodkin2023compositionandmetabolic pages 8-9
10. zhang2023multihemecytochromemediatedextracellular pages 1-2
11. zuo2024nitritedependentmicrobialutilization pages 1-2
12. molinamacias2024implementationofan pages 1-2
13. wissink2024probingdenitrifyinganaerobic pages 5-7
14. ouboter2024mechanismsofextracellular pages 1-5
15. krause2024spatialevidenceof pages 40-44
16. zuo2024nitritedependentmicrobialutilization pages 3-5
17. krause2024spatialevidenceof pages 23-30
18. https://doi.org/10.1101/2023.07.24.550278
19. https://doi.org/10.3390/microorganisms11030555
20. https://doi.org/10.1371/journal.pbio.3002292
21. https://doi.org/10.1021/acs.est.3c07197
22. https://doi.org/10.1038/s41564-023-01578-6
23. https://doi.org/10.3390/fermentation9070645
24. https://doi.org/10.1038/s41564-023-01578-6;
25. https://doi.org/10.3390/microorganisms11030555;
26. https://doi.org/10.5194/egusphere-2024-1603
27. https://doi.org/10.1371/journal.pbio.3002292;
28. https://doi.org/10.1101/2024.07.16.603764
29. https://doi.org/10.5194/egusphere-2024-1829
30. https://doi.org/10.1021/acs.est.3c07197;
31. https://doi.org/10.1016/j.wroa.2024.100231
32. https://doi.org/10.1007/s11270-024-07555-x
33. https://doi.org/10.3390/fermentation9070645,
34. https://doi.org/10.1021/acs.est.3c07197,
35. https://doi.org/10.1038/s41564-023-01578-6,
36. https://doi.org/10.1371/journal.pbio.3002292,
37. https://doi.org/10.5194/egusphere-2024-1829,
38. https://doi.org/10.3390/microorganisms11030555,
39. https://doi.org/10.1101/2023.07.24.550278,
40. https://doi.org/10.1101/2024.07.16.603764,
41. https://doi.org/10.5194/egusphere-2024-1603,
42. https://doi.org/10.1016/j.wroa.2024.100231,
43. https://doi.org/10.1007/s11270-024-07555-x,