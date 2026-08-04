# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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
**Generated:** 2026-08-03T23:08:35.940705

1. ta2018biosafetyandbiohazards pages 3-6
2. robilotti2023biosafetyandbiohazard pages 3-4
3. cornish2021clinicallaboratorybiosafety pages 16-18
4. zuo2024ahistoricalstudy pages 8-10
5. kimman2008evidencebasedbiosafetya pages 7-8
6. gulig2024areviewof pages 1-2
7. kimman2008evidencebasedbiosafetya pages 12-13
8. gulig2024areviewof pages 8-10
9. nolascoromero2024theexosexot pages 1-2
10. nolascoromero2024theexosexot pages 2-3
11. zuo2024ahistoricalstudy pages 1-2
12. nolascoromero2024theexosexot pages 6-8
13. gao2024frombiosafetyto pages 2-3
14. kimman2008evidencebasedbiosafetya pages 18-19
15. kimman2008evidencebasedbiosafetya pages 4-5
16. robilotti2023biosafetyandbiohazard pages 9-10
17. gulig2024areviewof pages 13-15
18. and
19. 10.3390/laboratories1020007
20. 10.1089/apb.2024.0002
21. 10.3390/pathogens13121030
22. 10.3390/laboratories1030013
23. 10.3389/fmolb.2023.1178382
24. 10.1016/j.bsheal.2023.04.006
25. 10.1128/CMR.00126-18
26. 10.1128/CMR.00014-08
27. 10.1007/978-1-4939-8935-5_19
28. https://doi.org/10.3390/laboratories1020007
29. https://doi.org/10.1089/apb.2024.0002
30. https://doi.org/10.3390/pathogens13121030
31. https://doi.org/10.3390/laboratories1030013
32. https://doi.org/10.3389/fmolb.2023.1178382
33. https://doi.org/10.1016/j.bsheal.2023.04.006
34. https://doi.org/10.1128/CMR.00126-18
35. https://doi.org/10.1128/CMR.00014-08
36. https://doi.org/10.1007/978-1-4939-8935-5_19
37. https://doi.org/10.1007/978-1-4939-8935-5\_19,
38. https://doi.org/10.1128/cmr.00014-08,
39. https://doi.org/10.3389/fmolb.2023.1178382,
40. https://doi.org/10.1128/cmr.00126-18,
41. https://doi.org/10.3390/laboratories1020007,
42. https://doi.org/10.1089/apb.2024.0002,
43. https://doi.org/10.3390/pathogens13121030,
44. https://doi.org/10.3390/laboratories1030013,