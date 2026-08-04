# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000636
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** aerobic_chemo_heterotrophy, chemoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemoheterotrophy to chemical energy and reduced organic carbon.) | DOI:10.1021/acsomega.3c02205: chemoheterotrophic (Review table supports chemoheterotrophic use of organic molecules as energy and carbon sources.)
- **Existing causal graph summary:** chemoheterotrophic_organic_energy_carbon: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **chemoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T10:56:38.162644

1. dupont2012genomicinsightsto pages 8-9
2. stebegg2023heterotrophyamongcyanobacteria pages 14-15
3. buckel2021energyconservationin pages 1-2
4. thomas2021genomicsexometabolomicsand pages 13-14
5. stebegg2023heterotrophyamongcyanobacteria pages 1-2
6. stebegg2023heterotrophyamongcyanobacteria pages 2-2
7. xiong2018isotopeassistedmetaboliteanalysis pages 1-2
8. laux2024livinginmangroves pages 13-14
9. laux2024livinginmangroves pages 24-25
10. has
11. 10.1021/acsomega.3c02205
12. 10.1186/s12866-024-03390-6
13. 10.3389/fmicb.2021.632731
14. 10.3389/fmicb.2021.703525
15. 10.3389/fmicb.2018.01947
16. 10.1038/ismej.2011.189
17. https://doi.org/10.1021/acsomega.3c02205
18. https://doi.org/10.1186/s12866-024-03390-6
19. https://doi.org/10.3389/fmicb.2021.632731
20. https://doi.org/10.3389/fmicb.2021.703525
21. https://doi.org/10.3389/fmicb.2018.01947
22. https://doi.org/10.1038/ismej.2011.189
23. https://doi.org/10.1021/acsomega.3c02205,
24. https://doi.org/10.1038/ismej.2011.189,
25. https://doi.org/10.3389/fmicb.2021.703525,
26. https://doi.org/10.3389/fmicb.2021.632731,
27. https://doi.org/10.3389/fmicb.2018.01947,
28. https://doi.org/10.1186/s12866-024-03390-6,