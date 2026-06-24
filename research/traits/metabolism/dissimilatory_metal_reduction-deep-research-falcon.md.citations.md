# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory metal reduction
- **METPO identifier:** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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
**Generated:** 2026-06-18T04:57:51.370074

1. hsu2024isolationandgenomic pages 1-2
2. portela2024widespreadextracellularelectron pages 2-3
3. hou2025cooccurrenceofdirect pages 1-2
4. soares2025toolsforenhancing pages 12-13
5. soares2025toolsforenhancing pages 5-8
6. nash2025thestructureand pages 20-25
7. soares2025toolsforenhancing pages 2-4
8. https://doi.org/10.1128/aem.00044-24
9. https://doi.org/10.1007/s11783-019-1173-9
10. https://doi.org/10.1128/spectrum.01226-24
11. https://doi.org/10.3390/fermentation11070381
12. https://doi.org/10.1038/s41467-024-46192-0
13. https://doi.org/10.1128/aem.00044-24,
14. https://doi.org/10.1007/s11783-019-1173-9,
15. https://doi.org/10.3390/fermentation11070381,
16. https://doi.org/10.1128/spectrum.01226-24,
17. https://doi.org/10.1038/s41467-024-46192-0,