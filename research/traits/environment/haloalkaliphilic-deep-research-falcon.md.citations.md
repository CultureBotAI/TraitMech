# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** haloalkaliphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000621
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism requires both high salt concentrations and alkaline pH for optimal growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** PMID:17203963: aerobic, haloalkaliphilic archaeon Natronomonas pharaonis (Organism example: Natronomonas pharaonis is described as haloalkaliphilic.)
- **Existing causal graph summary:** haloalkaliphilic_salt_alkaline_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **haloalkaliphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/haloalkaliphilic.yaml`.

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
**Generated:** 2026-08-04T00:57:18.763843

1. xing2024thepolyextremophilenatranaerobius pages 1-2
2. sorokin2018phenotypicandgenomic pages 1-2
3. bonnaud2024haloarchaeaaspromising pages 2-4
4. mesbah2009thehalophilicalkalithermophile pages 1-2
5. sorokin2018phenotypicandgenomic pages 6-7
6. sorokin2014microbialdiversityand pages 11-12
7. xing2024thepolyextremophilenatranaerobius pages 10-14
8. mesbah2008lifeatextreme pages 11-12
9. sorokin2018phenotypicandgenomic pages 7-10
10. sorokin2018phenotypicandgenomic pages 4-6
11. sorokin2014microbialdiversityand pages 6-8
12. 10.1128/aem.00145-24
13. 10.1111/j.1365-2958.2009.06845.x
14. 10.3389/fmicb.2018.02672
15. 10.1007/s00792-014-0670-9
16. 10.3390/microorganisms12081738
17. 10.1196/annals.1419.028
18. https://doi.org/10.1128/aem.00145-24
19. https://doi.org/10.1111/j.1365-2958.2009.06845.x
20. https://doi.org/10.3389/fmicb.2018.02672
21. https://doi.org/10.1007/s00792-014-0670-9
22. https://doi.org/10.3390/microorganisms12081738
23. https://doi.org/10.1196/annals.1419.028
24. https://doi.org/10.1128/aem.00145-24,
25. https://doi.org/10.3389/fmicb.2018.02672,
26. https://doi.org/10.3390/microorganisms12081738,
27. https://doi.org/10.1111/j.1365-2958.2009.06845.x,
28. https://doi.org/10.1007/s00792-014-0670-9,
29. https://doi.org/10.1196/annals.1419.028,