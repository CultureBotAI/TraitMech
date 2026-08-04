# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** white pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003029
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear white or nonpigmented because visible chromophore accumulation is absent or low.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_white
- **Existing evidence:** DOI:10.2147/IDR.S49039: white phenotypic variant of Staphylococcus aureus (Supports white colony appearance as a microbial pigmentation phenotype tied to absent or inducible staphyloxanthin production in a representative bacterium.)
- **Existing causal graph summary:** white_pigmented_low_chromophore: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **white pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/white_pigmented.yaml`.

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
**Generated:** 2026-08-04T10:36:00.908807

1. xiang2022transcriptomicanalysisreveals pages 1-2
2. painter2015staphylococcusaureusadapts pages 20-23
3. campbell2023variablestaphyloxanthinproduction pages 17-19
4. esteves2024serratiamarcescensatcc pages 8-9
5. campbell2023variablestaphyloxanthinproduction pages 30-38
6. campbell2023variablestaphyloxanthinproduction pages 8-10
7. nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11
8. campbell2023variablestaphyloxanthinproduction pages 38-41
9. nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2
10. nirmala2024enhancingstaphyloxanthinsynthesis pages 2-5
11. campbell2023variablestaphyloxanthinproduction pages 1-3
12. 10.1016/j.celrep.2023.113281
13. ing
14. 10.1038/s41598-024-68747-3
15. 10.7759/cureus.59892
16. 10.1186/s12866-022-02515-z
17. 10.3389/fmicb.2021.793202
18. 10.1128/IAI.03016-14
19. https://doi.org/10.1016/j.celrep.2023.113281
20. https://doi.org/10.1038/s41598-024-68747-3
21. https://doi.org/10.7759/cureus.59892
22. https://doi.org/10.1186/s12866-022-02515-z
23. https://doi.org/10.3389/fmicb.2021.793202
24. https://doi.org/10.1128/IAI.03016-14
25. https://doi.org/10.3389/fmicb.2021.793202,
26. https://doi.org/10.1016/j.celrep.2023.113281,
27. https://doi.org/10.1128/iai.03016-14,
28. https://doi.org/10.1038/s41598-024-68747-3,
29. https://doi.org/10.7759/cureus.59892,