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
- **Existing causal graph summary:** codon_bias_translation_efficiency: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:19:55.759901

1. farookhi2024differentialselectionfor pages 1-2
2. cope2024evolutionaryprinciplesunderpinning pages 11-14
3. plotkin2011synonymousbutnot pages 4-5
4. plotkin2011synonymousbutnot pages 2-3
5. hershberg2008selectiononcodon pages 2-3
6. nieuwkoop2023revealingdeterminantsof pages 1-1
7. mitchener2023molecularcopingmechanisms pages 1-2
8. mitchener2023molecularcopingmechanisms pages 4-5
9. yared2024beyondtheanticodon pages 11-12
10. delgado2024impactofthe pages 2-4
11. hoffmann2024temperaturedependenttrnamodifications pages 9-10
12. soman2023codonoptimalityhas pages 1-2
13. mitchener2023molecularcopingmechanisms pages 5-6
14. delgado2024impactofthe pages 7-8
15. plotkin2011synonymousbutnot pages 6-7
16. fan2024genrcaauserfriendly pages 3-5
17. johnson2023growthdependentgeneexpression pages 13-15
18. farookhi2024differentialselectionfor pages 19-21
19. johnson2023growthdependentgeneexpression pages 6-8
20. nieuwkoop2023revealingdeterminantsof pages 7-8
21. nieuwkoop2023revealingdeterminantsof pages 8-9
22. nieuwkoop2023revealingdeterminantsof pages 1-2
23. nieuwkoop2023revealingdeterminantsof pages 12-13
24. delgado2024impactofthe pages 6-7
25. hoffmann2024temperaturedependenttrnamodifications pages 1-2
26. hoffmann2024temperaturedependenttrnamodifications pages 17-19
27. fan2024genrcaauserfriendly pages 1-3
28. fan2024genrcaauserfriendly pages 5-8
29. cope2024evolutionaryprinciplesunderpinning pages 8-11
30. delgado2024impactofthe pages 1-2
31. johnson2023growthdependentgeneexpression pages 8-10
32. mitchener2023molecularcopingmechanisms pages 2-4
33. yared2024beyondtheanticodon pages 8-10
34. hoffmann2024temperaturedependenttrnamodifications pages 6-9
35. hoffmann2024temperaturedependenttrnamodifications pages 13-14
36. hoffmann2024temperaturedependenttrnamodifications pages 19-20
37. mitchener2023molecularcopingmechanisms pages 7-8
38. johnson2023growthdependentgeneexpression pages 1-3
39. johnson2023growthdependentgeneexpression pages 10-11
40. nieuwkoop2023revealingdeterminantsof pages 6-7
41. delgado2024impactofthe pages 4-6
42. hoffmann2024temperaturedependenttrnamodifications pages 10-11
43. nieuwkoop2023revealingdeterminantsof pages 9-10
44. fan2024genrcaauserfriendly pages 8-9
45. https://doi.org/10.1038/nrg2899
46. https://doi.org/10.1146/annurev.genet.42.110807.091442
47. https://doi.org/10.1146/annurev.genet.42.110807.091442;
48. https://doi.org/10.32942/x2802v
49. https://doi.org/10.1093/molbev/msad189
50. https://doi.org/10.3390/microorganisms12040768
51. https://doi.org/10.1038/nrg2899;
52. https://doi.org/10.1038/s41598-022-27164-0
53. https://doi.org/10.1093/nar/gkad035
54. https://doi.org/10.1021/acs.accounts.3c00572;
55. https://doi.org/10.3389/fmicb.2024.1412318
56. https://doi.org/10.1021/acs.accounts.3c00572
57. https://doi.org/10.3390/genes15030374
58. https://doi.org/10.3390/ijms25168823
59. https://doi.org/10.1186/s12859-024-05934-z
60. https://doi.org/10.1038/nrg2899,
61. https://doi.org/10.1093/nar/gkad035,
62. https://doi.org/10.3390/microorganisms12040768,
63. https://doi.org/10.32942/x2802v,
64. https://doi.org/10.1186/s12859-024-05934-z,
65. https://doi.org/10.1093/molbev/msad189,
66. https://doi.org/10.1146/annurev.genet.42.110807.091442,
67. https://doi.org/10.1021/acs.accounts.3c00572,
68. https://doi.org/10.3390/genes15030374,
69. https://doi.org/10.3389/fmicb.2024.1412318,
70. https://doi.org/10.3390/ijms25168823,
71. https://doi.org/10.1038/s41598-022-27164-0,