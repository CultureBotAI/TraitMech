# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Anaerobic respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **Anaerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_respiration.yaml`.

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
**Generated:** 2026-08-04T05:42:42.014439

1. marbehan2024combiningmetabolicflux pages 1-2
2. bueno2012bacterialadaptationof pages 1-2
3. stolz2006arsenicandselenium pages 2-3
4. hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2
5. richter2012dissimilatoryreductionof pages 1-2
6. little2024dietaryandhostderived pages 1-3
7. price2021bacterialapproachesto pages 6-8
8. price2021bacterialapproachesto pages 8-9
9. little2024dietaryandhostderived pages 3-4
10. wimalaweera2024enhancingrubberindustry pages 1-2
11. little2024dietaryandhostderived pages 9-11
12. hassan2024arseniccontaminationof pages 11-13
13. perchikov2024microbialbiofilmsfeatures pages 1-3
14. price2021bacterialapproachesto pages 11-12
15. little2024dietaryandhostderived pages 31-33
16. little2024dietaryandhostderived pages 8-9
17. little2024dietaryandhostderived pages 4-6
18. 4Fe-4S
19. 2Fe-2S
20. 10.1038/s41564-023-01560-2
21. 10.3389/fmicb.2024.1336360
22. 10.3390/membranes14060130
23. 10.3390/bios14060302
24. 10.3390/toxics12010089
25. 10.1111/mmi.14795
26. 10.1111/1462-2920.15293
27. 10.1038/s41396-018-0077-1
28. 10.1128/AEM.06803-11
29. 10.1089/ars.2011.4051
30. 10.1146/annurev.micro.60.080805.142053
31. 10.1128/MMBR.61.4.533-616.1997
32. https://doi.org/10.1038/s41564-023-01560-2
33. https://doi.org/10.3389/fmicb.2024.1336360
34. https://doi.org/10.3390/membranes14060130
35. https://doi.org/10.3390/bios14060302
36. https://doi.org/10.3390/toxics12010089
37. https://doi.org/10.1111/mmi.14795
38. https://doi.org/10.1111/1462-2920.15293
39. https://doi.org/10.1038/s41396-018-0077-1
40. https://doi.org/10.1128/AEM.06803-11
41. https://doi.org/10.1089/ars.2011.4051
42. https://doi.org/10.1146/annurev.micro.60.080805.142053
43. https://doi.org/10.1128/MMBR.61.4.533-616.1997
44. https://doi.org/10.1038/s41564-023-01560-2,
45. https://doi.org/10.1089/ars.2011.4051,
46. https://doi.org/10.1111/mmi.14795,
47. https://doi.org/10.3389/fmicb.2024.1336360,
48. https://doi.org/10.1146/annurev.micro.60.080805.142053,
49. https://doi.org/10.1038/s41396-018-0077-1,
50. https://doi.org/10.1128/aem.06803-11,
51. https://doi.org/10.1111/1462-2920.15293,
52. https://doi.org/10.3390/membranes14060130,
53. https://doi.org/10.3390/toxics12010089,
54. https://doi.org/10.3390/bios14060302,