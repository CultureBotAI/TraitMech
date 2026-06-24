# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** irregular shaped
- **METPO identifier:** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **irregular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/irregular_shaped.yaml`.

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
**Generated:** 2026-06-18T08:38:37.015686

1. claessen2024thestomatinlikeprotein pages 1-5
2. zhang2023coordinatedpeptidoglycansynthases pages 2-3
3. obando2024geneticinteractionmapping pages 15-17
4. claessen2024thestomatinlikeprotein pages 27-28
5. hayashi2024septalwallsynthesis pages 1-2
6. zhang2023coordinatedpeptidoglycansynthases pages 1-2
7. pohl2024adynamicbactofilin pages 1-2
8. hayashi2024septalwallsynthesis pages 2-3
9. zambri2024bacteriacombinepolar pages 13-18
10. zhang2023coordinatedpeptidoglycansynthases pages 4-5
11. claessen2024thestomatinlikeprotein pages 17-20
12. sen2024adispensablesepiva pages 1-2
13. hayashi2024septalwallsynthesis pages 7-8
14. ojima2024buddingandexplosive pages 1-2
15. zhang2023coordinatedpeptidoglycansynthases pages 6-7
16. ojima2024buddingandexplosive pages 4-5
17. ojima2024buddingandexplosive pages 7-10
18. zhang2023coordinatedpeptidoglycansynthases pages 3-4
19. zhang2023coordinatedpeptidoglycansynthases pages 5-6
20. claessen2024thestomatinlikeprotein pages 15-17
21. hayashi2024septalwallsynthesis pages 6-7
22. ojima2024buddingandexplosive pages 5-7
23. ing
24. 10.1038/s42003-024-07279-y
25. 10.3389/fmicb.2024.1400434
26. 10.1038/s41467-023-41082-3
27. 10.1371/journal.pgen.1011234
28. 10.21203/rs.3.rs-3811693/v1
29. 10.1101/2024.11.22.624946
30. 10.1101/2024.07.30.605496
31. 10.1186/s12866-024-03625-6
32. 10.7554/elife.86577.2
33. https://doi.org/10.1101/2024.11.22.624946
34. https://doi.org/10.3389/fmicb.2024.1400434
35. https://doi.org/10.1038/s41467-023-41082-3
36. https://doi.org/10.1371/journal.pgen.1011234
37. https://doi.org/10.21203/rs.3.rs-3811693/v1
38. https://doi.org/10.1038/s42003-024-07279-y
39. https://doi.org/10.1101/2024.07.30.605496
40. https://doi.org/10.1186/s12866-024-03625-6
41. https://doi.org/10.7554/elife.86577.2
42. https://doi.org/10.1101/2024.11.22.624946,
43. https://doi.org/10.1038/s41467-023-41082-3,
44. https://doi.org/10.21203/rs.3.rs-3811693/v1,
45. https://doi.org/10.1038/s42003-024-07279-y,
46. https://doi.org/10.3389/fmicb.2024.1400434,
47. https://doi.org/10.1371/journal.pgen.1011234,
48. https://doi.org/10.7554/elife.86577.2,
49. https://doi.org/10.1101/2024.07.30.605496,
50. https://doi.org/10.1186/s12866-024-03625-6,