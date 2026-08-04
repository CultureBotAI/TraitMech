# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** orange pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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
**Generated:** 2026-08-04T09:24:01.868469

1. mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7
2. barreto2023biotechnologicalapplicationsof pages 7-9
3. barreto2023microbialpigmentsmajor pages 4-6
4. raman2024nostoxanthinbiosynthesisby pages 2-4
5. janisch2023geneticunderpinningsof pages 10-12
6. janisch2023geneticunderpinningsof pages 17-19
7. mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8
8. mosquedamartinez2024inrhodotorulamucilaginosa pages 4-6
9. wang2024insightsintothe pages 8-9
10. wang2024insightsintothe pages 5-6
11. wang2024insightsintothe pages 6-8
12. raman2024nostoxanthinbiosynthesisby pages 1-2
13. janisch2023geneticunderpinningsof pages 2-4
14. raman2024nostoxanthinbiosynthesisby pages 5-8
15. mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9
16. janisch2023geneticunderpinningsof pages 19-20
17. singh2015characterizationofmycobacterium pages 1-2
18. wang2024insightsintothe pages 12-12
19. janisch2023geneticunderpinningsof pages 1-2
20. janisch2023geneticunderpinningsof pages 4-5
21. raman2024nostoxanthinbiosynthesisby pages 8-10
22. janisch2023geneticunderpinningsof pages 5-8
23. mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2
24. yang2021crucialrolesof pages 1-4
25. mosquedamartinez2024inrhodotorulamucilaginosa pages 9-10
26. 10.3390/pathogens12010086
27. 10.3389/ffunb.2024.1378590
28. 10.1007/s00284-024-03956-7
29. 10.3389/fmicb.2024.1447785
30. 10.3390/microorganisms11122920
31. 10.3390/biology12101346
32. 10.1002/mbo3.288
33. 10.1007/s00203-007-0262-5
34. 10.1007/s00253-015-6910-9
35. https://doi.org/10.3390/pathogens12010086
36. https://doi.org/10.3389/ffunb.2024.1378590
37. https://doi.org/10.1007/s00284-024-03956-7
38. https://doi.org/10.3389/fmicb.2024.1447785
39. https://doi.org/10.3390/microorganisms11122920
40. https://doi.org/10.3390/biology12101346
41. https://doi.org/10.1002/mbo3.288
42. https://doi.org/10.1007/s00203-007-0262-5
43. https://doi.org/10.1007/s00253-015-6910-9
44. https://doi.org/10.20944/preprints202310.0121.v1,
45. https://doi.org/10.3390/microorganisms11122920,
46. https://doi.org/10.3389/ffunb.2024.1378590,
47. https://doi.org/10.1007/s00284-024-03956-7,
48. https://doi.org/10.3390/pathogens12010086,
49. https://doi.org/10.3389/fmicb.2024.1447785,
50. https://doi.org/10.1101/2021.05.26.445811,
51. https://doi.org/10.1002/mbo3.288,