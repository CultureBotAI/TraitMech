# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Cable bacteria metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **Cable bacteria metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cable_bacteria_metabolism.yaml`.

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
**Generated:** 2026-08-04T05:41:41.280227

1. bjerg2018longdistanceelectrontransport pages 1-2
2. wang2024electrogenicsulfuroxidation pages 2-3
3. meysman2019ahighlyconductive pages 1-2
4. kjeldsen2019ontheevolution pages 1-1
5. hiralal2025anovelcable pages 10-13
6. reimers2017theidentificationof pages 1-2
7. wang2024electrogenicsulfuroxidation pages 3-3
8. zhuang2024electrontransferin pages 6-8
9. bonne2024interactionofliving pages 1-2
10. bonne2024interactionofliving pages 2-5
11. 10.1073/pnas.1800367115
12. 10.1038/s41467-019-12115-7
13. 10.1073/pnas.1903514116
14. 10.1016/j.ese.2023.100371
15. 10.1186/s12864-024-10594-7
16. 10.1128/aem.00795-24
17. 10.3390/life14050591
18. 10.3389/fmicb.2017.02055
19. https://doi.org/10.1073/pnas.1800367115
20. https://doi.org/10.1038/s41467-019-12115-7
21. https://doi.org/10.1073/pnas.1903514116
22. https://doi.org/10.1016/j.ese.2023.100371
23. https://doi.org/10.1186/s12864-024-10594-7
24. https://doi.org/10.1128/aem.00795-24
25. https://doi.org/10.3390/life14050591
26. https://doi.org/10.3389/fmicb.2017.02055
27. https://doi.org/10.1073/pnas.1800367115,
28. https://doi.org/10.1073/pnas.1903514116,
29. https://doi.org/10.1016/j.ese.2023.100371,
30. https://doi.org/10.1128/aem.00795-24,
31. https://doi.org/10.1038/s41467-019-12115-7,
32. https://doi.org/10.1128/aem.02502-24,
33. https://doi.org/10.3390/life14050591,
34. https://doi.org/10.3389/fmicb.2017.02055,