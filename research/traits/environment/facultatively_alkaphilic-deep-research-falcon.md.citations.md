# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively alkaphilic
- **METPO identifier:** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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
**Generated:** 2026-06-17T22:33:27.632864

1. kevbrin2019isolationandcultivation pages 1-4
2. matsuno2018formationofproton pages 4-5
3. preiss2015alkaliphilicbacteriawith pages 4-5
4. kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 88-91
5. preiss2015alkaliphilicbacteriawith pages 3-4
6. wang2023characterizationoftwo pages 7-8
7. horikoshi2016alkaliphiles pages 2-5
8. jong2024quantitativeproteomicsreveals pages 1-2
9. kim2024lineagespecificevolutionof pages 1-2
10. horikoshi2016alkaliphiles pages 6-8
11. horikoshi2016alkaliphiles pages 8-9
12. horikoshi2016alkaliphiles pages 9-11
13. preiss2015alkaliphilicbacteriawith pages 2-3
14. xing2024thepolyextremophilenatranaerobius pages 19-21
15. matsuno2018formationofproton pages 1-2
16. wang2023characterizationoftwo pages 10-12
17. goto2022differencesinbioenergetic pages 1-2
18. matsuno2018formationofproton pages 3-4
19. kanekar2022alkaliphilicalkalitolerantmicroorganisms pages 97-99
20. METPO:1003005
21. label-only
22. CHEBI:3311 for H+ context; label-only for condition
23. GO:0015385 candidate / label-only
24. mrpABCDEFG; GO:0015385 candidate / label-only
25. mrpABCDEFG
26. CHEBI:29101
27. CHEBI:15378
28. GO:0006885 candidate / label-only
29. label-only gene
30. GO:0046933 candidate / label-only
31. GO:0006754 candidate / label-only
32. CHEBI:15378 / label-only process
33. label-only; GO:0015385 candidate
34. CHEBI:29101, CHEBI:30145, CHEBI:29103
35. ENVO:09200000 candidate / label-only
36. NCBITaxon:label-only
37. https://doi.org/10.1007/10_2018_84
38. https://doi.org/10.3389/fbioe.2015.00075
39. https://doi.org/10.1007/978-981-19-1573-4_3
40. https://doi.org/10.3389/fmicb.2018.02331
41. https://doi.org/10.3389/fmicb.2025.1637315
42. https://doi.org/10.3390/ijms241310786
43. https://doi.org/10.1128/aem.00145-24
44. https://doi.org/10.1128/aem.02091-23
45. https://doi.org/10.3389/fmicb.2024.1468929
46. https://doi.org/10.1007/978-4-431-55408-0_4
47. https://doi.org/10.1007/10\_2018\_84,
48. https://doi.org/10.1007/978-4-431-55408-0\_4,
49. https://doi.org/10.3389/fbioe.2015.00075,
50. https://doi.org/10.1007/978-981-19-1573-4\_3,
51. https://doi.org/10.3389/fmicb.2018.02331,
52. https://doi.org/10.3390/ijms241310786,
53. https://doi.org/10.3389/fmicb.2024.1468929,
54. https://doi.org/10.1128/aem.02091-23,
55. https://doi.org/10.3389/fmicb.2025.1637315,
56. https://doi.org/10.3389/fmicb.2022.842785,
57. https://doi.org/10.1128/aem.00145-24,