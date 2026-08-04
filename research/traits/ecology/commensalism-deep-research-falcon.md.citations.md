# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** commensalism
- **METPO identifier:** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **commensalism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/commensalism.yaml`.

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
**Generated:** 2026-08-03T23:07:55.711227

1. drew2021microbialevolutionand pages 2-3
2. caballeroflores2023microbiotamediatedcolonizationresistance pages 12-14
3. xiao2021gutcolonizationmechanisms pages 7-9
4. costa2024thestaphylococcusaureus pages 1-2
5. donaldson2018gutmicrobiotautilize pages 2-3
6. donaldson2018gutmicrobiotautilize pages 3-4
7. fekete2023theroleof pages 1-5
8. porter2017asubsetof pages 2-4
9. caballeroflores2023microbiotamediatedcolonizationresistance pages 3-4
10. fachi2024hyperbaricoxygenaugments pages 1-2
11. joglekar2019intestinaligaregulates pages 3-4
12. lin2024areviewof pages 13-14
13. xiao2021gutcolonizationmechanisms pages 3-5
14. xiao2021gutcolonizationmechanisms pages 5-6
15. https://doi.org/10.1126/science.aaq0926
16. https://doi.org/10.1152/ajpgi.00261.2022
17. https://doi.org/10.1016/j.chom.2017.08.020
18. https://doi.org/10.1038/s41579-022-00833-7
19. https://doi.org/10.1080/19490976.2023.2297872
20. https://doi.org/10.1128/mbio.00453-24
21. https://doi.org/10.1038/s41579-021-00550-7
22. https://doi.org/10.3390/microorganisms12051026
23. https://doi.org/10.1146/annurev-food-061120-014739
24. https://doi.org/10.1128/mbio.02324-19
25. https://doi.org/10.1038/s41579-021-00550-7,
26. https://doi.org/10.1038/s41579-022-00833-7,
27. https://doi.org/10.1146/annurev-food-061120-014739,
28. https://doi.org/10.1128/mbio.00453-24,
29. https://doi.org/10.1126/science.aaq0926,
30. https://doi.org/10.1152/ajpgi.00261.2022,
31. https://doi.org/10.1016/j.chom.2017.08.020,
32. https://doi.org/10.1080/19490976.2023.2297872,
33. https://doi.org/10.1128/mbio.02324-19,
34. https://doi.org/10.3390/microorganisms12051026,