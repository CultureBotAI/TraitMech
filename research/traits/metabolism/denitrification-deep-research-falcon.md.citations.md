# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** denitrification
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000104
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced stepwise to gaseous dinitrogen via nitrite, nitric oxide, and nitrous oxide, removing fixed nitrogen from the system as gas.
- **Parent traits:** METPO:1000802
- **Synonyms:** denitrifying
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997:  (Zumft reviews the cell biology and molecular basis of denitrification, the stepwise respiratory reduction of nitrate to dinitrogen.) | DOI:10.1038/nrmicro.2018.9:  (Kuypers et al. place denitrification as a nitrogen-loss branch of the microbial nitrogen-cycling network.)
- **Existing causal graph summary:** denitrification_stepwise_nitrate_to_n2: 15 nodes, 9 edges

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
**Generated:** 2026-08-04T05:50:33.508473

1. hallin2018genomicsandecology pages 2-3
2. roothans2024aerobicdenitrificationas pages 1-2
3. mirallesrobledillo2021distributionofdenitrification pages 10-12
4. hallin2018genomicsandecology pages 11-12
5. hallin2018genomicsandecology pages 3-5
6. phan2024metaomicinsightsinto pages 21-23
7. bell2024denitrificationgenotypesof pages 1-6
8. crocker2024environmentallydependentinteractions pages 1-5
9. hallin2018genomicsandecology pages 5-9
10. 10.1016/j.tim.2017.07.003
11. 10.1093/ismejo/wrae116
12. 10.1038/s41396-021-01045-2
13. 10.1111/1751-7915.12352
14. 10.1101/2024.11.13.623363
15. 10.1264/jsme2.me23106
16. 10.3390/agriculture14020240
17. 10.1038/s41467-024-47827-y
18. 10.1093/ismeco/ycae020
19. 10.1038/s41564-024-01752-4
20. 10.3390/microorganisms9081669
21. https://doi.org/10.1016/j.tim.2017.07.003
22. https://doi.org/10.1093/ismejo/wrae116
23. https://doi.org/10.1038/s41396-021-01045-2
24. https://doi.org/10.1111/1751-7915.12352
25. https://doi.org/10.1101/2024.11.13.623363
26. https://doi.org/10.1264/jsme2.me23106
27. https://doi.org/10.3390/agriculture14020240
28. https://doi.org/10.1038/s41467-024-47827-y
29. https://doi.org/10.1093/ismeco/ycae020
30. https://doi.org/10.1038/s41564-024-01752-4
31. https://doi.org/10.3390/microorganisms9081669
32. https://doi.org/10.1016/j.tim.2017.07.003,
33. https://doi.org/10.1093/ismejo/wrae116,
34. https://doi.org/10.1101/2024.11.13.623363,
35. https://doi.org/10.3390/microorganisms9081669,
36. https://doi.org/10.1101/2024.05.17.594689,
37. https://doi.org/10.1038/s41564-024-01752-4,