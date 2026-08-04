# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T11:44:10.374019

1. braun2021reviewsandsyntheses pages 1-2
2. burgsdorf2021rethinkingsymbioticmetabolism pages 1-4
3. theodosiou2022exploitationofhetero pages 1-2
4. li2024arcobacteraceaeareubiquitous pages 10-12
5. halloran2024molecularcharacterizationof pages 32-36
6. clara2022phylogeneticallyandfunctionally pages 1-2
7. clara2022phylogeneticallyandfunctionally pages 7-8
8. xu2024activemicrobialpopulation pages 1-2
9. faulkner2023chemoautotrophicproductionof pages 1-2
10. burgsdorf2021rethinkingsymbioticmetabolism pages 13-16
11. eiler2006evidenceforthe pages 1-2
12. braun2021reviewsandsyntheses pages 2-4
13. braun2021reviewsandsyntheses pages 4-5
14. halloran2024molecularcharacterizationof pages 40-43
15. marella2021impactoforganic pages 6-8
16. marella2021impactoforganic pages 1-2
17. 10.1128/mbio.00177-24
18. 10.1128/msystems.00513-24
19. 10.1575/1912/69776
20. 10.1186/s13068-023-02404-1
21. 10.1038/s41467-021-27769-5
22. 10.3389/fbioe.2022.855715
23. 10.1111/1462-2920.15642
24. 10.5194/bg-18-3689-2021
25. 10.1186/s12934-021-01627-x
26. 10.1128/AEM.01559-06
27. 10.1101/2021.08.28.458021
28. https://doi.org/10.1128/mbio.00177-24
29. https://doi.org/10.1128/msystems.00513-24
30. https://doi.org/10.1575/1912/69776
31. https://doi.org/10.1186/s13068-023-02404-1
32. https://doi.org/10.1038/s41467-021-27769-5
33. https://doi.org/10.3389/fbioe.2022.855715
34. https://doi.org/10.1111/1462-2920.15642
35. https://doi.org/10.5194/bg-18-3689-2021
36. https://doi.org/10.1186/s12934-021-01627-x
37. https://doi.org/10.1128/AEM.01559-06
38. https://doi.org/10.1101/2021.08.28.458021
39. https://doi.org/10.5194/bg-18-3689-2021,
40. https://doi.org/10.1128/aem.01559-06,
41. https://doi.org/10.1101/2021.08.28.458021,
42. https://doi.org/10.1111/1462-2920.15642,
43. https://doi.org/10.1575/1912/69776,
44. https://doi.org/10.3389/fbioe.2022.855715,
45. https://doi.org/10.1128/mbio.00177-24,
46. https://doi.org/10.1038/s41467-021-27769-5,
47. https://doi.org/10.1128/msystems.00513-24,
48. https://doi.org/10.1186/s13068-023-02404-1,
49. https://doi.org/10.1186/s12934-021-01627-x,