# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** capsule
- **METPO identifier:** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **capsule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/capsule.yaml`.

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
**Generated:** 2026-06-18T06:50:52.955104

1. gao2024bacterialcapsulesoccurrence pages 1-3
2. gao2024bacterialcapsulesoccurrence pages 3-5
3. gao2024bacterialcapsulesoccurrence pages 7-8
4. gao2024bacterialcapsulesoccurrence pages 9-10
5. petchiappan2024rcsfindependentmechanismsof pages 1-2
6. yang2025identificationofa pages 1-2
7. cheetham2024specificityanddiversity pages 1-2
8. gao2024bacterialcapsulesoccurrence pages 8-9
9. xu2024klebsiellapneumoniaecapsular pages 11-12
10. ascari2025recentinsightsinto pages 1-2
11. gao2024bacterialcapsulesoccurrence pages 5-7
12. nguyen2025howklebsiellapneumoniae pages 15-16
13. gao2024bacterialcapsulesoccurrence pages 3-3
14. nguyen2025howklebsiellapneumoniae pages 8-10
15. nguyen2025howklebsiellapneumoniae pages 4-5
16. nguyen2025howklebsiellapneumoniae pages 16-17
17. nguyen2025howklebsiellapneumoniae pages 5-8
18. https://doi.org/10.1038/s41522-024-00497-6
19. https://doi.org/10.1371/journal.pgen.1011408
20. https://doi.org/10.1128/msystems.00262-24
21. https://doi.org/10.1128/jb.00387-24
22. https://doi.org/10.1042/EBC20240015
23. https://doi.org/10.1080/21505594.2024.2439509
24. https://doi.org/10.1128/jb.00417-24
25. https://doi.org/10.1038/s41522-024-00497-6,
26. https://doi.org/10.1128/jb.00417-24,
27. https://doi.org/10.1101/2024.08.29.610257,
28. https://doi.org/10.1128/msystems.00262-24,
29. https://doi.org/10.1128/jb.00387-24,
30. https://doi.org/10.1042/ebc20240015,
31. https://doi.org/10.1371/journal.ppat.1013499,
32. https://doi.org/10.1080/21505594.2024.2439509,