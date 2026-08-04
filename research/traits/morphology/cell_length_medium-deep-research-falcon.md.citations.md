# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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
**Generated:** 2026-08-04T07:44:30.852684

1. ojkic2021bacterialcellshape pages 1-2
2. westfall2017bacterialcellsize pages 11-12
3. hayashi2024septalwallsynthesis pages 1-2
4. westfall2018comprehensiveanalysisof pages 17-18
5. gulsoy2024divisomeminimizationshows pages 1-4
6. cameron2024insightsintothe pages 3-4
7. meunier2021bacterialcellproliferation pages 22-24
8. jun2018fundamentalprinciplesin pages 27-28
9. westfall2017bacterialcellsize pages 9-11
10. vadia2015growthrateand pages 4-6
11. vadia2015growthrateand pages 6-7
12. s
13. assembly/polymerization
14. 10.1038/s41579-023-00942-x
15. 10.1038/s42003-024-07279-y
16. 10.1101/2024.01.12.575403
17. https://doi.org/10.1038/s41579-023-00942-x
18. https://doi.org/10.1038/s42003-024-07279-y
19. https://doi.org/10.1101/2024.01.12.575403
20. https://doi.org/10.1093/femsre/fuaa046
21. https://doi.org/10.1371/journal.pgen.1007205
22. https://doi.org/10.1088/1361-6633/aaa628
23. https://doi.org/10.1146/annurev-micro-090816-093803
24. https://doi.org/10.1016/j.mib.2015.01.011
25. https://doi.org/10.1371/journal.pgen.1003663
26. https://doi.org/10.1038/s41579-023-00942-x](https://doi.org/10.1038/s41579-023-00942-x
27. https://doi.org/10.1038/s42003-024-07279-y](https://doi.org/10.1038/s42003-024-07279-y
28. https://doi.org/10.1101/2024.01.12.575403](https://doi.org/10.1101/2024.01.12.575403
29. https://doi.org/10.1093/femsre/fuaa046](https://doi.org/10.1093/femsre/fuaa046
30. https://doi.org/10.1371/journal.pgen.1007205](https://doi.org/10.1371/journal.pgen.1007205
31. https://doi.org/10.1088/1361-6633/aaa628](https://doi.org/10.1088/1361-6633/aaa628
32. https://doi.org/10.1146/annurev-micro-090816-093803](https://doi.org/10.1146/annurev-micro-090816-093803
33. https://doi.org/10.1016/j.mib.2015.01.011](https://doi.org/10.1016/j.mib.2015.01.011
34. https://doi.org/10.1371/journal.pgen.1003663](https://doi.org/10.1371/journal.pgen.1003663
35. https://doi.org/10.1101/2021.03.25.436990,
36. https://doi.org/10.1146/annurev-micro-090816-093803,
37. https://doi.org/10.1038/s42003-024-07279-y,
38. https://doi.org/10.1371/journal.pgen.1007205,
39. https://doi.org/10.1016/j.mib.2015.01.011,
40. https://doi.org/10.1093/femsre/fuaa046,
41. https://doi.org/10.1038/s41579-023-00942-x,
42. https://doi.org/10.1088/1361-6633/aaa628,
43. https://doi.org/10.1101/2024.01.12.575403,