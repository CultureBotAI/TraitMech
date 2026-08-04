# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell shape
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000666
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.cell shape, cell_shape
- **Existing evidence:** DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role in maintaining cell shape (Supports bacterial cell shape as determined by cell wall and cytoskeletal elements.)
- **Existing causal graph summary:** cell_shape_peptidoglycan_cytoskeleton: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **cell shape** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_shape.yaml`.

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
**Generated:** 2026-08-04T07:51:08.619023

1. goudin2023recoveryofvibrio pages 1-2
2. shlosman2023allostericactivationof pages 1-2
3. hussain2018mrebfilamentsalign pages 1-2
4. castanheira2023evidenceoftwo pages 1-2
5. dersch2024adaptationofbacillus pages 1-2
6. pohl2024anoutermembrane pages 1-2
7. cabeen2011thedomainorganization pages 1-2
8. richter2023interactingbactofilinsimpact pages 1-2
9. sen2024adispensablesepiva pages 1-2
10. schiller2024identificationofstructural pages 1-2
11. brown2024mindproteinsregulate pages 1-2
12. teeseling2017determinantsofbacterial pages 3-4
13. kysela2016diversitytakesshape pages 4-5
14. dersch2024adaptationofbacillus pages 15-17
15. richter2023interactingbactofilinsimpact pages 2-4
16. is
17. 10.1038/s41467-023-39037-9
18. 10.1038/s42003-023-05308-w
19. 10.3390/microorganisms12071309
20. 10.1038/s41467-024-51790-z
21. 10.1038/s41467-024-45196-0
22. 10.3389/fmicb.2024.1474697
23. 10.1371/journal.pgen.1010788
24. 10.1371/journal.pone.0293276
25. 10.1186/s12866-024-03625-6
26. 10.7554/eLife.32471
27. 10.3389/fmicb.2017.01264
28. 10.1371/journal.pbio.1002565
29. 10.1002/cm.20505
30. https://doi.org/10.1038/s41467-023-39037-9
31. https://doi.org/10.1038/s42003-023-05308-w
32. https://doi.org/10.3390/microorganisms12071309
33. https://doi.org/10.1038/s41467-024-51790-z
34. https://doi.org/10.1038/s41467-024-45196-0
35. https://doi.org/10.3389/fmicb.2024.1474697
36. https://doi.org/10.1371/journal.pgen.1010788
37. https://doi.org/10.1371/journal.pone.0293276
38. https://doi.org/10.1186/s12866-024-03625-6
39. https://doi.org/10.7554/eLife.32471
40. https://doi.org/10.3389/fmicb.2017.01264
41. https://doi.org/10.1371/journal.pbio.1002565
42. https://doi.org/10.1002/cm.20505
43. https://doi.org/10.3389/fmicb.2017.01264,
44. https://doi.org/10.1371/journal.pbio.1002565,
45. https://doi.org/10.1038/s41467-023-39037-9,
46. https://doi.org/10.3389/fmicb.2024.1474697,
47. https://doi.org/10.1038/s41467-024-45196-0,
48. https://doi.org/10.1371/journal.pone.0293276,
49. https://doi.org/10.7554/elife.32471,
50. https://doi.org/10.1371/journal.pgen.1010788,
51. https://doi.org/10.1186/s12866-024-03625-6,
52. https://doi.org/10.1038/s41467-024-51790-z,
53. https://doi.org/10.1038/s42003-023-05308-w,
54. https://doi.org/10.3390/microorganisms12071309,
55. https://doi.org/10.1002/cm.20505,