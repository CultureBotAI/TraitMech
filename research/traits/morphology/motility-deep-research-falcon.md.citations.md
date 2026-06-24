# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motility
- **METPO identifier:** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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
**Generated:** 2026-06-18T08:57:25.665713

1. jin2024microbesinporous pages 9-14
2. warrell2024interspeciessurfactantsserve pages 15-17
3. warrell2024interspeciessurfactantsserve pages 1-2
4. ohara2024surfacehydrophilicitypromotes pages 1-2
5. shibata2023filamentousstructuresin pages 1-2
6. carbo2024alytictransglycosylase pages 1-2
7. gaines2024towardsamolecular pages 1-2
8. charlesorszag2024adhesionpilusretraction pages 1-2
9. zhan2024acdigmpsignaling pages 1-2
10. li2024theeffectof pages 1-2
11. sofer2024perturbednglycosylationof pages 1-2
12. geiger2024abacterialsense pages 1-3
13. charlesorszag2024adhesionpilusretraction pages 4-6
14. zhan2024acdigmpsignaling pages 9-10
15. warrell2024interspeciessurfactantsserve pages 22-22
16. wang2024argrregulatesmotility pages 1-2
17. shibata2023filamentousstructuresin pages 5-6
18. charlesorszag2024adhesionpilusretraction pages 3-4
19. li2024theeffectof pages 2-3
20. es
21. https://doi.org/10.1128/jb.00281-24
22. https://doi.org/10.1128/msphere.00390-24
23. https://doi.org/10.1128/jb.00359-24
24. https://doi.org/10.1128/jb.00442-23
25. https://doi.org/10.1038/s41467-024-46149-3
26. https://doi.org/10.1038/s42003-024-07392-y
27. https://doi.org/10.3389/fmicb.2024.1340429
28. https://doi.org/10.1038/s42003-023-04472-3
29. https://doi.org/10.7554/elife.99273.1
30. https://doi.org/10.1038/s41467-024-50277-1
31. https://doi.org/10.3389/fmicb.2024.1474570
32. https://doi.org/10.1038/s41467-024-49101-7
33. https://doi.org/10.1038/s41467-024-53986-9
34. https://doi.org/10.1128/jb.00281-24,
35. https://doi.org/10.1128/msphere.00390-24,
36. https://doi.org/10.1007/s12551-024-01185-7,
37. https://doi.org/10.1038/s42003-023-04472-3,
38. https://doi.org/10.7554/elife.99273.1,
39. https://doi.org/10.1038/s41467-024-53986-9,
40. https://doi.org/10.1038/s41467-024-49101-7,
41. https://doi.org/10.1038/s41467-024-46149-3,
42. https://doi.org/10.3389/fmicb.2024.1340429,
43. https://doi.org/10.1128/jb.00442-23,
44. https://doi.org/10.1128/jb.00359-24,
45. https://doi.org/10.1038/s41467-024-50277-1,
46. https://doi.org/10.3389/fmicb.2024.1474570,
47. https://doi.org/10.1038/s42003-024-07392-y,