# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 10 nodes, 7 edges

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
**Generated:** 2026-08-04T01:54:59.292022

1. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
2. ionescu2024extremefluctuationsin pages 1-2
3. ding2022theosmoprotectantswitch pages 6-8
4. ding2022theosmoprotectantswitch pages 4-6
5. strakova2024unveilingthegenomic pages 16-17
6. saum2008regulationofosmoadaptation pages 13-14
7. ding2022theosmoprotectantswitch pages 8-13
8. ding2022theosmoprotectantswitch pages 2-4
9. ding2022theosmoprotectantswitch pages 1-2
10. ding2022theosmoprotectantswitch pages 13-14
11. ionescu2024extremefluctuationsin pages 6-7
12. 10.1038/s41559-024-02505-6
13. 10.3389/fmars.2024.1421769
14. 10.3389/frmbi.2023.1329925
15. 10.3390/genes13060939
16. 10.1186/1746-1448-4-4
17. https://doi.org/10.1038/s41559-024-02505-6
18. https://doi.org/10.3389/fmars.2024.1421769
19. https://doi.org/10.3389/frmbi.2023.1329925
20. https://doi.org/10.3390/genes13060939
21. https://doi.org/10.1186/1746-1448-4-4
22. https://doi.org/10.3390/genes13060939,
23. https://doi.org/10.1038/s41559-024-02505-6,
24. https://doi.org/10.3389/frmbi.2023.1329925,
25. https://doi.org/10.3389/fmars.2024.1421769,
26. https://doi.org/10.1186/1746-1448-4-4,