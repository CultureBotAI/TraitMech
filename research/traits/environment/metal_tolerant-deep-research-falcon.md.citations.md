# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metal tolerant
- **METPO identifier:** traitmech:000012
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism grows in the presence of elevated concentrations of toxic heavy-metal or metalloid ions, typically via efflux-based resistance determinants (RND-family CBA pumps, P-type ATPases, and cation diffusion facilitators).
- **Parent traits:** METPO:1000059
- **Synonyms:** metallophilic, heavy metal resistant
- **Existing evidence:** PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Review of efflux-mediated heavy-metal resistance supports active metal export as the dominant prokaryotic tolerance mechanism.) | DOI:10.3389/fmicb.2020.00047: This metallophilic strain BS1, harbors numerous gene clusters encoding metal-resistance determinants enabling detoxification of transition metal ions and complexes (Organism example: Cupriavidus metallidurans is the model metallophilic bacterium tolerating many toxic metals via dedicated resistance gene clusters.)
- **Existing causal graph summary:** metal_tolerance_efflux_detoxification: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **metal tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/metal_tolerant.yaml`.

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
**Generated:** 2026-06-17T22:56:07.950903

1. chatterjee2024multimodalcadmiumresistance pages 14-15
2. nies2024aflowequilibrium pages 1-3
3. shafiq2024mechanismsoftoxicity pages 9-10
4. rismondo2023thesensoryhistidine pages 1-2
5. bhat2024horizontalgenetransfer pages 1-2
6. xie2023wholegenomesequence pages 9-10
7. joshi2023rhizosphericbacteriathe pages 11-12
8. hirth2023fullcopperresistance pages 16-18
9. hirth2023fullcopperresistance pages 11-12
10. chatterjee2024pseudomonasaeruginosastrain pages 21-23
11. hirth2023fullcopperresistance pages 1-3
12. rismondo2023thesensoryhistidine pages 8-10
13. hirth2023fullcopperresistance pages 9-11
14. broad
15. ranked as
16. https://doi.org/10.1186/s12866-024-03391-5
17. https://doi.org/10.1128/aem.00567-23
18. https://doi.org/10.1128/jb.00080-24
19. https://doi.org/10.1128/spectrum.00291-23
20. https://doi.org/10.1038/s41598-024-80754-y
21. https://doi.org/10.3390/microorganisms11061518
22. https://doi.org/10.3389/fmicb.2023.1229828
23. https://doi.org/10.1186/s12866-024-03206-7
24. https://doi.org/10.1093/mtomcs/mfae058
25. https://doi.org/10.21203/rs.3.rs-4733845/v1
26. https://doi.org/10.52700/jmmg.v5i1.155
27. https://doi.org/10.7717/peerj.18383
28. https://doi.org/10.52700/jmmg.v5i1.155,
29. https://doi.org/10.1128/jb.00080-24,
30. https://doi.org/10.1128/aem.00567-23,
31. https://doi.org/10.1038/s41598-024-80754-y,
32. https://doi.org/10.1128/spectrum.00291-23,
33. https://doi.org/10.1186/s12866-024-03391-5,
34. https://doi.org/10.3390/microorganisms11061518,
35. https://doi.org/10.3389/fmicb.2023.1229828,
36. https://doi.org/10.21203/rs.3.rs-4733845/v1,