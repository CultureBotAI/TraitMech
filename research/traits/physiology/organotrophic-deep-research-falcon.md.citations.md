# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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
**Generated:** 2026-08-04T11:45:38.887027

1. schonheit2016ontheorigin pages 2-4
2. muller2012biochemistryandevolution pages 5-6
3. buckel2021energyconservationin pages 1-2
4. folch2021metabolicenergyconservation pages 20-21
5. folch2021metabolicenergyconservation pages 3-4
6. schonheit2016ontheorigin pages 8-10
7. 10.1016/j.tim.2015.10.003
8. 10.1111/1751-7915.13746
9. 10.1128/MMBR.05024-11
10. 10.3389/fmicb.2021.703525
11. 10.3390/molecules29102293
12. 10.1016/B978-012373944-5.00083-3
13. 10.1016/j.bbabio.2008.09.008
14. https://doi.org/10.1016/j.tim.2015.10.003
15. https://doi.org/10.1111/1751-7915.13746
16. https://doi.org/10.1128/MMBR.05024-11
17. https://doi.org/10.3389/fmicb.2021.703525
18. https://doi.org/10.3390/molecules29102293
19. https://doi.org/10.1016/B978-012373944-5.00083-3
20. https://doi.org/10.1016/j.bbabio.2008.09.008
21. https://doi.org/10.1016/j.tim.2015.10.003,
22. https://doi.org/10.3390/molecules29102293,
23. https://doi.org/10.1128/mmbr.05024-11,
24. https://doi.org/10.3389/fmicb.2021.703525,
25. https://doi.org/10.1111/1751-7915.13746,