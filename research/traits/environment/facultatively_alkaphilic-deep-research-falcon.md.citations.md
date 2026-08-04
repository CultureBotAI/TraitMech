# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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
**Generated:** 2026-08-04T00:48:58.927760

1. preiss2015alkaliphilicbacteriawith pages 1-2
2. maksimova2024metabolicandmorphological pages 1-2
3. horikoshi1999alkaliphilessomeapplications pages 1-3
4. preiss2015alkaliphilicbacteriawith pages 4-5
5. krulwich2011molecularaspectsof pages 12-14
6. preiss2015alkaliphilicbacteriawith pages 7-8
7. jong2024quantitativeproteomicsreveals pages 6-8
8. maksimova2024metabolicandmorphological pages 5-6
9. 10.1155/2024/3087296
10. 10.3389/fmicb.2024.1468929
11. 10.1007/10_2018_83
12. 10.3389/fbioe.2015.00075
13. 10.1038/nrmicro2549
14. 10.1128/MMBR.63.4.735-750.1999
15. https://doi.org/10.1155/2024/3087296
16. https://doi.org/10.3389/fmicb.2024.1468929
17. https://doi.org/10.1007/10_2018_83
18. https://doi.org/10.3389/fbioe.2015.00075
19. https://doi.org/10.1038/nrmicro2549
20. https://doi.org/10.1128/MMBR.63.4.735-750.1999
21. https://doi.org/10.3389/fbioe.2015.00075,
22. https://doi.org/10.1155/2024/3087296,
23. https://doi.org/10.1128/mmbr.63.4.735-750.1999,
24. https://doi.org/10.1038/nrmicro2549,
25. https://doi.org/10.1007/10\_2018\_83,
26. https://doi.org/10.3389/fmicb.2024.1468929,