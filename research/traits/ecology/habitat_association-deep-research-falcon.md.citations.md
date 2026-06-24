# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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
**Generated:** 2026-06-17T20:46:47.223177

1. ramoneda2024leveraginggenomicinformation pages 1-2
2. chase2023biogeographicpatternsof pages 1-2
3. ren2024microbialstrategiesof pages 11-15
4. ning2024environmentalstressmediates pages 1-4
5. feng2024functionaltraitsand pages 1-2
6. sun2024assemblyprocessand pages 6-9
7. wang2024adaptionmechanismand pages 1-2
8. martiny2006microbialbiogeographyputting pages 1-2
9. she2024definingthebiogeographical pages 4-7
10. feng2024functionaltraitsand pages 2-4
11. kumar2024acomprehensiveoverview pages 7-8
12. she2024definingthebiogeographical pages 8-9
13. she2024definingthebiogeographical pages 1-2
14. baker2024theoralmicrobiome pages 1-4
15. manriquedelacuba2024evidenceofhabitat pages 1-2
16. hao2024cooperationshapesbacterial pages 21-24
17. martiny2006microbialbiogeographyputting pages 8-9
18. martiny2006microbialbiogeographyputting pages 5-6
19. martiny2006microbialbiogeographyputting pages 3-4
20. martiny2006microbialbiogeographyputting pages 2-3
21. hao2024cooperationshapesbacterial pages 24-28
22. hao2024cooperationshapesbacterial pages 6-10
23. martiny2006microbialbiogeographyputting pages 6-7
24. ren2024microbialstrategiesof pages 15-20
25. she2024definingthebiogeographical pages 2-4
26. hao2024cooperationshapesbacterial pages 4-6
27. ren2024microbialstrategiesof pages 1-7
28. ren2024microbialstrategiesof pages 7-11
29. es
30. https://doi.org/10.1038/nrmicro1341
31. https://doi.org/10.1038/s41396-023-01410-3
32. https://doi.org/10.1038/s41564-023-01573-x
33. https://doi.org/10.1093/ismejo/wrae195
34. https://doi.org/10.1038/s41467-024-44720-6
35. https://doi.org/10.1038/s41579-023-00963-6
36. https://doi.org/10.1186/s40168-024-01979-7
37. https://doi.org/10.1038/s41522-024-00615-4
38. https://doi.org/10.1186/s40793-024-00648-4
39. https://doi.org/10.1128/spectrum.01051-24
40. https://doi.org/10.3389/fmicb.2024.1343572
41. https://doi.org/10.1101/2024.09.17.613589
42. https://doi.org/10.1101/2024.10.05.616009
43. https://doi.org/10.1038/nrmicro1341,
44. https://doi.org/10.1186/s40168-024-01979-7,
45. https://doi.org/10.1038/s41467-024-44720-6,
46. https://doi.org/10.1186/s40793-024-00648-4,
47. https://doi.org/10.1093/ismejo/wrae195,
48. https://doi.org/10.1101/2024.10.05.616009,
49. https://doi.org/10.1128/spectrum.01051-24,
50. https://doi.org/10.1038/s41564-023-01573-x,
51. https://doi.org/10.1038/s41396-023-01410-3,
52. https://doi.org/10.1101/2024.09.17.613589,
53. https://doi.org/10.1038/s41522-024-00615-4,
54. https://doi.org/10.3389/fmicb.2024.1343572,
55. https://doi.org/10.1038/s41579-023-00963-6,