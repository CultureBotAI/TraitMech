# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** codon usage bias
- **METPO identifier:** traitmech:000096
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing non-uniform usage of synonymous codons across a genome, shaped by mutational bias and translational selection and correlated with gene expression level.
- **Parent traits:** METPO:1000188
- **Synonyms:** codon bias
- **Existing evidence:** DOI:10.1038/nrg2899:  (Plotkin & Kudla review the causes and consequences of synonymous codon bias.) | DOI:10.1146/annurev.genet.42.110807.091442:  (Hershberg & Petrov review selection on codon bias across genomes.)
- **Existing causal graph summary:** codon_bias_translation_efficiency: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **codon usage bias** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/codon_usage_bias.yaml`.

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
**Generated:** 2026-06-30T00:55:24.244921

1. labella2019variationandselection pages 1-2
2. hanson2018codonoptimalitybias pages 1-2
3. liu2021synonymousbutnot pages 6-7
4. delgado2024impactofthe pages 1-2
5. sharp2005variationinthe pages 7-7
6. rocha2004codonusagebias pages 2-3
7. duviau2023whentranslationelongation pages 11-13
8. hanson2018codonoptimalitybias pages 6-7
9. liu2021synonymousbutnot pages 11-12
10. rocha2004codonusagebias pages 1-2
11. sharp2005variationinthe pages 10-10
12. plotkin2011synonymousbutnot pages 2-3
13. sharp2005variationinthe pages 6-7
14. duviau2023whentranslationelongation pages 1-2
15. liu2021synonymousbutnot pages 16-17
16. delgado2024impactofthe pages 4-6
17. carbone2005codonbiassignatures pages 13-13
18. sharp2005variationinthe pages 1-2
19. liu2021synonymousbutnot pages 7-9
20. liu2021synonymousbutnot pages 9-11
21. liu2021synonymousbutnot pages 26-29
22. duviau2023whentranslationelongation pages 13-14
23. liu2021synonymousbutnot pages 14-16
24. rocha2004codonusagebias pages 4-5
25. carbone2005codonbiassignatures pages 1-1
26. fu2023codonusagebias pages 20-21
27. liu2021synonymousbutnot pages 3-4
28. quax2015codonbiasas pages 7-8
29. hanson2018codonoptimalitybias pages 12-13
30. carbone2005codonbiassignatures pages 15-15
31. sharp2005variationinthe pages 7-8
32. https://doi.org/10.1371/journal.pgen.1008304,
33. https://doi.org/10.1038/nrg2899,
34. https://doi.org/10.1101/gr.2896904,
35. https://doi.org/10.1093/nar/gki242,
36. https://doi.org/10.1038/nrm.2017.91,
37. https://doi.org/10.1146/annurev-biochem-071320-112701,
38. https://doi.org/10.3389/fmicb.2024.1412318,
39. https://doi.org/10.1093/nar/gkad104,
40. https://doi.org/10.1093/molbev/msi040,
41. https://doi.org/10.3390/microorganisms11071833,
42. https://doi.org/10.1016/j.molcel.2015.05.035,