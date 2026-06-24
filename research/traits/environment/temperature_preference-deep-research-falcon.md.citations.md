# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature preference
- **METPO identifier:** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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
**Generated:** 2026-06-18T02:31:14.271733

1. ramon2023ageneraloverview pages 1-2
2. moon2023temperaturemattersbacterial pages 3-5
3. dessenne2024lipidomicanalysesreveal pages 12-13
4. ramon2023ageneraloverview pages 4-5
5. ramon2023ageneraloverview pages 5-7
6. ramon2023ageneraloverview pages 2-4
7. dessenne2024lipidomicanalysesreveal pages 8-12
8. moon2023temperaturemattersbacterial pages 1-3
9. li2024mechanismsunderlyingthe pages 9-10
10. li2024mechanismsunderlyingthe pages 10-12
11. bellanger2024theroleof pages 1-2
12. villain2025regulationofdna pages 10-12
13. villain2025regulationofdna pages 9-10
14. li2024mechanismsunderlyingthe pages 7-9
15. dessenne2024lipidomicanalysesreveal pages 1-2
16. bellanger2024theroleof pages 3-4
17. li2024mechanismsunderlyingthe pages 12-13
18. takemata2024howdothermophiles pages 1-2
19. bellanger2024theroleof pages 2-3
20. https://doi.org/10.1007/s42770-023-01057-4.
21. https://doi.org/10.1128/spectrum.00757-24.
22. https://doi.org/10.1007/s12275-023-00031-x.
23. https://doi.org/10.1264/jsme2.me23087.
24. https://doi.org/10.1111/mmi.15328.
25. https://doi.org/10.1038/s41598-024-67362-6.
26. https://doi.org/10.3389/fmicb.2024.1465627.
27. https://doi.org/10.1007/s12275-023-00031-x
28. https://doi.org/10.1007/s42770-023-01057-4
29. https://doi.org/10.1264/jsme2.me23087
30. https://doi.org/10.1038/s41598-024-67362-6
31. https://doi.org/10.1128/spectrum.00757-24
32. https://doi.org/10.3389/fmicb.2024.1465627
33. https://doi.org/10.1111/mmi.15328
34. https://doi.org/10.1007/s42770-023-01057-4,
35. https://doi.org/10.1007/s12275-023-00031-x,
36. https://doi.org/10.3389/fmicb.2024.1465627,
37. https://doi.org/10.1111/mmi.15328,
38. https://doi.org/10.1264/jsme2.me23087,
39. https://doi.org/10.1128/spectrum.00757-24,
40. https://doi.org/10.1038/s41598-024-67362-6,