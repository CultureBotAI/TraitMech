# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methanotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 20 nodes, 15 edges

## Research Objective

Research the microbial trait **methanotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methanotrophic.yaml`.

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
**Generated:** 2026-08-04T11:30:35.398421

1. ahmadi2024recentfindingsin pages 7-9
2. rasmussen2024diverseandunconventional pages 7-10
3. ahmadi2024recentfindingsin pages 1-2
4. koo2021biochemistryofaerobic pages 1-2
5. sina2024persistentactivityof pages 1-2
6. semrau2018metalsandmethanotrophy pages 3-5
7. kang2019theoriginof pages 1-1
8. dinh2024towardtheuse pages 1-2
9. wissink2024probingdenitrifyinganaerobic pages 1-2
10. dinh2024towardtheuse pages 2-4
11. ouboter2024mechanismsofextracellular pages 1-5
12. ouboter2024mechanismsofextracellular pages 10-16
13. sina2024persistentactivityof pages 6-7
14. samanta2024fromgenometo pages 12-14
15. wissink2024probingdenitrifyinganaerobic pages 4-5
16. wissink2024probingdenitrifyinganaerobic pages 5-7
17. dinh2024towardtheuse pages 4-5
18. sina2024persistentactivityof pages 2-3
19. sina2024persistentactivityof pages 3-4
20. wissink2024probingdenitrifyinganaerobic pages 2-3
21. wissink2024probingdenitrifyinganaerobic pages 3-4
22. ouboter2024mechanismsofextracellular pages 5-10
23. https://doi.org/10.1039/D3CY00737E.
24. https://doi.org/10.1007/s00253-023-12978-3.
25. https://doi.org/10.1038/s41467-024-49602-5.
26. https://doi.org/10.1021/acs.est.3c07197.
27. https://doi.org/10.1021/acs.accounts.4c00413.
28. https://doi.org/10.1128/msystems.00314-24.
29. https://doi.org/10.1128/msystems.00248-24.
30. https://doi.org/10.1039/D0CS01291B.
31. https://doi.org/10.1186/s40168-021-01112-y.
32. https://doi.org/10.1128/AEM.02289-17.
33. https://doi.org/10.1093/femsle/fnz096.
34. https://doi.org/10.1101/2023.07.24.550278.
35. https://doi.org/10.1128/msystems.00314-24,
36. https://doi.org/10.1128/aem.02289-17,
37. https://doi.org/10.1007/s00253-023-12978-3,
38. https://doi.org/10.1021/acs.est.3c07197,
39. https://doi.org/10.1021/acs.accounts.4c00413,
40. https://doi.org/10.1093/femsle/fnz096,
41. https://doi.org/10.1039/d0cs01291b,
42. https://doi.org/10.1038/s41467-024-49602-5,
43. https://doi.org/10.1186/s40168-021-01112-y,
44. https://doi.org/10.1101/2023.07.24.550278,
45. https://doi.org/10.1128/msystems.00248-24,