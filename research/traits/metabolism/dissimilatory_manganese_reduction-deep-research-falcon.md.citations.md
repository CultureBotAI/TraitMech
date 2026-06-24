# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory manganese reduction
- **METPO identifier:** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

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
**Generated:** 2026-06-18T04:58:47.313810

1. shi2012molecularunderpinningsof pages 1-2
2. naradasu2024electrochemicalcharacterizationof pages 8-9
3. ueki2021cytochromesinextracellular pages 8-10
4. sivan2024enigmaticfemnfueledanaerobic pages 8-12
5. ford2024theelectrontransport pages 12-14
6. sivan2024enigmaticfemnfueledanaerobic pages 1-4
7. shi2012molecularunderpinningsof pages 2-3
8. marco2022ericstevensand pages 84-88
9. zhang2023multihemecytochromemediatedextracellular pages 6-7
10. zhang2023multihemecytochromemediatedextracellulara pages 5-6
11. zhang2023multihemecytochromemediatedextracellulara pages 1-2
12. zhang2023multihemecytochromemediatedextracellulara pages 6-7
13. zhang2023multihemecytochromemediatedextracellular pages 1-2
14. ueki2021cytochromesinextracellular pages 10-12
15. alves2024potentialofelectrogenic pages 27-31
16. alves2024potentialofelectrogenic pages 57-60
17. hou2024biologicalandchemical pages 1-2
18. https://doi.org/10.1128/mr.55.2.259-287.1991
19. https://doi.org/10.3389/fmicb.2012.00050
20. https://doi.org/10.3390/microorganisms12020257
21. https://doi.org/10.1128/aem.03109-20
22. https://doi.org/10.5194/egusphere-2024-1829
23. https://doi.org/10.1128/aem.01387-23
24. https://doi.org/10.1128/mr.55.2.259-287.1991,
25. https://doi.org/10.3389/fmicb.2012.00050,
26. https://doi.org/10.5194/egusphere-2024-1829,
27. https://doi.org/10.3390/microorganisms12020257,
28. https://doi.org/10.1128/aem.03109-20,
29. https://doi.org/10.1128/aem.01387-23,
30. https://doi.org/10.3390/microorganisms12122454,