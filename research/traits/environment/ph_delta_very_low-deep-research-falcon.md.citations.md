# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000473
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a very narrow growth-supporting pH breadth of at most approximately 1 pH unit, characteristic of stenotopic pH-sensitive physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_<=1
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very narrow pH-tolerance breadths as the stenotopic / pH-sensitive phenotype.)
- **Existing causal graph summary:** ph_delta_very_low_stenotopic: 13 nodes, 7 edges

## Research Objective

Research the microbial trait **pH delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_very_low.yaml`.

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
**Generated:** 2026-08-04T02:38:00.840507

1. krulwich2011molecularaspectsof pages 1-3
2. schumacher2023ribosomeprofilingreveals pages 2-5
3. mueller2019plasticityofescherichia pages 5-6
4. tran2024activephregulation pages 5-7
5. krulwich2011molecularaspectsof pages 5-6
6. krulwich2011molecularaspectsof pages 12-14
7. carere2021growthonformic pages 4-5
8. acciarri2023redundantpotassiumtransporter pages 6-8
9. rebelo2023unravelingtherole pages 18-20
10. li2023comammoxnitrospiraand pages 9-11
11. chong2024archaeamembranesin pages 4-6
12. krulwich2011molecularaspectsof pages 3-5
13. lund2020understandinghowmicroorganisms pages 1-2
14. lund2020understandinghowmicroorganisms pages 2-3
15. mueller2019plasticityofescherichia pages 3-5
16. acciarri2023redundantpotassiumtransporter pages 5-6
17. carere2021growthonformic pages 3-4
18. tran2024activephregulation pages 2-5
19. chong2024archaeamembranesin pages 3-4
20. jiang2024exogenousputrescineplays pages 9-12
21. jiang2024exogenousputrescineplays pages 4-6
22. chiu2023membranelipidand pages 9-10
23. lund2020understandinghowmicroorganisms pages 3-5
24. chiu2023membranelipidand pages 3-5
25. https://doi.org/10.1128/AEM.00110-18
26. https://doi.org/10.7554/eLife.40754
27. https://doi.org/10.3389/fmicb.2023.1117684
28. https://doi.org/10.3389/fmicb.2021.651744
29. https://doi.org/10.1128/mbio.03387-23
30. https://doi.org/10.3389/frbis.2023.1338019
31. https://doi.org/10.1128/AEM.00569-24
32. https://doi.org/10.1038/nrmicro2549.
33. https://doi.org/10.1128/AEM.00110-18.
34. https://doi.org/10.7554/eLife.40754.
35. https://doi.org/10.3389/fmicb.2020.556140.
36. https://doi.org/10.3389/fmicb.2021.651744.
37. https://doi.org/10.3389/fmicb.2023.1117684.
38. https://doi.org/10.1128/AEM.00047-23.
39. https://doi.org/10.3389/fmicb.2023.1219779.
40. https://doi.org/10.3390/antibiotics12091474.
41. https://doi.org/10.1128/msystems.01037-23.
42. https://doi.org/10.3389/frbis.2023.1338019.
43. https://doi.org/10.1128/mbio.03387-23.
44. https://doi.org/10.1128/AEM.00569-24.
45. https://doi.org/10.1038/nrmicro2549,
46. https://doi.org/10.3390/antibiotics12091474,
47. https://doi.org/10.1128/msystems.01037-23,
48. https://doi.org/10.3389/fmicb.2020.556140,
49. https://doi.org/10.1128/aem.00110-18,
50. https://doi.org/10.7554/elife.40754,
51. https://doi.org/10.3389/fmicb.2023.1117684,
52. https://doi.org/10.3389/fmicb.2021.651744,
53. https://doi.org/10.1128/mbio.03387-23,
54. https://doi.org/10.3389/frbis.2023.1338019,
55. https://doi.org/10.1128/aem.00569-24,
56. https://doi.org/10.3389/fmicb.2023.1219779,
57. https://doi.org/10.1128/aem.00047-23,