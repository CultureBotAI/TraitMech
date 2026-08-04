# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gram variable
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000700
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria from the same culture show both gram-positive and gram-negative staining characteristics, often due to age of culture or cell wall degradation.
- **Parent traits:** METPO:1000697
- **Synonyms:** variable
- **Existing evidence:** DOI:10.1128/CMR.00043-07: cell wall structure (Bacterial cell-wall review supports peptidoglycan thinning and autolysis-mediated loss of crystal-violet retention as the basis for gram-variable staining.)
- **Existing causal graph summary:** gram_variable_wall_thinning: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **gram variable** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_variable.yaml`.

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
**Generated:** 2026-08-04T08:49:20.911981

1. beveridge1990mechanismofgram pages 1-2
2. beveridge1990mechanismofgram pages 11-12
3. beveridge2001useofthe pages 5-7
4. beveridge1990mechanismofgram pages 3-4
5. beveridge1990mechanismofgram pages 5-11
6. torrens2024mechanismsconferringbacterial pages 7-8
7. torrens2024mechanismsconferringbacterial pages 3-4
8. torrens2024mechanismsconferringbacterial pages 3-3
9. beveridge1990mechanismofgram pages 4-5
10. 10.1128/jb.172.3.1609-1620.1990
11. 10.1080/bih.76.3.111.118
12. 10.1042/BST20230027
13. 10.1128/JB.172.3.1609-1620.1990
14. https://doi.org/10.1128/jb.172.3.1609-1620.1990
15. https://doi.org/10.1080/bih.76.3.111.118
16. https://doi.org/10.1042/BST20230027
17. https://doi.org/10.1128/JB.172.3.1609-1620.1990
18. https://doi.org/10.1128/jb.172.3.1609-1620.1990,
19. https://doi.org/10.1080/bih.76.3.111.118,
20. https://doi.org/10.1042/bst20230027,