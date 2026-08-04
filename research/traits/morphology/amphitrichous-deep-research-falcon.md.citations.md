# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** amphitrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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
**Generated:** 2026-08-04T07:16:26.381533

1. schuhmacher2015howbacteriamaintain pages 5-7
2. burnham2020apolarflagellar pages 2-4
3. dornes2024polarconfinementof pages 2-4
4. dornes2024polarconfinementof pages 7-8
5. arroyoperez2024aconservedcellpole pages 14-15
6. arroyoperez2024aconservedcellpole pages 12-14
7. grognot2021morethanpropellers pages 4-5
8. grognot2021morethanpropellers pages 5-7
9. grognot2021morethanpropellers pages 1-2
10. grognot2021morethanpropellers pages 2-4
11. schuhmacher2015howbacteriamaintain pages 2-4
12. schuhmacher2015howbacteriamaintain pages 4-5
13. burnham2020apolarflagellar pages 7-9
14. and
15. 10.1111/mmi.14120
16. 10.1093/femsre/fuv034
17. 10.1128/mBio.03107-19
18. 10.1038/s41467-024-50274-4
19. 10.7554/eLife.93004.3
20. 10.3390/microorganisms11030634
21. 10.1016/j.mib.2021.02.005
22. https://doi.org/10.1111/mmi.14120
23. https://doi.org/10.1093/femsre/fuv034
24. https://doi.org/10.1128/mBio.03107-19
25. https://doi.org/10.1038/s41467-024-50274-4
26. https://doi.org/10.7554/eLife.93004.3
27. https://doi.org/10.3390/microorganisms11030634
28. https://doi.org/10.1016/j.mib.2021.02.005
29. https://doi.org/10.1111/mmi.14120,
30. https://doi.org/10.1016/j.mib.2021.02.005,
31. https://doi.org/10.1093/femsre/fuv034,
32. https://doi.org/10.7554/elife.93004.3,
33. https://doi.org/10.1128/mbio.03107-19,
34. https://doi.org/10.1038/s41467-024-50274-4,