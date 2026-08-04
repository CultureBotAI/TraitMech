# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** capsule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 11 nodes, 8 edges

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
**Generated:** 2026-08-04T07:38:34.534271

1. gao2024bacterialcapsulesoccurrence pages 1-3
2. gao2024bacterialcapsulesoccurrence pages 3-3
3. whitfield2020assemblyofbacterial pages 5-6
4. whitfield2020assemblyofbacterial pages 9-10
5. kuklewicz2024molecularinsightsinto pages 1-2
6. kuklewicz2024molecularinsightsinto pages 2-3
7. lee2024singlemissensemutations pages 1-2
8. gao2024bacterialcapsulesoccurrence pages 9-10
9. haudiquet2024capsulesandtheir pages 1-2
10. roberts1996thebiochemistryand pages 1-3
11. whitfield2020assemblyofbacterial pages 2-4
12. whitfield2020assemblyofbacterial pages 1-2
13. rendueles2020decipheringtherole pages 2-4
14. whitfield2020assemblyofbacterial pages 7-9
15. whitfield2020assemblyofbacterial pages 10-11
16. cheetham2024specificityanddiversity pages 1-2
17. lee2024singlemissensemutations pages 5-6
18. yang2025identificationofa pages 1-2
19. haudiquet2024capsulesandtheir pages 2-3
20. https://doi.org/10.1146/annurev.micro.50.1.285
21. https://doi.org/10.1146/annurev-micro-011420-075607
22. https://doi.org/10.1038/s41586-024-07248-9
23. https://doi.org/10.1038/s41522-024-00497-6
24. https://doi.org/10.1038/s41467-024-46147-5
25. https://doi.org/10.1038/s41467-024-49590-6
26. https://doi.org/10.1042/EBC20240015
27. https://doi.org/10.1128/jb.00387-24
28. https://doi.org/10.1146/annurev.micro.50.1.285,
29. https://doi.org/10.1146/annurev-micro-011420-075607,
30. https://doi.org/10.1038/s41522-024-00497-6,
31. https://doi.org/10.1038/s41586-024-07248-9,
32. https://doi.org/10.1111/mmi.14474,
33. https://doi.org/10.1038/s41467-024-49590-6,
34. https://doi.org/10.1128/jb.00387-24,
35. https://doi.org/10.1038/s41467-024-46147-5,
36. https://doi.org/10.1042/ebc20240015,