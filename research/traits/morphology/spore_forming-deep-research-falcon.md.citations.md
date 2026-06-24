# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spore forming
- **METPO identifier:** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

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
**Generated:** 2026-06-18T09:52:24.719093

1. bidnenko2024complexsporulationspecificexpression pages 17-17
2. rawson2023pathogenicityandvirulence pages 26-28
3. feaga2023elongationfactorp pages 1-2
4. updegrove2024altruisticfeedingand pages 9-10
5. bidnenko2024complexsporulationspecificexpression pages 17-18
6. matavacas2023proteostasisinbacillus pages 21-25
7. updegrove2024altruisticfeedingand pages 2-3
8. updegrove2024altruisticfeedingand pages 1-2
9. feaga2023elongationfactorp pages 2-4
10. updegrove2024altruisticfeedingand pages 4-5
11. label; ENVO candidate unavailable
12. label
13. label/UniProt candidate
14. label/UniProt candidates
15. GO candidate
16. label/GO molecular function candidate
17. labels
18. METPO:1000871
19. CHEBI candidate if available
20. GO/label
21. GO/CHEBI candidate
22. label/CHEBI candidate
23. https://doi.org/10.3390/microbiolres14020035
24. https://doi.org/10.1016/j.jbc.2024.107905
25. https://doi.org/10.1128/jb.00370-22
26. https://doi.org/10.1080/21505594.2023.2205251
27. https://doi.org/10.1126/sciadv.adq0791
28. https://doi.org/10.3390/microbiolres14020035,
29. https://doi.org/10.1016/j.jbc.2024.107905,
30. https://doi.org/10.1080/21505594.2023.2205251,
31. https://doi.org/10.1128/jb.00370-22,
32. https://doi.org/10.1126/sciadv.adq0791,