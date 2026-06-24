# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sphere shaped
- **METPO identifier:** METPO:1000683
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_sphere, sphere-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports spherical bacterial morphology as associated with septal peptidoglycan synthesis.)
- **Existing causal graph summary:** sphere_shaped_septal_peptidoglycan: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **sphere shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sphere_shaped.yaml`.

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
**Generated:** 2026-06-18T09:41:17.412539

1. pinho2013howtoget pages 1-2
2. ramosleon2025howdospherical pages 10-11
3. costa2024theroleof pages 6-8
4. pinho2013howtoget pages 2-3
5. pinho2013howtoget pages 5-6
6. battaje2023modelsversuspathogens pages 3-4
7. costa2024theroleof pages 11-13
8. ibrahim2024processingofltas pages 2-5
9. pinho2013howtoget pages 4-5
10. pinho2013howtoget pages 3-4
11. ramosleon2025howdospherical pages 2-3
12. pinho2013howtoget pages 11-11
13. costa2024theroleof pages 1-2
14. ibrahim2024processingofltas pages 1-2
15. ibrahim2024processingofltas pages 5-7
16. ramosleon2025howdospherical pages 5-6
17. https://doi.org/10.1038/nrmicro3088
18. https://doi.org/10.1042/bsr20221664
19. https://doi.org/10.1042/bst20240956
20. https://doi.org/10.1128/mbio.03235-23
21. https://doi.org/10.1128/mbio.02852-23
22. https://doi.org/10.1038/nrmicro3088,
23. https://doi.org/10.1042/bst20240956,
24. https://doi.org/10.1128/mbio.03235-23,
25. https://doi.org/10.1042/bsr20221664,
26. https://doi.org/10.1128/mbio.02852-23,