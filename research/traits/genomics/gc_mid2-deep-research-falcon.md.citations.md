# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid2.yaml`.

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
**Generated:** 2026-08-04T04:59:45.625251

1. teng2023genomiclegaciesof pages 2-5
2. lassalle2015gccontentevolutionin pages 4-6
3. long2018specificityofthe pages 1-2
4. teng2023genomiclegaciesof pages 8-10
5. waneka2021mutationalpressuredrives pages 1-2
6. teng2023genomiclegaciesof pages 5-8
7. weissman2019linkinghighgc pages 15-17
8. aliperti2023rkselectionof pages 3-6
9. aliperti2023rkselectionof pages 1-3
10. lassalle2015gccontentevolutionin pages 1-4
11. aliperti2023rkselectionof pages 9-11
12. aliperti2023rkselectionof pages 6-9
13. wu2012onthemolecular pages 2-4
14. wu2012onthemolecular pages 1-2
15. 10.1128/spectrum.02145-22
16. 10.1111/1462-2920.16511
17. 10.1101/011023
18. 10.1371/journal.pgen.1008493
19. 10.1093/molbev/msy134
20. 10.1093/gbe/evaa254
21. 10.1186/1745-6150-7-2
22. https://doi.org/10.1101/011023
23. https://doi.org/10.1128/spectrum.02145-22
24. https://doi.org/10.1093/gbe/evaa254
25. https://doi.org/10.1371/journal.pgen.1008493
26. https://doi.org/10.1111/1462-2920.16511
27. https://doi.org/10.1093/molbev/msy134
28. https://doi.org/10.1186/1745-6150-7-2
29. https://doi.org/10.1128/spectrum.02145-22,
30. https://doi.org/10.1101/011023,
31. https://doi.org/10.1111/1462-2920.16511,
32. https://doi.org/10.1093/molbev/msy134,
33. https://doi.org/10.1093/gbe/evaa254,
34. https://doi.org/10.1371/journal.pgen.1008493,
35. https://doi.org/10.1186/1745-6150-7-2,