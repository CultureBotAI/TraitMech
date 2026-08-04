# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** persister cell formation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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
**Generated:** 2026-08-04T11:57:02.115951

1. li2024intracellularatpconcentration pages 1-2
2. goormaghtigh2024understandingstaphylococcusaureus pages 8-9
3. pont2024proteomiccharacterizationof pages 1-2
4. blattman2024identificationandgenetic pages 3-4
5. blattman2024identificationandgenetic pages 7-8
6. yuan2024molecularmechanismand pages 3-6
7. yuan2024molecularmechanismand pages 6-7
8. niu2024bacterialpersistersmolecular pages 15-16
9. yuan2024molecularmechanismand pages 1-2
10. blattman2024identificationandgenetic pages 1-2
11. niu2024bacterialpersistersmolecular pages 1-3
12. prasetyoputri2019theeagleeffect pages 8-9
13. yuan2024molecularmechanismand pages 2-3
14. yuan2024molecularmechanismand pages 7-9
15. niu2024bacterialpersistersmolecular pages 3-4
16. vergoz2025antibioticpersistercells pages 3-3
17. blattman2024identificationandgenetic pages 5-6
18. blattman2024identificationandgenetic pages 6-6
19. blattman2024identificationandgenetic pages 23-30
20. niu2024bacterialpersistersmolecular pages 6-7
21. vergoz2025antibioticpersistercells pages 8-8
22. niu2024bacterialpersistersmolecular pages 28-29
23. niu2024bacterialpersistersmolecular pages 20-21
24. niu2024bacterialpersistersmolecular pages 21-22
25. niu2024bacterialpersistersmolecular pages 30-31
26. kunnath2024bacterialpersistercells pages 1-2
27. 10.1038/s41586-024-08124-2
28. 10.3389/fmicb.2024.1408701
29. 10.1186/s12866-023-03162-8
30. 10.1186/s12866-024-03628-3
31. 10.1128/jb.00208-24
32. 10.1111/1462-2920.70207
33. 10.1038/s41392-024-01866-5
34. 10.1080/14787210.2024.2303018
35. 10.1016/j.tim.2018.10.007
36. https://doi.org/10.1038/s41586-024-08124-2
37. https://doi.org/10.3389/fmicb.2024.1408701
38. https://doi.org/10.1186/s12866-023-03162-8
39. https://doi.org/10.1186/s12866-024-03628-3
40. https://doi.org/10.1128/jb.00208-24
41. https://doi.org/10.1111/1462-2920.70207
42. https://doi.org/10.1038/s41392-024-01866-5
43. https://doi.org/10.1080/14787210.2024.2303018
44. https://doi.org/10.1016/j.tim.2018.10.007
45. https://doi.org/10.1186/s12866-024-03628-3,
46. https://doi.org/10.1186/s12866-023-03162-8,
47. https://doi.org/10.1038/s41392-024-01866-5,
48. https://doi.org/10.1038/s41586-024-08124-2,
49. https://doi.org/10.1016/j.tim.2018.10.007,
50. https://doi.org/10.1128/jb.00208-24,
51. https://doi.org/10.1080/14787210.2024.2303018,
52. https://doi.org/10.1111/1462-2920.70207,
53. https://doi.org/10.3389/fmicb.2024.1408701,
54. https://doi.org/10.3389/bjbs.2024.12958,