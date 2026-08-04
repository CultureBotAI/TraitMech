# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hydrogenotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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
**Generated:** 2026-08-04T11:22:27.398011

1. cramm2009genomicviewof pages 1-2
2. frolov2023obligateautotrophyat pages 1-2
3. pichechoquette2019molecularhydrogena pages 11-13
4. neto2024exploringthepotential pages 1-2
5. jiao2021insightintothe pages 6-7
6. pichechoquette2019molecularhydrogena pages 9-11
7. pichechoquette2019molecularhydrogena pages 6-8
8. frolov2023obligateautotrophyat pages 8-9
9. culp2023crossfeedinginthe pages 7-9
10. boyd2023anaturalistperspective pages 8-9
11. mook2024lactatemediatedmixotrophiccocultivation pages 1-2
12. pichechoquette2019molecularhydrogena pages 8-9
13. NiFe
14. FeFe
15. https://doi.org/10.3389/fmicb.2023.1185739
16. https://doi.org/10.1111/1462-2920.16285
17. https://doi.org/10.1016/j.chom.2023.03.016
18. https://doi.org/10.1186/s12934-024-02481-3
19. https://doi.org/10.5713/ab.23.0294
20. https://doi.org/10.1007/s40726-024-00337-3
21. https://doi.org/10.1128/AEM.02418-18
22. https://doi.org/10.1038/s41396-021-00935-9
23. https://doi.org/10.1159/000142893
24. https://doi.org/10.31223/X5HC7H
25. https://doi.org/10.1016/j.chom.2023.03.016,
26. https://doi.org/10.1128/aem.02418-18,
27. https://doi.org/10.1159/000142893,
28. https://doi.org/10.3389/fmicb.2023.1185739,
29. https://doi.org/10.1007/s40726-024-00337-3,
30. https://doi.org/10.1038/s41396-021-00935-9,
31. https://doi.org/10.31223/x5hc7h,
32. https://doi.org/10.1111/1462-2920.16285,
33. https://doi.org/10.5713/ab.23.0294,
34. https://doi.org/10.1186/s12934-024-02481-3,