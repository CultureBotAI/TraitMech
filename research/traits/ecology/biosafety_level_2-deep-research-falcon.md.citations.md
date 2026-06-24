# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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
**Generated:** 2026-06-17T20:11:29.710444

1. kaufer2020laboratorybiosafetymeasures pages 3-4
2. blacksell2019biosafetyandbiosecurity pages 2-3
3. ta2018biosafetyandbiohazards pages 3-6
4. kaufer2020laboratorybiosafetymeasures pages 4-5
5. gao2024frombiosafetyto pages 5-6
6. resnik2024biosafetybiosecurityand pages 6-7
7. tran2025surveillanceoflaboratory pages 2-4
8. blacksell2019biosafetyandbiosecurity pages 4-5
9. blacksell2019biosafetyandbiosecurity pages 7-8
10. balbontin2024canadianlaboratoryincidents pages 1-2
11. thompson2022surveillanceoflaboratory pages 1-2
12. godwin2023environmentalhealthand pages 1-2
13. godwin2023environmentalhealthand pages 2-4
14. abalos2023surveillanceoflaboratory pages 1-2
15. ta2018biosafetyandbiohazards pages 6-8
16. https://doi.org/10.1016/j.pathol.2020.09.006,
17. https://doi.org/10.1186/s12879-019-4653-4,
18. https://doi.org/10.1007/978-1-4939-8935-5_19,
19. https://doi.org/10.3390/laboratories1030013,
20. https://doi.org/10.1089/apb.2023.0007,
21. https://doi.org/10.14745/ccdr.v49i09a06,
22. https://doi.org/10.14745/ccdr.v48i10a08,
23. https://doi.org/10.14745/ccdr.v50i05a04,
24. https://doi.org/10.14745/ccdr.v51i101112a04,
25. https://doi.org/10.14745/ccdr.v51i101112a04
26. https://doi.org/10.14745/ccdr.v50i05a04
27. https://doi.org/10.3390/laboratories1030013
28. https://doi.org/10.1007/s40592-024-00204-3
29. https://doi.org/10.1089/apb.2023.0007
30. https://doi.org/10.14745/ccdr.v49i09a06
31. https://doi.org/10.14745/ccdr.v48i10a08
32. https://doi.org/10.1016/j.pathol.2020.09.006
33. https://doi.org/10.1186/s12879-019-4653-4
34. https://doi.org/10.1007/978-1-4939-8935-5_19
35. https://doi.org/10.1007/978-1-4939-8935-5\_19,
36. https://doi.org/10.1007/s40592-024-00204-3,