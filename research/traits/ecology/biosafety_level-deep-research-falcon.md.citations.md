# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level
- **METPO identifier:** METPO:1001101
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that categorizes biological agents according to their hazard level and required containment measures.
- **Parent traits:** METPO:1000188
- **Synonyms:** Safety information.risk assessment.biosafety level
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports pathogen virulence characteristics (transmissibility, severity, treatability) as the biological inputs underlying biosafety-level classification.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector-mediated host damage as a virulence axis informing hazard assessment.)
- **Existing causal graph summary:** biosafety_level_hazard_classification: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **biosafety level** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level.yaml`.

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
**Generated:** 2026-06-17T19:55:56.386597

1. blacksell2023thebiosafetyresearch pages 1-2
2. gao2024frombiosafetyto pages 9-10
3. abalos2023surveillanceoflaboratory pages 1-2
4. balbontin2024canadianlaboratoryincidents pages 2-3
5. gao2025globalsafetyand pages 14-17
6. fan2025enhancingsafetywith pages 1-2
7. allende2025updateofthe pages 10-11
8. gao2024frombiosafetyto pages 5-6
9. bhavsar2007manipulationofhostcell pages 5-6
10. gao2024frombiosafetyto pages 6-7
11. thompson2022surveillanceoflaboratory pages 1-2
12. callihan2021considerationsforlaboratory pages 1-2
13. angot2007exploitationofeukaryotic pages 1-2
14. kimman2008evidencebasedbiosafetya pages 7-8
15. kimman2008evidencebasedbiosafetya pages 6-7
16. gao2024frombiosafetyto pages 3-5
17. gao2025globalsafetyand pages 6-8
18. coburn2007typeiiisecretion pages 2-3
19. atchessi2021surveillanceoflaboratory pages 1-2
20. coburn2007typeiiisecretion pages 1-2
21. ing
22. https://doi.org/10.3390/laboratories1030013
23. https://doi.org/10.26686/nzjhsp.v1i2.9540
24. https://doi.org/10.1089/apb.2022.0040
25. https://doi.org/10.14745/ccdr.v50i05a04
26. https://doi.org/10.14745/ccdr.v49i09a06
27. https://doi.org/10.14745/ccdr.v48i10a08
28. https://doi.org/10.1089/apb.20.0068
29. https://doi.org/10.3390/laboratories2010003
30. https://doi.org/10.1016/j.heliyon.2024.e40855
31. https://doi.org/10.1128/cmr.00013-07
32. https://doi.org/10.1038/nature06247
33. https://doi.org/10.1371/journal.ppat.0030003
34. https://doi.org/10.1128/cmr.00014-08
35. https://doi.org/10.3390/laboratories1030013,
36. https://doi.org/10.1128/cmr.00014-08,
37. https://doi.org/10.26686/nzjhsp.v1i2.9540,
38. https://doi.org/10.1016/j.jobb.2021.09.002,
39. https://doi.org/10.1089/apb.2022.0040,
40. https://doi.org/10.14745/ccdr.v49i09a06,
41. https://doi.org/10.14745/ccdr.v50i05a04,
42. https://doi.org/10.1089/apb.20.0068,
43. https://doi.org/10.3390/laboratories2010003,
44. https://doi.org/10.1016/j.heliyon.2024.e40855,
45. https://doi.org/10.14745/ccdr.v48i10a08,
46. https://doi.org/10.1128/cmr.00013-07,
47. https://doi.org/10.1038/nature06247,
48. https://doi.org/10.2903/j.efsa.2025.9169,
49. https://doi.org/10.14745/ccdr.v47i10a04,
50. https://doi.org/10.1371/journal.ppat.0030003,