# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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
**Generated:** 2026-08-04T07:59:28.040869

1. hussain2017mrebfilamentscreate pages 35-39
2. fivenson2023arolefor pages 7-8
3. morgenstein2015rodzlinksmreb pages 5-6
4. mao2023ontherole pages 2-3
5. shlosman2023allostericactivationof pages 2-3
6. morgenstein2015rodzlinksmreb pages 2-4
7. ago2023relationshipbetweenthe pages 14-16
8. ago2023relationshipbetweenthe pages 10-11
9. shlosman2023allostericactivationof pages 8-9
10. castanheira2023evidenceoftwo pages 7-8
11. castanheira2023evidenceoftwo pages 2-3
12. castanheira2023evidenceoftwo pages 13-14
13. fivenson2023arolefor pages 3-5
14. fivenson2023arolefor pages 2-3
15. mao2023ontherole pages 14-15
16. 10.1002/mbo3.1385
17. 10.1038/s42003-023-05308-w
18. 10.1073/pnas.2301987120
19. 10.7554/eLife.32471
20. Also available as bioRxiv preprint: DOI:10.1101/197475, October 2017
21. 10.7554/eLife.84505
22. 10.1073/pnas.1509610112
23. 10.1038/s41467-023-39037-9
24. 10.1128/mbio.00475-23
25. 10.1128/mbio.03235-23
26. 10.1101/2024.07.30.605496
27. Preprint; not peer-reviewed.
28. https://doi.org/10.1002/mbo3.1385
29. https://doi.org/10.1038/s42003-023-05308-w
30. https://doi.org/10.1073/pnas.2301987120
31. https://doi.org/10.7554/eLife.32471
32. https://doi.org/10.7554/eLife.84505
33. https://doi.org/10.1073/pnas.1509610112
34. https://doi.org/10.1038/s41467-023-39037-9
35. https://doi.org/10.1128/mbio.00475-23
36. https://doi.org/10.1128/mbio.03235-23
37. https://doi.org/10.1101/2024.07.30.605496
38. https://doi.org/10.1101/197475,
39. https://doi.org/10.1073/pnas.1509610112,
40. https://doi.org/10.7554/elife.84505,
41. https://doi.org/10.1002/mbo3.1385,
42. https://doi.org/10.1038/s41467-023-39037-9,
43. https://doi.org/10.1038/s42003-023-05308-w,
44. https://doi.org/10.1073/pnas.2301987120,