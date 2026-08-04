# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** material entity
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000186
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
**Generated:** 2026-08-04T12:18:49.003162

1. rabenberg2024groundingrealizableentities pages 1-3
2. rabenberg2024groundingrealizableentities pages 8-11
3. rabenberg2024groundingrealizableentities pages 3-6
4. santangelo2024integratingbiologicalknowledge pages 3-5
5. santangelo2024integratingbiologicalknowledge pages 12-13
6. callahan2024anopensource pages 2-4
7. zhang2024knowledgegraphderivedfeed pages 3-4
8. rabenberg2024groundingrealizableentities pages 11-13
9. santangelo2024integratingbiologicalknowledge pages 1-2
10. callahan2024anopensource pages 1-2
11. zhang2024knowledgegraphderivedfeed pages 1-3
12. santangelo2024integratingbiologicalknowledge pages 13-14
13. santangelo2024integratingbiologicalknowledge pages 2-3
14. callahan2024anopensource pages 17-18
15. 10.3233/AO-220262
16. 10.7551/mitpress/9780262527811.001.0001
17. 10.48550/arXiv.2405.00197
18. 10.3389/fmicb.2024.1351678
19. 10.1038/s41597-024-03171-w
20. 10.1038/s41598-024-64835-6
21. 10.1093/database/baab069
22. 10.1093/nar/gkab1016
23. https://doi.org/10.3233/AO-220262
24. https://doi.org/10.7551/mitpress/9780262527811.001.0001
25. https://doi.org/10.48550/arXiv.2405.00197
26. https://doi.org/10.3389/fmicb.2024.1351678
27. https://doi.org/10.1038/s41597-024-03171-w
28. https://doi.org/10.1038/s41598-024-64835-6
29. https://doi.org/10.1093/database/baab069
30. https://doi.org/10.1093/nar/gkab1016
31. https://doi.org/10.48550/arxiv.2405.00197,
32. https://doi.org/10.3389/fmicb.2024.1351678,
33. https://doi.org/10.1038/s41597-024-03171-w,
34. https://doi.org/10.1038/s41598-024-64835-6,