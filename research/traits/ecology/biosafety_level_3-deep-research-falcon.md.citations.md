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
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 10 nodes, 8 edges

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
**Generated:** 2026-08-03T23:06:10.187011

1. bawshkhah2024thebiosafetylevel pages 1-2
2. zuo2024ahistoricalstudy pages 4-6
3. kaufer2020laboratorybiosafetymeasures pages 1-3
4. blacksell2023thebiosafetyresearch pages 4-5
5. pavone2024biologicalcontainmentfor pages 3-5
6. ottendorfer2024establishmentofa pages 1-2
7. argyropoulos2023airbornetransmissionof pages 21-22
8. blacksell2023thebiosafetyresearch pages 8-9
9. blacksell2023thebiosafetyresearch pages 15-15
10. joseph2021managementsystemapproach pages 2-4
11. blacksell2023thebiosafetyresearch pages 10-12
12. woude2008regulationandfunction pages 1-2
13. blacksell2023thebiosafetyresearch pages 2-4
14. ziegler2024boundaryintegritytesting pages 1-2
15. zuo2024ahistoricalstudy pages 12-13
16. blacksell2023thebiosafetyresearch pages 9-10
17. ziegler2024boundaryintegritytesting pages 7-9
18. haider2024exploringthefactors pages 1-3
19. to
20. https://doi.org/10.1089/apb.2022.0038
21. https://doi.org/10.1089/apb.2023.0017
22. https://doi.org/10.3390/laboratories1020007
23. https://doi.org/10.3390/pathogens13020116
24. https://doi.org/10.3390/ani14030454
25. https://doi.org/10.1007/s11869-022-01286-w
26. https://doi.org/10.1016/j.pathol.2020.09.006
27. https://doi.org/10.1089/apb.2021.0007
28. https://doi.org/10.1146/annurev.micro.62.081307.162938.
29. https://doi.org/10.3390/laboratories1020007,
30. https://doi.org/10.64483/jmph-115,
31. https://doi.org/10.1089/apb.2022.0038,
32. https://doi.org/10.1016/j.pathol.2020.09.006,
33. https://doi.org/10.3390/ani14030454,
34. https://doi.org/10.3390/pathogens13020116,
35. https://doi.org/10.1007/s11869-022-01286-w,
36. https://doi.org/10.1089/apb.2023.0017,
37. https://doi.org/10.1089/apb.2021.0007,
38. https://doi.org/10.32388/lb0dky,
39. https://doi.org/10.1146/annurev.micro.62.081307.162938,