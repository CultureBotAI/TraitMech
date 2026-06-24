# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Syntrophy
- **METPO identifier:** METPO:1002006
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which the metabolism of one species is thermodynamically dependent on the removal of its products by another species.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2166: Interspecies electron transfer is a key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic communities.)
- **Existing causal graph summary:** syntrophy_interspecies_electron_transfer: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Syntrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/syntrophy.yaml`.

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
**Generated:** 2026-06-18T06:18:05.594732

1. su2023areviewon pages 3-4
2. kong2023enhancedanaerobicdigestion pages 1-2
3. singh2023syntrophicentanglementsfor pages 8-9
4. murali2023physiologicalpotentialand pages 12-13
5. zhuang2024electrontransferin pages 3-5
6. weng2024catabolismandinteractions pages 1-2
7. pinela2024impactofadditives pages 1-2
8. shi2024syntrophicmicrobesinvolved pages 13-14
9. nobu2020catabolismandinteractions pages 10-11
10. nobu2020catabolismandinteractions pages 8-10
11. westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15
12. nozhevnikova2020syntrophyandinterspecies pages 9-11
13. su2023areviewon pages 13-15
14. pinela2024impactofadditives pages 17-18
15. unmapped ENVO candidate
16. GO:0015948 candidate
17. unmapped
18. unmapped higher-level process
19. label node
20. unmapped family
21. CHEBI candidate/unmapped
22. CHEBI:16134
23. GO:0099536 candidate
24. GO:0019419 candidate
25. https://doi.org/10.3390/fermentation9050467
26. https://doi.org/10.3390/fermentation9100884
27. https://doi.org/10.1038/s41396-023-01504-y
28. https://doi.org/10.1371/journal.pbio.3002292
29. https://doi.org/10.3389/fmicb.2024.1389257
30. https://doi.org/10.1007/s00253-024-13263-7
31. https://doi.org/10.1128/aem.02047-23
32. https://doi.org/10.3390/life14050591
33. https://doi.org/10.1093/femsre/fuab057
34. https://doi.org/10.1186/s40168-020-00885-y
35. https://doi.org/10.1134/S0026261720020101
36. https://doi.org/10.3390/fermentation9050467,
37. https://doi.org/10.3390/fermentation9100884,
38. https://doi.org/10.1134/s0026261720020101,
39. https://doi.org/10.1093/femsre/fuab057,
40. https://doi.org/10.1186/s40168-020-00885-y,
41. https://doi.org/10.3390/life14050591,
42. https://doi.org/10.1038/s41396-023-01504-y,
43. https://doi.org/10.1371/journal.pbio.3002292,
44. https://doi.org/10.1007/s00253-024-13263-7,
45. https://doi.org/10.3389/fmicb.2024.1389257,
46. https://doi.org/10.1128/aem.02047-23,