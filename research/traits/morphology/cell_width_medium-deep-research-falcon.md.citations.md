# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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
**Generated:** 2026-08-04T07:56:59.964278

1. westfall2018comprehensiveanalysisof pages 1-2
2. garde2021peptidoglycanstructuresynthesis pages 13-15
3. turner2018molecularimagingof pages 1-2
4. middlemiss2024molecularmotortugofwar pages 8-9
5. ojima2024buddingandexplosive pages 1-2
6. willdigg2023adecreasein pages 1-3
7. gilman2024mrecmredstructurereveals pages 1-2
8. middlemiss2024molecularmotortugofwar pages 1-2
9. spahn2023transertionandcell pages 5-7
10. westfall2018comprehensiveanalysisof pages 8-10
11. shi2017deepphenotypicmapping pages 1-3
12. shi2017deepphenotypicmapping pages 9-9
13. hussain2018mrebfilamentsalign pages 1-2
14. hussain2018mrebfilamentsalign pages 13-15
15. gilman2024mrecmredstructurereveals pages 5-6
16. shi2017deepphenotypicmapping pages 8-9
17. 10.1038/s41467-024-49785-x
18. 10.3389/fmicb.2024.1400434
19. 10.1101/2024.10.08.617240
20. 10.1128/mbio.00475-23
21. 10.1101/2023.10.16.562172
22. 10.1128/ecosalplus.esp-0010-2020
23. 10.7554/eLife.32471
24. 10.1038/s41467-018-03551-y
25. 10.1371/journal.pgen.1007205
26. 10.1016/j.cub.2017.09.065
27. https://doi.org/10.1038/s41467-024-49785-x
28. https://doi.org/10.3389/fmicb.2024.1400434
29. https://doi.org/10.1101/2024.10.08.617240
30. https://doi.org/10.1128/mbio.00475-23
31. https://doi.org/10.1101/2023.10.16.562172
32. https://doi.org/10.1128/ecosalplus.esp-0010-2020
33. https://doi.org/10.7554/eLife.32471
34. https://doi.org/10.1038/s41467-018-03551-y
35. https://doi.org/10.1371/journal.pgen.1007205
36. https://doi.org/10.1016/j.cub.2017.09.065
37. https://doi.org/10.1371/journal.pgen.1007205,
38. https://doi.org/10.7554/elife.32471,
39. https://doi.org/10.1128/ecosalplus.esp-0010-2020,
40. https://doi.org/10.1038/s41467-018-03551-y,
41. https://doi.org/10.1038/s41467-024-49785-x,
42. https://doi.org/10.1101/2024.10.08.617240,
43. https://doi.org/10.3389/fmicb.2024.1400434,
44. https://doi.org/10.1128/mbio.00475-23,
45. https://doi.org/10.1101/2023.10.16.562172,
46. https://doi.org/10.1016/j.cub.2017.09.065,