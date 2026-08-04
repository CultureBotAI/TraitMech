# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Oxidative phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000803
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that generates ATP through the transfer of electrons from electron donors to electron acceptors via redox reactions, coupled to the pumping of protons across a membrane to create an electrochemical gradient.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/191144a0: phosphorylation to electron and hydrogen transfer (Mitchell's chemiosmotic proposal supports coupling electron transfer to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)
- **Existing causal graph summary:** oxidative_phosphorylation_chemiosmotic_coupling: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **Oxidative phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxidative_phosphorylation.yaml`.

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
**Generated:** 2026-08-04T06:45:43.890499

1. sawers2019anaerobicnitraterespiration pages 1-2
2. kao2022quinonebindingsites pages 1-3
3. muller2018electronbifurcationa pages 1-2
4. bajeli2020terminalrespiratoryoxidases pages 1-2
5. mulkidjanian2008thepastand pages 1-2
6. tsviklist2022thecpxstress pages 1-2
7. harrison2024remissionspectroscopyresolves pages 1-4
8. borisov2023cytochromebdas pages 1-3
9. kracke2015microbialelectrontransport pages 1-2
10. laux2024livinginmangroves pages 1-2
11. kuhlbrandt2019structureandmechanisms pages 1-2
12. sorescu2025breakthroughsinthe pages 24-25
13. 10.3390/ijms252413421
14. s
15. es
16. 10.1101/2024.12.03.626386
17. 10.1186/s12866-024-03390-6
18. 10.3390/ijms24065417
19. 10.1134/S0026893323060031
20. 10.3389/fmicb.2022.965620
21. 10.1042/BST20190963
22. 10.3389/fmicb.2021.732288
23. 10.3389/fcimb.2020.589318
24. 10.1111/1758-2229.12781
25. 10.1146/annurev-biochem-013118-110903
26. 10.1146/annurev-micro-090816-093440
27. 10.3389/fmicb.2015.00575
28. 10.1146/annurev-biochem-060614-034124
29. 10.1016/j.bbabio.2008.04.028
30. https://doi.org/10.3390/ijms252413421
31. https://doi.org/10.1101/2024.12.03.626386
32. https://doi.org/10.1186/s12866-024-03390-6
33. https://doi.org/10.3390/ijms24065417
34. https://doi.org/10.1134/S0026893323060031
35. https://doi.org/10.3389/fmicb.2022.965620
36. https://doi.org/10.1042/BST20190963
37. https://doi.org/10.3389/fmicb.2021.732288
38. https://doi.org/10.3389/fcimb.2020.589318
39. https://doi.org/10.1111/1758-2229.12781
40. https://doi.org/10.1146/annurev-biochem-013118-110903
41. https://doi.org/10.1146/annurev-micro-090816-093440
42. https://doi.org/10.3389/fmicb.2015.00575
43. https://doi.org/10.1146/annurev-biochem-060614-034124
44. https://doi.org/10.1016/j.bbabio.2008.04.028
45. https://doi.org/10.3389/fmicb.2021.732288,
46. https://doi.org/10.3390/ijms24065417,
47. https://doi.org/10.1111/1758-2229.12781,
48. https://doi.org/10.1042/bst20190963,
49. https://doi.org/10.1146/annurev-micro-090816-093440,
50. https://doi.org/10.3390/ijms252413421,
51. https://doi.org/10.3389/fcimb.2020.589318,
52. https://doi.org/10.1134/s0026893323060031,
53. https://doi.org/10.1016/j.bbabio.2008.04.028,
54. https://doi.org/10.3389/fmicb.2022.965620,
55. https://doi.org/10.1101/2024.12.03.626386,
56. https://doi.org/10.1146/annurev-biochem-060614-034124,
57. https://doi.org/10.3389/fmicb.2015.00575,
58. https://doi.org/10.1080/10409238.2025.2545785,
59. https://doi.org/10.1186/s12866-024-03390-6,
60. https://doi.org/10.1146/annurev-biochem-013118-110903,