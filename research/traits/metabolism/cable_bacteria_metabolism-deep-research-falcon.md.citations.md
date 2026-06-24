# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Cable bacteria metabolism
- **METPO identifier:** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 10 nodes, 9 edges

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
**Generated:** 2026-06-18T04:24:13.317375

1. bonne2024interactionofliving pages 1-2
2. veen2024amodelanalysis pages 1-2
3. bjerg2018longdistanceelectrontransport pages 1-2
4. smets2024multiwavelengthramanmicroscopy pages 10-11
5. veen2024temperaturedependentcharacterizationof pages 1-2
6. hiralal2024closingthegenome pages 9-11
7. hiralal2024comparativegenomicanalysis pages 1-2
8. zhuang2024electrontransferin pages 6-8
9. yang2024longdistanceelectrontransport pages 1-2
10. bonne2024interactionofliving pages 2-5
11. hiralal2024closingthegenome pages 11-13
12. hiralal2024comparativegenomicanalysis pages 5-7
13. smets2024multiwavelengthramanmicroscopy pages 1-2
14. bonne2024interactionofliving pages 5-8
15. smets2024multiwavelengthramanmicroscopy pages 11-12
16. smets2024multiwavelengthramanmicroscopy pages 12-14
17. yang2024longdistanceelectrontransport pages 18-19
18. zhuang2024electrontransferin pages 15-16
19. smets2024multiwavelengthraman pages 13-14
20. smets2024multiwavelengthraman pages 11-12
21. https://doi.org/10.1039/d3cp04466a
22. https://doi.org/10.7554/eLife.91097
23. https://doi.org/10.1073/pnas.1800367115
24. https://doi.org/10.1099/mgen.0.001197
25. https://doi.org/10.1186/s12864-024-10594-7
26. https://doi.org/10.1021/acsnano.4c12186
27. https://doi.org/10.3389/fmicb.2024.1208033
28. https://doi.org/10.1128/aem.00795-24
29. https://doi.org/10.3390/life14050591
30. https://doi.org/10.7554/elife.91097,
31. https://doi.org/10.1073/pnas.1800367115,
32. https://doi.org/10.1186/s12864-024-10594-7,
33. https://doi.org/10.1128/aem.00795-24,
34. https://doi.org/10.1039/d3cp04466a,
35. https://doi.org/10.3389/fmicb.2024.1208033,
36. https://doi.org/10.1021/acsnano.4c12186,
37. https://doi.org/10.1099/mgen.0.001197,
38. https://doi.org/10.3390/life14050591,