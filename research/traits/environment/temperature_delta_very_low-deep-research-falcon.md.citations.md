# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta very low
- **METPO identifier:** METPO:1000483
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 1–5 °C, characteristic of stenothermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_1_5
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very narrow thermal-tolerance breadths as the stenothermal phenotype with limited membrane-remodeling flexibility.)
- **Existing causal graph summary:** temperature_delta_very_low_stenothermal: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_very_low.yaml`.

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
**Generated:** 2026-06-18T02:17:04.214216

1. costello2023theuniversalevolutionary pages 3-4
2. hurtadobautista2024thermalplasticityand pages 16-17
3. ramon2023ageneraloverview pages 4-5
4. ramon2023ageneraloverview pages 2-4
5. moon2023temperaturemattersbacterial pages 3-5
6. mendoza2014temperaturesensingby pages 5-6
7. moon2023temperaturemattersbacterial pages 7-9
8. sidarta2024lipidphaseseparation pages 1-2
9. mendoza2014temperaturesensingby pages 6-8
10. hoogerland2024atemperaturesensitivemetabolic pages 2-3
11. hoogerland2024atemperaturesensitivemetabolic pages 5-6
12. hoogerland2024atemperaturesensitivemetabolic pages 9-10
13. moon2023temperaturemattersbacterial pages 14-15
14. dessenne2024lipidomicanalysesreveal pages 1-2
15. hurtadobautista2024thermalplasticityand pages 1-2
16. hurtadobautista2024thermalplasticityand pages 2-3
17. sidarta2024lipidphaseseparation pages 12-14
18. moon2023temperaturemattersbacterial pages 1-3
19. hoogerland2024atemperaturesensitivemetabolic pages 3-4
20. moon2023temperaturemattersbacterial pages 12-13
21. hoogerland2024atemperaturesensitivemetabolic pages 1-2
22. hoogerland2024atemperaturesensitivemetabolic pages 4-5
23. mendoza2014temperaturesensingby pages 14-15
24. label
25. approximate if needed
26. not direct; avoid if curating strictly
27. candidate
28. is
29. approximate
30. RNase R, candidate
31. generic
32. https://doi.org/10.1146/annurev-micro-091313-103612;
33. https://doi.org/10.1128/spectrum.03925-23
34. https://doi.org/10.1146/annurev-micro-091313-103612
35. https://doi.org/10.1007/s12275-023-00031-x
36. https://doi.org/10.1007/s42770-023-01057-4
37. https://doi.org/10.1007/s42770-023-01057-4;
38. https://doi.org/10.1038/s41467-024-53677-5
39. https://doi.org/10.1111/mmi.15323
40. https://doi.org/10.3390/biology13121088
41. https://doi.org/10.1038/s41467-024-53677-5;
42. https://doi.org/10.21425/f5fbg61673
43. https://doi.org/10.1128/spectrum.00757-24
44. https://doi.org/10.21425/f5fbg61673,
45. https://doi.org/10.3390/biology13121088,
46. https://doi.org/10.1128/spectrum.03925-23,
47. https://doi.org/10.1007/s12275-023-00031-x,
48. https://doi.org/10.1007/s42770-023-01057-4,
49. https://doi.org/10.1111/mmi.15323,
50. https://doi.org/10.1146/annurev-micro-091313-103612,
51. https://doi.org/10.1038/s41467-024-53677-5,
52. https://doi.org/10.1128/spectrum.00757-24,