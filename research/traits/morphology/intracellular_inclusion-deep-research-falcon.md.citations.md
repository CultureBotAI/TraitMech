# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** intracellular inclusion
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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
**Generated:** 2026-08-04T08:58:06.859786

1. ferrara2024bacterialorganellesin pages 1-2
2. mullersantos2021theprotectiverole pages 9-10
3. ferrara2024bacterialorganellesin pages 2-4
4. jost2022interactionofthe pages 2-3
5. ferrara2024bacterialorganellesin pages 12-14
6. rose2023innateandengineered pages 1-2
7. trettel2024modelingbacterialmicrocompartment pages 1-2
8. jost2022interactionofthe pages 1-2
9. jost2022interactionofthe pages 14-15
10. mullersantos2021theprotectiverole pages 35-36
11. mullersantos2021theprotectiverole pages 5-6
12. mullersantos2021theprotectiverole pages 40-41
13. mullersantos2021theprotectiverole pages 33-34
14. li2024nanoengineeringcarboxysomeshells pages 11-12
15. sarkar2024atomicviewof pages 7-8
16. iburg2024elucidatingtheassembly pages 1-2
17. trettel2024modelingbacterialmicrocompartment pages 12-12
18. 10.1039/D3TB00098B
19. 10.3389/fpls.2024.1346759
20. 10.3389/fmicb.2022.971917
21. 10.1111/mmi.15330
22. 10.1093/femsre/fuaa058
23. 10.1021/acsnano.3c11559
24. 10.1038/s44318-024-00178-2
25. 10.26434/chemrxiv-2024-kbcdf-v2
26. 10.1038/s41579-020-0413-0
27. 10.1038/nrmicro.2018.10
28. https://doi.org/10.1039/D3TB00098B
29. https://doi.org/10.3389/fpls.2024.1346759
30. https://doi.org/10.3389/fmicb.2022.971917
31. https://doi.org/10.1111/mmi.15330
32. https://doi.org/10.1093/femsre/fuaa058
33. https://doi.org/10.1021/acsnano.3c11559
34. https://doi.org/10.1038/s44318-024-00178-2
35. https://doi.org/10.26434/chemrxiv-2024-kbcdf-v2
36. https://doi.org/10.1038/s41579-020-0413-0
37. https://doi.org/10.1038/nrmicro.2018.10
38. https://doi.org/10.1111/mmi.15330,
39. https://doi.org/10.1039/d3tb00098b,
40. https://doi.org/10.1093/femsre/fuaa058,
41. https://doi.org/10.1038/s44318-024-00178-2,
42. https://doi.org/10.3389/fpls.2024.1346759,
43. https://doi.org/10.26434/chemrxiv-2024-kbcdf-v2,
44. https://doi.org/10.3389/fmicb.2022.971917,
45. https://doi.org/10.1021/acsnano.3c11559,