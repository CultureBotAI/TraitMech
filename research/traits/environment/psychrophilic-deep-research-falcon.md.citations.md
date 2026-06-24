# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrophilic
- **METPO identifier:** METPO:1000614
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at low temperatures, typically near or below ~15 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Supports psychrophilic growth at low temperatures.) | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)
- **Existing causal graph summary:** psychrophilic_cold_adaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrophilic.yaml`.

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
**Generated:** 2026-06-18T01:28:41.324926

1. moyer2017psychrophilesandpsychrotrophs pages 1-2
2. cavicchioli2016ontheconcept pages 1-2
3. dopson2023eurypsychrophilicacidophilesfrom pages 11-12
4. bao2023miningofkey pages 7-9
5. li2024mechanismsunderlyingthe pages 9-10
6. purwar2024adaptationsofpsychrophilic pages 10-11
7. damico2006psychrophilicmicroorganismschallenges pages 2-3
8. maayer2014somelikeit pages 5-6
9. yang2023coldadaptedproteasesan pages 12-14
10. maayer2014somelikeit pages 1-2
11. yang2023coldadaptedproteasesan pages 1-2
12. https://doi.org/10.1038/sj.embor.7400662,
13. https://doi.org/10.3389/fmicb.2023.1215837,
14. https://doi.org/10.1002/embr.201338170,
15. https://doi.org/10.3389/fmicb.2024.1465627,
16. https://doi.org/10.37256/amtt.5220244537,
17. https://doi.org/10.3389/fmicb.2023.1149903,
18. https://doi.org/10.3389/fmicb.2024.1465627
19. https://doi.org/10.1111/1751-7915.14467
20. https://doi.org/10.37256/amtt.5220244537
21. https://doi.org/10.3389/fmicb.2023.1215837
22. https://doi.org/10.3390/ijms24108532
23. https://doi.org/10.3389/fmicb.2023.1149903
24. https://doi.org/10.1002/embr.201338170
25. https://doi.org/10.1038/ismej.2015.160
26. https://doi.org/10.1038/sj.embor.7400662
27. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
28. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
29. https://doi.org/10.1038/ismej.2015.160,
30. https://doi.org/10.1111/1751-7915.14467,
31. https://doi.org/10.3390/ijms24108532,