# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000487
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth above approximately 30 °C, characteristic of extreme-eurythermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_>30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports robust thermostability as the basis of extending tolerance beyond standard mesophile ranges.)
- **Existing causal graph summary:** temperature_delta_high_eurythermal: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_high.yaml`.

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
**Generated:** 2026-08-04T03:38:06.833184

1. moon2023temperaturemattersbacterial pages 7-9
2. mendoza2014temperaturesensingby pages 2-4
3. mendoza2014temperaturesensingby pages 5-6
4. white2019thecompletegenome pages 10-11
5. white2019thecompletegenome pages 1-2
6. garciadescalzo2022comparativeproteomicanalysis pages 1-2
7. white2019thecompletegenome pages 17-18
8. white2019thecompletegenome pages 7-9
9. white2019thecompletegenome pages 3-4
10. zhou2021acoldshock pages 5-6
11. zhou2021acoldshock pages 1-2
12. mendoza2014temperaturesensingby pages 4-5
13. 10.1007/s12275-023-00031-x
14. 10.3389/fmicb.2022.841359
15. 10.1038/s41421-021-00246-5
16. 10.3389/fmicb.2018.03189
17. 10.1146/annurev-micro-091313-103612
18. 10.1128/MMBR.65.1.1-43.2001
19. https://doi.org/10.1007/s12275-023-00031-x
20. https://doi.org/10.3389/fmicb.2022.841359
21. https://doi.org/10.1038/s41421-021-00246-5
22. https://doi.org/10.3389/fmicb.2018.03189
23. https://doi.org/10.1146/annurev-micro-091313-103612
24. https://doi.org/10.1128/MMBR.65.1.1-43.2001
25. https://doi.org/10.3389/fmicb.2018.03189,
26. https://doi.org/10.1007/s12275-023-00031-x,
27. https://doi.org/10.1038/s41421-021-00246-5,
28. https://doi.org/10.1146/annurev-micro-091313-103612,
29. https://doi.org/10.3389/fmicb.2022.841359,