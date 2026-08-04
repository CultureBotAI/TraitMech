# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 15 nodes, 10 edges

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
**Generated:** 2026-08-04T11:04:30.246931

1. taubert2022bolsteringfitnessvia pages 1-2
2. wang2024characterizethegrowth pages 22-23
3. wright2023nitrificationandbeyond pages 1-2
4. bayer2024contributionofammonia pages 1-4
5. wright2023nitrificationandbeyond pages 3-5
6. laufermeiser2024oxidationofsulfur pages 4-6
7. zeldes2019determinantsofsulfur pages 1-5
8. claassens2020phosphoglycolatesalvagein pages 1-2
9. laufermeiser2024oxidationofsulfur pages 1-2
10. kucera2020amodelof pages 1-2
11. srivastava2023interplaybetweenautotrophic pages 5-7
12. srivastava2023interplaybetweenautotrophic pages 1-2
13. esparza2010genesandpathways pages 1-2
14. asplundsamuelsson2021widerangeof pages 1-2
15. tonietti2024unveilingthebioleaching pages 1-2
16. cozma2024biorecoveryofmetals pages 1-2
17. kucera2020amodelof pages 4-8
18. NiFe
19. 10.1093/ismejo/wrae173
20. 10.3390/microorganisms12030590
21. 10.3390/microorganisms12122407
22. 10.3390/pr12091793
23. 10.1101/2024.11.16.623942
24. 10.1038/s41396-023-01467-0
25. 10.1186/s40168-023-01688-7
26. 10.1038/s41396-021-01163-x
27. 10.1371/journal.pcbi.1008742
28. 10.3389/fmicb.2020.610836
29. 10.1073/pnas.2012288117
30. 10.1128/AEM.01344-19
31. 10.1111/1462-2920.14712
32. 10.1186/1471-2180-10-229
33. https://doi.org/10.1093/ismejo/wrae173
34. https://doi.org/10.3390/microorganisms12030590
35. https://doi.org/10.3390/microorganisms12122407
36. https://doi.org/10.3390/pr12091793
37. https://doi.org/10.1101/2024.11.16.623942
38. https://doi.org/10.1038/s41396-023-01467-0
39. https://doi.org/10.1186/s40168-023-01688-7
40. https://doi.org/10.1038/s41396-021-01163-x
41. https://doi.org/10.1371/journal.pcbi.1008742
42. https://doi.org/10.3389/fmicb.2020.610836
43. https://doi.org/10.1073/pnas.2012288117
44. https://doi.org/10.1128/AEM.01344-19
45. https://doi.org/10.1111/1462-2920.14712
46. https://doi.org/10.1186/1471-2180-10-229
47. https://doi.org/10.1093/ismejo/wrae173,
48. https://doi.org/10.1101/2024.11.16.623942,
49. https://doi.org/10.1128/aem.01344-19,
50. https://doi.org/10.1038/s41396-021-01163-x,
51. https://doi.org/10.3390/microorganisms12030590,
52. https://doi.org/10.1038/s41396-023-01467-0,
53. https://doi.org/10.3389/fmicb.2020.610836,
54. https://doi.org/10.1111/1462-2920.14712,
55. https://doi.org/10.1186/s40168-023-01688-7,
56. https://doi.org/10.1371/journal.pcbi.1008742,
57. https://doi.org/10.1186/1471-2180-10-229,
58. https://doi.org/10.1073/pnas.2012288117,
59. https://doi.org/10.3390/microorganisms12122407,
60. https://doi.org/10.3390/pr12091793,