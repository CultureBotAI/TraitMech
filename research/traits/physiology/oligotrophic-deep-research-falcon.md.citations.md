# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oligotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000654
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A nutrient adaptation characterized by the ability to thrive in environments with very low nutrient concentrations, typically possessing efficient nutrient uptake and utilization systems.
- **Parent traits:** METPO:1000731
- **Synonyms:** TT_oligotroph, oligotroph
- **Existing evidence:** DOI:10.1073/pnas.0903507106: high (copiotrophic) or low (oligotrophic) nutrient concentrations (Comparative genomics paper defines oligotrophy by low-nutrient adaptation.) | DOI:10.1038/ismej.2014.60: nutrients limit growth (Streamlining review links nutrient limitation to small-cell/genome adaptation.) | PMID:16109880: Pelagibacter ubique (Organism example: Pelagibacter ubique HTCC1062 (SAR11 clade) is the archetypal oligotrophic marine bacterium with a streamlined genome adapted to nutrient-poor open-ocean conditions (Giovannoni et al. 2005, Science).)
- **Existing causal graph summary:** oligotrophic_low_nutrient_efficiency: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **oligotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/oligotrophic.yaml`.

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
**Generated:** 2026-08-04T11:42:08.351033

1. noell2023areductionof pages 1-2
2. meyer2024singlecellanalysisreveals pages 1-2
3. zhu2024shapingofmicrobial pages 7-8
4. zhang2024genomereductionoccurred pages 1-5
5. noell2023areductionof pages 4-6
6. noell2023areductionof pages 15-18
7. giovannoni2014implicationsofstreamlining pages 8-9
8. giordano2024genomescalecommunitymodelling pages 1-2
9. giovannoni2014implicationsofstreamlining pages 7-8
10. williams2024novelendolithicbacteria pages 1-2
11. noell2023areductionof pages 8-10
12. marschmann2024predictionsofrhizosphere pages 1-2
13. fink2023microbialpopulationdynamics pages 1-2
14. giovannoni2014implicationsofstreamlining pages 1-2
15. roller2015thephysiologyand pages 5-6
16. fink2023microbialpopulationdynamics pages 7-8
17. marschmann2024predictionsofrhizosphere pages 6-7
18. noell2023areductionof pages 6-8
19. giordano2024genomescalecommunitymodelling pages 9-10
20. 10.1128/mmbr.00124-22
21. 10.1038/ismej.2014.60
22. 10.1101/2023.06.25.546417
23. 10.1038/s41467-024-48591-9
24. 10.1038/s41467-024-46374-w
25. 10.1128/aem.02264-23
26. 10.1038/s41564-023-01582-w
27. 10.1128/aem.00446-24
28. 10.1073/pnas.2207295120
29. 10.1038/ismej.2014.235
30. https://doi.org/10.1128/mmbr.00124-22
31. https://doi.org/10.1038/ismej.2014.60
32. https://doi.org/10.1101/2023.06.25.546417
33. https://doi.org/10.1038/s41467-024-48591-9
34. https://doi.org/10.1038/s41467-024-46374-w
35. https://doi.org/10.1128/aem.02264-23
36. https://doi.org/10.1038/s41564-023-01582-w
37. https://doi.org/10.1128/aem.00446-24
38. https://doi.org/10.1073/pnas.2207295120
39. https://doi.org/10.1038/ismej.2014.235
40. https://doi.org/10.1128/mmbr.00124-22,
41. https://doi.org/10.1073/pnas.2207295120,
42. https://doi.org/10.1128/aem.00446-24,
43. https://doi.org/10.1038/s41467-024-48591-9,
44. https://doi.org/10.1038/ismej.2014.60,
45. https://doi.org/10.1101/2023.06.25.546417,
46. https://doi.org/10.1038/s41467-024-46374-w,
47. https://doi.org/10.1128/aem.02264-23,
48. https://doi.org/10.1038/s41564-023-01582-w,
49. https://doi.org/10.1038/ismej.2014.235,