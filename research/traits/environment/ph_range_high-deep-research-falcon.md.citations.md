# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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
**Generated:** 2026-08-04T02:59:01.204230

1. maksimova2024metabolicandmorphological pages 1-2
2. mitchell2024penicillinbindingproteinredundancy pages 1-2
3. mitchell2024penicillinbindingproteinredundancy pages 10-12
4. krulwich2011molecularaspectsof pages 27-28
5. goto2022differencesinbioenergetic pages 1-2
6. jong2024quantitativeproteomicsreveals pages 6-8
7. preiss2015alkaliphilicbacteriawith pages 2-3
8. sorokin2014microbialdiversityand pages 3-5
9. maksimova2024metabolicandmorphological pages 5-6
10. krulwich2011molecularaspectsof pages 12-14
11. krulwich2011molecularaspectsof pages 1-3
12. preiss2015alkaliphilicbacteriawith pages 5-7
13. krulwich2011molecularaspectsof pages 5-6
14. krulwich2011molecularaspectsof pages 22-23
15. krulwich2011molecularaspectsof pages 20-22
16. preiss2015alkaliphilicbacteriawith pages 12-13
17. jong2024quantitativeproteomicsreveals pages 1-2
18. mitchell2024penicillinbindingproteinredundancy pages 4-6
19. maksimova2024metabolicandmorphological pages 9-10
20. terradot2024escherichiacolimaintains pages 1-2
21. terradot2024escherichiacolimaintains pages 8-9
22. 10.1038/nrmicro2549
23. 10.3389/fbioe.2015.00075
24. 10.3389/fmicb.2022.842785
25. 10.3389/fmicb.2024.1468929
26. 10.1128/aem.00548-23
27. 10.1155/2024/3087296
28. https://doi.org/10.1038/nrmicro2549
29. https://doi.org/10.3389/fbioe.2015.00075
30. https://doi.org/10.3389/fmicb.2022.842785
31. https://doi.org/10.3389/fmicb.2024.1468929
32. https://doi.org/10.1128/aem.00548-23
33. https://doi.org/10.1155/2024/3087296
34. https://doi.org/10.1038/nrmicro2549.
35. https://doi.org/10.3389/fbioe.2015.00075.
36. https://doi.org/10.3389/fmicb.2022.842785.
37. https://doi.org/10.1128/aem.00548-23.
38. https://doi.org/10.1155/2024/3087296.
39. https://doi.org/10.3389/fmicb.2024.1468929.
40. https://doi.org/10.1103/PRXLife.2.043015.
41. https://doi.org/10.1128/aem.00110-18.
42. https://doi.org/10.1007/s00792-014-0670-9.
43. https://doi.org/10.1038/nrmicro2549,
44. https://doi.org/10.3389/fbioe.2015.00075,
45. https://doi.org/10.1155/2024/3087296,
46. https://doi.org/10.1128/aem.00548-23,
47. https://doi.org/10.3389/fmicb.2022.842785,
48. https://doi.org/10.3389/fmicb.2024.1468929,
49. https://doi.org/10.1103/prxlife.2.043015,
50. https://doi.org/10.1007/s00792-014-0670-9,
51. https://doi.org/10.1128/aem.00110-18,