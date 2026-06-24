# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** rRNA operon copy number
- **METPO identifier:** traitmech:000101
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the number of ribosomal RNA (rrn) operons encoded in a genome, which correlates with maximal growth rate and ecological strategy.
- **Parent traits:** METPO:1000188
- **Synonyms:** rrn copy number
- **Existing evidence:** DOI:10.1128/AEM.66.4.1328-1333.2000:  (Klappenbach, Dunbar & Schmidt show rRNA operon copy number reflects ecological strategies, with fast responders carrying more copies.) | DOI:10.1038/nmicrobiol.2016.160:  (Roller, Stoddard & Schmidt link rrn copy number to bacterial growth rate and growth efficiency.)
- **Existing causal graph summary:** rrn_copy_growth_rate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **rRNA operon copy number** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/rrna_operon_copy_number.yaml`.

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
**Generated:** 2026-06-18T04:16:21.669174

1. klappenbach2000rrnaoperoncopy pages 1-2
2. fan2023rnapolymeraseredistribution pages 14-15
3. pan2023microbialdiversitybiased pages 1-2
4. he2025microbiallifehistorystrategies pages 13-15
5. anda2023bacteriacanmaintain pages 1-2
6. klappenbach2000rrnaoperoncopy pages 2-3
7. piton2023lifehistorystrategies pages 1-5
8. zhou2024thebiogeographyof pages 1-2
9. roller2016exploitingrrnaoperon pages 1-5
10. roller2016exploitingrrnaoperon pages 5-11
11. welfer2025impactsofribosomal pages 5-6
12. zhang2024antarcticsoilsselect pages 1-2
13. klappenbach2000rrnaoperoncopy pages 4-5
14. https://doi.org/10.1128/AEM.66.4.1328-1333.2000
15. https://doi.org/10.1038/nmicrobiol.2016.160
16. https://doi.org/10.1093/NAR/GKAD511
17. https://doi.org/10.1038/s41467-023-42681-w
18. https://doi.org/10.1038/s41467-024-53753-w
19. https://doi.org/10.1128/msystems.00178-25
20. https://doi.org/10.1038/s43705-023-00266-0
21. https://doi.org/10.1128/AEM.02108-22
22. https://doi.org/10.1093/nar/gkad511
23. https://doi.org/10.1128/aem.02108-22
24. https://doi.org/10.1038/s41564-023-01465-0
25. https://doi.org/10.3390/microorganisms12081689
26. https://doi.org/10.1128/aem.66.4.1328-1333.2000
27. https://doi.org/10.1128/aem.66.4.1328-1333.2000,
28. https://doi.org/10.1038/nmicrobiol.2016.160,
29. https://doi.org/10.1093/nar/gkad511,
30. https://doi.org/10.1128/aem.02108-22,
31. https://doi.org/10.1128/msystems.00178-25,
32. https://doi.org/10.1038/s41467-023-42681-w,
33. https://doi.org/10.1038/s41564-023-01465-0,
34. https://doi.org/10.1038/s41467-024-53753-w,
35. https://doi.org/10.1038/s43705-023-00266-0,
36. https://doi.org/10.1098/rstb.2023.0379,
37. https://doi.org/10.3390/microorganisms12081689,