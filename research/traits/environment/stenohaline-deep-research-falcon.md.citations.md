# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** stenohaline
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000626
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can only tolerate a narrow range of salinity concentrations and cannot survive significant changes in environmental salt levels.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/s40168-024-01817-w: narrow range of salinity (Supports stenohaline microorganisms as organisms thriving within a narrow salinity range.)
- **Existing causal graph summary:** stenohaline_narrow_salinity_tolerance: 17 nodes, 11 edges

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
**Generated:** 2026-08-04T03:30:59.240790

1. wu2024metagenomicinsightsinto pages 1-2
2. fan2024improvementinsalt pages 12-14
3. yu2024temporaldynamicsof pages 1-2
4. poolman2023physicochemicalhomeostasisin pages 4-5
5. wu2024metagenomicinsightsinto pages 7-9
6. xia2023genomicandtranscriptomic pages 5-7
7. zou2024metabolicengineeringof pages 1-2
8. corbett2021examiningtheosmotic pages 1-2
9. xia2023genomicandtranscriptomic pages 1-2
10. xing2024thepolyextremophilenatranaerobius pages 1-2
11. ionescu2024extremefluctuationsin pages 1-2
12. zou2024metabolicengineeringof pages 2-4
13. ionescu2024extremefluctuationsin pages 6-7
14. zou2024metabolicengineeringof pages 4-8
15. 10.1186/s40168-024-01817-w
16. 10.1128/msystems.01106-22
17. 10.1186/s12934-024-02358-5
18. 10.1128/aem.01905-23
19. 10.3390/biology13060404
20. 10.1128/aem.00145-24
21. 10.3389/frmbi.2023.1329925
22. 10.1093/femsre/fuad033
23. 10.3390/microorganisms10010022
24. https://doi.org/10.1186/s40168-024-01817-w
25. https://doi.org/10.1128/msystems.01106-22
26. https://doi.org/10.1186/s12934-024-02358-5
27. https://doi.org/10.1128/aem.01905-23
28. https://doi.org/10.3390/biology13060404
29. https://doi.org/10.1128/aem.00145-24
30. https://doi.org/10.3389/frmbi.2023.1329925
31. https://doi.org/10.1093/femsre/fuad033
32. https://doi.org/10.3390/microorganisms10010022
33. https://doi.org/10.1186/s40168-024-01817-w,
34. https://doi.org/10.1128/msystems.01106-22,
35. https://doi.org/10.1128/aem.01905-23,
36. https://doi.org/10.1186/s12934-024-02358-5,
37. https://doi.org/10.1093/femsre/fuad033,
38. https://doi.org/10.3390/biology13060404,
39. https://doi.org/10.3389/frmbi.2023.1329925,
40. https://doi.org/10.1128/aem.00145-24,
41. https://doi.org/10.3390/microorganisms10010022,