# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative oxygen preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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
**Generated:** 2026-08-04T00:42:41.224134

1. andre2021theselectiveadvantage pages 1-2
2. alvarez2024diversificationofsignal pages 14-15
3. lamoureux2023amultiscaleexpression pages 17-17
4. levanon2005effectofoxygen pages 1-2
5. federowicz2014determiningthecontrol pages 7-10
6. sun2023anodeassistedelectrofermentationwith pages 1-2
7. sun2023anodeassistedelectrofermentationwith pages 7-9
8. mrnjavac2024theradicalimpact pages 7-9
9. nastasi2024membraneboundredoxenzyme pages 2-4
10. sun2023anodeassistedelectrofermentationwith pages 5-7
11. borisov2021bacterialoxidasesof pages 18-19
12. bueno2012bacterialadaptationof pages 1-2
13. borisov2015oxygenasacceptor pages 2-4
14. borisov2015oxygenasacceptor pages 11-13
15. nastasi2024membraneboundredoxenzyme pages 4-7
16. sun2023anodeassistedelectrofermentationwith pages 10-11
17. nastasi2024membraneboundredoxenzyme pages 11-13
18. 4Fe–4S
19. 2Fe–2S
20. and
21. 4Fe-4S
22. 2Fe-2S
23. https://doi.org/10.1111/1751-7915.70051
24. https://doi.org/10.1371/journal.pone.0315238
25. https://doi.org/10.1002/1873-3468.14906
26. https://doi.org/10.3390/ijms25021277
27. https://doi.org/10.3390/inorganics11120450
28. https://doi.org/10.1186/s13068-022-02253-4
29. https://doi.org/10.1093/nar/gkad750
30. https://doi.org/10.1128/mmbr.00110-21
31. https://doi.org/10.1111/1462-2920.15293
32. https://doi.org/10.1111/cmi.13338
33. https://doi.org/10.1089/ars.2020.8039
34. https://doi.org/10.1089/ars.2011.4051
35. https://doi.org/10.1371/journal.pgen.1004264
36. https://doi.org/10.1128/ecosalplus.esp-0012-2015
37. https://doi.org/10.1002/bit.20381
38. https://doi.org/10.1073/pnas.94.12.6087
39. https://doi.org/10.1111/1462-2920.15293,
40. https://doi.org/10.1111/cmi.13338,
41. https://doi.org/10.1371/journal.pone.0315238,
42. https://doi.org/10.1093/nar/gkad750,
43. https://doi.org/10.1002/bit.20381,
44. https://doi.org/10.1111/1751-7915.70051,
45. https://doi.org/10.1128/ecosalplus.esp-0012-2015,
46. https://doi.org/10.3390/ijms25021277,
47. https://doi.org/10.1371/journal.pgen.1004264,
48. https://doi.org/10.1186/s13068-022-02253-4,
49. https://doi.org/10.1089/ars.2011.4051,
50. https://doi.org/10.1002/1873-3468.14906,
51. https://doi.org/10.1089/ars.2020.8039,