# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pink pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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
**Generated:** 2026-08-04T09:37:58.683741

1. rizk2021functionaldiversityof pages 2-3
2. ochoavinals2024currentadvancesin pages 1-2
3. florescotera2021decipheringthemechanism pages 1-2
4. rizk2021functionaldiversityof pages 9-11
5. ochoavinals2024currentadvancesin pages 2-5
6. kingkaew2023genomicinsightand pages 1-2
7. 10.1111/mmi.14794
8. 10.3390/fermentation10040190
9. 10.3390/fermentation9060501
10. 10.1093/jimb/kuab048
11. 10.3390/biology12101346
12. 10.1016/j.synbio.2023.08.002
13. 10.1128/AEM.69.12.7563-7566.2003
14. 10.1128/mbio.00985-21
15. 10.1108/AGJSR-03-2023-0127
16. 10.1080/1040841X.2025.2526423
17. https://doi.org/10.1111/mmi.14794
18. https://doi.org/10.3390/fermentation10040190
19. https://doi.org/10.3390/fermentation9060501
20. https://doi.org/10.1093/jimb/kuab048
21. https://doi.org/10.3390/biology12101346
22. https://doi.org/10.1016/j.synbio.2023.08.002
23. https://doi.org/10.1128/AEM.69.12.7563-7566.2003
24. https://doi.org/10.1128/mbio.00985-21
25. https://doi.org/10.1108/AGJSR-03-2023-0127
26. https://doi.org/10.1080/1040841X.2025.2526423
27. https://doi.org/10.1111/mmi.14794,
28. https://doi.org/10.3390/fermentation10040190,
29. https://doi.org/10.1093/jimb/kuab048,
30. https://doi.org/10.3390/fermentation9060501,