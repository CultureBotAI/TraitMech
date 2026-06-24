# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** quality
- **METPO identifier:** METPO:1000188
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A characteristic of an entity that depends on the entity's existence, size, color, and physiological traits.
- **Parent traits:** 
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: ontology of qualities termed Phenotype and Trait ontology (Supports quality as an upper class used to construct phenotype descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity (Supports qualities as entity-dependent phenotype descriptors.)
- **Existing causal graph summary:** quality_upper_child_context: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **quality** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/quality.yaml`.

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
**Generated:** 2026-06-18T13:16:05.754965

1. nedellec2024taecamanually pages 1-4
2. chibucos2014anontologyfor pages 2-5
3. gkoutos2018theanatomyof pages 5-6
4. chibucos2014anontologyfor pages 5-6
5. gkoutos2012ontologybasedcrossspeciesintegration pages 3-5
6. matentzoglu2025theunifiedphenotype pages 5-6
7. matentzoglu2025theunifiedphenotype pages 4-5
8. liu2023mycobacteriaceaephenomeatlas pages 1-2
9. gkoutos2012ontologybasedcrossspeciesintegration pages 5-8
10. liu2023mycobacteriaceaephenomeatlas pages 12-14
11. liu2023mycobacteriaceaephenomeatlas pages 2-5
12. thessen2020transformingthestudy pages 11-12
13. gkoutos2018theanatomyof pages 6-7
14. duque2024meetingreportfor pages 1-3
15. thessen2020transformingthestudy pages 8-11
16. (decreased length and (inheres in some femur) and (has modifier some abnormal))
17. https://doi.org/10.1186/s12866-014-0294-3
18. https://doi.org/10.1093/bib/bbx035
19. https://doi.org/10.1186/2041-1480-3-s2-s6
20. https://doi.org/10.1093/genetics/iyaf027
21. https://doi.org/10.1371/journal.pcbi.1008376
22. https://doi.org/10.1093/nar/gkad1072
23. https://doi.org/10.1007/s43657-023-00101-5
24. https://doi.org/10.1371/journal.pone.0305475
25. https://doi.org/10.1093/nar/gky1077
26. https://doi.org/10.1093/genetics/iyaf027,
27. https://doi.org/10.1093/bib/bbx035,
28. https://doi.org/10.1186/2041-1480-3-s2-s6,
29. https://doi.org/10.1186/s12866-014-0294-3,
30. https://doi.org/10.1371/journal.pone.0305475,
31. https://doi.org/10.1371/journal.pcbi.1008376,
32. https://doi.org/10.1093/nar/gky1077,
33. https://doi.org/10.1007/s43657-023-00101-5,
34. https://doi.org/10.3897/biss.8.115232,