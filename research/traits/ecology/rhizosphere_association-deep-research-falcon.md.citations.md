# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** rhizosphere association
- **METPO identifier:** traitmech:000051
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives in the rhizosphere — the soil zone influenced by plant roots and root exudates — a hotspot of microbial activity and plant-microbe interaction.
- **Parent traits:** traitmech:000047
- **Synonyms:** rhizosphere-associated
- **Existing evidence:** DOI:10.1038/nrmicro3109:  (Philippot et al., "Going back to the roots", define the rhizosphere as a distinct, root-influenced microbial habitat.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports the rhizosphere as a high-activity subset of the broader soil microbiome.)
- **Existing causal graph summary:** rhizosphere_root_exudate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **rhizosphere association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/rhizosphere_association.yaml`.

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
**Generated:** 2026-06-17T21:02:24.567981

1. kulkarni2024volatilemethyljasmonate pages 1-2
2. liu2024rootcolonizationby pages 1-2
3. yang2024mechanismsofrhizosphere pages 1-3
4. ji2023rhizobialmigrationtoward pages 1-2
5. velickovic2024rhizomapacomprehensive pages 1-2
6. moller2024targetingtheuntargeted pages 1-4
7. liu2024rootcolonizationby pages 2-3
8. park2023recruitmentofthe pages 1-2
9. ali2024rootexudatemetabolites pages 6-8
10. philippot2013goingbackto pages 2-3
11. ali2024rootexudatemetabolites pages 4-5
12. liu2024rootcolonizationby pages 3-4
13. yang2024mechanismsofrhizosphere pages 4-5
14. chen2024thefunctionof pages 3-4
15. arredondo2024differentialexudationcreates pages 1-6
16. ji2023rhizobialmigrationtoward pages 10-11
17. ji2023rhizobialmigrationtoward pages 8-10
18. ragland2024choreographingrootarchitecture pages 4-5
19. park2023recruitmentofthe pages 12-13
20. philippot2013goingbackto pages 1-2
21. arredondo2024differentialexudationcreates pages 10-14
22. ragland2024choreographingrootarchitecture pages 1-2
23. ragland2024choreographingrootarchitecture pages 5-6
24. chen2024thefunctionof pages 10-12
25. kulkarni2024volatilemethyljasmonate pages 2-3
26. park2023recruitmentofthe pages 10-12
27. candidate: root exudate; ENVO uncertain
28. METPO:traitmech:000051
29. ENVO:00005801
30. ENVO:00005774
31. label
32. GO:0006935
33. GO:0001539
34. GO:0009288
35. CHEBI:17234
36. CHEBI:17992
37. CHEBI:17268
38. GO:0042710
39. CHEBI:63517
40. N-acyl-L-homoserine lactone; CURIE uncertain
41. CHEBI class uncertain
42. PATO/label
43. CHEBI:30769
44. https://doi.org/10.1093/femsre/fuad066
45. https://doi.org/10.1038/s41589-023-01462-8
46. https://doi.org/10.3390/biology13020095
47. https://doi.org/10.3389/fpls.2024.1491495
48. https://doi.org/10.1038/s41396-023-01357-5
49. https://doi.org/10.1021/acs.est.4c04108
50. https://doi.org/10.1038/s41467-024-45272-5
51. https://doi.org/10.3389/fmicb.2023.1163832
52. https://doi.org/10.1186/s13007-024-01249-5
53. https://doi.org/10.1101/2024.09.17.613458
54. https://doi.org/10.3390/crops4010004
55. https://doi.org/10.1038/nrmicro3109
56. https://doi.org/10.1038/s41589-023-01462-8,
57. https://doi.org/10.1038/nrmicro3109,
58. https://doi.org/10.1093/femsre/fuad066,
59. https://doi.org/10.3389/fpls.2024.1491495,
60. https://doi.org/10.3390/biology13020095,
61. https://doi.org/10.1021/acs.est.4c04108,
62. https://doi.org/10.1038/s41396-023-01357-5,
63. https://doi.org/10.1186/s13007-024-01249-5,
64. https://doi.org/10.1101/2024.09.17.613458,
65. https://doi.org/10.1038/s41467-024-45272-5,
66. https://doi.org/10.3389/fmicb.2023.1163832,
67. https://doi.org/10.3390/crops4010004,