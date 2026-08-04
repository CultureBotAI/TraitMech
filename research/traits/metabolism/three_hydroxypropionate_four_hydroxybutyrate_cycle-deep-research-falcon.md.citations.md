# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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
**Generated:** 2026-08-04T07:17:04.169502

1. liu2021convergentevolutionof pages 1-2
2. johnson2024crystalstructureof pages 1-2
3. garritano2022carbonfixationpathways pages 1-2
4. qi2024analysisofnearly pages 7-8
5. qi2024analysisofnearly pages 1-2
6. straub2018biotechnologyofextremely pages 11-14
7. bierbaumer2023enzymaticconversionof pages 19-21
8. johnson2024crystalstructureof pages 2-3
9. https://doi.org/10.1126/science.1149976
10. https://doi.org/10.1074/jbc.M112.413195
11. https://doi.org/10.1128/AEM.04146-13
12. https://doi.org/10.1128/AEM.03390-14
13. https://doi.org/10.1093/femsre/fuy012
14. https://doi.org/10.1128/mSphere.01079-20
15. https://doi.org/10.3389/fmicb.2021.712030
16. https://doi.org/10.1093/pnasnexus/pgac226
17. https://doi.org/10.1021/acs.chemrev.2c00581
18. https://doi.org/10.1038/s41467-024-48498-5
19. https://doi.org/10.1038/s42003-024-06432-x
20. https://doi.org/10.1128/aem.04146-13,
21. https://doi.org/10.1074/jbc.m112.413195,
22. https://doi.org/10.3389/fmicb.2021.712030,
23. https://doi.org/10.1128/msphere.01079-20,
24. https://doi.org/10.1038/s42003-024-06432-x,
25. https://doi.org/10.1093/pnasnexus/pgac226,
26. https://doi.org/10.1038/s41467-024-48498-5,
27. https://doi.org/10.1093/femsre/fuy012,
28. https://doi.org/10.1021/acs.chemrev.2c00581,