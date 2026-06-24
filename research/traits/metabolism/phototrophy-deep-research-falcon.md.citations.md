# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophy
- **METPO identifier:** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T05:55:01.507373

1. hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2
2. grettenberger2024limitingfactorsin pages 1-2
3. li2024insitucommunity pages 13-15
4. okhrimenko2023mirrorproteorhodopsins pages 1-2
5. tu2023engineeringartificialphotosynthesis pages 2-3
6. chazan2023phototrophybyantennacontaining pages 1-7
7. tu2024engineeringbionanoreactorin pages 9-9
8. davison2022engineeringarhodopsinbased pages 1-2
9. oh2024effectoflight pages 1-2
10. tu2022rhodopsindrivenmicrobial pages 1-3
11. bryant2006prokaryoticphotosynthesisand pages 2-3
12. bryant2006prokaryoticphotosynthesisand pages 1-2
13. bryant2006prokaryoticphotosynthesisand pages 6-7
14. FeFe
15. https://doi.org/10.1093/ismejo/wrae175
16. https://doi.org/10.1128/spectrum.02177-23
17. https://doi.org/10.1111/1751-7915.14519
18. https://doi.org/10.1038/s42004-023-00884-8
19. https://doi.org/10.1038/s41467-023-43524-4
20. https://doi.org/10.1073/pnas.2404958121
21. https://doi.org/10.4014/jmb.2410.10034
22. https://doi.org/10.1038/s41586-023-05774-6
23. https://doi.org/10.1021/acssynbio.2c00397
24. https://doi.org/10.1111/1462-2920.16243
25. https://doi.org/10.1016/j.tim.2006.09.001
26. https://doi.org/10.1016/j.tim.2006.09.001,
27. https://doi.org/10.1093/ismejo/wrae175,
28. https://doi.org/10.1038/s41467-023-43524-4,
29. https://doi.org/10.1073/pnas.2404958121,
30. https://doi.org/10.1111/1751-7915.14519,
31. https://doi.org/10.1128/spectrum.02177-23,
32. https://doi.org/10.1038/s42004-023-00884-8,
33. https://doi.org/10.1038/s41586-023-05774-6,
34. https://doi.org/10.1021/acssynbio.2c00397,
35. https://doi.org/10.4014/jmb.2410.10034,
36. https://doi.org/10.1111/1462-2920.16243,