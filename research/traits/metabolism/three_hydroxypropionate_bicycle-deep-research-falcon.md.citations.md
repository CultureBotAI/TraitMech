# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate bicycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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
**Generated:** 2026-08-04T07:14:56.996802

1. garritano2022carbonfixationpathways pages 2-3
2. min2022crystalstructureof pages 1-2
3. hugler2011beyondthecalvin pages 9-10
4. berg2011ecologicalaspectsof pages 7-8
5. berg2011ecologicalaspectsof pages 8-9
6. mclean2023exploringalternativepathways pages 1-2
7. scott2024widespreaddissolvedinorganic pages 7-10
8. 10.1128/AEM.02473-10
9. 10.1146/annurev-marine-120709-142712
10. 10.3389/fmicb.2022.923367
11. 10.1093/pnasnexus/pgac226
12. 10.1126/sciadv.adh4299
13. 10.1128/AEM.01557-23
14. 10.1038/s41467-024-53762-9
15. https://doi.org/10.1128/AEM.02473-10
16. https://doi.org/10.1146/annurev-marine-120709-142712
17. https://doi.org/10.3389/fmicb.2022.923367
18. https://doi.org/10.1093/pnasnexus/pgac226
19. https://doi.org/10.1126/sciadv.adh4299
20. https://doi.org/10.1128/AEM.01557-23
21. https://doi.org/10.1038/s41467-024-53762-9
22. https://doi.org/10.1128/aem.02473-10,
23. https://doi.org/10.3389/fmicb.2022.923367,
24. https://doi.org/10.1146/annurev-marine-120709-142712,
25. https://doi.org/10.1093/pnasnexus/pgac226,
26. https://doi.org/10.1038/s41467-024-53762-9,
27. https://doi.org/10.1126/sciadv.adh4299,
28. https://doi.org/10.1128/aem.01557-23,