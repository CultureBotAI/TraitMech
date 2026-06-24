# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC mid1
- **METPO identifier:** METPO:1000430
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition above approximately 66.3% (the METPO `GC_>66.3` bin; note that the upstream label 'mid1' does not match this high-end numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_>66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion as the mechanism elevating GC content into the high range.)
- **Existing causal graph summary:** gc_mid1_high_gc_bin: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:33:17.899089

1. dagva2024correctionofnonrandom pages 1-2
2. deng2024anadditionalproofreader pages 3-4
3. weissman2019linkinghighgc pages 1-3
4. teng2023genomiclegaciesof pages 2-5
5. teng2023genomiclegaciesof pages 10-12
6. teng2023genomiclegaciesof pages 5-8
7. hu2022apositivecorrelation pages 12-13
8. weissman2019linkinghighgc pages 5-6
9. dagva2024correctionofnonrandom pages 9-10
10. wozniak2022bacterialdnaexcision pages 10-11
11. teng2023genomiclegaciesof pages 1-2
12. hu2022apositivecorrelation pages 1-2
13. hu2022apositivecorrelation pages 10-12
14. weissman2019linkinghighgc pages 14-15
15. weissman2019potentiallinkbetween pages 8-11
16. dagva2024correctionofnonrandom pages 10-11
17. deng2024anadditionalproofreader pages 1-2
18. deng2024anadditionalproofreader pages 2-3
19. ruis2023mutationalspectraare pages 2-3
20. ruis2023mutationalspectraare pages 4-5
21. weissman2019linkinghighgc pages 3-5
22. hu2022apositivecorrelation pages 13-15
23. deng2024anadditionalproofreader pages 2-2
24. https://doi.org/10.1371/journal.pgen.1008493
25. https://doi.org/10.1128/spectrum.02145-22
26. https://doi.org/10.1186/s12864-022-08353-7
27. https://doi.org/10.1093/nar/gkae132
28. https://doi.org/10.1073/pnas.2322938121
29. https://doi.org/10.17863/cam.102279
30. https://doi.org/10.1038/s41579-022-00694-0
31. https://doi.org/10.1128/spectrum.02145-22,
32. https://doi.org/10.1186/s12864-022-08353-7,
33. https://doi.org/10.1093/nar/gkae132,
34. https://doi.org/10.1073/pnas.2322938121,
35. https://doi.org/10.1371/journal.pgen.1008493,
36. https://doi.org/10.1101/544924,
37. https://doi.org/10.17863/cam.102279,
38. https://doi.org/10.1038/s41579-022-00694-0,