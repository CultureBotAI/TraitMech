# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000605
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur with or without molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: can grow in the presence or absence of oxygen (Supports facultative anaerobiosis as growth under oxic or anoxic conditions.) | DOI:10.1093/femsre/fuac008: Escherichia coli is a facultative anaerobe (Organism example: Escherichia coli is described as facultatively anaerobic.)
- **Existing causal graph summary:** facultative_anaerobe_oxygen_switch: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **facultatively anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_anaerobic.yaml`.

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
**Generated:** 2026-08-04T00:50:47.041527

1. andre2021theselectiveadvantage pages 1-2
2. price2021bacterialapproachesto pages 11-12
3. sevilla2019redoxbasedtranscriptionalregulation pages 14-16
4. brown2022thearcabtwocomponent pages 2-3
5. brown2022thearcabtwocomponent pages 14-15
6. ikeda2023supplementationwithamino pages 10-11
7. villamizar2023anaerobiosisaneglected pages 1-2
8. mobley2024fitnessfactorgenes pages 22-24
9. villamizar2023anaerobiosisaneglected pages 16-18
10. beilen2016allthreeendogenous pages 4-5
11. beilen2016allthreeendogenous pages 1-2
12. 4Fe–4S
13. 2Fe–2S
14. 4Fe-4S
15. 10.1111/1462-2920.15293
16. 2Fe-2S
17. 10.1089/ars.2017.7442
18. 10.3389/fmicb.2016.01339
19. 10.1128/mmbr.00110-21
20. 10.1111/mmi.14795
21. H
22. 10.1128/aem.00868-23
23. 10.1128/aem.01491-23
24. 10.1371/journal.ppat.1012495
25. 10.1038/s41467-024-51029-x
26. https://doi.org/10.1111/cmi.13338
27. https://doi.org/10.1111/1462-2920.15293
28. https://doi.org/10.1111/mmi.14795
29. https://doi.org/10.1128/mmbr.00110-21
30. https://doi.org/10.3389/fmicb.2016.01339
31. https://doi.org/10.1089/ars.2017.7442
32. https://doi.org/10.1128/aem.01491-23
33. https://doi.org/10.1128/aem.00868-23
34. https://doi.org/10.1371/journal.ppat.1012495
35. https://doi.org/10.1038/s41467-024-51029-x
36. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
37. https://doi.org/10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338
38. https://doi.org/10.1111/1462-2920.15293](https://doi.org/10.1111/1462-2920.15293
39. https://doi.org/10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795
40. https://doi.org/10.1128/mmbr.00110-21](https://doi.org/10.1128/mmbr.00110-21
41. https://doi.org/10.3389/fmicb.2016.01339](https://doi.org/10.3389/fmicb.2016.01339
42. https://doi.org/10.1089/ars.2017.7442](https://doi.org/10.1089/ars.2017.7442
43. https://doi.org/10.1128/aem.01491-23](https://doi.org/10.1128/aem.01491-23
44. https://doi.org/10.1128/aem.00868-23](https://doi.org/10.1128/aem.00868-23
45. https://doi.org/10.1371/journal.ppat.1012495](https://doi.org/10.1371/journal.ppat.1012495
46. https://doi.org/10.1038/s41467-024-51029-x](https://doi.org/10.1038/s41467-024-51029-x
47. https://doi.org/10.1111/cmi.13338,
48. https://doi.org/10.1111/mmi.14795,
49. https://doi.org/10.1111/1462-2920.15293,
50. https://doi.org/10.1089/ars.2017.7442,
51. https://doi.org/10.3389/fmicb.2016.01339,
52. https://doi.org/10.1128/mmbr.00110-21,
53. https://doi.org/10.1128/aem.00868-23,
54. https://doi.org/10.1128/aem.01491-23,
55. https://doi.org/10.1371/journal.ppat.1012495,