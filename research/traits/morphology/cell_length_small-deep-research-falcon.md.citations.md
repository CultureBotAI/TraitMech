# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **cell length small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_small.yaml`.

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
**Generated:** 2026-08-04T07:45:39.248528

1. mueller2020phdependentactivationof pages 2-3
2. westfall2018comprehensiveanalysisof pages 17-18
3. buske2013thecterminus pages 225-230
4. westfall2017bacterialcellsize pages 9-11
5. mueller2020phdependentactivationof pages 11-13
6. vashistha2023bacterialcellsizechanges pages 1-2
7. strydom2017analysisofgenes pages 33-36
8. vashistha2023bacterialcellsizechanges pages 8-9
9. westfall2017bacterialcellsize pages 7-9
10. mueller2020phdependentactivationof pages 1-2
11. 10.1371/journal.pgen.1008685
12. 10.1371/journal.pgen.1003663
13. 10.1038/s41467-023-41487-0
14. 10.1038/s41467-024-54242-w
15. 10.1038/s41540-024-00383-z
16. 10.1371/journal.pgen.1007205
17. 10.1146/annurev-micro-090816-093803
18. 10.1128/mBio.00935-14
19. 10.1371/journal.pone.0092229
20. 10.1016/j.cub.2019.04.062
21. https://doi.org/10.1371/journal.pgen.1008685
22. https://doi.org/10.1371/journal.pgen.1003663
23. https://doi.org/10.1038/s41467-023-41487-0
24. https://doi.org/10.1038/s41467-024-54242-w
25. https://doi.org/10.1038/s41540-024-00383-z
26. https://doi.org/10.1371/journal.pgen.1007205
27. https://doi.org/10.1146/annurev-micro-090816-093803
28. https://doi.org/10.1128/mBio.00935-14
29. https://doi.org/10.1371/journal.pone.0092229
30. https://doi.org/10.1016/j.cub.2019.04.062
31. https://doi.org/10.1371/journal.pgen.1008685,
32. https://doi.org/10.1371/journal.pgen.1007205,
33. https://doi.org/10.7936/k7668b61,
34. https://doi.org/10.1146/annurev-micro-090816-093803,
35. https://doi.org/10.1038/s41467-023-41487-0,
36. https://doi.org/10.1093/femsle/fnx016,