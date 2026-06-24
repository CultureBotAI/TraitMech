# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organotrophic
- **METPO identifier:** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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
**Generated:** 2026-06-18T12:17:02.916316

1. li2023reducedtracegas pages 7-8
2. li2023reducedtracegas pages 1-2
3. yamamoto2024rolesofflavoprotein pages 3-5
4. uriberamirez2024modificationsofthe pages 11-12
5. giordano2024nitricoxideand pages 8-13
6. uriberamirez2024modificationsofthe pages 1-2
7. garimella2024fromcellsto pages 1-2
8. garimella2024fromcellsto pages 2-4
9. zhao2023keygenesof pages 1-2
10. fernandes2024structuralandfunctional pages 38-41
11. alleman2023mechanismsforgenerating pages 7-9
12. gonzalezmontalvo2024therespiratorychain pages 1-2
13. li2023reducedtracegas pages 2-3
14. li2023reducedtracegas pages 8-9
15. garimella2024fromcellsto pages 4-6
16. gonzalezmontalvo2024therespiratorychain pages 13-13
17. giordano2024nitricoxideand pages 1-8
18. gonzalezmontalvo2024therespiratorychain pages 13-14
19. fernandes2024structuralandfunctional pages 41-45
20. s
21. https://doi.org/10.1038/s41396-023-01437-6,
22. https://doi.org/10.1186/s13213-024-01761-y,
23. https://doi.org/10.1007/s10863-024-10041-y,
24. https://doi.org/10.12938/bmfh.2024-002,
25. https://doi.org/10.1186/s13068-023-02430-z,
26. https://doi.org/10.1038/s41396-023-01437-6
27. https://doi.org/10.1128/aem.00378-23
28. https://doi.org/10.1186/s13068-023-02430-z
29. https://doi.org/10.12938/bmfh.2024-002
30. https://doi.org/10.1186/s13213-024-01761-y
31. https://doi.org/10.1007/s10863-024-10041-y
32. https://doi.org/10.3389/fmicb.2024.1479714
33. https://doi.org/10.3389/fmicb.2024.1479714,
34. https://doi.org/10.1128/aem.00378-23,