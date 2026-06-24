# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length large
- **METPO identifier:** METPO:1000886
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension exceeds approximately 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_>3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports large cell length under fast-growth or division-delayed regimes.) | DOI:10.1038/nrmicro2671: directs cell division (FtsZ-divisome review supports division-site timing as a control point governing whether cells reach larger lengths before constriction.)
- **Existing causal graph summary:** cell_length_large_division_delay: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_large.yaml`.

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
**Generated:** 2026-06-18T06:56:43.216657

1. yu2023plasmidscanshift pages 1-2
2. mannik2024determiningtheratelimiting pages 1-2
3. cameron2024insightsintothe pages 15-16
4. bojer2020sosainstaphylococci pages 2-4
5. nieto2024mechanismsofcell pages 6-7
6. ramirezdiaz2025theinterplayof pages 3-5
7. aguilarluviano2025conditionalfilamentationenhances pages 18-20
8. aguilarluviano2025conditionalfilamentationenhances pages 1-3
9. aguilarluviano2025conditionalfilamentationenhances pages 6-9
10. prinster2025cranberryconstituentsprevent pages 15-16
11. cameron2024insightsintothe pages 18-19
12. ramirezdiaz2025theinterplayof pages 39-42
13. https://doi.org/10.1101/2025.05.13.653778
14. https://doi.org/10.1128/iai.00600-24
15. https://doi.org/10.1002/advs.202203260
16. https://doi.org/10.1038/s41467-024-54242-w
17. https://doi.org/10.1038/s41540-024-00383-z
18. https://doi.org/10.1038/s41579-023-00942-x
19. https://doi.org/10.1101/2025.05.18.654715
20. https://doi.org/10.1007/s00294-019-01052-z
21. https://doi.org/10.1101/2025.05.13.653778,
22. https://doi.org/10.1002/advs.202203260,
23. https://doi.org/10.1038/s41467-024-54242-w,
24. https://doi.org/10.1038/s41579-023-00942-x,
25. https://doi.org/10.1128/iai.00600-24,
26. https://doi.org/10.1007/s00294-019-01052-z,
27. https://doi.org/10.1038/s41540-024-00383-z,
28. https://doi.org/10.1101/2025.05.18.654715,