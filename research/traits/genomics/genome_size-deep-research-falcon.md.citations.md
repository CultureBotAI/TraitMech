# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genome size
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000098
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the total length of an organism's genome (typically expressed in megabase pairs), which varies widely across prokaryotes and reflects lifestyle and evolutionary forces.
- **Parent traits:** METPO:1000188
- **Synonyms:** genome length
- **Existing evidence:** DOI:10.1038/nrmicro3331:  (Batut et al. review reductive genome evolution, linking genome size to population size and lifestyle across prokaryotes.) | DOI:10.1038/ismej.2014.60:  (Giovannoni et al. discuss streamlining theory and the small genomes of abundant free-living microbes.)
- **Existing causal graph summary:** genome_size_population_lifestyle: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **genome size** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genome_size.yaml`.

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
**Generated:** 2026-08-04T05:04:23.183425

1. hutchison2016designandsynthesis pages 5-6
2. lee2012repeatedselectiondrivengenome pages 7-8
3. zhang2024genomereductionoccurred pages 10-14
4. kurokawa2016correlationbetweengenome pages 4-5
5. wang2024aneutralprocess pages 25-28
6. zhang2024genomereductionoccurred pages 7-10
7. dong2024ecoevolutionarystrategiesfor pages 9-10
8. wang2024aneutralprocess pages 1-5
9. wang2024aneutralprocess pages 14-17
10. zhang2024genomereductionoccurred pages 14-16
11. uncertain/generalization-limited
12. model-supported
13. context-specific
14. https://doi.org/10.1101/2024.02.04.578831
15. https://doi.org/10.1101/2023.06.25.546417
16. https://doi.org/10.1038/s41467-024-50368-z
17. https://doi.org/10.1038/s41467-024-46374-w
18. https://doi.org/10.1128/mbio.03530-23
19. https://doi.org/10.1111/1751-7915.14408
20. https://doi.org/10.1038/nrmicro3331
21. https://doi.org/10.1371/journal.pgen.1002651
22. https://doi.org/10.1093/dnares/dsw035
23. https://doi.org/10.1126/science.aad6253
24. https://doi.org/10.1371/journal.pgen.1004742
25. https://doi.org/10.1073/pnas.0503654102
26. https://doi.org/10.1101/2024.02.04.578831,
27. https://doi.org/10.1101/2023.06.25.546417,
28. https://doi.org/10.1126/science.aad6253,
29. https://doi.org/10.1371/journal.pgen.1002651,
30. https://doi.org/10.1093/dnares/dsw035,
31. https://doi.org/10.1038/s41467-024-50368-z,