# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** brown pigmented
- **METPO identifier:** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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
**Generated:** 2026-06-18T06:40:04.595168

1. qin2024melanininfungi pages 10-11
2. thomsen2023beetredfood pages 5-6
3. moustafa2024mutationofhmga pages 2-4
4. qin2024melanininfungi pages 7-8
5. thiourmauprivez2023assessingtheeffects pages 1-5
6. elzawawy2024bioproductionandoptimization pages 1-2
7. moustafa2024mutationofhmga pages 1-2
8. thiourmauprivez2023assessingtheeffects pages 8-11
9. thomsen2023beetredfood pages 6-7
10. thiourmauprivez2023assessingtheeffects pages 5-8
11. https://doi.org/10.1038/s41564-023-01517-5
12. https://doi.org/10.1128/spectrum.00410-24
13. https://doi.org/10.1007/s11356-022-22801-7
14. https://doi.org/10.1186/s12934-024-02614-8
15. https://doi.org/10.1101/2024.04.11.589128
16. https://doi.org/10.1186/s12934-023-02276-y
17. https://doi.org/10.1128/spectrum.00410-24,
18. https://doi.org/10.1007/s11356-022-22801-7,
19. https://doi.org/10.1186/s12934-024-02614-8,
20. https://doi.org/10.1038/s41564-023-01517-5,
21. https://doi.org/10.1101/2024.04.11.589128,
22. https://doi.org/10.1186/s12934-023-02276-y,