# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** heterotrophic
- **METPO identifier:** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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
**Generated:** 2026-06-18T11:47:48.518868

1. stebegg2023heterotrophyamongcyanobacteria pages 2-4
2. sim2024highthroughputoptimizationof pages 1-2
3. coe2024emergenceofmetabolic pages 8-9
4. karnachuk2024novelthermophilicgenera pages 10-11
5. lucius2024theprimarycarbon pages 2-3
6. zhang2024metagenomiccharacterizationof pages 6-8
7. karnachuk2024novelthermophilicgenera pages 5-8
8. muramatsu2024nutrientacquisitionstrategies pages 1-2
9. lucius2024theprimarycarbon pages 1-2
10. liaqat2023mixotrophiccultivationof pages 12-12
11. zhang2024metagenomiccharacterizationof pages 1-2
12. liaqat2023mixotrophiccultivationof pages 13-13
13. coe2024emergenceofmetabolic pages 1-2
14. zhang2024metagenomiccharacterizationof pages 4-6
15. karnachuk2024novelthermophilicgenera pages 11-13
16. sim2024highthroughputoptimizationof pages 9-11
17. https://doi.org/10.1021/acsomega.3c02205
18. https://doi.org/10.3389/fpls.2024.1417680
19. https://doi.org/10.1186/s40168-023-01728-2
20. https://doi.org/10.1111/raq.12700
21. https://doi.org/10.3389/fmicb.2024.1441865
22. https://doi.org/10.1016/j.chom.2024.05.011
23. https://doi.org/10.1093/ismeco/ycae131
24. https://doi.org/10.1186/s12934-024-02560-5
25. https://doi.org/10.1021/acsomega.3c02205,
26. https://doi.org/10.1016/j.chom.2024.05.011,
27. https://doi.org/10.3389/fpls.2024.1417680,
28. https://doi.org/10.1111/raq.12700,
29. https://doi.org/10.3389/fmicb.2024.1441865,
30. https://doi.org/10.1186/s12934-024-02560-5,
31. https://doi.org/10.1186/s40168-023-01728-2,
32. https://doi.org/10.1093/ismeco/ycae131,