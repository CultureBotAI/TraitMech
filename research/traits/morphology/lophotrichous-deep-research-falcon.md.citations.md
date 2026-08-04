# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lophotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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
**Generated:** 2026-08-04T09:03:49.936440

1. burnham2020apolarflagellar pages 1-2
2. burnham2020apolarflagellar pages 17-19
3. schwan2022constitutiveproductionof pages 1-4
4. pulianmackal2024positioningofcellular pages 8-9
5. pulianmackal2024positioningofcellular pages 3-4
6. pulianmackal2024positioningofcellular pages 6-8
7. schuhmacher2015howbacteriamaintain pages 8-9
8. rossmann2017spatialregulationof pages 17-20
9. schuhmacher2015howbacteriamaintain pages 7-8
10. pulianmackal2024positioningofcellular pages 4-6
11. rossmann2017spatialregulationof pages 117-120
12. 10.1093/femsre/fuv034
13. 10.17192/z2017.0061
14. 10.1128/mbio.03107-19
15. 10.1016/j.mib.2024.102485
16. 10.1128/JB.00462-16
17. 10.1101/2022.07.21.500047
18. s
19. 10.3389/fmicb.2021.655239
20. Vibrio only
21. Shewanella-supported
22. 10.1101/2022.06.09.495121
23. 10.1073/pnas.1419388112
24. https://doi.org/10.1093/femsre/fuv034
25. https://doi.org/10.17192/z2017.0061
26. https://doi.org/10.1128/mbio.03107-19
27. https://doi.org/10.1016/j.mib.2024.102485
28. https://doi.org/10.1128/JB.00462-16
29. https://doi.org/10.1101/2022.07.21.500047
30. https://doi.org/10.3389/fmicb.2021.655239
31. https://doi.org/10.1101/2022.06.09.495121
32. https://doi.org/10.1073/pnas.1419388112
33. https://doi.org/10.1128/mbio.03107-19,
34. https://doi.org/10.1016/j.mib.2024.102485,
35. https://doi.org/10.1101/2022.07.21.500047,
36. https://doi.org/10.1093/femsre/fuv034,
37. https://doi.org/10.17192/z2017.0061,