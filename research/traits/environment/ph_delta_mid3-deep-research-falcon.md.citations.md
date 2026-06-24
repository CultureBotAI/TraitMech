# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid3
- **METPO identifier:** METPO:1000477
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 4–5 pH units, characteristic of organisms with wide pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_4_5
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)
- **Existing causal graph summary:** ph_delta_mid3_wide_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid3.yaml`.

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
**Generated:** 2026-06-18T00:20:17.106312

1. krulwich2011molecularaspectsof pages 1-3
2. krulwich2011molecularaspectsof pages 3-5
3. poolman2023physicochemicalhomeostasisin pages 1-2
4. ramoneda2023buildingagenomebased pages 3-5
5. yao2023howmethanotrophsrespond pages 5-7
6. krulwich2011molecularaspectsof pages 5-6
7. krulwich2011molecularaspectsof pages 27-28
8. krulwich2011molecularaspectsof pages 11-12
9. is one of
10. https://doi.org/10.1038/nrmicro2549
11. https://doi.org/10.1038/nrmicro2549;
12. https://doi.org/10.1093/femsre/fuad033
13. https://doi.org/10.3389/fmicb.2022.1034164
14. https://doi.org/10.1126/sciadv.adf8998
15. https://doi.org/10.1038/nrmicro2549,
16. https://doi.org/10.1093/femsre/fuad033,
17. https://doi.org/10.1126/sciadv.adf8998,
18. https://doi.org/10.3389/fmicb.2022.1034164,