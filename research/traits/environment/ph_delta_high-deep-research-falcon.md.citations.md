# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta high
- **METPO identifier:** METPO:1000478
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 5–9 pH units, characteristic of euryphilic pH-tolerance physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_5_9
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very broad pH-homeostasis as a hallmark of generalist pH-tolerance physiology.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust proton extrusion and import machinery as the basis of very broad pH-tolerance.)
- **Existing causal graph summary:** ph_delta_high_euryphilic_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_high.yaml`.

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
**Generated:** 2026-06-18T00:16:13.794841

1. krulwich2011molecularaspectsof pages 1-3
2. krulwich2011molecularaspectsof pages 3-5
3. poolman2023physicochemicalhomeostasisin pages 1-2
4. ramoneda2023buildingagenomebased pages 1-2
5. ramoneda2023buildingagenomebased pages 3-5
6. ramoneda2023buildingagenomebased pages 6-7
7. atasoy2024exploitationofmicrobial pages 3-4
8. atasoy2024exploitationofmicrobial pages 26-27
9. beilen2013compartmentspecificphmonitoring pages 3-4
10. krulwich2011molecularaspectsof pages 6-8
11. atasoy2024exploitationofmicrobial pages 2-3
12. atasoy2024exploitationofmicrobial pages 4-5
13. krulwich2011molecularaspectsof pages 5-6
14. https://doi.org/10.1093/femsre/fuad033
15. https://doi.org/10.1038/nrmicro2549
16. https://doi.org/10.1126/sciadv.adf8998
17. https://doi.org/10.1093/femsre/fuad062
18. https://doi.org/10.3389/fmicb.2013.00157
19. https://doi.org/10.1038/nrmicro2549,
20. https://doi.org/10.1093/femsre/fuad033,
21. https://doi.org/10.1126/sciadv.adf8998,
22. https://doi.org/10.1093/femsre/fuad062,
23. https://doi.org/10.3389/fmicb.2013.00157,