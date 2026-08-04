# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** disc shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000689
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism is flat and circular.
- **Parent traits:** METPO:1000666
- **Synonyms:** disc
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports flat-disc geometry as a determined morphological phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea description supports flat disc-shaped cell morphology in the wild.)
- **Existing causal graph summary:** disc_shaped_anisotropic_wall_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **disc shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/disc_shaped.yaml`.

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
**Generated:** 2026-08-04T08:17:52.781649

1. silva2021improvedgrowthand pages 1-2
2. schiller2024identificationofstructural pages 3-5
3. cooper2023archaealtubulinlikeproteins pages 1-2
4. schiller2024identificationofstructural pages 6-7
5. brown2024mindproteinsregulate pages 1-2
6. schiller2024identificationofstructural pages 5-6
7. schiller2024identificationofstructural pages 5-5
8. schiller2024identificationofstructural pages 7-9
9. schiller2024identificationofstructural pages 9-9
10. schiller2024identificationofstructural pages 1-2
11. 10.1038/s41467-024-45196-0
12. 10.3389/fmicb.2024.1474697
13. 10.3389/fmicb.2023.1270665
14. 10.3390/genes14101861
15. 10.1099/mic.0.001012
16. https://doi.org/10.1038/s41467-024-45196-0
17. https://doi.org/10.3389/fmicb.2024.1474697
18. https://doi.org/10.3389/fmicb.2023.1270665
19. https://doi.org/10.3390/genes14101861
20. https://doi.org/10.1099/mic.0.001012
21. https://doi.org/10.1038/s41467-024-45196-0,
22. https://doi.org/10.1099/mic.0.001012,
23. https://doi.org/10.3389/fmicb.2023.1270665,
24. https://doi.org/10.3390/genes14101861,
25. https://doi.org/10.3389/fmicb.2024.1474697,