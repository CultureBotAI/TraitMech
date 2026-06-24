# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** symbiosis
- **METPO identifier:** traitmech:000040
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which a microorganism lives in persistent physical association with a host or partner organism. It encompasses mutualism, commensalism, and parasitism, which form an evolutionary continuum.
- **Parent traits:** METPO:1000059
- **Synonyms:** symbiotic
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al., "Animals in a bacterial world", supports persistent host-microbe association (symbiosis) as a pervasive microbial lifestyle; parent of the mutualism/commensalism/parasitism sub-variants.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. frame symbioses as a parasite-mutualist continuum, supporting symbiosis as the umbrella lifestyle for these interaction modes.)
- **Existing causal graph summary:** symbiosis_host_interaction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/symbiosis.yaml`.

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
**Generated:** 2026-06-17T21:03:00.907104

1. wilde2024hostcontrolof pages 15-17
2. liu2024rootcolonizationby pages 1-2
3. wiesmann2023originsofsymbiosis pages 1-2
4. liu2024rootcolonizationby pages 2-3
5. essockburns2023maturationstateof pages 1-2
6. porter2024hostimposedcontrolmechanisms pages 6-7
7. liu2024rootcolonizationby pages 3-4
8. liu2024rootcolonizationby pages 5-5
9. lin2024areviewof pages 9-10
10. wiesmann2023originsofsymbiosis pages 4-5
11. wiesmann2023originsofsymbiosis pages 6-8
12. liu2024rootcolonizationby pages 6-7
13. wiesmann2023originsofsymbiosis pages 2-3
14. lin2024areviewof pages 1-2
15. lin2024areviewof pages 2-5
16. obeng2023bacterialcdigmphas pages 1-2
17. obeng2023bacterialcdigmphas pages 2-3
18. porter2024hostimposedcontrolmechanisms pages 4-5
19. porter2024hostimposedcontrolmechanisms pages 1-3
20. porter2024hostimposedcontrolmechanisms pages 7-8
21. aminov2023theroleof pages 3-4
22. aminov2023theroleof pages 1-2
23. lin2024areviewof pages 17-18
24. aminov2023theroleof pages 5-6
25. liu2024rootcolonizationby pages 4-5
26. lin2024areviewof pages 7-9
27. aminov2023theroleof pages 2-3
28. lin2024areviewof pages 10-11
29. lin2024areviewof pages 6-7
30. aminov2023theroleof pages 4-5
31. liu2024rootcolonizationby pages 5-6
32. porter2024hostimposedcontrolmechanisms pages 10-11
33. porter2024hostimposedcontrolmechanisms pages 8-9
34. lin2024areviewof pages 16-17
35. aminov2023theroleof pages 6-7
36. aminov2023theroleof pages 9-10
37. yang2024mechanismsofrhizosphere pages 1-3
38. https://doi.org/10.1093/femsre/fuac048
39. https://doi.org/10.1093/femsre/fuad066
40. https://doi.org/10.3390/microorganisms12051026
41. https://doi.org/10.1038/s41564-023-01468-x
42. https://doi.org/10.1038/s41564-024-01762-2
43. https://doi.org/10.1093/glycob/cwad073
44. https://doi.org/10.1186/s40168-023-01509-x
45. https://doi.org/10.1007/s44297-024-00038-9
46. https://doi.org/10.1126/science.adi3338
47. https://doi.org/10.1073/pnas.1218525110
48. https://doi.org/10.1093/femsre/fuac048,
49. https://doi.org/10.1126/science.adi3338,
50. https://doi.org/10.3390/microorganisms12051026,
51. https://doi.org/10.1038/s41564-023-01468-x,
52. https://doi.org/10.1038/s41564-024-01762-2,
53. https://doi.org/10.1093/glycob/cwad073,
54. https://doi.org/10.1093/femsre/fuad066,
55. https://doi.org/10.1007/s44297-024-00038-9,
56. https://doi.org/10.1186/s40168-023-01509-x,
57. https://doi.org/10.3389/fpls.2024.1491495,