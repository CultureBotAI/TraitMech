# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** nitrogen-fixing symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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
**Generated:** 2026-08-04T15:27:53.627339

1. ledermann2021howrhizobiaadapt pages 6-7
2. ma2021nitrogenandphosphorus pages 2-4
3. lepetit2023controlofthe pages 1-2
4. dong2020thesignificanceof pages 5-7
5. lima2024expandingagriculturalpotential pages 1-2
6. dong2020thesignificanceof pages 3-5
7. ledermann2021howrhizobiaadapt pages 4-6
8. ledermann2021howrhizobiaadapt pages 7-9
9. rathor2024thebiostimulatoryeffect pages 1-2
10. wu2024naturalnitrogenboosters pages 7-8
11. lima2024expandingagriculturalpotential pages 4-5
12. lima2024expandingagriculturalpotential pages 5-6
13. dong2020thesignificanceof pages 13-15
14. 10.3389/fpls.2023.1114840
15. 10.21475/ajcs.24.18.06.p4104
16. 10.1002/sae2.70001
17. 10.1128/JB.00539-20
18. 10.3389/fpls.2021.683601
19. 10.3390/ijms21165926
20. 10.1038/nrmicro.2017.171
21. 10.1038/nrmicro2990
22. https://doi.org/10.3389/fpls.2023.1114840
23. https://doi.org/10.21475/ajcs.24.18.06.p4104
24. https://doi.org/10.1002/sae2.70001
25. https://doi.org/10.1128/JB.00539-20
26. https://doi.org/10.3389/fpls.2021.683601
27. https://doi.org/10.3390/ijms21165926
28. https://doi.org/10.1038/nrmicro.2017.171
29. https://doi.org/10.1038/nrmicro2990
30. https://doi.org/10.3389/fpls.2023.1114840,
31. https://doi.org/10.1128/jb.00539-20,
32. https://doi.org/10.21475/ajcs.24.18.06.p4104,
33. https://doi.org/10.3390/ijms21165926,
34. https://doi.org/10.3389/fpls.2021.683601,
35. https://doi.org/10.1002/sae2.70001,
36. https://doi.org/10.5376/msb.2024.15.0009,