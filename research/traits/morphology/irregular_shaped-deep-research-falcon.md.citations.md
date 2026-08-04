# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** irregular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 10 nodes, 9 edges

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
**Generated:** 2026-08-04T09:04:28.313022

1. joyce2012celldivisionsite pages 1-2
2. shi2018howtobuild pages 2-3
3. shi2018howtobuild pages 6-7
4. mao2023ontherole pages 1-2
5. errington2017cellwalldeficientlform pages 1-2
6. errington2017cellwalldeficientlform pages 4-5
7. frirdich2023multiplecampylobacterjejuni pages 1-2
8. govers2023apparentsimplicityand pages 1-4
9. caccamo2018themolecularbasis pages 11-12
10. woldemeskel2017shapeshiftingtosurvive pages 2-5
11. kysela2016diversitytakesshape pages 4-5
12. caccamo2018themolecularbasis pages 1-2
13. frirdich2023multiplecampylobacterjejuni pages 5-6
14. caccamo2018themolecularbasis pages 6-7
15. cell-wall
16. GO candidate label
17. CHEBI candidate label
18. gene/protein label; actin homolog
19. gene/protein label
20. mutant allele label
21. 10.3389/fmicb.2022.1085918
22. 10.7554/eLife.84505
23. 10.3389/fmicb.2023.1162806
24. 10.1101/2023.01.16.524295
25. 10.1016/j.cell.2018.02.050
26. 10.1016/j.tim.2017.09.012
27. 10.1016/j.tim.2017.03.006
28. 10.1042/BST20160435
29. 10.1371/journal.pbio.1002565
30. 10.1371/journal.pone.0044582
31. https://doi.org/10.3389/fmicb.2022.1085918
32. https://doi.org/10.7554/eLife.84505
33. https://doi.org/10.3389/fmicb.2023.1162806
34. https://doi.org/10.1101/2023.01.16.524295
35. https://doi.org/10.1016/j.cell.2018.02.050
36. https://doi.org/10.1016/j.tim.2017.09.012
37. https://doi.org/10.1016/j.tim.2017.03.006
38. https://doi.org/10.1042/BST20160435
39. https://doi.org/10.1371/journal.pbio.1002565
40. https://doi.org/10.1371/journal.pone.0044582
41. https://doi.org/10.1016/j.tim.2017.09.012,
42. https://doi.org/10.1371/journal.pbio.1002565,
43. https://doi.org/10.1016/j.cell.2018.02.050,
44. https://doi.org/10.1042/bst20160435,
45. https://doi.org/10.1371/journal.pone.0044582,
46. https://doi.org/10.7554/elife.84505,
47. https://doi.org/10.3389/fmicb.2022.1085918,
48. https://doi.org/10.3389/fmicb.2023.1162806,
49. https://doi.org/10.1016/j.tim.2017.03.006,
50. https://doi.org/10.1101/2023.01.16.524295,