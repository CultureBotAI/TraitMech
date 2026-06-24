# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **METPO identifier:** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 4 nodes, 2 edges

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
**Generated:** 2026-06-18T04:50:39.940386

1. egas2024anovelmechanism pages 1-2
2. egas2024anovelmechanism pages 2-5
3. yuan2024spatiotemporalpatternsand pages 4-5
4. hird2025fromgenesto pages 11-13
5. egas2024anovelmechanism pages 9-10
6. wu2024aerobiccarbonmetabolism pages 1-5
7. hong2024artificialcultivationof pages 8-11
8. yuan2024spatiotemporalpatternsand pages 7-10
9. wu2024aerobiccarbonmetabolism pages 5-8
10. zhao2025investigationofnitrogen pages 15-17
11. kostyuk2024mathematicalmodellingof pages 8-12
12. yuan2024spatiotemporalpatternsand pages 2-4
13. wu2024aerobiccarbonmetabolism pages 12-16
14. CHEBI:17632
15. CHEBI:16301
16. CHEBI:28938
17. CHEBI:17234
18. CHEBI:16480
19. CHEBI:17045
20. https://doi.org/10.1128/msystems.00967-23
21. https://doi.org/10.1128/aem.00292-25
22. https://doi.org/10.3389/fmicb.2015.00542
23. https://doi.org/10.3390/land13101557
24. https://doi.org/10.1101/2024.11.04.621907
25. https://doi.org/10.3389/fmicb.2024.1411753
26. https://doi.org/10.1016/j.jwpe.2025.107536
27. https://doi.org/10.1128/msystems.00967-23,
28. https://doi.org/10.1101/2024.11.04.621907,
29. https://doi.org/10.3389/fmicb.2024.1411753,
30. https://doi.org/10.1128/aem.00292-25,
31. https://doi.org/10.3390/land13101557,
32. https://doi.org/10.1016/j.jwpe.2025.107536,