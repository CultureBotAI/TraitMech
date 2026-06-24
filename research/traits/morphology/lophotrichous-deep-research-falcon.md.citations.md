# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lophotrichous
- **METPO identifier:** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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
**Generated:** 2026-06-18T08:40:21.606783

1. park2024bundlinginstabilityof pages 2-3
2. schuhmacher2015howbacteriamaintain pages 2-4
3. schuhmacher2015howbacteriamaintain pages 5-7
4. arroyoperez2024aconservedcellpole pages 2-3
5. schuhmacher2015howbacteriamaintain pages 7-8
6. guan2024flhfaffectsthe pages 1-2
7. arroyoperez2024aconservedcellpole pages 14-15
8. schuhmacher2015howbacteriamaintain pages 4-5
9. guan2024flhfaffectsthe pages 2-6
10. fast2026swimmingpatternsof pages 1-2
11. dornes2024polarconfinementof pages 1-2
12. park2024bundlinginstabilityof pages 1-2
13. schuhmacher2015howbacteriamaintain pages 8-9
14. arroyoperez2024aconservedcellpole pages 1-2
15. arroyoperez2024aconservedcellpole pages 3-6
16. pradhan2024thebacterialdivision pages 4-8
17. guan2024flhfaffectsthe pages 6-8
18. pradhan2024thebacterialdivision pages 1-2
19. s
20. https://doi.org/10.7554/elife.93004.3,
21. https://doi.org/10.1093/femsre/fuv034,
22. https://doi.org/10.1038/s41467-024-50274-4,
23. https://doi.org/10.1016/j.jbc.2024.107117,
24. https://doi.org/10.1128/aem.01548-23,
25. https://doi.org/10.1016/j.bpj.2026.05.032,
26. https://doi.org/10.1063/5.0228395,
27. https://doi.org/10.7554/elife.93004.3
28. https://doi.org/10.1038/s41467-024-50274-4
29. https://doi.org/10.1128/aem.01548-23
30. https://doi.org/10.1016/j.jbc.2024.107117
31. https://doi.org/10.1063/5.0228395
32. https://doi.org/10.1093/femsre/fuv034