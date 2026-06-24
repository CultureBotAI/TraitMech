# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellar arrangement
- **METPO identifier:** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T07:51:39.049318

1. kumar2016syntheticcysticfibrosis pages 1-2
2. schuhmacher2015howbacteriamaintain pages 2-4
3. dornes2024polarconfinementof pages 2-4
4. dornes2024polarconfinementof pages 1-2
5. schuhmacher2015howbacteriamaintain pages 4-5
6. dornes2024polarconfinementof pages 4-6
7. kumar2016syntheticcysticfibrosis pages 4-7
8. schuhmacher2015howbacteriamaintain pages 7-8
9. dornes2024polarconfinementof pages 6-7
10. schuhmacher2015howbacteriamaintain pages 5-7
11. schuhmacher2015howbacteriamaintain pages 8-9
12. pulianmackal2024positioningofcellular pages 4-6
13. schuhmacher2015howbacteriamaintain pages 1-2
14. pulianmackal2024positioningofcellular pages 3-4
15. pulianmackal2024positioningofcellular pages 12-14
16. s
17. https://doi.org/10.1038/s41467-024-50274-4
18. https://doi.org/10.1093/femsre/fuv034
19. https://doi.org/10.1016/j.mib.2024.102485
20. https://doi.org/10.3389/fcimb.2016.00065
21. https://doi.org/10.1038/s41467-024-50274-4,
22. https://doi.org/10.1093/femsre/fuv034,
23. https://doi.org/10.3389/fcimb.2016.00065,
24. https://doi.org/10.1016/j.mib.2024.102485,