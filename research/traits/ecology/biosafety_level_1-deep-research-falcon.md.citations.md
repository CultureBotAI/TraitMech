# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 1
- **METPO identifier:** METPO:1001102
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses minimal potential hazard to laboratory workers and the environment, requiring only standard microbiological practices.
- **Parent traits:** METPO:1001101
- **Synonyms:** 1
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the absence or low expression of virulence factors in BSL-1 agents (non-pathogenic to healthy adults).)
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **biosafety level 1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_1.yaml`.

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
**Generated:** 2026-08-03T22:55:48.255387

1. gao2024frombiosafetyto pages 5-6
2. hoffmann2023safetybydesign pages 7-8
3. hoffmann2023safetybydesign pages 8-10
4. biosafety2013biosafetyguidelinesfor pages 1-2
5. pavao2023biocontainmenttechniquesand pages 5-7
6. kim2023systemsandsynthetic pages 5-6
7. kim2023systemsandsynthetic pages 12-13
8. gomeztatay2024xenobiologyforthe pages 4-5
9. gomeztatay2024xenobiologyforthe pages 5-7
10. pavao2023biocontainmenttechniquesand pages 13-15
11. gomeztatay2024xenobiologyforthe pages 7-8
12. siguenza2024engineeredbacterialtherapeutics pages 6-7
13. siguenza2024engineeredbacterialtherapeutics pages 9-11
14. https://doi.org/10.3390/laboratories1030013
15. https://doi.org/10.3390/life14080996
16. https://doi.org/10.1016/j.trecan.2024.04.001
17. https://doi.org/10.3389/fbioe.2023.1267378
18. https://doi.org/10.1016/j.isci.2023.106165
19. https://doi.org/10.3390/fermentation9040341
20. https://doi.org/10.1128/jmbe.v14i1.531
21. https://doi.org/10.1128/jmbe.v14i1.531,
22. https://doi.org/10.3390/laboratories1030013,
23. https://doi.org/10.3390/life14080996,
24. https://doi.org/10.1016/j.isci.2023.106165,
25. https://doi.org/10.3390/fermentation9040341,
26. https://doi.org/10.1016/j.trecan.2024.04.001,
27. https://doi.org/10.3389/fbioe.2023.1267378,