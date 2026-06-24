# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** material entity
- **METPO identifier:** METPO:1000186
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An object or portion of a substance or mixture of substances that consists of matter
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.3233/AO-220262: BFO is a genuine top-level ontology (Supports material entity as a top-level ontology class rather than a concrete microbial trait.) | DOI:10.7551/mitpress/9780262527811.001.0001: specific top-level ontology, the Basic Formal Ontology (Supports BFO as the upper ontology context for material entity.)
- **Existing causal graph summary:** material_entity_bfo_upper_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **material entity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/material_entity.yaml`.

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
**Generated:** 2026-06-18T12:56:58.664563

1. beverley2024capabilities pages 3-6
2. jensen2024thecommoncore pages 1-3
3. jensen2024thecommoncore pages 3-6
4. smart2023secureontologiesfor pages 35-42
5. smart2023secureontologiesfor pages 29-35
6. santangelo2024integratingbiologicalknowledge pages 12-13
7. bernabe2023theuseof pages 4-6
8. bernabe2023theuseof pages 1-2
9. santangelo2024integratingbiologicalknowledge pages 9-10
10. santangelo2024integratingbiologicalknowledge pages 10-11
11. santangelo2024integratingbiologicalknowledge pages 3-5
12. karlsen2023fromgenotypeto pages 1-2
13. karlsen2023fromgenotypeto pages 2-3
14. karlsen2023fromgenotypeto pages 5-6
15. santangelo2024integratingbiologicalknowledge pages 1-2
16. bernabe2023theuseof pages 8-10
17. bernabe2023theuseof pages 10-11
18. karlsen2023fromgenotypeto pages 18-19
19. https://doi.org/10.48550/arxiv.2405.00183
20. https://doi.org/10.48550/arxiv.2404.17758
21. https://doi.org/10.1093/femsre/fuad030
22. https://doi.org/10.3389/fmicb.2024.1351678
23. https://doi.org/10.1186/s13326-023-00300-z
24. https://doi.org/10.48550/arxiv.2405.00183,
25. https://doi.org/10.48550/arxiv.2404.17758,
26. https://doi.org/10.3389/fmicb.2024.1351678,
27. https://doi.org/10.1186/s13326-023-00300-z,
28. https://doi.org/10.1093/femsre/fuad030,