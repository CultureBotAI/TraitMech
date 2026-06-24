# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezotolerant
- **METPO identifier:** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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
**Generated:** 2026-06-18T01:05:44.656310

1. tamby2023microbialmembranelipid pages 1-2
2. malas2024biologicalfunctionsat pages 1-2
3. coffin2024responseandadaptation pages 1-2
4. tamby2023microbialmembranelipid pages 2-4
5. scheffer2023themysteryof pages 9-10
6. shymialevich2024thenovelconcept pages 5-7
7. scheffer2023themysteryof pages 6-7
8. scheffer2023themysteryof pages 7-9
9. shymialevich2024thenovelconcept pages 7-8
10. wisniewski2023impactofhighpressure pages 1-2
11. munir2023physicaltreatmentsto pages 12-14
12. shymialevich2024thenovelconcept pages 4-5
13. shymialevich2024thenovelconcept pages 2-4
14. wisniewski2023impactofhighpressure pages 6-7
15. shymialevich2024thenovelconcept pages 1-2
16. uncertain: pressure vs temperature confounded
17. taxon-specific
18. uncertain
19. uncertain, cross-adaptation
20. inferred
21. https://doi.org/10.3390/microorganisms11071629
22. https://doi.org/10.3389/fmolb.2022.1058381
23. https://doi.org/10.3389/fmicb.2024.1470617
24. https://doi.org/10.3390/microorganisms11071629;
25. https://doi.org/10.3390/foods13010014
26. https://doi.org/10.3390/foods13162519;
27. https://doi.org/10.3390/foods13162519
28. https://doi.org/10.3389/fmicb.2024.1293928
29. https://doi.org/10.3390/foods12081580
30. https://doi.org/10.3389/fmolb.2022.1058381,
31. https://doi.org/10.3389/fmicb.2024.1293928,
32. https://doi.org/10.3389/fmicb.2024.1470617,
33. https://doi.org/10.3390/foods13010014,
34. https://doi.org/10.3390/foods13162519,
35. https://doi.org/10.3390/microorganisms11071629,
36. https://doi.org/10.3390/foods12081580,