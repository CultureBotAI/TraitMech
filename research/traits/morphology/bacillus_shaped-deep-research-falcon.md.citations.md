# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** bacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000667
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an elongated, rod cylindrical morphology with relatively parallel sides and rounded ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** bacillus
- **Existing evidence:** DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)
- **Existing causal graph summary:** bacillus_shaped_rod_elongation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **bacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/bacillus_shaped.yaml`.

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
**Generated:** 2026-08-04T15:05:59.791386

1. galinier2023recentadvancesin pages 3-5
2. goudin2023recoveryofvibrio pages 1-2
3. schiller2024identificationofstructural pages 1-2
4. williams2019mechanismsofpolar pages 57-61
5. fivenson2023arolefor pages 1-2
6. costa2024theroleof pages 13-14
7. schafer2024dissectingantibioticeffects pages 1-2
8. dion2018celldiameterin pages 10-12
9. pohl2024adynamicbactofilin pages 19-21
10. dion2018celldiameterin pages 3-6
11. dion2018celldiameterin pages 1-3
12. dion2018celldiameterin pages 8-10
13. s
14. s an
15. https://doi.org/10.1073/pnas.2301987120
16. https://doi.org/10.3390/biom13050720
17. https://doi.org/10.1371/journal.pone.0293276
18. https://doi.org/10.1038/s41467-024-45196-0
19. https://doi.org/10.1128/mbio.03235-23
20. https://doi.org/10.1128/spectrum.03275-23
21. https://doi.org/10.7554/eLife.86577.2
22. https://doi.org/10.1101/392837
23. https://doi.org/10.1146/annurev-cellbio-010521-010834
24. https://doi.org/10.1038/s41579-020-0366-3
25. https://doi.org/10.3390/biom13050720,
26. https://doi.org/10.1371/journal.pone.0293276,
27. https://doi.org/10.1038/s41467-024-45196-0,
28. https://doi.org/10.32469/10355/79574,
29. https://doi.org/10.1073/pnas.2301987120,
30. https://doi.org/10.1101/392837,
31. https://doi.org/10.1128/mbio.03235-23,
32. https://doi.org/10.1128/spectrum.03275-23,
33. https://doi.org/10.7554/elife.86577.2,