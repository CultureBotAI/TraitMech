# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mobile genetic element
- **METPO identifier:** traitmech:000089
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of DNA segments that can move within or between genomes and mediate horizontal gene transfer, including plasmids, prophages, transposable elements, and genomic islands.
- **Parent traits:** METPO:1000188
- **Synonyms:** MGE
- **Existing evidence:** DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic elements as the agents of horizontal gene transfer and genome plasticity; parent of the plasmid, prophage, transposable- element, and genomic-island sub-variants.) | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion sequences as a major class of mobile genetic elements shaping bacterial genomes.)
- **Existing causal graph summary:** mge_horizontal_gene_transfer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mobile genetic element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/mobile_genetic_element.yaml`.

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
**Generated:** 2026-06-18T03:59:13.885214

1. weisberg2023mobilegeneticelement pages 1-2
2. tokuda2024microbialevolutionthrough pages 1-3
3. weisberg2023mobilegeneticelement pages 2-4
4. lee2024genomicanalysisof pages 1-2
5. aresarroyo2023originsoftransfer pages 1-2
6. botelho2023defensesystemsare pages 2-3
7. botelho2023defensesystemsare pages 1-2
8. tokuda2024microbialevolutionthrough pages 3-4
9. mazzamurro2024intragenomicconflictswith pages 10-12
10. botelho2023theeskapemobilome pages 13-15
11. audrey2023asystematicapproach pages 6-8
12. ali2024integronsinthe pages 9-10
13. daveri2023characterizationofan pages 1-2
14. fahy2024fromspeciesto pages 4-5
15. tokuda2024microbialevolutionthrough pages 4-5
16. audrey2023asystematicapproach pages 1-2
17. fahy2024fromspeciesto pages 2-4
18. botelho2023theeskapemobilome pages 1-2
19. uncertain/general
20. anti-phage defense
21. uncertain/taxon-specific
22. https://doi.org/10.1128/AEM.01360-24;
23. https://doi.org/10.1093/nar/gkad024;
24. https://doi.org/10.1128/IAI.00436-22;
25. https://doi.org/10.1111/1751-7915.14408;
26. https://doi.org/10.3390/antibiotics13070661;
27. https://doi.org/10.1146/annurev-micro-032521-022006;
28. https://doi.org/10.1093/nar/gkad282;
29. https://doi.org/10.1093/nar/gkae489;
30. https://doi.org/10.1093/nar/gkad644;
31. https://doi.org/10.1093/nar/gkac1079;
32. https://doi.org/10.1371/journal.pbio.3002814;
33. https://doi.org/10.1146/annurev-micro-032521-022006
34. https://doi.org/10.1093/nar/gkad282
35. https://doi.org/10.1093/nar/gkac1220
36. https://doi.org/10.1093/nar/gkad024
37. https://doi.org/10.1093/nar/gkad644
38. https://doi.org/10.1093/nar/gkac1079
39. https://doi.org/10.1128/AEM.01360-24
40. https://doi.org/10.1093/nar/gkad935
41. https://doi.org/10.1111/1751-7915.14408
42. https://doi.org/10.3390/antibiotics13070661
43. https://doi.org/10.3390/microorganisms12122579
44. https://doi.org/10.1371/journal.pbio.3002814
45. https://doi.org/10.1093/nar/gkae489
46. https://doi.org/10.1146/annurev-micro-032521-022006,
47. https://doi.org/10.1111/1751-7915.14408,
48. https://doi.org/10.1093/nar/gkad282,
49. https://doi.org/10.3390/antibiotics13070661,
50. https://doi.org/10.1128/aem.01360-24,
51. https://doi.org/10.1093/nar/gkad935,
52. https://doi.org/10.1093/nar/gkad024,
53. https://doi.org/10.1093/nar/gkac1079,
54. https://doi.org/10.1093/nar/gkad644,
55. https://doi.org/10.1371/journal.pbio.3002814,
56. https://doi.org/10.1093/nar/gkac1220,
57. https://doi.org/10.3390/microorganisms12122579,