# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **dissimilatory nitrate reduction to ammonium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`.

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
**Generated:** 2026-08-04T06:08:25.439295

1. egas2024anovelmechanism pages 1-2
2. yuan2024spatiotemporalpatternsand pages 1-2
3. sorokin2023trichlorobacterammonificansa pages 2-3
4. wu2024anaerobicoxidationof pages 1-2
5. xie2024usingstaticmagnetic pages 1-2
6. sorokin2023trichlorobacterammonificansa pages 2-2
7. egas2024anovelmechanism pages 10-13
8. sorokin2023trichlorobacterammonificansa pages 3-4
9. xie2024longtermoperationand pages 1-2
10. egas2024anovelmechanism pages 2-5
11. wu2024aerobiccarbonmetabolism pages 8-12
12. sorokin2023trichlorobacterammonificansa pages 6-7
13. xie2024longtermoperationand pages 2-4
14. NiFe
15. 10.1128/msystems.00967-23
16. 10.1038/s41396-023-01473-2
17. 10.1093/ismejo/wrae063
18. 10.3389/fmicb.2024.1411753
19. 10.1038/s41545-024-00352-3
20. 10.1038/s41545-024-00356-z
21. 10.1101/2024.11.04.621907
22. https://doi.org/10.1128/msystems.00967-23
23. https://doi.org/10.1038/s41396-023-01473-2
24. https://doi.org/10.1093/ismejo/wrae063
25. https://doi.org/10.3389/fmicb.2024.1411753
26. https://doi.org/10.1038/s41545-024-00352-3
27. https://doi.org/10.1038/s41545-024-00356-z
28. https://doi.org/10.1101/2024.11.04.621907
29. https://doi.org/10.1128/msystems.00967-23,
30. https://doi.org/10.3389/fmicb.2024.1411753,
31. https://doi.org/10.1038/s41396-023-01473-2,
32. https://doi.org/10.1093/ismejo/wrae063,
33. https://doi.org/10.1038/s41545-024-00352-3,
34. https://doi.org/10.1038/s41545-024-00356-z,
35. https://doi.org/10.1101/2024.11.04.621907,