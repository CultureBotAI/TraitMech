# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** radiotolerant
- **METPO identifier:** traitmech:000007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives doses of ionizing and/or ultraviolet radiation that are lethal to most microorganisms, typically via efficient DNA repair and oxidative-damage protection.
- **Parent traits:** METPO:1000059
- **Synonyms:** radioresistant
- **Existing evidence:** DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Review of extreme radiation resistance supports manganese-antioxidant protection of the proteome as a core radiotolerance mechanism in Deinococcus radiodurans, "a champion of extreme radiation resistance".) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans tolerates ionizing radiation, UV radiation, and desiccation.)
- **Existing causal graph summary:** radiotolerance_repair_antioxidant: 4 nodes, 3 edges

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
**Generated:** 2026-06-18T01:28:41.093561

1. sweet2024tolradamodel pages 2-4
2. lourenco2023environmentalradiobiology pages 11-13
3. rai2024anovelionizing pages 1-3
4. pal2024unravelingradiationresistance pages 1-2
5. sweet2024tolradamodel pages 1-2
6. pal2024unravelingradiationresistance pages 32-34
7. sharma2024naturaltransformationspecificdpra pages 10-12
8. subramani2023involvementofnucleotide pages 7-9
9. subramani2023involvementofnucleotide pages 1-2
10. subramani2023involvementofnucleotide pages 5-7
11. tan2025radiationresistantbacteriapotential pages 5-8
12. sharma2024naturaltransformationspecificdpra pages 12-14
13. rai2024anovelionizing pages 13-14
14. abbaszadeh2024theecologyand pages 24-28
15. tan2025radiationresistantbacteriapotential pages 4-5
16. abbaszadeh2024theecologyanda pages 24-28
17. https://doi.org/10.1371/journal.pone.0304810
18. https://doi.org/10.1128/aem.01538-23
19. https://doi.org/10.1128/spectrum.03838-23
20. https://doi.org/10.1128/aem.01948-23
21. https://doi.org/10.3390/su17177864
22. https://doi.org/10.3390/genes14091803
23. https://doi.org/10.1007/978-3-031-18810-7_9
24. https://doi.org/10.1128/spectrum.03838-23,
25. https://doi.org/10.1007/978-3-031-18810-7\_9,
26. https://doi.org/10.1128/aem.01538-23,
27. https://doi.org/10.1128/aem.01948-23,
28. https://doi.org/10.1371/journal.pone.0304810,
29. https://doi.org/10.3390/genes14091803,
30. https://doi.org/10.3390/su17177864,