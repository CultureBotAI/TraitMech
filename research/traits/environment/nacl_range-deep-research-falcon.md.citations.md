# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range
- **METPO identifier:** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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
**Generated:** 2026-06-17T23:32:46.609964

1. schneegurt2012mediaandconditions pages 6-9
2. bartha2022investigatingextremotolerantmicrobes pages 21-25
3. xing2024thepolyextremophilenatranaerobius pages 6-7
4. xing2024thepolyextremophilenatranaerobius pages 17-19
5. hu2024cdiampaccumulationimpairs pages 6-9
6. hu2024cdiampaccumulationimpairs pages 2-6
7. foster2024bacterialcellvolume pages 8-10
8. foster2024bacterialcellvolume pages 12-13
9. foster2024bacterialcellvolume pages 6-8
10. https://doi.org/10.1128/AEM.00145-24
11. https://doi.org/10.1128/MMBR.00181-23
12. https://doi.org/10.1128/SPECTRUM.03786-23
13. https://doi.org/10.1007/978-94-007-5539-0_2
14. https://doi.org/10.1128/aem.00145-24
15. https://doi.org/10.1128/mmbr.00181-23
16. https://doi.org/10.1128/spectrum.03786-23
17. https://doi.org/10.1128/aem.00145-24,
18. https://doi.org/10.1007/978-94-007-5539-0\_2,
19. https://doi.org/10.1128/mmbr.00181-23,
20. https://doi.org/10.1128/spectrum.03786-23,