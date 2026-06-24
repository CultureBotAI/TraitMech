# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** viable but nonculturable state
- **METPO identifier:** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **viable but nonculturable state** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/viable_but_nonculturable_state.yaml`.

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
**Generated:** 2026-06-18T12:52:49.464130

1. pazosrojas2023theviablebut pages 10-11
2. gou2024viablebutnonculturable pages 1-2
3. pazosrojas2023theviablebut pages 1-2
4. prosdocimi2023cellphenotypechanges pages 1-2
5. polivtseva2024identificationcharacterizationand pages 2-4
6. zhang2023currentperspectiveson pages 4-5
7. izgordu2024understandingthetransition pages 1-2
8. pazosrojas2023theviablebut pages 11-13
9. yang2024resuscitationofviable pages 6-9
10. yang2024resuscitationofviable pages 9-10
11. li2024resuscitationpromotionfactor pages 1-3
12. li2024quantitativedetectionand pages 15-17
13. li2024quantitativedetectionand pages 11-13
14. li2024quantitativedetectionand pages 1-2
15. gou2024viablebutnonculturable pages 8-9
16. yang2024resuscitationofviable pages 1-2
17. yang2024resuscitationofviable pages 2-4
18. cantlay2024phenotypicandtranscriptional pages 2-3
19. li2024quantitativedetectionand pages 7-9
20. li2024quantitativedetectionand pages 4-7
21. gou2024viablebutnonculturable pages 2-3
22. polivtseva2024identificationcharacterizationand pages 15-16
23. pazosrojas2023theviablebut pages 14-15
24. pazosrojas2023theviablebut pages 21-21
25. https://doi.org/10.1186/s13213-022-01703-6
26. https://doi.org/10.3390/microorganisms12122662
27. https://doi.org/10.3390/foods12061179
28. https://doi.org/10.3390/microorganisms12010039
29. https://doi.org/10.1016/j.jare.2023.08.002
30. https://doi.org/10.3390/microorganisms12081528
31. https://doi.org/10.1128/spectrum.00249-24
32. https://doi.org/10.3389/fcimb.2024.1486426
33. https://doi.org/10.3389/fmicb.2024.1347488
34. https://doi.org/10.1007/s11274-024-04019-6
35. https://doi.org/10.1007/s11274-024-04019-6,
36. https://doi.org/10.1186/s13213-022-01703-6,
37. https://doi.org/10.3390/microorganisms12010039,
38. https://doi.org/10.3389/fcimb.2024.1486426,
39. https://doi.org/10.3390/microorganisms12122662,
40. https://doi.org/10.3390/foods12061179,
41. https://doi.org/10.1016/j.jare.2023.08.002,
42. https://doi.org/10.3390/microorganisms12081528,
43. https://doi.org/10.1128/spectrum.00249-24,
44. https://doi.org/10.3389/fmicb.2024.1347488,