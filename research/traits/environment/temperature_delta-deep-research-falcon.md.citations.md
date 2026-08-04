# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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
**Generated:** 2026-08-04T03:38:30.558953

1. noll2020modelingandexploiting pages 6-8
2. siliakus2017adaptationsofarchaeal pages 8-10
3. mendoza2014temperaturesensingby pages 5-6
4. rudolph2010evolutionofescherichia pages 1-2
5. murata2011molecularstrategyfor pages 4-5
6. murata2011molecularstrategyfor pages 1-2
7. hurtadobautista2024thermalplasticityand pages 16-17
8. weber2003bacterialcoldshock pages 36-38
9. figaj2025theroleof pages 8-10
10. hurtadobautista2024thermalplasticityand pages 1-2
11. siliakus2017adaptationsofarchaeal pages 14-15
12. \Delta T_{growth}=T_{max,growth}-T_{min,growth}
\
13. 10.1146/annurev-micro-091313-103612
14. 10.1007/s00792-017-0939-x
15. 10.1074/jbc.M110.103374
16. 10.1371/journal.pone.0020063
17. 10.3390/biology13121088
18. 10.3184/003685003783238707
19. 10.1038/s41467-024-53046-2
20. 10.3390/ijms26020528
21. 10.3390/pr8010121
22. https://doi.org/10.3390/biology13121088
23. https://doi.org/10.1038/s41467-024-53046-2
24. https://doi.org/10.1128/mbio.03105-23
25. https://doi.org/10.1007/s00792-017-0939-x
26. https://doi.org/10.1146/annurev-micro-091313-103612
27. https://doi.org/10.1371/journal.pone.0020063
28. https://doi.org/10.1074/jbc.M110.103374
29. https://doi.org/10.3390/pr8010121
30. https://doi.org/10.3184/003685003783238707
31. https://doi.org/10.3390/ijms26020528
32. https://doi.org/10.3390/biology13121088](https://doi.org/10.3390/biology13121088
33. https://doi.org/10.1038/s41467-024-53046-2](https://doi.org/10.1038/s41467-024-53046-2
34. https://doi.org/10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23
35. https://doi.org/10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x
36. https://doi.org/10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612
37. https://doi.org/10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063
38. https://doi.org/10.1074/jbc.M110.103374](https://doi.org/10.1074/jbc.M110.103374
39. https://doi.org/10.3390/pr8010121](https://doi.org/10.3390/pr8010121
40. https://doi.org/10.3184/003685003783238707](https://doi.org/10.3184/003685003783238707
41. https://doi.org/10.3390/ijms26020528](https://doi.org/10.3390/ijms26020528
42. https://doi.org/10.3390/pr8010121,
43. https://doi.org/10.1007/s00792-017-0939-x,
44. https://doi.org/10.1146/annurev-micro-091313-103612,
45. https://doi.org/10.1074/jbc.m110.103374,
46. https://doi.org/10.1371/journal.pone.0020063,
47. https://doi.org/10.3390/biology13121088,
48. https://doi.org/10.3184/003685003783238707,
49. https://doi.org/10.3390/ijms26020528,