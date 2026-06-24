# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length small
- **METPO identifier:** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 4 nodes, 3 edges

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
**Generated:** 2026-06-18T07:09:22.988399

1. vashistha2023bacterialcellsizechanges pages 2-3
2. nieto2024mechanismsofcell pages 1-2
3. cameron2024insightsintothe pages 1-3
4. mannik2024determiningtheratelimiting pages 1-2
5. gong2024thedivisomeis pages 1-3
6. vashistha2023bacterialcellsizechanges pages 1-2
7. hayashi2024septalwallsynthesis pages 7-8
8. thiermann2024toolsandmethods pages 10-11
9. yokoyama2024capturingofextracellular pages 1-2
10. yokoyama2024capturingofextracellular pages 6-7
11. nieto2024bacterialcellsize pages 5-7
12. nieto2024ageneralizedadder pages 1-2
13. nieto2024mechanismsofcell pages 6-7
14. nieto2024mechanismsofcell pages 4-6
15. yokoyama2024capturingofextracellular pages 5-6
16. cameron2024insightsintothe pages 10-12
17. cameron2024insightsintothe pages 20-22
18. nieto2024bacterialcellsize pages 7-9
19. https://doi.org/10.1038/s41540-024-00383-z
20. https://doi.org/10.1038/s41467-024-54242-w
21. https://doi.org/10.1038/s41467-024-52217-5
22. https://doi.org/10.1101/2024.04.08.588611
23. https://doi.org/10.7554/eLife.88463
24. https://doi.org/10.1039/d3lc00707c
25. https://doi.org/10.1038/s41467-023-41487-0
26. https://doi.org/10.7554/elife.88463
27. https://doi.org/10.1038/s42003-024-07279-y
28. https://doi.org/10.1101/2024.09.24.614723
29. https://doi.org/10.1038/s41579-023-00942-x
30. https://doi.org/10.1101/2024.04.08.588611,
31. https://doi.org/10.1038/s41467-023-41487-0,
32. https://doi.org/10.7554/elife.88463,
33. https://doi.org/10.1039/d3lc00707c,
34. https://doi.org/10.1101/2024.09.24.614723,
35. https://doi.org/10.1101/2024.09.13.612972,
36. https://doi.org/10.1038/s41540-024-00383-z,
37. https://doi.org/10.1038/s41579-023-00942-x,
38. https://doi.org/10.1038/s41467-024-54242-w,
39. https://doi.org/10.1038/s41467-024-52217-5,
40. https://doi.org/10.1038/s42003-024-07279-y,