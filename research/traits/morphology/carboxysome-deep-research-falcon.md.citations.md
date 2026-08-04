# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxysome
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000072
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A bacterial microcompartment — a polyhedral protein-shelled organelle that encapsulates RuBisCO and carbonic anhydrase to concentrate CO2 for carbon fixation in cyanobacteria and many chemoautotrophs.
- **Parent traits:** traitmech:000066
- **Synonyms:** bacterial microcompartment
- **Existing evidence:** DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments; the carboxysome is the archetypal protein-shelled CO2-fixing microcompartment.) | DOI:10.1038/nrmicro1913:  (Yeates et al. describe protein-based organelles in bacteria (carboxysomes and related microcompartments), including the carboxysome shell and its encapsulated enzymes.)
- **Existing causal graph summary:** carboxysome_co2_concentrating: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **carboxysome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carboxysome.yaml`.

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
**Generated:** 2026-08-04T07:33:33.817375

1. maccready2024orthogonalityofshell pages 1-2
2. huffine2024cyanobacteriaforma pages 1-3
3. huang2022probingtheinternal pages 1-2
4. mahinthichaichan2018selectivepermeabilityof pages 8-10
5. wieschollek2024anewtype pages 1-2
6. sarkar2024atomicviewof pages 1-2
7. long2018carboxysomeencapsulationof pages 1-2
8. trettel2024modelingbacterialmicrocompartment pages 1-2
9. sarkar2024atomicviewof pages 7-8
10. bicarbonate
11. https://doi.org/10.1126/sciadv.adk7283.
12. https://doi.org/10.1128/aem.01075-24.
13. https://doi.org/10.1073/pnas.2402277121.
14. https://doi.org/10.1101/2024.06.28.601118.
15. https://doi.org/10.1101/2024.03.19.585794.
16. https://doi.org/10.1038/s41467-018-06044-0.
17. https://doi.org/10.21203/rs.3.rs-4511266/v1.
18. https://doi.org/10.3389/fpls.2024.1346759,
19. https://doi.org/10.3389/fpls.2024.1346759.
20. https://doi.org/10.1021/acs.biomac.2c00781.
21. https://doi.org/10.1021/acs.jpcb.8b06822.
22. https://doi.org/10.1126/sciadv.adk7283,
23. https://doi.org/10.1021/acs.biomac.2c00781,
24. https://doi.org/10.1101/2024.03.19.585794,
25. https://doi.org/10.21203/rs.3.rs-4511266/v1,
26. https://doi.org/10.1101/2024.06.28.601118,
27. https://doi.org/10.1073/pnas.2402277121,
28. https://doi.org/10.1021/acs.jpcb.8b06822,
29. https://doi.org/10.1128/aem.01075-24,
30. https://doi.org/10.1038/s41467-018-06044-0,