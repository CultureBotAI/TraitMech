# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 15 nodes, 14 edges

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
**Generated:** 2026-08-04T00:41:46.355472

1. yao2023howmethanotrophsrespond pages 4-5
2. ji2021candidatuseremiobacterotaa pages 7-9
3. gonzalezrosales2022integrativegenomicssheds pages 1-2
4. ji2021candidatuseremiobacterotaa pages 10-12
5. carere2021growthonformic pages 4-5
6. gonzalezrosales2022integrativegenomicssheds pages 9-12
7. carere2021growthonformic pages 1-2
8. boase2022predictionandinferred pages 1-2
9. gonzalez2024acidophilicheterotrophsbasic pages 1-2
10. gonzalez2024acidophilicheterotrophsbasic pages 3-4
11. dopson2023eurypsychrophilicacidophilesfrom pages 2-4
12. dopson2023eurypsychrophilicacidophilesfrom pages 1-2
13. gonzalez2024acidophilicheterotrophsbasic pages 2-3
14. gonzalez2024acidophilicheterotrophsbasic pages 6-7
15. 10.3389/fmicb.2024.1374800
16. 10.1103/PRXLife.2.043015
17. 10.3389/fmicb.2023.1149903
18. 10.3389/fmicb.2022.1034164
19. 10.3389/fmicb.2021.822229
20. 10.3389/fmicb.2022.848410
21. 10.1038/s41396-021-00944-8
22. 10.3389/fmicb.2021.651744
23. 10.1099/ijs.0.066175-0
24. https://doi.org/10.3389/fmicb.2024.1374800
25. https://doi.org/10.1103/PRXLife.2.043015
26. https://doi.org/10.3389/fmicb.2023.1149903
27. https://doi.org/10.3389/fmicb.2022.1034164
28. https://doi.org/10.3389/fmicb.2021.822229
29. https://doi.org/10.3389/fmicb.2022.848410
30. https://doi.org/10.1038/s41396-021-00944-8
31. https://doi.org/10.3389/fmicb.2021.651744
32. https://doi.org/10.1099/ijs.0.066175-0
33. https://doi.org/10.3389/fmicb.2024.1374800,
34. https://doi.org/10.3389/fmicb.2023.1149903,
35. https://doi.org/10.3389/fmicb.2022.1034164,
36. https://doi.org/10.1038/s41396-021-00944-8,
37. https://doi.org/10.3389/fmicb.2021.822229,
38. https://doi.org/10.3389/fmicb.2021.651744,
39. https://doi.org/10.3389/fmicb.2022.848410,