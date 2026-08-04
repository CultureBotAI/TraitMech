# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000483
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 1–5 °C, characteristic of stenothermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_1_5
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very narrow thermal-tolerance breadths as the stenothermal phenotype with limited membrane-remodeling flexibility.)
- **Existing causal graph summary:** temperature_delta_very_low_stenothermal: 9 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_very_low.yaml`.

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
**Generated:** 2026-08-04T03:47:13.166075

1. he2023highspeciationrate pages 1-2
2. herren2022decreasedthermalniche pages 8-9
3. white2019thecompletegenome pages 9-10
4. zhu2024shapingofmicrobial pages 1-2
5. zerouki2023wholegenomesequenceand pages 1-2
6. collins2019psychrophiliclifestylesmechanisms pages 5-8
7. herren2022decreasedthermalniche pages 3-4
8. herren2022decreasedthermalniche pages 4-5
9. lambros2021emergingadaptivestrategies pages 1-2
10. white2019thecompletegenome pages 1-2
11. he2023highspeciationrate pages 4-8
12. zerouki2023wholegenomesequenceand pages 6-7
13. collins2019psychrophiliclifestylesmechanisms pages 1-5
14. siliakus2017adaptationsofarchaeal pages 1-3
15. ernst2016homeoviscousadaptationand pages 1-2
16. anesi2016comparativeanalysisof pages 1-2
17. siliakus2017adaptationsofarchaeal pages 3-5
18. siliakus2017adaptationsofarchaeal pages 5-7
19. herren2022decreasedthermalniche pages 1-2
20. collins2019psychrophiliclifestylesmechanisms pages 8-10
21. the envelope
22. 10.1007/s00253-019-09659-5
23. 10.1007/s00792-017-0939-x
24. 10.1016/j.jmb.2016.08.013
25. 10.1038/s41396-022-01235-6
26. 10.3389/fmicb.2021.724982
27. 10.1038/s41396-023-01447-4
28. 10.3389/fmicb.2018.03189
29. 10.1007/s00438-023-02073-7
30. uncertain
31. 10.1038/s41467-024-48591-9
32. 10.3389/fpls.2016.00524
33. https://doi.org/10.1007/s00253-019-09659-5
34. https://doi.org/10.1007/s00792-017-0939-x
35. https://doi.org/10.1016/j.jmb.2016.08.013
36. https://doi.org/10.1038/s41396-022-01235-6
37. https://doi.org/10.3389/fmicb.2021.724982
38. https://doi.org/10.1038/s41396-023-01447-4
39. https://doi.org/10.3389/fmicb.2018.03189
40. https://doi.org/10.1007/s00438-023-02073-7
41. https://doi.org/10.1038/s41467-024-48591-9
42. https://doi.org/10.3389/fpls.2016.00524
43. https://doi.org/10.1038/s41396-023-01447-4,
44. https://doi.org/10.1038/s41396-022-01235-6,
45. https://doi.org/10.3389/fmicb.2018.03189,
46. https://doi.org/10.1007/s00253-019-09659-5,
47. https://doi.org/10.1007/s00792-017-0939-x,
48. https://doi.org/10.1038/s41467-024-48591-9,
49. https://doi.org/10.1007/s00438-023-02073-7,
50. https://doi.org/10.1016/j.jmb.2016.08.013,
51. https://doi.org/10.3389/fmicb.2021.724982,
52. https://doi.org/10.3389/fpls.2016.00524,