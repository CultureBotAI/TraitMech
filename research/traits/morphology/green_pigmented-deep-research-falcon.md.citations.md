# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** green pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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
**Generated:** 2026-08-04T08:55:30.332125

1. mendoza2024thehistidinekinase pages 2-5
2. ringel2018thebiosynthesisof pages 1-3
3. schalk2020anoverviewof pages 12-13
4. marey2024transformingmicrobialpigment pages 1-2
5. mendoza2024thehistidinekinase pages 12-14
6. mendoza2024thehistidinekinase pages 1-2
7. mendoza2024thehistidinekinase pages 5-9
8. 10.1128/jb.00276-23
9. 10.1186/s12934-024-02486-y
10. 10.1186/s12934-024-02438-6
11. 10.1186/s12934-023-02122-1
12. 10.1007/s11274-023-03548-w
13. 10.1111/1462-2920.14937
14. 10.15698/mic2018.10.649
15. https://doi.org/10.1128/jb.00276-23
16. https://doi.org/10.1186/s12934-024-02486-y
17. https://doi.org/10.1186/s12934-024-02438-6
18. https://doi.org/10.1186/s12934-023-02122-1
19. https://doi.org/10.1007/s11274-023-03548-w
20. https://doi.org/10.1111/1462-2920.14937
21. https://doi.org/10.15698/mic2018.10.649
22. https://doi.org/10.1186/s12934-023-02122-1,
23. https://doi.org/10.1007/s11274-023-03548-w,
24. https://doi.org/10.1111/1462-2920.14937,
25. https://doi.org/10.15698/mic2018.10.649,
26. https://doi.org/10.1186/s12934-024-02438-6,
27. https://doi.org/10.1128/jb.00276-23,
28. https://doi.org/10.1186/s12934-024-02486-y,