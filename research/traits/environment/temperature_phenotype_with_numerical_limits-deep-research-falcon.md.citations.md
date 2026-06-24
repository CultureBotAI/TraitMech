# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature phenotype with numerical limits
- **METPO identifier:** METPO:1000533
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific temperature values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports temperature as the quantitative axis defining psychrophile, mesophile, and thermophile classification.) | DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports the low end of the temperature axis as a distinct quantitative phenotype.)
- **Existing causal graph summary:** temperature_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_phenotype_with_numerical_limits.yaml`.

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
**Generated:** 2026-06-18T02:33:42.887550

1. purwar2024adaptationsofpsychrophilic pages 1-3
2. purwar2024adaptationsofpsychrophilic pages 8-10
3. jie2025thermaldiversityof pages 1-4
4. ramon2023ageneraloverview pages 1-2
5. moon2023temperaturemattersbacterial pages 7-9
6. maiti2024extrememakeoverthe pages 3-4
7. ramon2023ageneraloverview pages 2-4
8. moon2023temperaturemattersbacterial pages 1-3
9. purwar2024adaptationsofpsychrophilic pages 13-15
10. omac2025comparisonofsecondary pages 1-2
11. ramon2023ageneraloverview pages 4-5
12. purwar2024adaptationsofpsychrophilic pages 6-7
13. ramon2023ageneraloverview pages 21-22
14. ramon2023ageneraloverview pages 22-23
15. purwar2024adaptationsofpsychrophilic pages 3-4
16. ATP
17. ADP
18. https://doi.org/10.1007/s42770-023-01057-4
19. https://doi.org/10.1007/s12275-023-00031-x
20. https://doi.org/10.37256/amtt.5220244537
21. https://doi.org/10.1039/d4cc03114h
22. https://doi.org/10.24925/turjaf.v13is3.3927-3933.8140
23. https://doi.org/10.1007/s42770-023-01057-4,
24. https://doi.org/10.1007/s12275-023-00031-x,
25. https://doi.org/10.37256/amtt.5220244537,
26. https://doi.org/10.24925/turjaf.v13is3.3927-3933.8140,
27. https://doi.org/10.1039/d4cc03114h,