# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively acidophilic
- **METPO identifier:** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_acidophilic.yaml`.

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
**Generated:** 2026-06-17T22:12:40.772931

1. gonzalez2024acidophilicheterotrophsbasic pages 1-2
2. gonzalezrosales2022integrativegenomicssheds pages 1-2
3. vergara2020evolutionofpredicted pages 1-3
4. li2024responseofescherichia pages 1-2
5. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
6. qin2024characterizationofmild pages 1-2
7. vergara2020evolutionofpredicted pages 16-17
8. nie2024researchprogressin pages 11-12
9. yao2023howmethanotrophsrespond pages 5-7
10. dopson2023eurypsychrophilicacidophilesfrom pages 2-4
11. boase2022predictionandinferred pages 1-2
12. boase2022predictionandinferred pages 2-3
13. provided
14. https://doi.org/10.3389/fmicb.2021.822229;
15. https://doi.org/10.3389/fmicb.2023.1149903
16. https://doi.org/10.3389/fmicb.2023.1149903;
17. https://doi.org/10.3390/microorganisms12081565
18. https://doi.org/10.3389/fmicb.2019.02455
19. https://doi.org/10.1111/1758-2229.70019
20. https://doi.org/10.1128/AEM.00047-23;
21. https://doi.org/10.3389/fmicb.2022.848410
22. https://doi.org/10.3389/fmicb.2021.822229
23. https://doi.org/10.3390/genes11040389
24. https://doi.org/10.13343/j.cnki.wsxb.20230336;
25. https://doi.org/10.3389/fmicb.2022.1034164;
26. https://doi.org/10.3390/genes11040389;
27. https://doi.org/10.13343/j.cnki.wsxb.20230336
28. https://doi.org/10.3389/fmicb.2022.1034164
29. https://doi.org/10.3389/fmicb.2022.848410;
30. https://doi.org/10.3389/fmicb.2024.1374800
31. https://doi.org/10.3390/microorganisms12091774
32. https://doi.org/10.3389/fmicb.2024.1374800,
33. https://doi.org/10.3389/fmicb.2021.822229,
34. https://doi.org/10.3390/genes11040389,
35. https://doi.org/10.3390/microorganisms12091774,
36. https://doi.org/10.3389/fmicb.2023.1149903,
37. https://doi.org/10.13343/j.cnki.wsxb.20230336,
38. https://doi.org/10.3390/microorganisms12081565,
39. https://doi.org/10.1111/1758-2229.70019,
40. https://doi.org/10.3389/fmicb.2022.1034164,
41. https://doi.org/10.3389/fmicb.2022.848410,