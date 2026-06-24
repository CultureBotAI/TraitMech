# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copiotrophic
- **METPO identifier:** METPO:1000642
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A nutrient adaptation in which an organism thrives in environments with high nutrient concentrations, typically exhibiting rapid growth rates and utilizing diverse carbon sources.
- **Parent traits:** METPO:1000731
- **Synonyms:** copiotroph
- **Existing evidence:** DOI:10.1073/pnas.0903507106: high (copiotrophic) or low (oligotrophic) nutrient concentrations (Comparative genomics paper defines copiotrophic growth strategy by high-nutrient adaptation.) | DOI:10.1002/bies.1091: common in environments with greater nutritional opportunities (Essay contrasts copiotrophs with oligotrophs in nutrient-rich environments.)
- **Existing causal graph summary:** copiotrophic_high_nutrient_fast_growth: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **copiotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/copiotrophic.yaml`.

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
**Generated:** 2026-06-18T11:30:32.083008

1. couso2023ecologytheorydisentangles pages 1-4
2. wang2023bacterialgenomesize pages 6-7
3. zhang2024antarcticsoilsselect pages 1-2
4. dragone2024taxonomicandgenomic pages 3-4
5. serwecinska2024sewagesludgefertilization pages 1-2
6. he2025microbiallifehistorystrategies pages 6-8
7. zhu2024shapingofmicrobial pages 7-8
8. zhu2024shapingofmicrobial pages 5-7
9. demin2025oligotrophyandorganic pages 1-3
10. demin2025oligotrophyandorganic pages 14-19
11. lauro2009thegenomicbasis pages 1-2
12. serwecinska2024sewagesludgefertilization pages 10-10
13. dragone2024taxonomicandgenomic pages 8-10
14. lauro2009thegenomicbasis pages 2-3
15. lori2023soilmicrobialcommunities pages 6-8
16. he2025microbiallifehistorystrategies pages 8-11
17. serwecinska2024sewagesludgefertilization pages 5-7
18. dragone2024taxonomicandgenomic pages 7-8
19. he2025microbiallifehistorystrategies pages 1-2
20. label-only high nutrient environment
21. label-only
22. approx.
23. broad
24. genus
25. https://doi.org/10.1111/1462-2920.16495
26. https://doi.org/10.1093/ismeco/ycae081
27. https://doi.org/10.1038/s41598-024-71656-0
28. https://doi.org/10.1128/msystems.00178-25
29. https://doi.org/10.3390/microorganisms12081689
30. https://doi.org/10.1093/ismeco/ycae081;
31. https://doi.org/10.1073/pnas.0903507106
32. https://doi.org/10.1101/2025.11.25.690425
33. https://doi.org/10.1186/s40168-025-02182-y
34. https://doi.org/10.1038/s41467-023-43297-w
35. https://doi.org/10.1038/s41467-024-48591-9
36. https://doi.org/10.1186/s40168-024-01762-8
37. https://doi.org/10.1093/femsec/fiad046
38. https://doi.org/10.1002/bies.1091
39. https://doi.org/10.1111/1462-2920.16495,
40. https://doi.org/10.1073/pnas.0903507106,
41. https://doi.org/10.1093/ismeco/ycae081,
42. https://doi.org/10.1038/s41467-024-48591-9,
43. https://doi.org/10.1038/s41467-023-43297-w,
44. https://doi.org/10.3390/microorganisms12081689,
45. https://doi.org/10.1038/s41598-024-71656-0,
46. https://doi.org/10.1128/msystems.00178-25,
47. https://doi.org/10.1101/2025.11.25.690425,
48. https://doi.org/10.1093/femsec/fiad046,