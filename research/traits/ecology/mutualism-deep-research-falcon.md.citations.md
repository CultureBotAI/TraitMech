# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mutualism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000041
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which both the microorganism and its host or partner benefit from the association, often through exchange of nutrients or services.
- **Parent traits:** traitmech:000040
- **Synonyms:** mutualist
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document widespread mutually beneficial host-microbe associations across animals.) | DOI:10.1126/science.1104816:  (Bäckhed et al., "Host-bacterial mutualism in the human intestine", supports reciprocal benefit (nutrient harvest for the host, habitat for the microbes) as the defining feature of mutualism.)
- **Existing causal graph summary:** mutualism_reciprocal_benefit: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **mutualism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/mutualism.yaml`.

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
**Generated:** 2026-08-04T14:53:53.058220

1. cheng2020ecologicalimportanceof pages 13-15
2. lasarre2020covertcrossfeedingrevealed pages 1-2
3. henriques2020metaboliccrossfeedingin pages 1-2
4. duan2024crosskingdomnutrientexchange pages 3-4
5. pena2024mycorrhizalsymbiosisand pages 1-3
6. culp2023crossfeedinginthe pages 15-17
7. culp2023crossfeedinginthe pages 2-4
8. escriva2022distinctnand pages 1-2
9. escriva2022distinctnand pages 5-6
10. giri2022prevalentemergenceof pages 1-2
11. mataigne2021microbialsystemsecology pages 4-6
12. culp2023crossfeedinginthe pages 1-2
13. culp2023crossfeedinginthe pages 23-26
14. giri2022prevalentemergenceof pages 2-3
15. 10.1128/msystems.01484-21
16. 10.1038/s43705-022-00155-y
17. 10.1016/j.chom.2023.03.016
18. 10.1007/s00253-024-13298-w
19. https://doi.org/10.1038/s41579-024-01073-7
20. https://doi.org/10.1007/s00253-024-13298-w
21. https://doi.org/10.1016/j.chom.2023.03.016
22. https://doi.org/10.1038/s43705-022-00155-y
23. https://doi.org/10.1128/msystems.01484-21
24. https://doi.org/10.1128/AEM.00190-20
25. https://doi.org/10.1038/s41467-020-18049-9
26. https://doi.org/10.1128/AEM.00543-20
27. https://doi.org/10.3389/fmicb.2021.780469
28. https://doi.org/10.1073/pnas.1218525110
29. https://doi.org/10.1126/science.1104816
30. https://doi.org/10.1038/s41579-024-01073-7](https://doi.org/10.1038/s41579-024-01073-7
31. https://doi.org/10.1007/s00253-024-13298-w](https://doi.org/10.1007/s00253-024-13298-w
32. https://doi.org/10.1016/j.chom.2023.03.016](https://doi.org/10.1016/j.chom.2023.03.016
33. https://doi.org/10.1038/s43705-022-00155-y](https://doi.org/10.1038/s43705-022-00155-y
34. https://doi.org/10.1128/msystems.01484-21](https://doi.org/10.1128/msystems.01484-21
35. https://doi.org/10.1128/AEM.00190-20](https://doi.org/10.1128/AEM.00190-20
36. https://doi.org/10.1038/s41467-020-18049-9](https://doi.org/10.1038/s41467-020-18049-9
37. https://doi.org/10.1128/AEM.00543-20](https://doi.org/10.1128/AEM.00543-20
38. https://doi.org/10.3389/fmicb.2021.780469](https://doi.org/10.3389/fmicb.2021.780469
39. https://doi.org/10.1073/pnas.1218525110](https://doi.org/10.1073/pnas.1218525110
40. https://doi.org/10.1126/science.1104816](https://doi.org/10.1126/science.1104816
41. https://doi.org/10.1016/j.chom.2023.03.016,
42. https://doi.org/10.1007/s00253-024-13298-w,
43. https://doi.org/10.1038/s43705-022-00155-y,
44. https://doi.org/10.1128/aem.00190-20,
45. https://doi.org/10.1128/aem.00543-20,
46. https://doi.org/10.1038/s41467-020-18049-9,
47. https://doi.org/10.1038/s41579-024-01073-7,
48. https://doi.org/10.1128/msystems.01484-21,
49. https://doi.org/10.3389/fmicb.2021.780469,