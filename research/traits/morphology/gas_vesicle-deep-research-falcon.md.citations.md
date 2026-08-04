# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gas vesicle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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
**Generated:** 2026-08-04T08:35:28.141821

1. pfeifer2022recentadvancesin pages 1-2
2. pfeifer2022recentadvancesin pages 4-5
3. feng2024advancesinthe pages 4-5
4. iburg2024elucidatingtheassembly pages 13-14
5. jazbec2024proteingasvesicles pages 5-6
6. feng2024advancesinthe pages 2-4
7. pfeifer2022recentadvancesin pages 10-12
8. jazbec2024proteingasvesicles pages 3-5
9. hurt2024directedevolutionof pages 7-8
10. pfeifer2022recentadvancesin pages 12-14
11. pfeifer2022recentadvancesin pages 14-15
12. iburg2024elucidatingtheassembly pages 1-2
13. Pfeifer 2022
14. Feng et al. 2024
15. Jazbec et al. 2024
16. Iburg et al. 2024
17. 10.1038/s44318-024-00178-2
18. 10.1021/acsnano.4c01498
19. 10.1021/acssynbio.4c00283
20. 10.1002/btm2.10584
21. 10.1186/s13036-024-00426-3
22. 10.1021/acs.nanolett.3c02780
23. 10.3390/life12091455
24. https://doi.org/10.3390/life12091455
25. https://doi.org/10.1186/s13036-024-00426-3
26. https://doi.org/10.1021/acsnano.4c01498
27. https://doi.org/10.1038/s44318-024-00178-2
28. https://doi.org/10.1021/acssynbio.4c00283
29. https://doi.org/10.1002/btm2.10584
30. https://doi.org/10.1021/acs.nanolett.3c02780
31. https://doi.org/10.1186/s13036-024-00426-3,
32. https://doi.org/10.3390/life12091455,
33. https://doi.org/10.1038/s44318-024-00178-2,
34. https://doi.org/10.1021/acsnano.4c01498,
35. https://doi.org/10.1021/acssynbio.4c00283,
36. https://doi.org/10.1002/btm2.10584,
37. https://doi.org/10.1021/acs.nanolett.3c02780,