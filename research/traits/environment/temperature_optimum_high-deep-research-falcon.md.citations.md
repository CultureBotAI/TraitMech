# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 16 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_high.yaml`.

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
**Generated:** 2026-08-04T03:55:43.483338

1. pandey2026extremethermalenvironments pages 5-6
2. murata2011molecularstrategyfor pages 1-2
3. atomi2004reversegyraseis pages 3-5
4. kampmann2004reversegyrasehas pages 1-2
5. villain2021thehyperthermophilicarchaeon pages 11-12
6. esteves2014mannosylglycerateanddi pages 9-12
7. esteves2014mannosylglycerateanddi pages 16-20
8. cario2016molecularchaperoneaccumulation pages 3-4
9. rastadter2020thecellmembrane pages 5-7
10. blum2023distributionandabundance pages 2-2
11. blum2023distributionandabundance pages 6-7
12. ren2024couplingthermotoleranceand pages 1-2
13. chiu2023membranelipidand pages 2-3
14. lipscomb2017reversegyraseis pages 1-2
15. lipscomb2017reversegyraseis pages 2-4
16. lipscomb2017reversegyraseis pages 4-5
17. esteves2014mannosylglycerateanddi pages 20-28
18. 10.1007/s00792-017-0929-z
19. 10.1128/JB.186.14.4829-4833.2004
20. 10.1093/nar/gkh683
21. 10.1093/nar/gkab869
22. 10.1128/AEM.00559-14
23. 10.1038/srep29483
24. 10.3389/fmicb.2023.1219779
25. 10.3390/ijms21113935
26. 10.1111/1462-2920.16375
27. 10.1371/journal.pone.0020063
28. 10.1038/s42003-024-06341-z
29. indirect/uncertain
30. redundant, taxon-specific
31. https://doi.org/10.1007/s00792-017-0929-z
32. https://doi.org/10.1128/JB.186.14.4829-4833.2004
33. https://doi.org/10.1093/nar/gkh683
34. https://doi.org/10.1093/nar/gkab869
35. https://doi.org/10.1128/AEM.00559-14
36. https://doi.org/10.1038/srep29483
37. https://doi.org/10.3389/fmicb.2023.1219779
38. https://doi.org/10.3390/ijms21113935
39. https://doi.org/10.1111/1462-2920.16375
40. https://doi.org/10.1371/journal.pone.0020063
41. https://doi.org/10.1038/s42003-024-06341-z
42. https://doi.org/10.3389/fmicb.2025.1739143,
43. https://doi.org/10.1371/journal.pone.0020063,
44. https://doi.org/10.1007/s00792-017-0929-z,
45. https://doi.org/10.1128/jb.186.14.4829-4833.2004,
46. https://doi.org/10.1093/nar/gkh683,
47. https://doi.org/10.1093/nar/gkab869,
48. https://doi.org/10.1128/aem.00559-14,
49. https://doi.org/10.1038/srep29483,
50. https://doi.org/10.3389/fmicb.2023.1219779,
51. https://doi.org/10.3390/ijms21113935,
52. https://doi.org/10.1111/1462-2920.16375,
53. https://doi.org/10.1038/s42003-024-06341-z,