# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** filament shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000674
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_filament, filament, filament-shaped
- **Existing evidence:** DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports filamentous Streptomyces morphology as a polar-growth cell-shape system.)
- **Existing causal graph summary:** filament_shaped_streptomyces_polar_growth: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **filament shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/filament_shaped.yaml`.

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
**Generated:** 2026-08-04T08:24:36.195716

1. sen2024adispensablesepiva pages 10-12
2. zhang2020branchingofsporogenic pages 27-41
3. sen2024adispensablesepiva pages 1-2
4. bhowmick2024cellshapeand pages 8-10
5. bhowmick2024cellshapeand pages 1-2
6. claessen2024thestomatinlikeprotein pages 27-28
7. claessen2024thestomatinlikeprotein pages 20-27
8. 10.1128/mbio.01492-24
9. 10.1186/s12866-024-03625-6
10. 10.21203/rs.3.rs-3811693/v1
11. 10.1101/2020.12.26.424426
12. 10.1016/j.mib.2010.10.002
13. https://doi.org/10.1128/mbio.01492-24
14. https://doi.org/10.1186/s12866-024-03625-6
15. https://doi.org/10.21203/rs.3.rs-3811693/v1
16. https://doi.org/10.1101/2020.12.26.424426
17. https://doi.org/10.1016/j.mib.2010.10.002
18. https://doi.org/10.1186/s12866-024-03625-6,
19. https://doi.org/10.1101/2020.12.26.424426,
20. https://doi.org/10.1128/mbio.01492-24,
21. https://doi.org/10.21203/rs.3.rs-3811693/v1,