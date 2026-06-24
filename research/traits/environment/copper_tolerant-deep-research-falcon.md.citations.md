# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copper tolerant
- **METPO identifier:** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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
**Generated:** 2026-06-17T21:51:16.635106

1. rebelo2023unravelingtherole pages 6-8
2. hirth2023fullcopperresistance pages 16-18
3. wong2023coppereffluxsystem pages 8-10
4. wong2023coppereffluxsystem pages 5-8
5. wong2023coppereffluxsystem pages 1-2
6. rismondo2023thesensoryhistidine pages 1-2
7. rismondo2023thesensoryhistidine pages 5-8
8. elsen2024crossregulationandcrosstalk pages 3-5
9. elsen2024crossregulationandcrosstalk pages 5-7
10. elsen2024crossregulationandcrosstalk pages 16-18
11. hikal2024theacquiredpco pages 3-4
12. hikal2024theacquiredpco pages 7-9
13. yu2024isolationofhighly pages 2-3
14. yu2024isolationofhighly pages 6-8
15. elsen2024crossregulationandcrosstalk pages 9-11
16. hikal2024theacquiredpco pages 2-3
17. wong2023coppereffluxsystem pages 10-12
18. rismondo2023thesensoryhistidine pages 2-5
19. elsen2024crossregulationandcrosstalk pages 7-9
20. yu2024isolationofhighly pages 4-6
21. yu2024isolationofhighly pages 9-11
22. https://doi.org/10.1128/iai.00091-23
23. https://doi.org/10.1128/spectrum.00291-23
24. https://doi.org/10.1371/journal.pgen.1011325
25. https://doi.org/10.3389/fmicb.2024.1454763
26. https://doi.org/10.3389/fmicb.2024.1390451
27. https://doi.org/10.1128/aem.00567-23
28. https://doi.org/10.3390/antibiotics12091474
29. https://doi.org/10.1128/spectrum.00291-23,
30. https://doi.org/10.3389/fmicb.2024.1454763,
31. https://doi.org/10.1128/aem.00567-23,
32. https://doi.org/10.3390/antibiotics12091474,
33. https://doi.org/10.1371/journal.pgen.1011325,
34. https://doi.org/10.3389/fmicb.2024.1390451,
35. https://doi.org/10.1128/iai.00091-23,