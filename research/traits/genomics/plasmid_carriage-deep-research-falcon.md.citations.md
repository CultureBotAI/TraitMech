# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plasmid carriage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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
**Generated:** 2026-08-04T05:15:17.631237

1. robertson2023aglobalsurvey pages 1-2
2. dimitriu2024variousplasmidstrategies pages 1-2
3. lobatomarquez2016stabilizationofthe pages 1-2
4. lazdins2020potentiationofcuring pages 1-2
5. toribiocelestino2024aplasmidchromosomecrosstalk pages 1-2
6. rouches2022aplasmidsystem pages 1-2
7. wright2024achromosomalmutation pages 1-2
8. jiang2013dealingwiththe pages 1-2
9. haudiquet2024capsulesandtheir pages 1-2
10. wang2024interplasmidtransferof pages 1-2
11. yang2024evolutionoftriclosan pages 1-2
12. mathers2024developingaframework pages 1-2
13. riva2024conjugalplasmidtransfer pages 1-2
14. liu2024compensatoryevolutionof pages 10-11
15. wright2024achromosomalmutation pages 14-15
16. 10.1093/nar/gkae896
17. 10.1371/journal.pgen.1003844
18. 10.1038/s41467-024-46147-5
19. 10.1038/s41467-024-48006-9
20. 10.1371/journal.pbio.3002926
21. 10.1038/s41467-024-55169-y
22. 10.1093/ismejo/wrad032
23. 10.1099/mgen.0.001002
24. 10.1038/s44259-024-00069-w
25. 10.3389/fmicb.2024.1457854
26. 10.1371/journal.pone.0225202
27. 10.1038/s41467-022-31422-0
28. https://doi.org/10.1093/nar/gkae896
29. https://doi.org/10.1371/journal.pbio.3002926
30. https://doi.org/10.1038/s41467-024-55169-y
31. https://doi.org/10.1038/s41467-024-48006-9
32. https://doi.org/10.1038/s41467-024-46147-5
33. https://doi.org/10.1093/ismejo/wrad032
34. https://doi.org/10.1038/s44259-024-00069-w
35. https://doi.org/10.3389/fmicb.2024.1457854
36. https://doi.org/10.1002/ece3.70121
37. https://doi.org/10.1099/mgen.0.001002
38. https://doi.org/10.1038/s41467-022-31422-0
39. https://doi.org/10.1371/journal.pone.0225202
40. https://doi.org/10.3389/fmolb.2016.00066
41. https://doi.org/10.1371/journal.pgen.1003844
42. https://doi.org/10.1093/nar/gkae896](https://doi.org/10.1093/nar/gkae896
43. https://doi.org/10.1371/journal.pbio.3002926](https://doi.org/10.1371/journal.pbio.3002926
44. https://doi.org/10.1038/s41467-024-55169-y](https://doi.org/10.1038/s41467-024-55169-y
45. https://doi.org/10.1038/s41467-024-48006-9](https://doi.org/10.1038/s41467-024-48006-9
46. https://doi.org/10.1038/s41467-024-46147-5](https://doi.org/10.1038/s41467-024-46147-5
47. https://doi.org/10.1093/ismejo/wrad032](https://doi.org/10.1093/ismejo/wrad032
48. https://doi.org/10.1038/s44259-024-00069-w](https://doi.org/10.1038/s44259-024-00069-w
49. https://doi.org/10.3389/fmicb.2024.1457854](https://doi.org/10.3389/fmicb.2024.1457854
50. https://doi.org/10.1002/ece3.70121](https://doi.org/10.1002/ece3.70121
51. https://doi.org/10.1099/mgen.0.001002](https://doi.org/10.1099/mgen.0.001002
52. https://doi.org/10.1038/s41467-022-31422-0](https://doi.org/10.1038/s41467-022-31422-0
53. https://doi.org/10.1371/journal.pone.0225202](https://doi.org/10.1371/journal.pone.0225202
54. https://doi.org/10.3389/fmolb.2016.00066](https://doi.org/10.3389/fmolb.2016.00066
55. https://doi.org/10.1371/journal.pgen.1003844](https://doi.org/10.1371/journal.pgen.1003844
56. https://doi.org/10.1099/mgen.0.001002,
57. https://doi.org/10.1093/nar/gkae896,
58. https://doi.org/10.3389/fmolb.2016.00066,
59. https://doi.org/10.1371/journal.pone.0225202,
60. https://doi.org/10.1038/s41467-024-55169-y,
61. https://doi.org/10.1038/s41467-022-31422-0,
62. https://doi.org/10.1371/journal.pbio.3002926,
63. https://doi.org/10.1371/journal.pgen.1003844,
64. https://doi.org/10.1038/s41467-024-46147-5,
65. https://doi.org/10.1093/ismejo/wrad032,
66. https://doi.org/10.1038/s41467-024-48006-9,
67. https://doi.org/10.1038/s44259-024-00069-w,
68. https://doi.org/10.3389/fmicb.2024.1457854,
69. https://doi.org/10.1002/ece3.70121,