# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biopolymer degradation
- **METPO identifier:** traitmech:000110
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism secretes enzymes to depolymerize recalcitrant biopolymers (such as cellulose, hemicellulose, chitin, and lignin) into assimilable units for growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** biomass degradation
- **Existing evidence:** DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. review lignocellulose degradation mechanisms across the tree of life, using complementary enzymes to deconstruct plant biopolymers; parent of the polymer-specific sub-variants.) | DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial utilization of cellulose, the archetypal biopolymer-degradation process.)
- **Existing causal graph summary:** biopolymer_degradation_extracellular_hydrolysis: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biopolymer degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/biopolymer_degradation.yaml`.

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
**Generated:** 2026-06-18T04:29:41.584378

1. hsin2024lignocellulosedegradationin pages 8-11
2. meunier2024selectionofmarine pages 1-2
3. schiml2024microbialconsortiadriving pages 15-16
4. saraf2024comparativegenomicinsight pages 9-11
5. datta2024enzymaticdegradationof pages 1-3
6. beidler2023polysaccharidedegradationby pages 29-31
7. schiml2024microbialconsortiadriving pages 13-14
8. wong2024bacteroidesthetaiotaomicronmetabolic pages 1-2
9. kalenborn2024genesforlaminarin pages 1-2
10. wu2024microbialmechanismsfor pages 2-3
11. datta2024enzymaticdegradationof pages 8-10
12. li2024biochemicalcharacterizationof pages 2-5
13. hsin2024lignocellulosedegradationin pages 5-8
14. kalenborn2024genesforlaminarin pages 5-6
15. schiml2024microbialconsortiadriving pages 1-2
16. hsin2024lignocellulosedegradationin pages 1-5
17. ponsetto2024thepotentialof pages 1-2
18. schiml2024microbialconsortiadriving pages 11-12
19. https://doi.org/10.1101/2024.11.06.622210
20. https://doi.org/10.1128/aem.01742-24
21. https://doi.org/10.1128/msphere.00278-24
22. https://doi.org/10.1128/mbio.02599-23
23. https://doi.org/10.3389/fmicb.2024.1393588
24. https://doi.org/10.1016/j.heliyon.2024.e24022
25. https://doi.org/10.1128/spectrum.00886-24
26. https://doi.org/10.1186/s40168-024-01908-8
27. https://doi.org/10.3389/fbioe.2024.1423935
28. https://doi.org/10.1016/j.heliyon.2024.e24022,
29. https://doi.org/10.1101/2024.11.06.622210,
30. https://doi.org/10.1128/mbio.02599-23,
31. https://doi.org/10.3389/fmicb.2024.1393588,
32. https://doi.org/10.1128/aem.01742-24,
33. https://doi.org/10.1128/msphere.00278-24,
34. https://doi.org/10.1101/2024.11.11.623002,
35. https://doi.org/10.1128/spectrum.00886-24,
36. https://doi.org/10.1186/s40168-024-01908-8,
37. https://doi.org/10.3389/fbioe.2024.1423935,