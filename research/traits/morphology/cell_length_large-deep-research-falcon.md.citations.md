# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000886
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension exceeds approximately 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_>3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports large cell length under fast-growth or division-delayed regimes.) | DOI:10.1038/nrmicro2671: directs cell division (FtsZ-divisome review supports division-site timing as a control point governing whether cells reach larger lengths before constriction.)
- **Existing causal graph summary:** cell_length_large_division_delay: 10 nodes, 6 edges

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
**Generated:** 2026-08-04T07:40:24.738519

1. chimileski2024tipextensionand pages 5-7
2. jun2018fundamentalprinciplesin pages 27-28
3. mannik2024determiningtheratelimiting pages 8-9
4. chu2024auniquecell pages 4-5
5. adeleye2024queuosinebiosyntheticenzyme pages 1-5
6. chu2024auniquecell pages 1-2
7. koo2024comprehensivedoublemutantanalysis pages 46-47
8. koo2024comprehensivedoublemutantanalysis pages 32-35
9. 10.1038/s41467-024-54242-w
10. 10.7554/eLife.87922.4
11. 10.1101/2023.10.31.565030
12. 10.1101/2024.08.14.608006
13. 10.1073/pnas.2408654121
14. 10.1088/1361-6633/aaa628
15. https://doi.org/10.1038/s41467-024-54242-w
16. https://doi.org/10.7554/elife.87922.4
17. https://doi.org/10.1101/2023.10.31.565030
18. https://doi.org/10.1101/2024.08.14.608006
19. https://doi.org/10.1073/pnas.2408654121
20. https://doi.org/10.1088/1361-6633/aaa628
21. https://doi.org/10.1073/pnas.2408654121,
22. https://doi.org/10.1088/1361-6633/aaa628,
23. https://doi.org/10.1038/s41467-024-54242-w,
24. https://doi.org/10.7554/elife.87922.4,
25. https://doi.org/10.1101/2023.10.31.565030,
26. https://doi.org/10.1101/2024.08.14.608006,