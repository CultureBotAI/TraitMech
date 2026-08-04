# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** thermotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000619
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at elevated temperatures without an obligate high-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/00207713-52-6-2203: Pseudomonas thermotolerans sp. nov., a thermotolerant species (Organism example: Pseudomonas thermotolerans is described as thermotolerant.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports protein-stability features underlying facultative growth at elevated temperatures.)
- **Existing causal graph summary:** thermotolerant_facultative_heat_adaptation: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **thermotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermotolerant.yaml`.

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
**Generated:** 2026-08-04T04:41:42.699174

1. mcguire2023wholegenomesequencinganalysis pages 1-2
2. murata2011molecularstrategyfor pages 1-2
3. montini2022identificationofa pages 6-8
4. montini2022identificationofa pages 2-3
5. xia2024adaptiveresponsesof pages 1-2
6. hua2024regulatorymechanismsof pages 9-11
7. salasnavarrete2023adaptiveresponsesof pages 1-2
8. asefi2024comprehensivenetworkof pages 8-9
9. ren2024couplingthermotoleranceand pages 1-2
10. ren2024couplingthermotoleranceand pages 10-11
11. murata2011molecularstrategyfor pages 5-6
12. ren2024couplingthermotoleranceand pages 9-10
13. 10.1007/s00253-024-13103-8
14. 10.1038/s42003-024-06341-z
15. 10.1186/s12934-024-02602-y
16. 10.1186/s12934-024-02459-1
17. 10.1007/s00253-023-12556-7
18. 10.1186/s12864-023-09266-9
19. 10.1099/mic.0.001148
20. 10.1186/s13068-017-0984-9
21. 10.1371/journal.pone.0020063
22. https://doi.org/10.1007/s00253-024-13103-8
23. https://doi.org/10.1038/s42003-024-06341-z
24. https://doi.org/10.1186/s12934-024-02602-y
25. https://doi.org/10.1186/s12934-024-02459-1
26. https://doi.org/10.1007/s00253-023-12556-7
27. https://doi.org/10.1186/s12864-023-09266-9
28. https://doi.org/10.1099/mic.0.001148
29. https://doi.org/10.1186/s13068-017-0984-9
30. https://doi.org/10.1371/journal.pone.0020063
31. https://doi.org/10.1186/s12864-023-09266-9,
32. https://doi.org/10.1371/journal.pone.0020063,
33. https://doi.org/10.1099/mic.0.001148,
34. https://doi.org/10.1038/s42003-024-06341-z,
35. https://doi.org/10.1007/s00253-024-13103-8,
36. https://doi.org/10.1186/s12934-024-02602-y,
37. https://doi.org/10.1007/s00253-023-12556-7,
38. https://doi.org/10.1186/s12934-024-02459-1,