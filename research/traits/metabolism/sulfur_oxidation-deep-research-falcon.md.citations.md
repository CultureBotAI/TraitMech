# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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
**Generated:** 2026-08-04T07:09:17.686705

1. zhou2025diversityandecology pages 7-9
2. zhou2025diversityandecology pages 3-5
3. li2024yeeelikebacterialsoxt pages 8-9
4. li2024yeeelikebacterialsoxt pages 7-8
5. zhang2023microbedrivenelementalcycling pages 10-12
6. zhou2025diversityandecology pages 32-34
7. 10.1038/s41579-024-01104-3
8. 10.3390/microorganisms11061436
9. a
10. es
11. is a
12. 10.1038/s42003-024-07270-7
13. 10.1186/s40168-023-01601-2
14. 10.1111/j.1574-6976.2009.00187.x
15. 10.1128/AEM.67.7.2873-2882.2001
16. https://doi.org/10.1038/s41579-024-01104-3
17. https://doi.org/10.3390/microorganisms11061436
18. https://doi.org/10.1038/s42003-024-07270-7
19. https://doi.org/10.1186/s40168-023-01601-2
20. https://doi.org/10.1111/j.1574-6976.2009.00187.x
21. https://doi.org/10.1128/AEM.67.7.2873-2882.2001
22. https://doi.org/10.3390/microorganisms11061436,
23. https://doi.org/10.1038/s41579-024-01104-3,
24. https://doi.org/10.1186/s40168-023-01601-2,
25. https://doi.org/10.1038/s42003-024-07270-7,