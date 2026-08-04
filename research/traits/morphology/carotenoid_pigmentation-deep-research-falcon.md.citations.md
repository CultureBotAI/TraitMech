# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carotenoid pigmentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003031
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype caused by microbial production and accumulation of carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_carotenoid
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)
- **Existing causal graph summary:** carotenoid_pigmentation_crt_pathway: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **carotenoid pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carotenoid_pigmentation.yaml`.

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
**Generated:** 2026-08-04T07:37:53.071210

1. sandmann2023genesandpathway pages 5-6
2. janisch2023geneticunderpinningsof pages 8-10
3. janisch2023geneticunderpinningsof pages 14-15
4. janisch2023geneticunderpinningsof pages 17-19
5. zhan2024expandingthecrispr pages 10-12
6. mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2
7. elfeky2024exploringthelipids pages 1-2
8. yehia2022celastrolmitigatesstaphyloxanthin pages 1-2
9. wang2024insightsintothe pages 5-6
10. wang2024insightsintothe pages 12-12
11. sandmann2023genesandpathway pages 3-5
12. tobin2024omicsdrivenonboardingof pages 1-2
13. wang2024insightsintothe pages 8-9
14. saini2019microbialplatformsto pages 11-13
15. janisch2023geneticunderpinningsof pages 4-5
16. sandmann2023genesandpathway pages 8-10
17. zhan2024expandingthecrispr pages 2-3
18. yehia2022celastrolmitigatesstaphyloxanthin pages 4-5
19. 10.3390/pathogens12010086
20. 10.3390/biology12101346
21. 10.1128/spectrum.04361-22
22. 10.3390/microorganisms12040803
23. 10.3389/ffunb.2024.1378590
24. 10.1186/s12866-024-03585-x
25. 10.1007/s00253-024-13379-w
26. 10.3389/fmicb.2024.1447785
27. 10.1186/s12866-022-02515-z
28. 10.1007/s10295-018-2104-7
29. https://doi.org/10.3390/pathogens12010086
30. https://doi.org/10.3390/biology12101346
31. https://doi.org/10.1128/spectrum.04361-22
32. https://doi.org/10.3390/microorganisms12040803
33. https://doi.org/10.3389/ffunb.2024.1378590
34. https://doi.org/10.1186/s12866-024-03585-x
35. https://doi.org/10.1007/s00253-024-13379-w
36. https://doi.org/10.3389/fmicb.2024.1447785
37. https://doi.org/10.1186/s12866-022-02515-z
38. https://doi.org/10.1007/s10295-018-2104-7
39. https://doi.org/10.3390/pathogens12010086,
40. https://doi.org/10.3390/biology12101346,
41. https://doi.org/10.1128/spectrum.04361-22,
42. https://doi.org/10.3390/microorganisms12040803,
43. https://doi.org/10.1186/s12866-022-02515-z,
44. https://doi.org/10.3389/ffunb.2024.1378590,
45. https://doi.org/10.1186/s12866-024-03585-x,
46. https://doi.org/10.3389/fmicb.2024.1447785,
47. https://doi.org/10.1007/s00253-024-13379-w,
48. https://doi.org/10.1007/s10295-018-2104-7,