# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory iron reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella, often via extracellular electron transfer.
- **Parent traits:** traitmech:000039
- **Synonyms:** ferric iron respiration, dissimilatory Fe(III) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and Mn(IV) as terminal electron acceptors competitive with nitrate.)
- **Existing causal graph summary:** dir_ferric_iron_respiration: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory iron reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_iron_reduction.yaml`.

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
**Generated:** 2026-08-04T05:57:23.811974

1. beblawy2018extracellularreductionof pages 6-9
2. jiang2023thevariedroles pages 1-2
3. schwarz2024lackofphysiological pages 2-4
4. schwarz2024lackofphysiological pages 4-8
5. conley2020ahybridextracellular pages 29-31
6. Beblawy et al., July 2018
7. Shi et al., October 2024
8. Schwarz et al., May 2024
9. Jiang et al., October 2023
10. 10.1128/mbio.00690-24
11. 10.1007/s10533-024-01186-4
12. 10.3389/fmicb.2023.1251346
13. 10.1111/mmi.14067
14. 10.1128/AEM.01253-20
15. https://doi.org/10.1111/mmi.14067
16. https://doi.org/10.1007/s10533-024-01186-4
17. https://doi.org/10.1128/mbio.00690-24
18. https://doi.org/10.3389/fmicb.2023.1251346
19. https://doi.org/10.1128/AEM.01253-20
20. https://doi.org/10.1111/mmi.14067,
21. https://doi.org/10.3389/fmicb.2023.1251346,
22. https://doi.org/10.1007/s10533-024-01186-4,
23. https://doi.org/10.1128/mbio.00690-24,
24. https://doi.org/10.1128/aem.01253-20,