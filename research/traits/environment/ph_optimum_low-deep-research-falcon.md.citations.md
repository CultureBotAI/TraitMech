# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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
**Generated:** 2026-08-04T02:48:16.470982

1. lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5
2. riveraaraya2019osmoticimbalancecytoplasm pages 1-2
3. krulwich2011molecularaspectsof pages 1-3
4. vergara2020evolutionofpredicted pages 1-3
5. zhang2024accumulatedcoppertailing pages 5-8
6. gonzalezrosales2022integrativegenomicssheds pages 1-2
7. vergara2020evolutionofpredicted pages 16-17
8. zhang2024accumulatedcoppertailing pages 1-2
9. 10.1038/nrmicro2549
10. 10.3390/genes11040389
11. 10.1111/1758-2229.70019
12. 10.3389/fmicb.2021.822229
13. 10.1128/AEM.04031-15
14. 10.3389/fmicb.2019.02455
15. 10.3390/min14101051
16. https://doi.org/10.1038/nrmicro2549
17. https://doi.org/10.3390/genes11040389
18. https://doi.org/10.1111/1758-2229.70019
19. https://doi.org/10.3389/fmicb.2021.822229
20. https://doi.org/10.1128/AEM.04031-15
21. https://doi.org/10.3389/fmicb.2019.02455
22. https://doi.org/10.3390/min14101051
23. https://doi.org/10.3389/fmicb.2021.822229,
24. https://doi.org/10.1038/nrmicro2549,
25. https://doi.org/10.1128/aem.04031-15,
26. https://doi.org/10.3390/genes11040389,
27. https://doi.org/10.3389/fmicb.2019.02455,
28. https://doi.org/10.1111/1758-2229.70019,
29. https://doi.org/10.3390/min14101051,