# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta low
- **METPO identifier:** METPO:1000484
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 5–10 °C, characteristic of organisms with limited thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_5_10
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports limited thermal-adaptation flexibility as the basis of narrow thermal-tolerance breadths.)
- **Existing causal graph summary:** temperature_delta_low_limited_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_low.yaml`.

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
**Generated:** 2026-06-18T02:00:14.826543

1. ramon2023ageneraloverview pages 1-2
2. mendoza2014temperaturesensingby pages 5-6
3. sidarta2024lipidphaseseparation pages 1-2
4. barbotin2024quantificationofmembrane pages 1-3
5. barbotin2024quantificationofmembrane pages 10-11
6. ramon2023ageneraloverview pages 4-5
7. ianutsevich2024membranelipidsand pages 1-2
8. ianutsevich2024membranelipidsand pages 8-9
9. safronova2023fromhotto pages 10-12
10. rasanen2024adaptationtofluctuating pages 14-17
11. safronova2023fromhotto pages 8-10
12. mendoza2014temperaturesensingby pages 1-2
13. portner2007thermallimitsand pages 2-3
14. ianutsevich2024membranelipidsand pages 9-11
15. ramon2023ageneraloverview pages 2-4
16. ianutsevich2024membranelipidsand pages 2-4
17. wu2023molecularmechanismsof pages 16-17
18. mendoza2014temperaturesensingby pages 4-5
19. barbotin2024quantificationofmembrane pages 11-14
20. safronova2023fromhotto pages 35-35
21. s
22. https://doi.org/10.1007/s42770-023-01057-4;
23. https://doi.org/10.1146/annurev-micro-091313-103612;
24. https://doi.org/10.1128/spectrum.03925-23;
25. https://doi.org/10.1101/2023.10.13.562271;
26. https://doi.org/10.3390/ijms25063380;
27. https://doi.org/10.1101/2023.11.10.566608;
28. https://doi.org/10.1128/spectrum.03925-23
29. https://doi.org/10.1146/annurev-micro-091313-103612
30. https://doi.org/10.1007/s42770-023-01057-4
31. https://doi.org/10.1101/2023.10.13.562271
32. https://doi.org/10.3390/ijms25063380
33. https://doi.org/10.1101/2023.11.10.566608
34. https://doi.org/10.32942/x2hp6f
35. https://doi.org/10.1098/rstb.2006.1947
36. https://doi.org/10.1007/s001140100216
37. https://doi.org/10.1007/s42770-023-01057-4,
38. https://doi.org/10.1128/spectrum.03925-23,
39. https://doi.org/10.1146/annurev-micro-091313-103612,
40. https://doi.org/10.1101/2023.10.13.562271,
41. https://doi.org/10.3390/ijms25063380,
42. https://doi.org/10.1101/2023.11.10.566608,
43. https://doi.org/10.1098/rstb.2006.1947,
44. https://doi.org/10.1007/s001140100216,