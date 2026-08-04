# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000430
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition above approximately 66.3% (the METPO `GC_>66.3` bin; note that the upstream label 'mid1' does not match this high-end numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_>66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion as the mechanism elevating GC content into the high range.)
- **Existing causal graph summary:** gc_mid1_high_gc_bin: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **GC mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid1.yaml`.

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
**Generated:** 2026-08-04T05:02:06.593247

1. hu2022apositivecorrelation pages 1-2
2. horton2023mutationbiasand pages 1-2
3. lassalle2015gccontentevolutionin pages 6-9
4. lassalle2015gccontentevolutionin pages 9-11
5. lassalle2015gccontentevolutionin pages 4-6
6. dagva2024correctionofnonrandom pages 1-2
7. dagva2024correctionofnonrandom pages 8-9
8. long2018specificityofthe pages 1-2
9. couce2017mutatorgenomesdecay pages 1-3
10. kucukyildirim2016therateand pages 1-2
11. weissman2019linkinghighgc pages 5-6
12. weissman2019linkinghighgc pages 15-17
13. hu2022apositivecorrelation pages 13-15
14. lassalle2015gccontentevolutionin pages 1-4
15. lassalle2015gccontentevolutionin pages 11-14
16. weissman2019linkinghighgc pages 10-11
17. lassalle2015gccontentevolutionin pages 14-16
18. GC_w=\frac{G+C}{A+T+G+C}>0.663\;\text{(approximately)}.
\
19. e
20. 10.1093/nar/gkae132
21. 10.1099/mic.0.001404
22. 10.1186/s12864-022-08353-7
23. 10.1371/journal.pgen.1008493
24. 10.1093/molbev/msy134
25. 10.1073/pnas.1705887114
26. 10.1534/g3.116.030130
27. 10.1101/011023
28. 10.1101/cshperspect.a018077
29. https://doi.org/10.1093/nar/gkae132
30. https://doi.org/10.1099/mic.0.001404
31. https://doi.org/10.1186/s12864-022-08353-7
32. https://doi.org/10.1371/journal.pgen.1008493
33. https://doi.org/10.1093/molbev/msy134
34. https://doi.org/10.1073/pnas.1705887114
35. https://doi.org/10.1534/g3.116.030130
36. https://doi.org/10.1101/011023
37. https://doi.org/10.1101/cshperspect.a018077
38. https://doi.org/10.1101/cshperspect.a018077,
39. https://doi.org/10.1186/s12864-022-08353-7,
40. https://doi.org/10.1093/molbev/msy134,
41. https://doi.org/10.1093/nar/gkae132,
42. https://doi.org/10.1099/mic.0.001404,
43. https://doi.org/10.1101/011023,
44. https://doi.org/10.1073/pnas.1705887114,
45. https://doi.org/10.1534/g3.116.030130,
46. https://doi.org/10.1371/journal.pgen.1008493,