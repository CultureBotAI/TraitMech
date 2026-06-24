# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width
- **METPO identifier:** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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
**Generated:** 2026-06-18T07:05:36.382330

1. wilson2023anexhaustivemultiple pages 8-10
2. costa2024theroleof pages 1-2
3. shlosman2023allostericactivationof pages 1-2
4. middlemiss2024molecularmotortugofwar pages 8-9
5. castanheira2023evidenceoftwo pages 1-2
6. willdigg2023adecreasein pages 1-3
7. basan2024homeostasisofcytoplasmic pages 10-12
8. middlemiss2024molecularmotortugofwar pages 1-2
9. galinier2023recentadvancesin pages 15-16
10. galinier2023recentadvancesin pages 14-15
11. https://doi.org/10.3390/biom13050720
12. https://doi.org/10.1038/s41467-023-39037-9
13. https://doi.org/10.1038/s41467-024-49785-x
14. https://doi.org/10.1038/s42003-023-05308-w
15. https://doi.org/10.1128/mbio.00475-23
16. https://doi.org/10.1128/mbio.01760-23
17. https://doi.org/10.1128/mbio.03235-23
18. https://doi.org/10.21203/rs.3.rs-4138690/v1
19. https://doi.org/10.1101/2024.11.22.624946
20. https://doi.org/10.1038/s41467-024-49785-x,
21. https://doi.org/10.1128/mbio.00475-23,
22. https://doi.org/10.1128/mbio.03235-23,
23. https://doi.org/10.1128/mbio.01760-23,
24. https://doi.org/10.1101/2024.11.22.624946,
25. https://doi.org/10.1038/s41467-023-39037-9,
26. https://doi.org/10.1038/s42003-023-05308-w,
27. https://doi.org/10.21203/rs.3.rs-4138690/v1,
28. https://doi.org/10.3390/biom13050720,