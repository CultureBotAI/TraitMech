# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative oxygen preference
- **METPO identifier:** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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
**Generated:** 2026-06-17T22:01:32.517858

1. caulat2024physiologicalroleand pages 1-2
2. butler2023bacteroidesfragilismaintains pages 1-2
3. brown2023conservedmetabolicregulator pages 12-14
4. loivamaa2024aerobicadaptationand pages 9-12
5. loivamaa2024aerobicadaptationand pages 6-9
6. villamizar2023anaerobiosisaneglected pages 13-16
7. villamizar2023anaerobiosisaneglected pages 11-13
8. baker2024largininesupplementationabrogates pages 1-3
9. yaeger2023centralmetabolismis pages 8-9
10. brown2023conservedmetabolicregulator pages 1-3
11. loivamaa2024aerobicadaptationand pages 18-20
12. https://doi.org/10.1128/mbio.01448-23;
13. https://doi.org/10.1128/aem.01491-23
14. https://doi.org/10.1128/mbio.01448-23
15. https://doi.org/10.1371/journal.pgen.1011013
16. https://doi.org/10.1128/jb.00389-22
17. https://doi.org/10.1128/msphere.00774-23;
18. https://doi.org/10.1128/msphere.00774-23
19. https://doi.org/10.1128/mbio.01591-24
20. https://doi.org/10.1128/mbio.02589-22
21. https://doi.org/10.1128/msystems.00615-24
22. https://doi.org/10.1128/mbio.01448-23,
23. https://doi.org/10.1128/jb.00389-22,
24. https://doi.org/10.1128/mbio.01591-24,
25. https://doi.org/10.1128/msystems.00615-24,
26. https://doi.org/10.1128/aem.01491-23,
27. https://doi.org/10.1128/msphere.00774-23,
28. https://doi.org/10.1371/journal.pgen.1011013,