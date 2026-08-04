# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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
**Generated:** 2026-08-04T02:10:00.441464

1. dopson2023eurypsychrophilicacidophilesfrom pages 2-4
2. gonzalezrosales2022integrativegenomicssheds pages 1-2
3. yao2023howmethanotrophsrespond pages 5-7
4. vergara2020evolutionofpredicted pages 1-3
5. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
6. zhang2024accumulatedcoppertailing pages 5-8
7. tonietti2024unveilingthebioleaching pages 1-2
8. cozma2024biorecoveryofmetals pages 10-11
9. gonzalez2024acidophilicheterotrophsbasic pages 3-4
10. vergara2020evolutionofpredicted pages 16-17
11. carere2021growthonformic pages 3-4
12. carere2021growthonformic pages 4-5
13. carere2021growthonformic pages 9-10
14. carere2021growthonformic pages 1-2
15. carere2021growthonformic pages 5-7
16. carere2021growthonformic pages 2-3
17. zhang2024accumulatedcoppertailing pages 1-2
18. gonzalez2024acidophilicheterotrophsbasic pages 2-3
19. https://doi.org/10.1111/1758-2229.70019
20. https://doi.org/10.3390/min14101051
21. https://doi.org/10.3390/microorganisms12122407
22. https://doi.org/10.3390/pr12091793
23. https://doi.org/10.3389/fmicb.2024.1374800
24. https://doi.org/10.3389/fmicb.2023.1149903
25. https://doi.org/10.3389/fmicb.2022.1034164
26. https://doi.org/10.3389/fmicb.2021.822229
27. https://doi.org/10.3389/fmicb.2021.651744
28. https://doi.org/10.3390/genes11040389
29. https://doi.org/10.3389/fmicb.2023.1149903,
30. https://doi.org/10.3390/genes11040389,
31. https://doi.org/10.3389/fmicb.2021.822229,
32. https://doi.org/10.3389/fmicb.2021.651744,
33. https://doi.org/10.3389/fmicb.2022.1034164,
34. https://doi.org/10.1111/1758-2229.70019,
35. https://doi.org/10.3390/min14101051,
36. https://doi.org/10.3390/microorganisms12122407,
37. https://doi.org/10.3390/pr12091793,
38. https://doi.org/10.3389/fmicb.2024.1374800,