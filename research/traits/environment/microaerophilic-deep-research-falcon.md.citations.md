# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** microaerophilic
- **METPO identifier:** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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
**Generated:** 2026-06-17T23:07:02.812437

1. fuduche2019anovelhighly pages 1-2
2. wallace2018metabolicandphysiological pages 40-45
3. gadkari2018purificationofthe pages 137-141
4. jong2024quantitativeproteomicsreveals pages 1-2
5. azarkina2023interactionofterminal pages 1-2
6. stoakes2024identificationofcampylobacter pages 1-2
7. rogers2023thephysiologyand pages 29-33
8. delaporte2024aerotolerancyofcampylobacter pages 8-9
9. delaporte2024aerotolerancyofcampylobacter pages 9-11
10. mele2023oxidoreductasesandmetal pages 16-17
11. fuduche2019anovelhighly pages 3-5
12. alqurashi2020theroleof pages 24-28
13. label only
14. candidate
15. quinol oxidase activity, candidate
16. aerobic electron transport chain, candidate
17. two-component response regulator activity, candidate
18. superoxide, candidate
19. respiratory electron transport chain
20. https://www.ncbi.nlm.nih.gov/books/NBK154539/:
21. https://doi.org/10.3389/fmicb.2019.00534
22. https://doi.org/10.3390/ijms24076428
23. https://doi.org/10.1128/spectrum.02767-23
24. https://doi.org/10.3390/pathogens13100842
25. https://doi.org/10.1186/s12866-024-03201-y
26. https://doi.org/10.3389/fmicb.2024.1468929
27. https://doi.org/10.3389/fmicb.2019.00534,
28. https://doi.org/10.3390/pathogens13100842,
29. https://doi.org/10.3390/ijms24076428,
30. https://doi.org/10.3389/fmicb.2024.1468929,
31. https://doi.org/10.1128/spectrum.02767-23,
32. https://doi.org/10.1042/ebc20230012,
33. https://doi.org/10.1186/s12866-024-03201-y,