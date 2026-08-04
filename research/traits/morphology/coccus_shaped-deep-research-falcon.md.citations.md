# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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
**Generated:** 2026-08-04T08:09:14.485697

1. costa2024theroleof pages 13-14
2. battaje2023modelsversuspathogens pages 4-5
3. battaje2023modelsversuspathogens pages 3-4
4. puls2023inhibitionofpeptidoglycan pages 4-5
5. myrbraten2022smdaisa pages 1-2
6. myrbraten2022smdaisa pages 5-7
7. pinho2013howtoget pages 11-11
8. battaje2023modelsversuspathogens pages 1-3
9. puls2023inhibitionofpeptidoglycan pages 3-4
10. puls2023inhibitionofpeptidoglycan pages 2-3
11. myrbraten2022smdaisa pages 12-14
12. puls2023inhibitionofpeptidoglycan pages 1-2
13. puls2023inhibitionofpeptidoglycan pages 5-7
14. battaje2023modelsversuspathogens pages 20-21
15. 10.1042/BSR20221664
16. 10.1126/sciadv.ade9023
17. 10.1128/mbio.03404-21
18. 10.1128/mbio.03235-23
19. 10.1128/spectrum.04750-22
20. 10.1038/nrmicro3088
21. https://doi.org/10.1042/bsr20221664
22. https://doi.org/10.1126/sciadv.ade9023
23. https://doi.org/10.1128/mbio.03404-21
24. https://doi.org/10.1128/mbio.03235-23
25. https://doi.org/10.1038/nrmicro3088
26. https://doi.org/10.1128/spectrum.04750-22
27. https://doi.org/10.1042/BSR20221664
28. https://doi.org/10.1042/bsr20221664,
29. https://doi.org/10.1128/mbio.03235-23,
30. https://doi.org/10.1126/sciadv.ade9023,
31. https://doi.org/10.1128/mbio.03404-21,
32. https://doi.org/10.1038/nrmicro3088,