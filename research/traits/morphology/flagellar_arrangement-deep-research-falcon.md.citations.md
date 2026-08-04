# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellar arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **flagellar arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellar_arrangement.yaml`.

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
**Generated:** 2026-08-04T08:25:38.405873

1. dornes2024polarconfinementof pages 2-4
2. arroyoperez2024aconservedcellpole pages 1-2
3. schuhmacher2015howbacteriamaintain pages 8-9
4. gibson2023controlofthe pages 11-13
5. dornes2024polarconfinementof pages 4-6
6. dornes2024polarconfinementof pages 7-8
7. gibson2023controlofthe pages 1-2
8. arroyoperez2024aconservedcellpole pages 14-15
9. arroyoperez2024aconservedcellpole pages 8-11
10. arroyoperez2024aconservedcellpole pages 12-14
11. dornes2024polarconfinementof pages 1-2
12. arroyoperez2024aconservedcellpole pages 2-3
13. dornes2024polarconfinementof pages 6-7
14. arroyoperez2024aconservedcellpole pages 11-12
15. rossmann2017spatialregulationof pages 117-120
16. 10.1038/s41467-024-50274-4
17. 10.1128/JB.00236-20
18. 10.1093/femsre/fuv034
19. es
20. 10.1128/JB.00110-23
21. caused
22. 10.7554/eLife.93004.3
23. 10.3389/fmicb.2021.655239
24. 10.1128/mBio.02286-19
25. 10.1128/mBio.03107-19
26. https://doi.org/10.1038/s41467-024-50274-4
27. https://doi.org/10.1128/JB.00236-20
28. https://doi.org/10.1093/femsre/fuv034
29. https://doi.org/10.1128/JB.00110-23
30. https://doi.org/10.7554/eLife.93004.3
31. https://doi.org/10.3389/fmicb.2021.655239
32. https://doi.org/10.1128/mBio.02286-19
33. https://doi.org/10.1128/mBio.03107-19
34. https://doi.org/10.7554/elife.93004.3,
35. https://doi.org/10.1038/s41467-024-50274-4,
36. https://doi.org/10.1093/femsre/fuv034,
37. https://doi.org/10.1128/jb.00110-23,
38. https://doi.org/10.17192/z2017.0061,