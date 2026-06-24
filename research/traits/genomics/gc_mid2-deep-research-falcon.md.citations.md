# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC mid2
- **METPO identifier:** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:38:41.405104

1. deka2025basesubstitutionsin pages 1-3
2. radai2024anoverlookedphenomenon pages 10-12
3. lassalle2015gccontentevolutionin pages 9-11
4. lassalle2015gccontentevolutionin pages 1-4
5. weissman2019linkinghighgc pages 14-15
6. weissman2019linkinghighgc pages 15-17
7. fuente2023genomicsignaturein pages 13-15
8. weissman2019linkinghighgc pages 5-6
9. hale2025elevatedratesand pages 14-17
10. lassalle2015gccontentevolutionin pages 4-6
11. weissman2019linkinghighgc pages 21-24
12. dagva2024correctionofnonrandom pages 1-2
13. torrance2025homologousrecombinationshapes pages 1-4
14. deka2025basesubstitutionsin pages 13-15
15. dagva2024correctionofnonrandom pages 12-13
16. weissman2019linkinghighgc pages 10-11
17. deka2025basesubstitutionsin pages 3-5
18. https://doi.org/10.1186/s12864-023-09910-4
19. https://doi.org/10.1093/nar/gkae132
20. https://doi.org/10.3390/biology12020322
21. https://doi.org/10.1101/011023
22. https://doi.org/10.1371/journal.pgen.1008493
23. https://doi.org/10.63635/mrj.v1i4.188
24. https://doi.org/10.1128/mbio.03054-25
25. https://doi.org/10.1093/nar/gkae1265
26. https://doi.org/10.1371/journal.pbio.3003569
27. https://doi.org/10.63635/mrj.v1i4.188,
28. https://doi.org/10.1371/journal.pbio.3003569,
29. https://doi.org/10.1186/s12864-023-09910-4,
30. https://doi.org/10.1101/011023,
31. https://doi.org/10.1371/journal.pgen.1008493,
32. https://doi.org/10.1093/nar/gkae132,
33. https://doi.org/10.3390/biology12020322,
34. https://doi.org/10.1093/nar/gkae1265,
35. https://doi.org/10.1128/mbio.03054-25,