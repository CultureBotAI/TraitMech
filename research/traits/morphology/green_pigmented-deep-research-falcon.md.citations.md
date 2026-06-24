# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** green pigmented
- **METPO identifier:** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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
**Generated:** 2026-06-18T08:24:06.072850

1. herr2024commonfluorescentpseudomonas pages 1-6
2. mudaliar2024abiomedicalperspective pages 4-6
3. mendoza2024thehistidinekinase pages 2-5
4. manko2024pvdlorchestratesthe pages 1-2
5. manko2024pvdlorchestratesthe pages 2-5
6. zhang2024amultimodalnonlinear pages 11-16
7. puja2024biosynthesisofa pages 1-2
8. faisal2024effectofantibiotics pages 1-2
9. jassim2024anticanceractivityof pages 1-2
10. almuhawish2024productionandantibacterial pages 1-2
11. herr2024commonfluorescentpseudomonas pages 52-55
12. mendoza2024thehistidinekinase pages 1-2
13. sotoaceves2024therelationshipbetween pages 2-4
14. sotoaceves2024therelationshipbetween pages 6-8
15. herr2024commonfluorescentpseudomonas pages 27-31
16. mudaliar2024abiomedicalperspective pages 1-4
17. CHEBI:candidate
18. label-only candidate
19. METPO:1003025
20. GO:candidate
21. label-only gene cluster
22. gene/protein, label-only
23. label-only
24. GO:0009372
25. histidine kinase, label-only
26. ENVO:candidate
27. s
28. NCBITaxon:candidate group
29. https://doi.org/10.1186/s12934-023-02122-1
30. https://doi.org/10.1007/s11274-023-03548-w
31. https://doi.org/10.1128/jb.00276-23
32. https://doi.org/10.1128/jb.00138-24
33. https://doi.org/10.3390/ijms25116013
34. https://doi.org/10.1101/2024.04.26.591271
35. https://doi.org/10.1002/jbio.202300384
36. https://doi.org/10.1007/s11274-024-03889-0
37. https://doi.org/10.1186/s12934-024-02472-4
38. https://doi.org/10.31018/jans.v16i2.5590
39. https://doi.org/10.3390/ph17091126
40. https://doi.org/10.31018/jans.v16i2.5506
41. https://doi.org/10.1186/s12934-023-02122-1,
42. https://doi.org/10.1101/2024.04.26.591271,
43. https://doi.org/10.1002/jbio.202300384,
44. https://doi.org/10.1007/s11274-023-03548-w,
45. https://doi.org/10.1007/s11274-024-03889-0,
46. https://doi.org/10.1128/jb.00276-23,
47. https://doi.org/10.3390/ijms25116013,
48. https://doi.org/10.1128/jb.00138-24,
49. https://doi.org/10.1186/s12934-024-02472-4,
50. https://doi.org/10.31018/jans.v16i2.5590,
51. https://doi.org/10.31018/jans.v16i2.5506,
52. https://doi.org/10.3390/ph17091126,