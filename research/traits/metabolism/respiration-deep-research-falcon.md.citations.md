# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/respiration.yaml`.

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
**Generated:** 2026-08-04T07:07:26.010438

1. little2024dietaryandhostderived pages 1-3
2. simon2008theorganisationof pages 1-3
3. dyksma2023oxygenrespirationand pages 1-2
4. sina2024persistentactivityof pages 1-2
5. wikstrom2018oxygenactivationand pages 1-2
6. diao2023globaldiversityand pages 1-2
7. little2024dietaryandhostderived pages 3-4
8. ford2024theelectrontransport pages 1-2
9. shaw2025independentlyevolvedextracellular pages 1-2
10. soares2025toolsforenhancing pages 1-2
11. burton2025electrontransportacross pages 18-19
12. soares2025toolsforenhancing pages 5-8
13. braissant2020areviewof pages 1-2
14. soares2025toolsforenhancing pages 4-5
15. soares2025toolsforenhancing pages 2-4
16. soares2025toolsforenhancing pages 9-11
17. little2024dietaryandhostderived pages 31-33
18. 10.1038/s41564-023-01560-2
19. 10.1016/j.bbabio.2008.09.008
20. 10.3390/ijms252413421
21. 10.1021/acs.chemrev.7b00664
22. 10.1128/aem.01387-23
23. oxidizing
24. 10.1038/s41467-023-42074-z
25. 10.1093/femsre/fuad058
26. 10.1038/s41467-024-49602-5
27. 10.1093/ismejo/wraf097
28. 10.3390/fermentation11070381
29. https://doi.org/10.1038/s41564-023-01560-2
30. https://doi.org/10.1016/j.bbabio.2008.09.008
31. https://doi.org/10.3390/ijms252413421
32. https://doi.org/10.1021/acs.chemrev.7b00664
33. https://doi.org/10.1128/aem.01387-23
34. https://doi.org/10.1038/s41467-023-42074-z
35. https://doi.org/10.1093/femsre/fuad058
36. https://doi.org/10.1038/s41467-024-49602-5
37. https://doi.org/10.1093/ismejo/wraf097
38. https://doi.org/10.3390/fermentation11070381
39. https://doi.org/10.1038/s41564-023-01560-2,
40. https://doi.org/10.1016/j.bbabio.2008.09.008,
41. https://doi.org/10.1038/s41467-023-42074-z,
42. https://doi.org/10.1038/s41467-024-49602-5,
43. https://doi.org/10.1021/acs.chemrev.7b00664,
44. https://doi.org/10.1128/aem.01387-23,
45. https://doi.org/10.1093/femsre/fuad058,
46. https://doi.org/10.1093/ismejo/wraf097,
47. https://doi.org/10.3390/fermentation11070381,
48. https://doi.org/10.3389/fmicb.2020.547458,
49. https://doi.org/10.3390/ijms252413421,
50. https://doi.org/10.1146/annurev-biochem-052621-092202,