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
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 3 nodes, 2 edges

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
**Generated:** 2026-06-17T20:12:08.454171

1. siegel2022principlesofbiosafety pages 32-44
2. siegel2022principlesofbiosafety pages 17-32
3. gao2024frombiosafetyto pages 5-6
4. mendonca2024enhancingbiosafetymanagement pages 28-31
5. gao2024frombiosafetyto pages 6-7
6. gao2025globalsafetyand pages 14-17
7. niu2024thestateof pages 2-3
8. byrd2019guidelinesforbiosafety pages 1-2
9. pokharel2023thediversityof pages 1-2
10. sarwar2022amodifiedhand pages 1-2
11. cong2025analysisofcompliance pages 1-2
12. niu2024thestateof pages 1-2
13. https://doi.org/10.3390/laboratories1030013
14. https://doi.org/10.2172/1887109
15. https://doi.org/10.47328/ufvbbt.2024.220
16. https://doi.org/10.3389/fpubh.2022.965853
17. https://doi.org/10.3390/microorganisms11020344
18. https://doi.org/10.3389/fpubh.2024.1436503
19. https://doi.org/10.3389/fbioe.2025.1637056
20. https://doi.org/10.1128/jmbe.v20i3.1975
21. https://doi.org/10.1089/apb.2022.0040
22. https://doi.org/10.3390/laboratories1030013,
23. https://doi.org/10.2172/1887109,
24. https://doi.org/10.47328/ufvbbt.2024.220,
25. https://doi.org/10.3390/laboratories2010003,
26. https://doi.org/10.3389/fpubh.2024.1436503,
27. https://doi.org/10.1128/jmbe.v20i3.1975,
28. https://doi.org/10.3390/microorganisms11020344,
29. https://doi.org/10.3389/fpubh.2022.965853,
30. https://doi.org/10.3389/fbioe.2025.1637056,