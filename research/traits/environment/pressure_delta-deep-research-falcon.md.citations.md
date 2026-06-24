# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure delta
- **METPO identifier:** traitmech:000006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits expressing the breadth (maximum minus minimum) of hydrostatic pressure supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the breadth of the pressure-tolerance span as a derived descriptor of pressure-adaptation flexibility.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (The 80-140 MPa span of Colwellia marinimaniae MTCD1 (delta = 60 MPa) illustrates the breadth this phenotype records.)
- **Existing causal graph summary:** pressure_delta_breadth_descriptor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_delta.yaml`.

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
**Generated:** 2026-06-18T01:28:39.643899

1. stief2023hydrostaticpressureinduces pages 1-2
2. malas2024biologicalfunctionsat pages 1-2
3. peters2023effectsofcrowding pages 7-9
4. stief2023hydrostaticpressureinduces pages 8-9
5. malas2024biologicalfunctionsat pages 2-3
6. peters2023effectsofcrowding pages 9-11
7. malas2024biologicalfunctionsat pages 9-10
8. malas2024biologicalfunctionsat pages 6-9
9. miller2023carnobacteriumspeciescapableof pages 1-3
10. peoples2020distinctivegeneand pages 11-12
11. makhatadze2024modulationofelectrostatic pages 1-3
12. peoples2020distinctivegeneand pages 5-7
13. peoples2020distinctivegeneand pages 1-2
14. miller2023carnobacteriumspeciescapableof pages 8-9
15. peoples2020distinctivegeneand pages 9-11
16. https://doi.org/10.1186/s12864-020-07102-y,
17. https://doi.org/10.1021/acs.chemrev.3c00432,
18. https://doi.org/10.1038/s43247-023-01045-4,
19. https://doi.org/10.3389/fmicb.2024.1293928,
20. https://doi.org/10.1101/2024.07.28.605522,
21. https://doi.org/10.1089/ast.2022.0043,
22. https://doi.org/10.3389/fmicb.2024.1293928
23. https://doi.org/10.1021/acs.chemrev.3c00432
24. https://doi.org/10.1038/s43247-023-01045-4
25. https://doi.org/10.1089/ast.2022.0043
26. https://doi.org/10.1186/s12864-020-07102-y
27. https://doi.org/10.1101/2024.07.28.605522