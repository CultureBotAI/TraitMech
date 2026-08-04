# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000640
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds through oxidation.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemical energy, reduced organic electron source, and reduced organic carbon source to chemoorganoheterotrophy.) | DOI:10.1021/acsomega.3c02205: chemoorganoheterotrophic (Review table supports organic molecules as energy, electron, and carbon sources in chemoorganoheterotrophy.)
- **Existing causal graph summary:** chemoorganoheterotrophic_organic_energy_carbon: 13 nodes, 15 edges

## Research Objective

Research the microbial trait **chemoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T11:05:29.991340

1. stebegg2023heterotrophyamongcyanobacteria pages 1-2
2. buckel2021energyconservationin pages 1-2
3. karnachuk2024novelthermophilicgenera pages 5-8
4. sarkar2024extremelyoligotrophicand pages 1-4
5. stebegg2023heterotrophyamongcyanobacteria pages 4-5
6. yadav2024organicmatterdegradation pages 1-2
7. khan2024cnratioeffect pages 1-2
8. yu2024isolationofhighly pages 1-2
9. smorada2024bacterialdegradationof pages 1-3
10. rakitin2024verrucomicrobiaofthe pages 1-2
11. sarkar2024extremelyoligotrophicand pages 12-15
12. sarkar2024extremelyoligotrophicand pages 4-6
13. sarkar2024extremelyoligotrophicand pages 23-26
14. 10.1021/acsomega.3c02205
15. 10.3389/fmicb.2024.1441865
16. 10.1186/s40168-024-01816-x
17. 10.3390/microorganisms12112271
18. 10.1101/2023.10.31.564988
19. 10.1038/s41598-024-72490-0
20. 10.3389/fmicb.2024.1390451
21. 10.1016/j.copbio.2024.103170
22. 10.3389/fmicb.2021.703525
23. https://doi.org/10.1021/acsomega.3c02205
24. https://doi.org/10.3389/fmicb.2024.1441865
25. https://doi.org/10.1186/s40168-024-01816-x
26. https://doi.org/10.3390/microorganisms12112271
27. https://doi.org/10.1101/2023.10.31.564988
28. https://doi.org/10.1038/s41598-024-72490-0
29. https://doi.org/10.3389/fmicb.2024.1390451
30. https://doi.org/10.1016/j.copbio.2024.103170
31. https://doi.org/10.3389/fmicb.2021.703525
32. https://doi.org/10.1021/acsomega.3c02205,
33. https://doi.org/10.3389/fmicb.2021.703525,
34. https://doi.org/10.3389/fmicb.2024.1441865,
35. https://doi.org/10.1101/2023.10.31.564988,
36. https://doi.org/10.1186/s40168-024-01816-x,
37. https://doi.org/10.1038/s41598-024-72490-0,
38. https://doi.org/10.3389/fmicb.2024.1390451,
39. https://doi.org/10.1016/j.copbio.2024.103170,
40. https://doi.org/10.3390/microorganisms12112271,