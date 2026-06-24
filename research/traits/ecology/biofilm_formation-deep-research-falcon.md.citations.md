# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biofilm formation
- **METPO identifier:** traitmech:000053
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which cells form surface-attached, matrix-enclosed multicellular communities (biofilms) held together by extracellular polymeric substances — a widespread mode of microbial life.
- **Parent traits:** METPO:1000059
- **Synonyms:** biofilm-forming
- **Existing evidence:** DOI:10.1038/nrmicro.2016.94:  (Flemming et al. describe matrix-enclosed, surface-associated communities (biofilms) as an emergent, distinct mode of bacterial life.) | DOI:10.1038/s41579-019-0162-0:  (Flemming & Wuertz support the global ubiquity of the biofilm lifestyle across microbial habitats.)
- **Existing causal graph summary:** biofilm_eps_matrix_community: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biofilm formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biofilm_formation.yaml`.

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
**Generated:** 2026-06-17T19:25:10.692718

1. erkihun2024medicalscopeof pages 1-2
2. bohning2024theroleof pages 1-2
3. wang2025researchprogresson pages 2-4
4. angeli2025environmentalsensingand pages 14-20
5. bohning2024theroleof pages 10-12
6. erkihun2024medicalscopeof pages 6-8
7. flemming2023thebiofilmmatrix pages 16-18
8. fuentes2024nanoparticlebasednitricoxide pages 11-13
9. erkihun2024medicalscopeof pages 12-14
10. nadell2017flowenvironmentand pages 1-2
11. scalia2025targetingbacterialbiofilms pages 1-6
12. gong2024multiplebiologicalcharacteristics pages 6-7
13. participate in
14. https://doi.org/10.1042/BCJ20210301
15. https://doi.org/10.3390/w17131944
16. https://doi.org/10.3390/antibiotics13111047
17. https://doi.org/10.3390/bacteria3030008
18. https://doi.org/10.1038/s41579-022-00791-0
19. https://doi.org/10.7554/eLife.21855
20. https://doi.org/10.3390/bacteria3030008,
21. https://doi.org/10.1042/bcj20210301,
22. https://doi.org/10.3390/w17131944,
23. https://doi.org/10.1038/s41579-022-00791-0,
24. https://doi.org/10.3390/antibiotics13111047,
25. https://doi.org/10.3389/fmicb.2024.1445630,
26. https://doi.org/10.7554/elife.21855,
27. https://doi.org/10.3390/antibiotics14080802,