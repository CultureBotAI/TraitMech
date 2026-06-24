# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** white pigmented
- **METPO identifier:** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **white pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/white_pigmented.yaml`.

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
**Generated:** 2026-06-18T10:41:00.755239

1. alves2024experimentalevolutionof pages 13-15
2. siems2023identificationofstaphyloxanthin pages 6-8
3. esteves2024serratiamarcescensatcc pages 1-2
4. erdmann2024thetetonsystem pages 1-2
5. esteves2024serratiamarcescensatcc pages 2-3
6. ni2024glmsplaysa pages 5-7
7. andamora2024increasedproteolyticactivity pages 1-2
8. koc2024prodigiosinapromising pages 1-3
9. alves2024experimentalevolutionof pages 9-13
10. ni2024glmsplaysa pages 7-10
11. ni2024glmsplaysa pages 1-2
12. esteves2024serratiamarcescensatcc pages 9-10
13. esteves2024serratiamarcescensatcc pages 5-7
14. https://doi.org/10.1128/mbio.00346-24
15. https://doi.org/10.1080/21505594.2024.2352476
16. https://doi.org/10.3389/fmicb.2023.1272734
17. https://doi.org/10.1038/s41598-024-68747-3
18. https://doi.org/10.33073/pjm-2024-002
19. https://doi.org/10.1080/21501203.2023.2249010
20. https://doi.org/10.1007/s00792-024-01354-2
21. https://doi.org/10.1128/mbio.00346-24,
22. https://doi.org/10.1080/21501203.2023.2249010,
23. https://doi.org/10.3389/fmicb.2023.1272734,
24. https://doi.org/10.1038/s41598-024-68747-3,
25. https://doi.org/10.1007/s00792-024-01354-2,
26. https://doi.org/10.1080/21505594.2024.2352476,
27. https://doi.org/10.33073/pjm-2024-002,
28. https://doi.org/10.16970/entoted.1517520,