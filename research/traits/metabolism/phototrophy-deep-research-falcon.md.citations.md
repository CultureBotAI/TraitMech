# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/phototrophy.yaml`.

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
**Generated:** 2026-08-04T06:50:28.823832

1. tinguely2023diurnalcyclesdrive pages 9-10
2. bryant2006prokaryoticphotosynthesisand pages 2-3
3. bryant2006prokaryoticphotosynthesisand pages 1-2
4. kushkevych2024anoxygenicphotosynthesiswith pages 18-18
5. peterson2023usinglightfor pages 1-5
6. li2023globallydistributedmyxococcota pages 4-5
7. davison2022engineeringarhodopsinbased pages 1-2
8. kacar2406foundationsforreconstructing pages 15-18
9. tu2024engineeringrhodopsinbasedartificial pages 102-105
10. kacar2406foundationsforreconstructing pages 18-21
11. https://doi.org/10.1016/j.tim.2006.09.001.
12. https://doi.org/10.1038/s41467-023-42193-7.
13. https://doi.org/10.1038/s43705-023-00334-5.
14. https://doi.org/10.3389/fmicb.2024.1417714.
15. https://doi.org/10.1021/acssynbio.2c00397.
16. https://doi.org/10.1101/2022.12.06.519405.
17. https://doi.org/10.48550/arXiv.2406.09354.
18. https://doi.org/10.1016/j.tim.2006.09.001,
19. https://doi.org/10.1101/2022.12.06.519405,
20. https://doi.org/10.48550/arxiv.2406.09354,
21. https://doi.org/10.3389/fmicb.2024.1417714,
22. https://doi.org/10.1021/acssynbio.2c00397,
23. https://doi.org/10.1038/s43705-023-00334-5,
24. https://doi.org/10.1038/s41467-023-42193-7,