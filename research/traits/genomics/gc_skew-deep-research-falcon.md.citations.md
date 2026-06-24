# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC skew
- **METPO identifier:** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC skew** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_skew.yaml`.

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
**Generated:** 2026-06-18T03:34:47.476585

1. grigoriev1998analyzinggenomeswith pages 1-2
2. mottez2023structuringeffectsof pages 1-4
3. mottez2023structuringeffectsof pages 4-11
4. meel2024orcapredictingreplication pages 4-6
5. sahu2024highnucleotideskew pages 1-3
6. paravel2026ontheorigins pages 2-3
7. paravel2026ontheorigins pages 6-7
8. grigoriev1998analyzinggenomeswith pages 2-4
9. paravel2026ontheorigins pages 1-2
10. meel2024orcapredictingreplication pages 1-4
11. cumsille2023genovianopensource pages 1-2
12. cumsille2023genovianopensource pages 2-4
13. paravel2026ontheorigins pages 3-4
14. mclean1998basecompositionskews pages 1-2
15. grigoriev1998analyzinggenomeswith pages 4-4
16. mottez2023structuringeffectsof pages 11-12
17. sahu2024highnucleotideskewa pages 17-18
18. https://doi.org/10.1101/2023.11.15.567178;
19. https://doi.org/10.3389/fmicb.2026.1727296
20. https://doi.org/10.1101/2023.11.15.567178
21. https://doi.org/10.3389/fmicb.2026.1727296;
22. https://doi.org/10.1007/pl00006428
23. https://doi.org/10.1093/nar/26.10.2286
24. https://doi.org/10.1101/2024.03.28.587133
25. https://doi.org/10.1371/journal.pcbi.1010998
26. https://doi.org/10.1007/s00239-024-10202-y
27. https://doi.org/10.1093/nar/26.10.2286,
28. https://doi.org/10.1101/2023.11.15.567178,
29. https://doi.org/10.3389/fmicb.2026.1727296,
30. https://doi.org/10.1101/2024.03.28.587133,
31. https://doi.org/10.1371/journal.pcbi.1010998,
32. https://doi.org/10.1007/s00239-024-10202-y,
33. https://doi.org/10.1007/pl00006428,
34. https://doi.org/10.48550/arxiv.2407.13260,