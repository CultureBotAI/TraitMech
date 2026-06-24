# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** square shaped
- **METPO identifier:** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **square shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/square_shaped.yaml`.

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
**Generated:** 2026-06-18T10:18:37.718050

1. saponetti2011morphologicalandstructural pages 1-2
2. wolferen2022thecellbiology pages 3-4
3. dudek2023previouslyuncharacterizedrectangular pages 45-48
4. saponetti2011morphologicalandstructural pages 5-8
5. wolferen2022thecellbiology pages 4-6
6. kugelgen2024membranelesschannelssieve pages 1-2
7. kugelgen2024membranelesschannelssieve pages 5-6
8. saponetti2011morphologicalandstructural pages 8-8
9. martincuadrado2015diversityofthe pages 1-2
10. martincuadrado2015diversityofthe pages 7-8
11. martincuadrado2015diversityofthe pages 4-7
12. wolferen2022thecellbiology pages 7-9
13. wolferen2022thecellbiology pages 9-11
14. saponetti2011morphologicalandstructural pages 3-5
15. https://doi.org/10.1038/s41564-022-01215-8
16. https://doi.org/10.1371/journal.pone.0018653
17. https://doi.org/10.1186/s12864-015-1794-8
18. https://doi.org/10.1038/s41586-024-07462-5
19. https://doi.org/10.1101/2021.10.23.465578
20. https://doi.org/10.1371/journal.pone.0018653,
21. https://doi.org/10.1038/s41564-022-01215-8,
22. https://doi.org/10.1101/2021.10.23.465578,
23. https://doi.org/10.1038/s41586-024-07462-5,
24. https://doi.org/10.1186/s12864-015-1794-8,