# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width small
- **METPO identifier:** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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
**Generated:** 2026-06-18T07:22:26.723370

1. ouzounov2016mreborientationcorrelates pages 1-2
2. tesson2022magnesiumrescuesthe pages 1-2
3. shlosman2023allostericactivationof pages 1-2
4. ago2023relationshipbetweenthe pages 1-3
5. shlosman2023allostericactivationof pages 6-7
6. micelli2023aconservedzincbinding pages 1-2
7. tesson2022magnesiumrescuesthe pages 8-9
8. tesson2022magnesiumrescuesthe pages 2-3
9. galinier2023recentadvancesin pages 1-3
10. shi2018howtobuild pages 7-9
11. costa2024theroleof pages 1-2
12. shi2018howtobuild pages 6-7
13. ago2023relationshipbetweenthe pages 14-16
14. ago2023relationshipbetweenthe pages 11-14
15. middlemiss2023moleculartugofwarregulates pages 19-23
16. middlemiss2023moleculartugofwarregulatesa pages 19-23
17. galinier2023recentadvancesin pages 15-16
18. jain2023understandingelongasomeunit pages 2-4
19. jain2023understandingelongasomeunit pages 5-7
20. https://doi.org/10.1038/s41467-023-39037-9
21. https://doi.org/10.1002/mbo3.1385
22. https://doi.org/10.1016/j.cell.2018.02.050;
23. https://doi.org/10.1016/j.bpj.2016.07.017
24. https://doi.org/10.1038/s41598-021-04294-5
25. https://doi.org/10.1073/pnas.2215237120
26. https://doi.org/10.1101/2024.11.22.624946
27. https://doi.org/10.1128/mbio.03235-23
28. https://doi.org/10.3390/biom13050720
29. https://doi.org/10.33696/signaling.4.101
30. https://doi.org/10.1016/j.cell.2018.02.050
31. https://doi.org/10.1101/2024.11.22.624946,
32. https://doi.org/10.1016/j.bpj.2016.07.017,
33. https://doi.org/10.1038/s41598-021-04294-5,
34. https://doi.org/10.1038/s41467-023-39037-9,
35. https://doi.org/10.1002/mbo3.1385,
36. https://doi.org/10.1016/j.cell.2018.02.050,
37. https://doi.org/10.1073/pnas.2215237120,
38. https://doi.org/10.3390/biom13050720,
39. https://doi.org/10.1128/mbio.03235-23,
40. https://doi.org/10.33696/signaling.4.101,