# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cadmium tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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
**Generated:** 2026-08-04T00:18:43.845393

1. chatterjee2024multimodalcadmiumresistance pages 14-15
2. legatzki2003interplayofthe pages 1-2
3. schulz2024theeffluxsystem pages 1-3
4. chatterjee2024multimodalcadmiumresistance pages 1-2
5. chatterjee2024multimodalcadmiumresistance pages 17-19
6. thai2023syntheticbacteriafor pages 15-17
7. sharma2024mechanismsofmicrobial pages 12-13
8. legatzki2003interplayofthe pages 3-4
9. legatzki2003interplayofthe pages 6-7
10. chatterjee2024multimodalcadmiumresistance pages 15-16
11. thai2023syntheticbacteriafor pages 19-19
12. 10.1038/s41598-024-80754-y
13. 10.1128/jb.00299-24
14. 10.1111/1751-7915.14399
15. 10.1007/s40201-023-00887-6
16. 10.3389/fbioe.2023.1178680
17. 10.1128/JB.185.15.4354-4361.2003
18. 10.1111/j.1365-2958.2009.06792.x
19. https://doi.org/10.1038/s41598-024-80754-y
20. https://doi.org/10.1128/jb.00299-24
21. https://doi.org/10.1111/1751-7915.14399
22. https://doi.org/10.1007/s40201-023-00887-6
23. https://doi.org/10.3389/fbioe.2023.1178680
24. https://doi.org/10.1128/JB.185.15.4354-4361.2003
25. https://doi.org/10.1111/j.1365-2958.2009.06792.x
26. https://doi.org/10.1038/s41598-024-80754-y,
27. https://doi.org/10.1128/jb.185.15.4354-4361.2003,
28. https://doi.org/10.1128/jb.00299-24,
29. https://doi.org/10.1007/s40201-023-00887-6,
30. https://doi.org/10.1111/1751-7915.14399,
31. https://doi.org/10.3389/fbioe.2023.1178680,