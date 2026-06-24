# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum low
- **METPO identifier:** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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
**Generated:** 2026-06-18T02:13:27.106672

1. ramon2023ageneraloverview pages 1-2
2. purwar2024adaptationsofpsychrophilic pages 7-8
3. gao2023thegrowthlipid pages 1-2
4. ramasamy2023comprehensiveinsightson pages 3-4
5. barbotin2024quantificationofmembrane pages 1-3
6. purwar2024adaptationsofpsychrophilic pages 10-11
7. purwar2024adaptationsofpsychrophilic pages 6-7
8. sidarta2024lipidphaseseparation pages 1-2
9. liu2023psychrophilicyeastsinsights pages 4-5
10. purwar2024adaptationsofpsychrophilic pages 8-10
11. barbotin2024quantificationofmembrane pages 10-11
12. gao2023thegrowthlipid pages 10-11
13. wu2023molecularmechanismsof pages 3-5
14. purwar2024adaptationsofpsychrophilic pages 3-4
15. sidarta2024lipidphaseseparation pages 12-14
16. liu2023psychrophilicyeastsinsights pages 7-11
17. es
18. https://doi.org/10.1101/2023.10.13.562271
19. https://doi.org/10.1128/spectrum.03925-23
20. https://doi.org/10.37256/amtt.5220244537
21. https://doi.org/10.1186/s13068-022-02249-0
22. https://doi.org/10.3390/genes14010158
23. https://doi.org/10.1007/s42770-023-01057-4
24. https://doi.org/10.3390/cells12101353
25. https://doi.org/10.3389/fmicb.2023.1197797
26. https://doi.org/10.1007/s42770-023-01057-4,
27. https://doi.org/10.1186/s13068-022-02249-0,
28. https://doi.org/10.37256/amtt.5220244537,
29. https://doi.org/10.1101/2023.10.13.562271,
30. https://doi.org/10.1128/spectrum.03925-23,
31. https://doi.org/10.3390/genes14010158,
32. https://doi.org/10.3389/fmicb.2023.1197797,
33. https://doi.org/10.3390/cells12101353,