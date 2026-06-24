# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidotolerant
- **METPO identifier:** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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
**Generated:** 2026-06-17T21:15:25.578818

1. krulwich2011molecularaspectsof pages 14-15
2. qin2024characterizationofmild pages 1-2
3. xu2023transcriptomicandmetabolomic pages 1-2
4. xu2023transcriptomicandmetabolomic pages 2-5
5. krulwich2011molecularaspectsof pages 3-5
6. li2024responseofescherichia pages 7-9
7. liu2024expressionofstress pages 3-4
8. li2024responseofescherichia pages 2-4
9. li2024responseofescherichia pages 4-5
10. li2024responseofescherichia pages 5-7
11. jiang2024exogenousputrescineplays pages 6-9
12. krulwich2011molecularaspectsof pages 6-8
13. jiang2024exogenousputrescineplays pages 1-2
14. krulwich2011molecularaspectsof pages 1-3
15. krulwich2011molecularaspectsof pages 5-6
16. jiang2024exogenousputrescineplays pages 9-12
17. liu2024expressionofstress pages 4-6
18. liu2024expressionofstress pages 6-7
19. liu2024expressionofstress pages 1-2
20. liu2024expressionofstress pages 2-3
21. xu2023transcriptomicandmetabolomic pages 10-11
22. s
23. https://doi.org/10.1038/nrmicro2549
24. https://doi.org/10.3390/microorganisms12091774
25. https://doi.org/10.1128/spectrum.00022-23
26. https://doi.org/10.1128/spectrum.00022-23;
27. https://doi.org/10.3390/microorganisms12081565
28. https://doi.org/10.1128/aem.00569-24
29. https://doi.org/10.3389/fmicb.2024.1437803
30. https://doi.org/10.1038/nrmicro2549,
31. https://doi.org/10.3390/microorganisms12091774,
32. https://doi.org/10.3390/microorganisms12081565,
33. https://doi.org/10.1128/spectrum.00022-23,
34. https://doi.org/10.1128/aem.00569-24,
35. https://doi.org/10.3389/fmicb.2024.1437803,