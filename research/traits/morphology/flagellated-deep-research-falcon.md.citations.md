# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellated
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **flagellated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellated.yaml`.

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
**Generated:** 2026-08-04T08:35:02.873002

1. lo2016regulationofmotility pages 11-14
2. minamino2023structureassemblyand pages 22-23
3. chilcott2000couplingofflagellar pages 7-8
4. nedeljkovic2021bacterialflagellarfilament pages 9-10
5. nedeljkovic2021bacterialflagellarfilament pages 1-2
6. wu2024torquespeedrelationshipof pages 17-19
7. mckee2013thesecondmessenger pages 10-11
8. chilcott2000couplingofflagellar pages 1-1
9. nedeljkovic2021bacterialflagellarfilament pages 27-28
10. lo2016regulationofmotility pages 14-15
11. 10.1128/ecosalplus.esp-0011-2023
12. 10.1128/mbio.00745-24
13. 10.3390/ijms22147521
14. 10.3390/biom11020186
15. 10.1128/MMBR.64.4.694-708.2000
16. 10.1371/journal.pone.0155397
17. 10.1128/JB.00501-13
18. 10.1128/mbio.00189-23
19. 10.1146/annurev-micro-032421-110850
20. 10.1093/femsre/fuaa006
21. https://doi.org/10.1128/mmbr.64.4.694-708.2000
22. https://doi.org/10.3390/ijms22147521
23. https://doi.org/10.3390/biom11020186
24. https://doi.org/10.1016/j.tibs.2021.06.005
25. https://doi.org/10.1016/j.tim.2020.03.010
26. https://doi.org/10.1128/ecosalplus.esp-0011-2023
27. https://doi.org/10.1128/mbio.00189-23
28. https://doi.org/10.1146/annurev-micro-032421-110850
29. https://doi.org/10.1128/jb.00501-13
30. https://doi.org/10.1371/journal.pone.0155397
31. https://doi.org/10.1093/femsre/fuaa006
32. https://doi.org/10.1128/mbio.00745-24
33. https://doi.org/10.1128/MMBR.64.4.694-708.2000
34. https://doi.org/10.1128/JB.00501-13
35. https://doi.org/10.3390/ijms22147521,
36. https://doi.org/10.1128/ecosalplus.esp-0011-2023,
37. https://doi.org/10.1371/journal.pone.0155397,
38. https://doi.org/10.1128/mmbr.64.4.694-708.2000,
39. https://doi.org/10.1128/mbio.00745-24,
40. https://doi.org/10.1128/jb.00501-13,