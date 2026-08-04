# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** peritrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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
**Generated:** 2026-08-04T09:32:19.830564

1. schuhmacher2015howbacteriamaintain pages 1-2
2. schuhmacher2015howbacteriamaintain pages 2-4
3. schuhmacher2015howbacteriamaintain pages 4-5
4. dunn2025nascentflagellarbasal pages 1-2
5. dunn2025nascentflagellarbasal pages 17-18
6. schuhmacher2015howbacteriamaintain pages 9-10
7. taxon-specific
8. taxon-specific; direct 2025 evidence
9. taxon-specific; mechanistic inference
10. taxon-specific; inferred synthesis
11. E. coli; condition-specific
12. downstream function, not pattern formation
13. 10.1093/femsre/fuv034
14. 10.1128/mbio.00530-25
15. https://doi.org/10.1093/femsre/fuv034
16. https://doi.org/10.1128/mbio.00530-25
17. https://doi.org/10.1093/femsre/fuv034,
18. https://doi.org/10.1128/mbio.00530-25,