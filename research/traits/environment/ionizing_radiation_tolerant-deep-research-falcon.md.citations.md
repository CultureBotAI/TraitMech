# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ionizing radiation tolerant
- **METPO identifier:** traitmech:000008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ionizing radiation (e.g. gamma rays), typically via efficient repair of DNA double-strand breaks and protection of the proteome from oxidative damage.
- **Parent traits:** traitmech:000007
- **Synonyms:** gamma radiation resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates gamma (ionizing) radiation D10 doses exceeding 12 kGy.) | DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Mechanism support — manganese-mediated oxidative-damage protection underlies survival of lethal ionizing-radiation doses.)
- **Existing causal graph summary:** ionizing_radiation_tolerance_dsb_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **ionizing radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ionizing_radiation_tolerant.yaml`.

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
**Generated:** 2026-06-17T22:45:28.758778

1. lourenco2023environmentalradiobiology pages 11-13
2. petit2023firstisolationand pages 8-9
3. subramani2023involvementofnucleotide pages 1-2
4. pal2024unravelingradiationresistance pages 2-4
5. lu2024thedeinococcusprotease pages 1-2
6. lu2024thedeinococcusprotease pages 7-8
7. gregory2024radioactivewastemicrobiology pages 13-14
8. rai2024anovelionizing pages 1-3
9. petit2023firstisolationand pages 1-2
10. lu2024thedeinococcusprotease pages 4-5
11. lu2024thedeinococcusprotease pages 8-9
12. lu2024thedeinococcusprotease pages 9-10
13. pal2024unravelingradiationresistance pages 44-45
14. https://doi.org/10.1007/978-3-031-18810-7_9
15. https://doi.org/10.3390/microorganisms11081871
16. https://doi.org/10.3390/genes14091803
17. https://doi.org/10.1371/journal.pone.0304810
18. https://doi.org/10.1093/femsre/fuae001;
19. https://doi.org/10.1038/s41467-024-46208-9
20. https://doi.org/10.1101/cshperspect.a012765
21. https://doi.org/10.1128/aem.01538-23
22. https://doi.org/10.1093/femsre/fuae001
23. https://doi.org/10.1101/cshperspect.a012765;
24. https://doi.org/10.1007/978-3-031-18810-7\_9,
25. https://doi.org/10.3390/microorganisms11081871,
26. https://doi.org/10.3390/genes14091803,
27. https://doi.org/10.1371/journal.pone.0304810,
28. https://doi.org/10.1093/femsre/fuae001,
29. https://doi.org/10.1038/s41467-024-46208-9,
30. https://doi.org/10.1128/aem.01538-23,