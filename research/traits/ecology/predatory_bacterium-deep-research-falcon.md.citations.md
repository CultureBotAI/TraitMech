# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** predatory bacterium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **predatory bacterium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/predatory_bacterium.yaml`.

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
**Generated:** 2026-08-03T23:51:28.786278

1. kaplan2023bdellovibriopredationcycle pages 4-6
2. kaplan2023bdellovibriopredationcycle pages 1-3
3. lien2024mechanismofbacterial pages 10-13
4. caulton2024bdellovibriobacteriovorususes pages 4-4
5. caulton2024bdellovibriobacteriovorususes pages 1-2
6. wang2024thepredatoryproperties pages 5-8
7. alexakis2024predatorybacteriain pages 1-2
8. lai2024quantitativeproteomeof pages 1-4
9. avidan2017identificationandcharacterization pages 10-11
10. negus2017predatorversuspathogen pages 2-4
11. kaplan2023bdellovibriopredationcycle pages 3-4
12. mun2023predatorybacteriaas pages 1-2
13. lien2024mechanismofbacterial pages 1-5
14. lien2024mechanismofbacterial pages 13-16
15. wang2024thepredatoryproperties pages 1-2
16. caulton2024bdellovibriobacteriovorususes pages 2-4
17. caulton2024bdellovibriobacteriovorususes pages 8-9
18. lai2024quantitativeproteomeof pages 27-30
19. sester2020secondarymetabolismof pages 34-37
20. wang2024thepredatoryproperties pages 2-4
21. caulton2024bdellovibriobacteriovorususes pages 4-5
22. alexakis2024predatorybacteriain pages 4-5
23. alexakis2024predatorybacteriain pages 14-15
24. mun2023predatorybacteriaas pages 12-13
25. 10.1038/s41564-023-01552-2
26. 10.1126/science.adp0614
27. 10.1038/s41564-023-01401-2
28. 10.3390/microorganisms12102008
29. 10.3390/idr16040052
30. 10.1101/2024.12.23.630089
31. 10.1007/s10068-023-01310-4
32. 10.1038/s41598-017-00951-w
33. 10.1146/annurev-micro-090816-093618
34. 10.1111/1462-2920.13171
35. https://doi.org/10.1038/s41564-023-01552-2
36. https://doi.org/10.1126/science.adp0614
37. https://doi.org/10.1038/s41564-023-01401-2
38. https://doi.org/10.3390/microorganisms12102008
39. https://doi.org/10.3390/idr16040052
40. https://doi.org/10.1101/2024.12.23.630089
41. https://doi.org/10.1007/s10068-023-01310-4
42. https://doi.org/10.1038/s41598-017-00951-w
43. https://doi.org/10.1146/annurev-micro-090816-093618
44. https://doi.org/10.1111/1462-2920.13171
45. https://doi.org/10.1038/s41564-023-01401-2,
46. https://doi.org/10.3390/idr16040052,
47. https://doi.org/10.1007/s10068-023-01310-4,
48. https://doi.org/10.1126/science.adp0614,
49. https://doi.org/10.3390/microorganisms12102008,
50. https://doi.org/10.1146/annurev-micro-090816-093618,
51. https://doi.org/10.1038/s41564-023-01552-2,
52. https://doi.org/10.1101/2024.12.23.630089,
53. https://doi.org/10.1007/978-3-030-45599-6\_5,
54. https://doi.org/10.1038/s41598-017-00951-w,