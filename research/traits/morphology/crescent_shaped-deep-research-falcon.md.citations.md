# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** crescent shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000669
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved crescent-like morphology with a concave inner side and a convex outer side.
- **Parent traits:** METPO:1000666
- **Synonyms:** crescent-shaped
- **Existing evidence:** DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal determinant of curved Caulobacter cell shape.)
- **Existing causal graph summary:** crescent_shaped_crescentin_curvature: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **crescent shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/crescent_shaped.yaml`.

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
**Generated:** 2026-08-04T08:11:24.954571

1. cabeen2009bacterialcellcurvature pages 6-7
2. nikolai2020rnamediatedcontrolof pages 4-6
3. nikolai2020rnamediatedcontrolof pages 1-2
4. banks2022asymmetricpeptidoglycanediting pages 1-2
5. banks2022asymmetricpeptidoglycanediting pages 4-6
6. barrows2023synchronizedswarmersand pages 11-13
7. cabeen2009bacterialcellcurvature pages 1-2
8. cabeen2010mutationsinthe pages 1-2
9. fernandez2020vibriocholeraeadapts pages 1-1
10. pohl2024anoutermembrane pages 1-2
11. pohl2024anoutermembrane pages 13-14
12. cabeen2010mutationsinthe pages 5-7
13. liu2024filamentstructureand pages 6-8
14. sundararajan2017cytoskeletalproteinsin pages 16-17
15. liu2024filamentstructureand pages 10-11
16. fernandez2020vibriocholeraeadapts pages 5-6
17. pohl2024anoutermembrane pages 4-5
18. pohl2024anoutermembrane pages 7-8
19. 10.1128/jb.00384-22
20. 10.1038/emboj.2009.61
21. 10.1073/pnas.2309984121
22. 10.1038/s41467-024-51790-z
23. 10.1038/s41467-022-29007-y
24. 10.1038/s41467-020-19890-8
25. 10.1073/pnas.2010199117
26. 10.1128/JB.01371-09
27. 10.1016/S0092-8674(03)00935-8
28. https://doi.org/10.1128/jb.00384-22
29. https://doi.org/10.1038/emboj.2009.61
30. https://doi.org/10.1073/pnas.2309984121
31. https://doi.org/10.1038/s41467-024-51790-z
32. https://doi.org/10.1038/s41467-022-29007-y
33. https://doi.org/10.1038/s41467-020-19890-8
34. https://doi.org/10.1073/pnas.2010199117
35. https://doi.org/10.1128/JB.01371-09
36. https://doi.org/10.1016/S0092-8674(03
37. https://doi.org/10.1073/pnas.2309984121,
38. https://doi.org/10.1038/s41467-024-51790-z,
39. https://doi.org/10.1007/978-3-319-53047-5\_4,
40. https://doi.org/10.1038/emboj.2009.61,
41. https://doi.org/10.1128/jb.00384-22,
42. https://doi.org/10.1128/jb.01371-09,
43. https://doi.org/10.1038/s41467-020-19890-8,
44. https://doi.org/10.1073/pnas.2010199117,
45. https://doi.org/10.1038/s41467-022-29007-y,