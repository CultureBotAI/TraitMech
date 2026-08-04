# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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
**Generated:** 2026-08-03T23:27:57.275230

1. wu2024metagenomicinsightsinto pages 1-2
2. ng2023singlestrainbehaviorpredicts pages 1-2
3. ramoneda2023buildingagenomebased pages 3-5
4. liu2024rootcolonizationby pages 3-4
5. blancoromero2023adaptionofpseudomonas pages 1-2
6. ji2023rhizobialmigrationtoward pages 1-2
7. ramoneda2023buildingagenomebased pages 1-1
8. wu2024metagenomicinsightsinto pages 7-9
9. liu2024rootcolonizationby pages 7-8
10. ramoneda2024leveraginggenomicinformation pages 6-7
11. ren2024microbialstrategiesof pages 7-11
12. ramoneda2024leveraginggenomicinformation pages 1-2
13. ramoneda2024leveraginggenomicinformation pages 4-6
14. 10.1126/sciadv.adf8998
15. 10.1128/mbio.00753-23
16. 10.1186/s40168-024-01817-w
17. 10.1093/femsre/fuad066
18. 10.3390/microorganisms11041037
19. 10.1038/s41396-023-01357-5
20. 10.1093/ismejo/wrae195
21. 10.1101/2024.09.17.613589
22. https://doi.org/10.1126/sciadv.adf8998
23. https://doi.org/10.1128/mbio.00753-23
24. https://doi.org/10.1186/s40168-024-01817-w
25. https://doi.org/10.1093/femsre/fuad066
26. https://doi.org/10.3390/microorganisms11041037
27. https://doi.org/10.1038/s41396-023-01357-5
28. https://doi.org/10.1093/ismejo/wrae195
29. https://doi.org/10.1101/2024.09.17.613589
30. https://doi.org/10.1093/ismejo/wrae195,
31. https://doi.org/10.1186/s40168-024-01817-w,
32. https://doi.org/10.1128/mbio.00753-23,
33. https://doi.org/10.3390/microorganisms11041037,
34. https://doi.org/10.1093/femsre/fuad066,
35. https://doi.org/10.1126/sciadv.adf8998,
36. https://doi.org/10.1038/s41396-023-01357-5,
37. https://doi.org/10.1101/2024.09.17.613589,