# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixotrophic
- **METPO identifier:** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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
**Generated:** 2026-06-18T12:00:01.990215

1. eiler2006evidenceforthe pages 2-3
2. li2024arcobacteraceaeareubiquitous pages 1-2
3. eiler2006evidenceforthe pages 1-2
4. srivastava2023interplaybetweenautotrophic pages 1-2
5. li2024insitucommunity pages 13-15
6. ray2023clearingtheair pages 4-6
7. tothero2024leptothrixochraceagenomes pages 13-15
8. parada2023constrainingthecomposition pages 10-13
9. tothero2024leptothrixochraceagenomes pages 9-13
10. parada2023constrainingthecomposition pages 17-19
11. parada2023constrainingthecomposition pages 1-6
12. NiFe
13. https://doi.org/10.1186/s40168-023-01688-7
14. https://doi.org/10.1128/msystems.00513-24
15. https://doi.org/10.1128/aem.00599-24
16. https://doi.org/10.1111/1462-2920.16299
17. https://doi.org/10.1128/spectrum.02177-23
18. https://doi.org/10.1128/AEM.01559-06
19. https://doi.org/10.1128/mmbr.00048-23
20. https://doi.org/10.1073/pnas.1305998110
21. https://doi.org/10.1128/aem.01559-06,
22. https://doi.org/10.1128/msystems.00513-24,
23. https://doi.org/10.1111/1462-2920.16299,
24. https://doi.org/10.1128/mmbr.00048-23,
25. https://doi.org/10.1128/aem.00599-24,
26. https://doi.org/10.1186/s40168-023-01688-7,
27. https://doi.org/10.1128/spectrum.02177-23,