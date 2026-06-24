# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** stenohaline
- **METPO identifier:** METPO:1000626
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can only tolerate a narrow range of salinity concentrations and cannot survive significant changes in environmental salt levels.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/s40168-024-01817-w: narrow range of salinity (Supports stenohaline microorganisms as organisms thriving within a narrow salinity range.)
- **Existing causal graph summary:** stenohaline_narrow_salinity_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **stenohaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/stenohaline.yaml`.

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
**Generated:** 2026-06-18T01:59:34.479223

1. wu2024metagenomicinsightsinto pages 1-2
2. oren2024novelinsightsinto pages 1-2
3. schiavo2025proposalfornew pages 4-7
4. wu2024metagenomicinsightsinto pages 7-9
5. foster2024bacterialcellvolume pages 10-12
6. foster2024bacterialcellvolume pages 13-16
7. foster2024bacterialcellvolume pages 31-33
8. xing2024thepolyextremophilenatranaerobius pages 1-2
9. xing2024thepolyextremophilenatranaerobius pages 17-19
10. xing2024thepolyextremophilenatranaerobius pages 6-7
11. bhowmick2023osmoticstressresponses pages 3-4
12. bhowmick2023osmoticstressresponses pages 7-8
13. wu2024metagenomicinsightsinto pages 2-4
14. wu2024metagenomicinsightsinto pages 11-13
15. wu2024metagenomicinsightsinto pages 14-16
16. wu2024metagenomicinsightsinto pages 13-14
17. foster2024bacterialcellvolume pages 6-8
18. foster2024bacterialcellvolume pages 8-10
19. matarredona2024understandingthetolerance pages 2-4
20. velez2019impactofsalinity pages 1-3
21. s
22. https://doi.org/10.1186/s40168-024-01817-w
23. https://doi.org/10.1128/mmbr.00181-23
24. https://doi.org/10.1038/s44185-024-00050-w
25. https://doi.org/10.1128/aem.00145-24
26. https://doi.org/10.1093/femsml/uqad020
27. https://doi.org/10.1111/1758-2229.70039
28. https://doi.org/10.21203/rs.3.rs-8012852/v1
29. https://doi.org/10.1186/s40168-024-01817-w,
30. https://doi.org/10.1007/978-3-030-18975-4\_7,
31. https://doi.org/10.1038/s44185-024-00050-w,
32. https://doi.org/10.21203/rs.3.rs-8012852/v1,
33. https://doi.org/10.1128/mmbr.00181-23,
34. https://doi.org/10.1128/aem.00145-24,
35. https://doi.org/10.1093/femsml/uqad020,
36. https://doi.org/10.1111/1758-2229.70039,