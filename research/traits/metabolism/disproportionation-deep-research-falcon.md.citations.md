# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Disproportionation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 14 nodes, 15 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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
**Generated:** 2026-08-04T06:09:07.872564

1. wang2023disproportionationofinorganic pages 15-17
2. guo2016sulfurmetabolismpathways pages 7-8
3. finster2013completegenomesequence pages 1-2
4. thamdrup1993bacterialdisproportionationof pages 1-2
5. wang2023disproportionationofinorganic pages 9-12
6. wang2023disproportionationofinorganic pages 1-2
7. hashimoto2022physiologicalandcomparative pages 12-13
8. hashimoto2022physiologicalandcomparative pages 7-9
9. hashimoto2022physiologicalandcomparative pages 9-10
10. wang2023disproportionationofinorganic pages 12-13
11. wang2023disproportionationofinorganic pages 7-9
12. thamdrup1993bacterialdisproportionationof pages 5-6
13. kanao2024tetrathionatehydrolasefrom pages 1-2
14. canfield1998isotopefractionationand pages 1-2
15. vliet2021thebacterialsulfur pages 13-14
16. canfield1998isotopefractionationand pages 7-8
17. kanao2024tetrathionatehydrolasefrom pages 3-4
18. hashimoto2022physiologicalandcomparative pages 6-7
19. wang2023disproportionationofinorganic pages 2-4
20. thamdrup1993bacterialdisproportionationof pages 3-4
21. canfield1998isotopefractionationand pages 9-10
22. Fe(III)
23. Mn(IV)
24. 10.1128/msystems.00954-22
25. 10.3389/fmicb.2024.1338669
26. 10.3389/fmicb.2022.1042116
27. 10.4056/sigs.3777412
28. 10.1128/AEM.59.1.101-108.1993
29. 10.4319/lo.1998.43.2.0253
30. 10.3389/fmicb.2016.01861
31. 10.1111/1462-2920.15265
32. 10.1080/17415990802105770
33. https://doi.org/10.1128/msystems.00954-22
34. https://doi.org/10.3389/fmicb.2024.1338669
35. https://doi.org/10.3389/fmicb.2022.1042116
36. https://doi.org/10.4056/sigs.3777412
37. https://doi.org/10.1128/AEM.59.1.101-108.1993
38. https://doi.org/10.4319/lo.1998.43.2.0253
39. https://doi.org/10.3389/fmicb.2016.01861
40. https://doi.org/10.1111/1462-2920.15265
41. https://doi.org/10.1080/17415990802105770
42. https://doi.org/10.1128/aem.59.1.101-108.1993,
43. https://doi.org/10.4056/sigs.3777412,
44. https://doi.org/10.1128/msystems.00954-22,
45. https://doi.org/10.3389/fmicb.2022.1042116,
46. https://doi.org/10.4319/lo.1998.43.2.0253,
47. https://doi.org/10.3389/fmicb.2016.01861,
48. https://doi.org/10.3389/fmicb.2024.1338669,
49. https://doi.org/10.1111/1462-2920.15265,