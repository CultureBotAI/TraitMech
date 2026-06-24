# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** denitrification
- **METPO identifier:** traitmech:000104
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced stepwise to gaseous dinitrogen via nitrite, nitric oxide, and nitrous oxide, removing fixed nitrogen from the system as gas.
- **Parent traits:** METPO:1000802
- **Synonyms:** denitrifying
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997:  (Zumft reviews the cell biology and molecular basis of denitrification, the stepwise respiratory reduction of nitrate to dinitrogen.) | DOI:10.1038/nrmicro.2018.9:  (Kuypers et al. place denitrification as a nitrogen-loss branch of the microbial nitrogen-cycling network.)
- **Existing causal graph summary:** denitrification_stepwise_nitrate_to_n2: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **denitrification** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/denitrification.yaml`.

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
**Generated:** 2026-06-18T04:42:26.546616

1. sennett2024determininghowoxygen pages 1-2
2. bano2024soilpropertiesdrive pages 1-2
3. schacksen2024unravelingthegenetic pages 1-2
4. intrator2024aquaticnitrousoxide pages 1-2
5. roothans2024aerobicdenitrificationas pages 1-2
6. roothans2024aerobicdenitrificationas pages 8-9
7. pold2024phylogeneticsandenvironmental pages 1-2
8. pold2024phylogeneticsandenvironmental pages 8-11
9. pold2024phylogeneticsandenvironmental pages 12-13
10. murali2024diversityandevolution pages 2-4
11. xiang2023denitrificationcontributesto pages 1-2
12. xiang2023denitrificationcontributesto pages 2-3
13. sennett2024determininghowoxygen pages 6-7
14. intrator2024aquaticnitrousoxide pages 12-12
15. bano2024soilpropertiesdrive pages 9-13
16. https://doi.org/10.1186/s40793-024-00643-9
17. https://doi.org/10.3389/fmicb.2023.1218207
18. https://doi.org/10.1093/ismeco/ycae020
19. https://doi.org/10.3389/fmicb.2024.1407573
20. https://doi.org/10.1038/s41467-024-51688-w
21. https://doi.org/10.1128/aem.02177-23
22. https://doi.org/10.1093/ismejo/wrae116
23. https://doi.org/10.1073/pnas.2316422121
24. https://doi.org/10.1038/s41467-024-51688-w,
25. https://doi.org/10.1128/aem.02177-23,
26. https://doi.org/10.1186/s40793-024-00643-9,
27. https://doi.org/10.3389/fmicb.2024.1407573,
28. https://doi.org/10.1093/ismejo/wrae116,
29. https://doi.org/10.3389/fmicb.2023.1218207,
30. https://doi.org/10.1093/ismeco/ycae020,
31. https://doi.org/10.1073/pnas.2316422121,