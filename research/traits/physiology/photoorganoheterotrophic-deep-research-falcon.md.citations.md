# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoorganoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000659
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-809633-8.20672-9: light-induced redox chemistry (Phototrophy chapter supports light-driven reaction-center electron transfer.) | DOI:10.1021/acsomega.3c02205: photoorganoheterotrophic (Review table classifies photoorganoheterotrophy by light with organic electron and carbon sources.)
- **Existing causal graph summary:** photoorganoheterotrophic_light_organic_electrons: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **photoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoorganoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T12:05:42.338475

1. thiel2018diversityofchlorophototrophic pages 10-11
2. larimer2004completegenomesequence pages 1-2
3. dhar2023anoxygenicphototrophicpurple pages 1-3
4. tinguely2023diurnalcyclesdrive pages 2-2
5. thiel2018diversityofchlorophototrophic pages 2-3
6. edreira2024elucidatingmetabolictuning pages 1-2
7. bryant2006prokaryoticphotosynthesisand pages 2-3
8. oh2024effectoflight pages 13-14
9. tinguely2023diurnalcyclesdrive pages 1-2
10. tinguely2023diurnalcyclesdrive pages 9-10
11. edreira2024elucidatingmetabolictuning pages 5-6
12. wada2023valorizationofpurple pages 1-2
13. sepulvedamunoz2023wastewatertreatmentusing pages 14-15
14. dhar2023anoxygenicphototrophicpurple pages 14-15
15. oh2024effectoflight pages 1-2
16. edreira2024elucidatingmetabolictuning pages 9-10
17. oh2024effectoflight pages 14-15
18. sepulvedamunoz2023wastewatertreatmentusing pages 1-2
19. wada2023valorizationofpurple pages 11-12
20. 10.1038/nbt923
21. 10.1093/femsec/fiae090
22. 10.1146/annurev-arplant-042817-040500
23. 10.1016/j.tim.2006.09.001
24. 10.1038/s43705-022-00201-9
25. 10.1038/s43705-023-00334-5
26. 10.4014/jmb.2410.10034
27. 10.1038/s42003-024-07188-0
28. 10.1007/s13399-023-04518-w
29. 10.3390/sym15020525
30. 10.1007/s11274-023-03729-7
31. https://doi.org/10.1038/nbt923
32. https://doi.org/10.1093/femsec/fiae090
33. https://doi.org/10.1146/annurev-arplant-042817-040500
34. https://doi.org/10.1016/j.tim.2006.09.001
35. https://doi.org/10.1038/s43705-022-00201-9
36. https://doi.org/10.1038/s43705-023-00334-5
37. https://doi.org/10.4014/jmb.2410.10034
38. https://doi.org/10.1038/s42003-024-07188-0
39. https://doi.org/10.1007/s13399-023-04518-w
40. https://doi.org/10.3390/sym15020525
41. https://doi.org/10.1007/s11274-023-03729-7
42. https://doi.org/10.1016/j.tim.2006.09.001,
43. https://doi.org/10.1146/annurev-arplant-042817-040500,
44. https://doi.org/10.4014/jmb.2410.10034,
45. https://doi.org/10.1038/nbt923,
46. https://doi.org/10.1038/s43705-023-00334-5,
47. https://doi.org/10.1038/s42003-024-07188-0,
48. https://doi.org/10.1007/s11274-023-03729-7,
49. https://doi.org/10.3390/sym15020525,
50. https://doi.org/10.1007/s13399-023-04518-w,
51. https://doi.org/10.1038/s43705-022-00201-9,