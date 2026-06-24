# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** predatory bacterium
- **METPO identifier:** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 3 nodes, 2 edges

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
**Generated:** 2026-06-17T21:11:36.353480

1. kaplan2023bdellovibriopredationcycle pages 1-3
2. kaplan2023bdellovibriopredationcycle pages 3-4
3. kaplan2023bdellovibriopredationcycle pages 6-7
4. caulton2024bdellovibriobacteriovorususes pages 1-2
5. tyson2024preykillingwithout pages 1-2
6. santin2024lifecycleofa pages 1-4
7. das2024howdogramnegative pages 3-4
8. das2024howdogramnegative pages 4-6
9. xi2024evaluationofthe pages 10-11
10. mohsenipour2024predationonbacterial pages 8-10
11. mohsenipour2024predationonbacterial pages 6-8
12. rosberg2024regulationofantibiotic pages 3-7
13. salgado2024controllingtheexpression pages 12-14
14. alexakis2024predatorybacteriain pages 1-2
15. wang2024thepredatoryproperties pages 1-2
16. mookherjee2024flagellarstatorgenes pages 13-15
17. caulton2024bdellovibriobacteriovorususes pages 8-9
18. salgado2024controllingtheexpression pages 1-2
19. das2024howdogramnegative pages 3-3
20. mohsenipour2024predationonbacterial pages 1-2
21. rosberg2024regulationofantibiotic pages 7-9
22. salgado2024controllingtheexpression pages 7-8
23. salgado2024controllingtheexpression pages 14-15
24. https://doi.org/10.1038/s41564-023-01401-2
25. https://doi.org/10.1038/s41467-024-47412-3
26. https://doi.org/10.1038/s41564-023-01552-2
27. https://doi.org/10.1101/2023.10.25.563945
28. https://doi.org/10.1038/s44259-024-00048-1
29. https://doi.org/10.1007/s00253-024-13250-y
30. https://doi.org/10.1038/s41598-024-63418-9
31. https://doi.org/10.1186/s12866-024-03672-z
32. https://doi.org/10.3390/antibiotics13080750
33. https://doi.org/10.1111/1751-7915.14517
34. https://doi.org/10.1111/1462-2920.13171
35. https://doi.org/10.1111/1462-2920.13171,
36. https://doi.org/10.1038/s41564-023-01401-2,
37. https://doi.org/10.1101/2023.10.25.563945,
38. https://doi.org/10.3390/idr16040052,
39. https://doi.org/10.3390/microorganisms12102008,
40. https://doi.org/10.1128/mbio.00715-24,
41. https://doi.org/10.1038/s41564-023-01552-2,
42. https://doi.org/10.1038/s41467-024-47412-3,
43. https://doi.org/10.1038/s44259-024-00048-1,
44. https://doi.org/10.1111/1751-7915.14517,
45. https://doi.org/10.1186/s12866-024-03672-z,
46. https://doi.org/10.1007/s00253-024-13250-y,
47. https://doi.org/10.1038/s41598-024-63418-9,
48. https://doi.org/10.3390/antibiotics13080750,