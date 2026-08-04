# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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
**Generated:** 2026-08-04T01:59:44.959281

1. oren2008microbiallifeat pages 1-2
2. leon2018compatiblesolutesynthesis pages 4-5
3. ugwuodo2024changesinenvironmental pages 1-2
4. ionescu2024extremefluctuationsin pages 1-2
5. ding2022theosmoprotectantswitch pages 4-6
6. strakova2024unveilingthegenomic pages 1-2
7. ding2022theosmoprotectantswitch pages 1-2
8. ding2022theosmoprotectantswitch pages 6-8
9. bonnaud2024haloarchaeaaspromising pages 2-4
10. reang2024extremozymesandcompatible pages 8-11
11. dindhoria2024metagenomicassembledgenomes pages 1-2
12. reang2024extremozymesandcompatible pages 16-16
13. reang2024extremozymesandcompatible pages 1-2
14. leon2018compatiblesolutesynthesis pages 1-2
15. reang2024extremozymesandcompatible pages 4-5
16. reang2024extremozymesandcompatible pages 2-3
17. ding2022theosmoprotectantswitch pages 2-4
18. reang2024extremozymesandcompatible pages 3-4
19. reang2024extremozymesandcompatible pages 15-16
20. https://doi.org/10.3390/genes13060939
21. https://doi.org/10.1186/1746-1448-4-2
22. https://doi.org/10.1186/1746-1448-4-2;
23. https://doi.org/10.3390/microorganisms12081738
24. https://doi.org/10.3389/fmicb.2018.00108
25. https://doi.org/10.1128/spectrum.02334-23
26. https://doi.org/10.3389/frmbi.2023.1329925
27. https://doi.org/10.3389/fmars.2024.1421769
28. https://doi.org/10.1038/s41598-024-63581-z
29. https://doi.org/10.1128/msystems.01050-23
30. https://doi.org/10.3390/genes13060939,
31. https://doi.org/10.1186/1746-1448-4-2,
32. https://doi.org/10.3389/frmbi.2023.1329925,
33. https://doi.org/10.1128/spectrum.02334-23,
34. https://doi.org/10.3389/fmicb.2018.00108,
35. https://doi.org/10.1038/s41598-024-63581-z,
36. https://doi.org/10.3390/microorganisms12081738,
37. https://doi.org/10.3389/fmars.2024.1421769,
38. https://doi.org/10.1128/msystems.01050-23,