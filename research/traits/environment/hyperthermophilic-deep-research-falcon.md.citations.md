# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hyperthermophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000617
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at very high temperatures, typically ≥80 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme thermophilic
- **Existing evidence:** DOI:10.1111/j.1574-6976.1996.tb00233.x: optimal growth temperatures between 80°C and 110°C (Supports hyperthermophile growth at very high temperatures.) | PMID:9348040: hyperthermophilic archaeon, Pyrococcus furiosus (Organism example: Pyrococcus furiosus is described as hyperthermophilic.)
- **Existing causal graph summary:** hyperthermophilic_thermostability: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/hyperthermophilic.yaml`.

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
**Generated:** 2026-08-04T01:07:17.619797

1. furr2024structuralstabilitycomparisons pages 1-2
2. takemata2024howdothermophiles pages 4-5
3. pollo2015insightsintothermoadaptation pages 14-17
4. grunberger2023uncoveringthetemporal pages 1-2
5. grunberger2023uncoveringthetemporal pages 23-24
6. okabe2025proteomelevelrobustnessand pages 8-12
7. https://doi.org/10.1128/mbio.02174-23.
8. https://doi.org/10.3390/microorganisms12112348.
9. https://doi.org/10.1264/jsme2.me23087.
10. https://doi.org/10.1128/mbio.02174-23
11. https://doi.org/10.3390/microorganisms12112348
12. https://doi.org/10.1264/jsme2.me23087
13. https://doi.org/10.1139/cjm-2015-0073
14. https://doi.org/10.1007/s00792-023-01321-3.
15. https://doi.org/10.33640/2405-609X.3367.
16. https://doi.org/10.1139/cjm-2015-0073.
17. https://doi.org/10.1039/D4CC03114H.
18. https://doi.org/10.1128/AEM.69.4.2365-2371.2003.
19. https://doi.org/10.1042/ETLS20180024.
20. https://doi.org/10.1038/srep29483.
21. https://doi.org/10.1128/MMBR.65.1.1-43.2001.
22. https://doi.org/10.1101/2025.05.02.651969.
23. https://doi.org/10.1128/mbio.02174-23,
24. https://doi.org/10.1264/jsme2.me23087,
25. https://doi.org/10.1139/cjm-2015-0073,
26. https://doi.org/10.3390/microorganisms12112348,
27. https://doi.org/10.1101/2025.05.02.651969,