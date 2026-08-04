# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** square shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 10 nodes, 7 edges

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
**Generated:** 2026-08-04T10:12:24.133065

1. cooper2023archaealtubulinlikeproteins pages 1-2
2. saponetti2011morphologicalandstructural pages 2-3
3. oren2024novelinsightsinto pages 1-2
4. dyallsmith2011haloquadratumwalsbyi pages 1-2
5. saponetti2011morphologicalandstructural pages 1-2
6. saponetti2011morphologicalandstructural pages 5-8
7. saponetti2011morphologicalandstructural pages 3-5
8. martincuadrado2015diversityofthe pages 1-2
9. kugelgen2021completeatomicstructure pages 1-3
10. cui2024proposedminimalstandards pages 1-2
11. s
12. UNCERTAIN
13. 10.1371/journal.pone.0018653
14. 10.1371/journal.pone.0020968
15. 10.1186/s12864-015-1794-8
16. 10.1016/j.celrep.2021.110052
17. 10.3390/genes14101861
18. 10.1099/ijsem.0.006290
19. 10.1038/s44185-024-00050-w
20. https://doi.org/10.1371/journal.pone.0018653
21. https://doi.org/10.1371/journal.pone.0020968
22. https://doi.org/10.1186/s12864-015-1794-8
23. https://doi.org/10.1016/j.celrep.2021.110052
24. https://doi.org/10.3390/genes14101861
25. https://doi.org/10.1099/ijsem.0.006290
26. https://doi.org/10.1038/s44185-024-00050-w
27. https://doi.org/10.1371/journal.pone.0018653,
28. https://doi.org/10.1016/j.celrep.2021.110052,
29. https://doi.org/10.1186/s12864-015-1794-8,
30. https://doi.org/10.3390/genes14101861,
31. https://doi.org/10.1371/journal.pone.0020968,
32. https://doi.org/10.1038/s44185-024-00050-w,
33. https://doi.org/10.1099/ijsem.0.006290,