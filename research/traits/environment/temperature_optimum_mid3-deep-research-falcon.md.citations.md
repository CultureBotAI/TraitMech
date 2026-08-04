# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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
**Generated:** 2026-08-04T04:04:27.208707

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. yang2023insightintothe pages 1-2
3. mendoza2014temperaturesensingby pages 5-6
4. knapp2025metabolicrearrangementenables pages 23-24
5. knapp2025metabolicrearrangementenables pages 4-5
6. hurtadobautista2024thermalplasticityand pages 1-2
7. hurtadobautista2024thermalplasticityand pages 16-17
8. wu2024effectoftemperature pages 1-2
9. hua2024regulatorymechanismsof pages 1-3
10. lehmann2023adaptivelaboratoryevolution pages 6-7
11. price2004temperaturedependenceof pages 1-1
12. knapp2025metabolicrearrangementenables pages 1-2
13. knapp2025metabolicrearrangementenables pages 3-4
14. 10.1146/annurev-micro-091313-103612
15. 10.1038/s41564-024-01841-4
16. 10.3390/biology13121088
17. 10.3389/fmicb.2023.1265216
18. 10.1128/AEM.01928-22
19. 10.3390/agronomy14122991
20. 10.1186/s12934-024-02602-y
21. 10.1073/pnas.0400522101
22. https://doi.org/10.1146/annurev-micro-091313-103612
23. https://doi.org/10.1038/s41564-024-01841-4
24. https://doi.org/10.3390/biology13121088
25. https://doi.org/10.3389/fmicb.2023.1265216
26. https://doi.org/10.1128/AEM.01928-22
27. https://doi.org/10.3390/agronomy14122991
28. https://doi.org/10.1186/s12934-024-02602-y
29. https://doi.org/10.1073/pnas.0400522101
30. https://doi.org/10.3389/fmicb.2023.1265216,
31. https://doi.org/10.3390/biology13121088,
32. https://doi.org/10.1128/aem.01928-22,
33. https://doi.org/10.1146/annurev-micro-091313-103612,
34. https://doi.org/10.1038/s41564-024-01841-4,
35. https://doi.org/10.3390/agronomy14122991,
36. https://doi.org/10.1186/s12934-024-02602-y,
37. https://doi.org/10.1073/pnas.0400522101,