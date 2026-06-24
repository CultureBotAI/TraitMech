# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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
**Generated:** 2026-06-18T12:42:41.110916

1. tinguely2023diurnalcyclesdrive pages 1-2
2. alarcon2024evidenceforautotrophic pages 1-2
3. koblizek2015ecologyofaerobic pages 2-4
4. villenaalemany2024phenologyandecological pages 1-2
5. piwosz2024responseofaerobic pages 3-4
6. stojan2024ecologyofaerobic pages 1-2
7. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
8. tahon2016diversityofphototrophic pages 1-2
9. stojan2024ecologyofaerobic pages 2-5
10. piwosz2024responseofaerobic pages 2-3
11. koblizek2015ecologyofaerobic pages 9-11
12. https://doi.org/10.1038/s43705-023-00334-5
13. https://doi.org/10.3389/fmicb.2024.1417714
14. https://doi.org/10.3389/fmicb.2016.02026
15. https://doi.org/10.1128/aem.00863-24
16. https://doi.org/10.1186/s40793-024-00573-6
17. https://doi.org/10.1093/femsre/fuv032
18. https://doi.org/10.48550/arxiv.2406.09354
19. https://doi.org/10.1093/femsec/fiae090
20. https://doi.org/10.1186/s40168-024-01786-0
21. https://doi.org/10.1038/s43705-023-00334-5,
22. https://doi.org/10.1093/femsre/fuv032,
23. https://doi.org/10.1186/s40168-024-01786-0,
24. https://doi.org/10.3389/fmicb.2024.1417714,
25. https://doi.org/10.3389/fmicb.2016.02026,
26. https://doi.org/10.1186/s40793-024-00573-6,
27. https://doi.org/10.1128/aem.00863-24,
28. https://doi.org/10.1093/femsec/fiae090,