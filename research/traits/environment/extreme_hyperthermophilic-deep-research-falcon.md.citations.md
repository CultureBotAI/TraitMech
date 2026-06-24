# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** extreme hyperthermophilic
- **METPO identifier:** METPO:1000721
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference that grows optimally at temperatures above 90°C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme hyperthermophile, extremely hyperthermophilic
- **Existing evidence:** DOI:10.1007/s007920050010: It grew at between 90 degrees C and 113 degrees C (Organism example: Pyrolobus fumarii grows in the extreme hyperthermophilic range.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports extreme protein and membrane stability as the basis of hyperthermophile physiology.)
- **Existing causal graph summary:** extreme_hyperthermophilic_archaeal_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **extreme hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/extreme_hyperthermophilic.yaml`.

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
**Generated:** 2026-06-17T22:03:55.764077

1. irwin2004extremophilesandtheir pages 1-2
2. atomi2004reversegyraseis pages 3-5
3. lipscomb2017reversegyraseis pages 1-2
4. takemata2024howdothermophiles pages 1-2
5. rao2024unravelingthemultiplicity pages 2-4
6. rao2024unravelingthemultiplicity pages 1-2
7. acevedolopez2024roleofpolyphosphate pages 1-2
8. mondal2024aquificaeovercomescompetition pages 1-2
9. ali2023extremophilesandlimits pages 3-4
10. ali2023extremophilesandlimits pages 1-3
11. dumina2023thermolasparaginasesfromthe pages 2-4
12. irwin2004extremophilesandtheir pages 2-3
13. lipscomb2017reversegyraseis pages 2-4
14. mondal2024aquificaeovercomescompetition pages 35-36
15. kampmann2004reversegyrasehas pages 1-2
16. irwin2004extremophilesandtheir pages 3-5
17. irwin2004extremophilesandtheir pages 5-6
18. https://doi.org/10.1186/2046-0481-57-6-348
19. https://doi.org/10.1007/s007920050010;
20. https://doi.org/10.1264/jsme2.me23087
21. https://doi.org/10.3390/ijms18071340
22. https://doi.org/10.1007/s00792-017-0929-z
23. https://doi.org/10.1007/s00792-023-01330-2
24. https://doi.org/10.1371/journal.pone.0310595
25. https://doi.org/10.3390/microorganisms12122627
26. https://doi.org/10.1264/jsme2.me23087;
27. https://doi.org/10.1093/nar/gkh683
28. https://doi.org/10.1128/jb.186.14.4829-4833.2004
29. https://doi.org/10.3390/molecules28083446
30. https://doi.org/10.3389/fmicb.2024.1443342
31. https://doi.org/10.5772/intechopen.110471
32. https://doi.org/10.3390/ijms24032674
33. https://doi.org/10.1186/2046-0481-57-6-348,
34. https://doi.org/10.1128/jb.186.14.4829-4833.2004,
35. https://doi.org/10.1007/s00792-017-0929-z,
36. https://doi.org/10.1264/jsme2.me23087,
37. https://doi.org/10.1007/s00792-023-01330-2,
38. https://doi.org/10.3390/microorganisms12122627,
39. https://doi.org/10.1371/journal.pone.0310595,
40. https://doi.org/10.5772/intechopen.110471,
41. https://doi.org/10.3390/ijms24032674,
42. https://doi.org/10.3389/fmicb.2024.1443342,
43. https://doi.org/10.1093/nar/gkh683,