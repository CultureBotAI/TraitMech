# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** radiotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives doses of ionizing and/or ultraviolet radiation that are lethal to most microorganisms, typically via efficient DNA repair and oxidative-damage protection.
- **Parent traits:** METPO:1000059
- **Synonyms:** radioresistant
- **Existing evidence:** DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Review of extreme radiation resistance supports manganese-antioxidant protection of the proteome as a core radiotolerance mechanism in Deinococcus radiodurans, "a champion of extreme radiation resistance".) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans tolerates ionizing radiation, UV radiation, and desiccation.)
- **Existing causal graph summary:** radiotolerance_repair_antioxidant: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **radiotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/radiotolerant.yaml`.

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
**Generated:** 2026-08-04T03:21:23.701944

1. pal2024unravelingradiationresistance pages 1-2
2. krisko2013biologyofextreme pages 4-6
3. guo2023developmentandregulation pages 1-2
4. chen2023memoryeffecton pages 1-2
5. rai2024anovelionizing pages 7-8
6. rai2024anovelionizing pages 13-14
7. rai2024anovelionizing pages 8-9
8. basu2012gammaradiationinducedproteome pages 3-5
9. munteanu2015recentprogressin pages 4-5
10. subramani2023involvementofnucleotide pages 7-9
11. subramani2023involvementofnucleotide pages 5-7
12. subramani2023involvementofnucleotide pages 9-10
13. subramani2023involvementofnucleotide pages 1-2
14. 10.1371/journal.pone.0304810
15. 10.1128/spectrum.03474-22
16. 10.1101/cshperspect.a012765
17. 10.1128/aem.01538-23
18. 10.1074/mcp.M111.011734
19. 10.1007/s00792-015-0759-9
20. 10.3390/genes14091803
21. 10.3390/ijms25010421
22. https://doi.org/10.1371/journal.pone.0304810
23. https://doi.org/10.1128/spectrum.03474-22
24. https://doi.org/10.1101/cshperspect.a012765
25. https://doi.org/10.1128/aem.01538-23
26. https://doi.org/10.1074/mcp.M111.011734
27. https://doi.org/10.1007/s00792-015-0759-9
28. https://doi.org/10.3390/genes14091803
29. https://doi.org/10.3390/ijms25010421
30. https://doi.org/10.1101/cshperspect.a012765,
31. https://doi.org/10.1128/spectrum.03474-22,
32. https://doi.org/10.1371/journal.pone.0304810,
33. https://doi.org/10.1128/aem.01538-23,
34. https://doi.org/10.1007/s00792-015-0759-9,
35. https://doi.org/10.1074/mcp.m111.011734,
36. https://doi.org/10.3390/genes14091803,
37. https://doi.org/10.3390/ijms25010421,