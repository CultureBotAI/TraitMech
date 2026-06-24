# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** opportunistic pathogen
- **METPO identifier:** traitmech:000046
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A host-association lifestyle in which a normally commensal or environmental microorganism causes disease only when host defenses are compromised or it reaches a normally sterile site.
- **Parent traits:** METPO:1004000
- **Synonyms:** opportunistic infection
- **Existing evidence:** DOI:10.1016/j.tim.2012.04.005:  (Brown, Cornforth & Mideo, "Evolution of virulence in opportunistic pathogens", support context-dependent virulence maintained by advantages outside the host.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. support facultative shifts toward parasitism/pathogenicity along the parasite-mutualist continuum, the basis of opportunistic disease.)
- **Existing causal graph summary:** opportunistic_pathogen_context_dependent_virulence: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **opportunistic pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/opportunistic_pathogen.yaml`.

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
**Generated:** 2026-06-17T20:48:45.039455

1. uberoi2024thewoundmicrobiota pages 1-2
2. froismartins2024candidaalbicansvirulence pages 1-2
3. sebastian2024leafmicrobiomedysbiosis pages 3-4
4. jacobsen2023theroleof pages 1-2
5. sebastian2024leafmicrobiomedysbiosis pages 2-3
6. jensen2024controllingcandida pages 1-2
7. sangiorgio2024theimpactof pages 9-10
8. alsoubhi2024theecologyof pages 4-6
9. sebastian2024leafmicrobiomedysbiosis pages 11-12
10. sangiorgio2024theimpactof pages 1-2
11. sebastian2024leafmicrobiomedysbiosis pages 1-2
12. are
13. es
14. https://doi.org/10.3390/pathogens13050409
15. https://doi.org/10.1038/s41579-024-01035-z
16. https://doi.org/10.1007/s40588-023-00190-w
17. https://doi.org/10.1007/s40588-024-00235-8
18. https://doi.org/10.1128/iai.00516-23
19. https://doi.org/10.1111/1751-7915.14241
20. https://doi.org/10.1038/s41564-023-01555-z
21. https://doi.org/10.1038/s41579-024-01035-z,
22. https://doi.org/10.1007/s40588-023-00190-w,
23. https://doi.org/10.1007/s40588-024-00235-8,
24. https://doi.org/10.3390/pathogens13050409,
25. https://doi.org/10.1038/s41564-023-01555-z,
26. https://doi.org/10.1111/1751-7915.14241,
27. https://doi.org/10.1128/iai.00516-23,