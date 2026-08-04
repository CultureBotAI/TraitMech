# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000484
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 5–10 °C, characteristic of organisms with limited thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_5_10
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports limited thermal-adaptation flexibility as the basis of narrow thermal-tolerance breadths.)
- **Existing causal graph summary:** temperature_delta_low_limited_breadth: 8 nodes, 8 edges

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
**Generated:** 2026-08-04T03:41:07.383886

1. chandler2023theeffectof pages 31-35
2. sidarta2024lipidphaseseparation pages 1-2
3. liang2024interactionsbetweenchaperone pages 8-10
4. hurtadobautista2024thermalplasticityand pages 2-3
5. mendoza2014temperaturesensingby pages 2-4
6. sionek2024theimpactof pages 3-5
7. hurtadobautista2024thermalplasticityand pages 16-17
8. hurtadobautista2024thermalplasticityand pages 17-18
9. hurtadobautista2024thermalplasticityand pages 1-2
10. mansilla2004controlofmembrane pages 5-5
11. hunger2004geneticevidencefor pages 1-2
12. mendoza2014temperaturesensingby pages 5-6
13. liang2024interactionsbetweenchaperone pages 16-17
14. hurtadobautista2024thermalplasticityand pages 15-16
15. 10.3390/biology13121088
16. 10.1128/spectrum.03925-23
17. 10.7717/peerj.17197
18. 10.3390/fermentation10060298
19. 10.1038/s41467-024-53046-2
20. 10.25959/23236217
21. 10.1146/annurev-micro-091313-103612
22. 10.1128/JB.186.20.6681-6688.2004
23. 10.1016/S0378-1097(03)00852-8
24. 10.1002/mbo3.154
25. https://doi.org/10.3390/biology13121088
26. https://doi.org/10.1128/spectrum.03925-23
27. https://doi.org/10.7717/peerj.17197
28. https://doi.org/10.3390/fermentation10060298
29. https://doi.org/10.1038/s41467-024-53046-2
30. https://doi.org/10.25959/23236217
31. https://doi.org/10.1146/annurev-micro-091313-103612
32. https://doi.org/10.1128/JB.186.20.6681-6688.2004
33. https://doi.org/10.1016/S0378-1097(03
34. https://doi.org/10.1002/mbo3.154
35. https://doi.org/10.25959/23236217,
36. https://doi.org/10.1128/jb.186.20.6681-6688.2004,
37. https://doi.org/10.1128/spectrum.03925-23,
38. https://doi.org/10.1016/s0378-1097(03
39. https://doi.org/10.1146/annurev-micro-091313-103612,
40. https://doi.org/10.3390/fermentation10060298,
41. https://doi.org/10.3390/biology13121088,
42. https://doi.org/10.7717/peerj.17197,