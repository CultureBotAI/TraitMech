# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 3
- **METPO identifier:** METPO:1001104
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that can cause serious or potentially lethal disease through inhalation or other routes, requiring specialized containment facilities with controlled access, directional airflow, and strict safety protocols.
- **Parent traits:** METPO:1001101
- **Synonyms:** 3, 3**
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports highly virulent aerosol-transmissible pathogens (serious or potentially lethal disease) as BSL-3 agents.)
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_3.yaml`.

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
**Generated:** 2026-06-17T20:25:10.051178

1. bawshkhah2024thebiosafetylevel pages 2-3
2. mendonca2024enhancingbiosafetymanagement pages 93-95
3. blacksell2023thebiosafetyresearchc pages 9-10
4. blacksell2023thebiosafetyresearchc pages 2-3
5. blacksell2023thebiosafetyresearchc pages 8-9
6. bawshkhah2024thebiosafetylevel pages 1-2
7. blacksell2023thebiosafetyresearcha pages 6-8
8. blacksell2023thebiosafetyresearchc pages 12-13
9. blacksell2023thebiosafetyresearchc pages 6-8
10. blacksell2023thebiosafetyresearchb pages 9-10
11. ziegler2024boundaryintegritytesting pages 7-9
12. ziegler2024boundaryintegritytesting pages 9-9
13. mushasha2024existingoperationalstandards pages 8-9
14. mushasha2024existingoperationalstandards pages 1-2
15. ziegler2024boundaryintegritytesting pages 1-2
16. mendonca2024enhancingbiosafetymanagement pages 37-39
17. gao2024frombiosafetyto pages 5-6
18. gao2024frombiosafetyto pages 6-7
19. blacksell2023thebiosafetyresearchc pages 13-14
20. bawshkhah2024thebiosafetylevel pages 3-4
21. blacksell2023thebiosafetyresearchc pages 1-2
22. ziegler2024boundaryintegritytesting pages 5-7
23. bawshkhah2024thebiosafetylevel pages 4-6
24. gao2024frombiosafetyto pages 9-10
25. mendonca2024enhancingbiosafetymanagement pages 28-31
26. https://doi.org/10.1089/apb.2022.0038
27. https://doi.org/10.64483/jmph-115
28. https://doi.org/10.1089/apb.2022.0042
29. https://doi.org/10.1089/apb.2023.0017
30. https://doi.org/10.3389/fpubh.2024.1455738
31. https://doi.org/10.26686/nzjhsp.v1i2.9540
32. https://doi.org/10.1089/apb.2022.0039
33. https://doi.org/10.3390/laboratories1030013
34. https://doi.org/10.47328/ufvbbt.2024.220
35. https://doi.org/10.64483/jmph-115,
36. https://doi.org/10.3390/laboratories1030013,
37. https://doi.org/10.1089/apb.2022.0042,
38. https://doi.org/10.47328/ufvbbt.2024.220,
39. https://doi.org/10.1089/apb.2022.0038,
40. https://doi.org/10.1089/apb.2023.0017,
41. https://doi.org/10.26686/nzjhsp.v1i2.9540,
42. https://doi.org/10.1089/apb.2022.0039,
43. https://doi.org/10.3389/fpubh.2024.1455738,