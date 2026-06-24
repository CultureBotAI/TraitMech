# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** S-layer
- **METPO identifier:** traitmech:000064
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell surface is coated by a crystalline, two-dimensional array of self-assembling proteinaceous (glyco)protein subunits (a surface layer), found in many bacteria and most archaea.
- **Parent traits:** METPO:1000059
- **Synonyms:** surface layer
- **Existing evidence:** DOI:10.1038/nrmicro3213:  (Fagan & Fairweather describe the S-layer as a self-assembled, regularly spaced two-dimensional protein array coating the cell surface.) | DOI:10.1038/s41579-025-01258-8:  (Review of assembly, architecture and functional roles of microbial surface layers supports the S-layer as a defined cell-surface structure.)
- **Existing causal graph summary:** s_layer_2d_protein_array: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **S-layer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/s_layer.yaml`.

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
**Generated:** 2026-06-18T09:41:57.755859

1. wong2023surfacelayerproteinis pages 1-2
2. herdman2024cellcycledependent pages 8-9
3. gambelli2024structureofthe pages 1-2
4. gambelli2024structureofthe pages 12-13
5. sagmeister2024themoleculararchitecture pages 1-2
6. sagmeister2024themoleculararchitecture pages 6-9
7. sogues2023structureandfunction pages 1-2
8. paillat2023ajourneywith pages 7-8
9. decout2024lactobacilluscrispatusslayer pages 1-2
10. qing2023scalablebiomimeticsensing pages 5-6
11. farci2023thesdbcis pages 1-2
12. royer2023clostridioidesdifficileslayer pages 8-10
13. royer2023clostridioidesdifficileslayer pages 4-6
14. yuliawati2024potencyofsurface pages 2-4
15. royer2023clostridioidesdifficileslayer pages 1-2
16. royer2023clostridioidesdifficileslayer pages 2-4
17. royer2023clostridioidesdifficileslayer pages 10-12
18. that
19. https://doi.org/10.1073/pnas.2401686121
20. https://doi.org/10.1038/s41467-024-47529-5
21. https://doi.org/10.1038/s41467-023-42826-x
22. https://doi.org/10.7554/eLife.84617
23. https://doi.org/10.1128/spectrum.03894-22
24. https://doi.org/10.1038/s41467-024-55233-7
25. https://doi.org/10.1038/s41396-023-01388-y
26. https://doi.org/10.1126/sciadv.adf1402
27. https://doi.org/10.7554/elife.84617
28. https://doi.org/10.1099/mic.0.001320
29. https://doi.org/10.1016/j.jbc.2022.102784
30. https://doi.org/10.7554/elife.84617,
31. https://doi.org/10.1038/s41467-023-42826-x,
32. https://doi.org/10.1073/pnas.2401686121,
33. https://doi.org/10.1038/s41396-023-01388-y,
34. https://doi.org/10.1038/s41467-024-47529-5,
35. https://doi.org/10.1128/spectrum.03894-22,
36. https://doi.org/10.1099/mic.0.001320,
37. https://doi.org/10.1038/s41467-024-55233-7,
38. https://doi.org/10.1126/sciadv.adf1402,
39. https://doi.org/10.1016/j.jbc.2022.102784,
40. https://doi.org/10.7324/japs.2024.199203,