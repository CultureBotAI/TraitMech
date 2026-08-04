# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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
**Generated:** 2026-08-04T03:47:29.002791

1. mendoza2014temperaturesensingby pages 1-2
2. mendoza2014temperaturesensingby pages 5-6
3. riccardi2023metabolicrobustnessto pages 1-2
4. riccardi2023metabolicrobustnessto pages 10-12
5. hurtadobautista2024thermalplasticityand pages 16-17
6. rodrigues2008architectureofthermal pages 1-2
7. hurtadobautista2024thermalplasticityand pages 1-2
8. liang2023developmentofheatshock pages 1-2
9. herren2022decreasedthermalniche pages 3-4
10. herren2022decreasedthermalniche pages 1-1
11. liang2023developmentofheatshock pages 7-9
12. liang2023developmentofheatshock pages 14-16
13. herren2022decreasedthermalniche pages 4-5
14. hurtadobautista2024thermalplasticityand pages 2-3
15. herren2022decreasedthermalniche pages 3-3
16. herren2022decreasedthermalniche pages 7-8
17. herren2022decreasedthermalniche pages 1-2
18. rodrigues2008architectureofthermal pages 6-8
19. 10.3390/biology13121088
20. 10.1128/msystems.01124-22
21. 10.1128/aem.00666-23
22. 10.1038/s41396-022-01235-6
23. 10.1146/annurev-micro-091313-103612
24. 10.1128/JB.01377-08
25. 10.1186/1471-2164-9-547
26. https://doi.org/10.3390/biology13121088
27. https://doi.org/10.1128/msystems.01124-22
28. https://doi.org/10.1128/aem.00666-23
29. https://doi.org/10.1038/s41396-022-01235-6
30. https://doi.org/10.1146/annurev-micro-091313-103612
31. https://doi.org/10.1128/JB.01377-08
32. https://doi.org/10.1186/1471-2164-9-547
33. https://doi.org/10.1128/jb.01377-08,
34. https://doi.org/10.1186/1471-2164-9-547,
35. https://doi.org/10.1146/annurev-micro-091313-103612,
36. https://doi.org/10.1128/msystems.01124-22,
37. https://doi.org/10.3390/biology13121088,
38. https://doi.org/10.1038/s41396-022-01235-6,
39. https://doi.org/10.1128/aem.00666-23,