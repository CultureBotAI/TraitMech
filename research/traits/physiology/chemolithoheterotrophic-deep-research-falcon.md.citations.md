# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoheterotrophic
- **METPO identifier:** METPO:1000638
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors for energy generation while utilizing organic compounds as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake of organic compounds (Study supports sulfur oxidation coupled to organic compound uptake in a chemolithoheterotrophic symbiont context.)
- **Existing causal graph summary:** chemolithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **chemolithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoheterotrophic.yaml`.

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
**Generated:** 2026-06-18T11:13:39.451961

1. quinn2025characterizingstratifiedmicrobiala pages 20-23
2. seah2019sulfuroxidizingsymbiontswithout pages 10-12
3. taubert2022bolsteringfitnessvia pages 5-6
4. hutt2021insightsintogrowth pages 1-6
5. zhong2022metagenomicfeaturescharacterized pages 10-13
6. trutschel2023determiningresidentmicrobial pages 10-11
7. rudenko2024mechanismofintracellular pages 10-12
8. zhuang2024electrontransferin pages 5-6
9. seah2019sulfuroxidizingsymbiontswithout pages 2-4
10. https://doi.org/10.1128/AEM.01344-19
11. https://doi.org/10.1128/mBio.01112-19
12. https://doi.org/10.1128/spectrum.00614-22
13. https://doi.org/10.3389/fmicb.2023.1182497
14. https://doi.org/10.1038/s41396-021-01163-x
15. https://doi.org/10.3390/ijms252010962
16. https://doi.org/10.3390/life14050591
17. https://doi.org/10.1007/s00203-020-02028-1
18. https://doi.org/10.1128/mbio.01112-19,
19. https://doi.org/10.1038/s41396-021-01163-x,
20. https://doi.org/10.1007/s00203-020-02028-1,
21. https://doi.org/10.1128/aem.01344-19,
22. https://doi.org/10.1128/spectrum.00614-22,
23. https://doi.org/10.3389/fmicb.2023.1182497,
24. https://doi.org/10.3390/ijms252010962,
25. https://doi.org/10.3390/life14050591,