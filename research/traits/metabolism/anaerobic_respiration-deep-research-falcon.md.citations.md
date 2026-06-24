# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Anaerobic respiration
- **METPO identifier:** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Anaerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_respiration.yaml`.

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
**Generated:** 2026-06-18T04:20:41.162207

1. sennett2024determininghowoxygen pages 1-2
2. schacksen2024unravelingthegenetic pages 9-11
3. tsypin2024geneticallydissectingthe pages 26-31
4. roothans2024aerobicdenitrificationas pages 8-9
5. kim2024anaerobicrespirationof pages 8-10
6. kim2024anaerobicrespirationof pages 11-13
7. kim2024anaerobicrespirationof pages 6-8
8. kim2024anaerobicrespirationof pages 5-6
9. egas2024anovelmechanism pages 2-5
10. egas2024anovelmechanism pages 9-10
11. tsypin2024geneticallydissectingthe pages 31-36
12. tsypin2024geneticallydissectingthe pages 21-26
13. schacksen2024unravelingthegenetic pages 1-2
14. schacksen2024unravelingthegenetic pages 11-13
15. sennett2024determininghowoxygen pages 2-3
16. schacksen2024unravelingthegenetic pages 7-9
17. egas2024anovelmechanism pages 10-13
18. kim2024anaerobicrespirationof pages 10-11
19. tsypin2024geneticallydissectingthe pages 1-6
20. tsypin2024geneticallydissectingthe pages 6-9
21. tsypin2024geneticallydissectingthe pages 36-40
22. kim2024anaerobicrespirationof pages 31-36
23. kim2024anaerobicrespirationof pages 15-16
24. tsypin2024geneticallydissectingthe pages 9-16
25. sennett2024determininghowoxygen pages 9-10
26. roothans2024aerobicdenitrificationas pages 12-13
27. sennett2024determininghowoxygen pages 8-9
28. schacksen2024unravelingthegenetic pages 13-15
29. schacksen2024unravelingthegenetic pages 4-7
30. candidate ENVO
31. gene symbols
32. label
33. CHEBI candidate, label-only if unresolved
34. was
35. https://doi.org/10.1038/s41467-024-51688-w
36. https://doi.org/10.1093/ismejo/wrae116
37. https://doi.org/10.1016/j.chom.2024.01.004
38. https://doi.org/10.1128/msystems.00967-23
39. https://doi.org/10.1101/2023.11.14.567096
40. https://doi.org/10.1128/aem.02177-23
41. https://doi.org/10.1093/ismejo/wrae116,
42. https://doi.org/10.1038/s41467-024-51688-w,
43. https://doi.org/10.1128/msystems.00967-23,
44. https://doi.org/10.1016/j.chom.2024.01.004,
45. https://doi.org/10.1101/2023.11.14.567096,
46. https://doi.org/10.1128/aem.02177-23,