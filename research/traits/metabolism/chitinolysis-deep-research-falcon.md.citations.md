# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chitinolysis
- **METPO identifier:** traitmech:000112
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes chitin to N-acetylglucosamine oligomers and monomers using secreted chitinases.
- **Parent traits:** traitmech:000110
- **Synonyms:** chitinolytic, chitin degradation
- **Existing evidence:** DOI:10.3389/fmicb.2013.00149:  (Beier & Bertilsson review bacterial chitin degradation mechanisms and ecophysiological strategies.) | DOI:10.1080/07388550601168223:  (Bhattacharya et al. review the properties and potential of bacterial chitinases.)
- **Existing causal graph summary:** chitinolysis_chitinase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chitinolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/chitinolysis.yaml`.

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
**Generated:** 2026-06-18T04:31:31.610756

1. polishchuk2024genesofstreptomyces pages 1-3
2. son2024functionalcomparisonof pages 1-2
3. sanram2023structuraldisplacementmodel pages 1-2
4. sanram2023structuraldisplacementmodel pages 7-8
5. ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 5-7
6. ran2023genomicanalysisand pages 7-9
7. guo2024heterologousexpressionand pages 10-12
8. ran2023genomicanalysisand pages 6-7
9. unuofin2024chitinasesexpandingthe pages 5-6
10. ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 1-2
11. ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 16-17
12. ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 17-17
13. ohnuma2023periplasmicchitooligosaccharidebindingprotein pages 7-10
14. unuofin2024chitinasesexpandingthe pages 2-5
15. sanram2023structuraldisplacementmodel pages 14-15
16. guo2024heterologousexpressionand pages 12-13
17. https://doi.org/10.3389/fmicb.2013.00149;
18. https://doi.org/10.1007/s11356-024-33728-6
19. https://doi.org/10.3390/toxins16010026
20. https://doi.org/10.1038/s41598-023-47253-y;
21. https://doi.org/10.1016/j.jbc.2023.105000
22. https://doi.org/10.1038/s41598-023-47253-y
23. https://doi.org/10.15407/microbiolj86.04.053
24. https://doi.org/10.15407/microbiolj86.04.053;
25. https://doi.org/10.3389/fpls.2023.1335646
26. https://doi.org/10.3389/fmicb.2023.1121720
27. https://doi.org/10.3390/md22060287
28. https://doi.org/10.1186/s12866-024-03414-1
29. https://doi.org/10.3389/fmicb.2013.00149
30. https://doi.org/10.3389/fmicb.2013.00149,
31. https://doi.org/10.3389/fmicb.2023.1121720,
32. https://doi.org/10.1016/j.jbc.2023.105000,
33. https://doi.org/10.15407/microbiolj86.04.053,
34. https://doi.org/10.3390/toxins16010026,
35. https://doi.org/10.1038/s41598-023-47253-y,
36. https://doi.org/10.3390/md22060287,
37. https://doi.org/10.1186/s12866-024-03414-1,
38. https://doi.org/10.1007/s11356-024-33728-6,