# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range high
- **METPO identifier:** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_high.yaml`.

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
**Generated:** 2026-06-17T23:37:38.439759

1. cirachavez2019kineticsofhalophilic pages 1-3
2. lee2018naclsaturatedbrinesare pages 12-15
3. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
4. khanh2024metabolicpathwayengineering pages 1-2
5. ghosh2019microbialdiversityof pages 13-15
6. ionescu2024extremefluctuationsin pages 1-2
7. xing2024thepolyextremophilenatranaerobius pages 1-2
8. bartha2022investigatingextremotolerantmicrobes pages 25-28
9. lee2018naclsaturatedbrinesare pages 15-17
10. xing2024thepolyextremophilenatranaerobius pages 10-14
11. bartha2022investigatingextremotolerantmicrobes pages 21-25
12. label-only
13. approx. label-only for salt-in strategy
14. https://doi.org/10.1038/s41559-024-02505-6
15. https://doi.org/10.1093/femsre/fuy026
16. https://doi.org/10.1128/aem.00145-24
17. https://doi.org/10.3389/frmbi.2023.1329925
18. https://doi.org/10.1128/aem.01195-24
19. https://doi.org/10.1007/978-3-030-18975-4_4
20. https://doi.org/10.5772/intechopen.81100
21. https://doi.org/10.3389/fmicb.2022.1075274
22. https://doi.org/10.1038/s41559-024-02505-6,
23. https://doi.org/10.1128/aem.00145-24,
24. https://doi.org/10.1128/aem.01195-24,
25. https://doi.org/10.3389/frmbi.2023.1329925,
26. https://doi.org/10.1093/femsre/fuy026,
27. https://doi.org/10.5772/intechopen.81100,
28. https://doi.org/10.1007/978-3-030-18975-4\_4,
29. https://doi.org/10.3389/fmicb.2022.1075274,