# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithotrophic
- **METPO identifier:** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **chemolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithotrophic.yaml`.

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
**Generated:** 2026-06-18T11:24:42.811514

1. chen2024adaptationmechanismsof pages 1-2
2. cornell2024genomeencodedmetabolicpotential pages 15-18
3. han2024adaptivetraitsof pages 9-11
4. cornell2024genomeencodedmetabolicpotential pages 13-15
5. bayer2024contributionofammonia pages 1-4
6. wang2024characterizethegrowth pages 1-2
7. boersma2024metagenomicanalysisof pages 1-4
8. beaver2024microbialecologyof pages 2-3
9. twible2024phandthiosulfate pages 1-2
10. rudenko2024mechanismofintracellular pages 12-13
11. li2024yeeelikebacterialsoxt pages 1-2
12. zhou2023effectsofacidification pages 6-7
13. rudenko2024mechanismofintracellular pages 10-12
14. zhou2023effectsofacidification pages 1-2
15. wang2024characterizethegrowth pages 13-15
16. li2024arcobacteraceaeareubiquitous pages 1-2
17. barla2024sustainablesynergisticapproach pages 1-2
18. barla2024sustainablesynergisticapproach pages 3-4
19. zhang2023microbedrivenelementalcycling pages 4-6
20. barla2024sustainablesynergisticapproach pages 7-8
21. yan2024characterizationofsulfur pages 59-63
22. twible2024phandthiosulfate pages 5-6
23. cornell2024genomeencodedmetabolicpotential pages 86-89
24. zhou2023effectsofacidification pages 5-6
25. li2024yeeelikebacterialsoxt pages 7-8
26. wang2024characterizethegrowth pages 22-23
27. barla2024sustainablesynergisticapproach pages 2-3
28. li2024arcobacteraceaeareubiquitous pages 10-12
29. Fe(II)
30. s
31. NiFe
32. https://doi.org/10.3389/fmicb.2024.1426584
33. https://doi.org/10.3390/ijms252010962
34. https://doi.org/10.1038/s42003-024-07270-7
35. https://doi.org/10.3389/fmars.2024.1491690
36. https://doi.org/10.1128/mbio.02169-24
37. https://doi.org/10.21203/rs.3.rs-4032669/v1?
38. https://doi.org/10.1101/2024.11.16.623942
39. https://doi.org/10.1038/s41467-023-37104-9
40. https://doi.org/10.3390/microorganisms12030590
41. https://doi.org/10.1016/j.jbc.2024.107703
42. https://doi.org/10.1093/femsec/fiae105
43. https://doi.org/10.1128/msystems.00513-24
44. https://doi.org/10.1038/s41598-024-67053-2
45. https://doi.org/10.1093/ismejo/wrae091
46. https://doi.org/10.1101/2024.12.25.630300
47. https://doi.org/10.1186/s40168-023-01601-2
48. https://doi.org/10.3389/fmars.2024.1491690,
49. https://doi.org/10.1038/s41467-023-37104-9,
50. https://doi.org/10.1128/mbio.02169-24,
51. https://doi.org/10.3390/microorganisms12030590,
52. https://doi.org/10.1016/j.jbc.2024.107703,
53. https://doi.org/10.3389/fmicb.2024.1426584,
54. https://doi.org/10.1128/msystems.00513-24,
55. https://doi.org/10.1093/ismejo/wrae091,
56. https://doi.org/10.1093/femsec/fiae105,
57. https://doi.org/10.1038/s41598-024-67053-2,
58. https://doi.org/10.1101/2024.11.16.623942,
59. https://doi.org/10.3390/ijms252010962,
60. https://doi.org/10.1186/s40168-023-01601-2,
61. https://doi.org/10.1038/s42003-024-07270-7,
62. https://doi.org/10.1101/2024.12.25.630300,