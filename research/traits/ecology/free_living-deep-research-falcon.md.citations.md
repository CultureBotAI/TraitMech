# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** free-living
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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
**Generated:** 2026-08-04T14:53:35.202116

1. martiny2006microbialbiogeographyputting pages 1-2
2. ramoneda2023taxonomicandenvironmental pages 1-2
3. hauer2023geographynotlifestyle pages 1-2
4. wisniewska2024expandedgeneand pages 12-13
5. suzzi2023spatialpatternsin pages 1-2
6. xu2016onthereversibility pages 1-2
7. hollensteiner2023pangenomeanalysisof pages 1-2
8. dragone2024taxonomicandgenomic pages 1-2
9. obeng2023bacterialcdigmphas pages 1-2
10. wisniewska2024expandedgeneand pages 1-3
11. https://doi.org/10.1186/s12915-024-02013-w.
12. https://doi.org/10.1093/ismeco/ycae081.
13. https://doi.org/10.1371/journal.pone.0287947.
14. https://doi.org/10.1038/s41467-023-43435-4.
15. https://doi.org/10.1038/s41564-023-01468-x.
16. https://doi.org/10.1093/femsec/fiad061.
17. https://doi.org/10.1186/s40168-023-01493-2.
18. https://doi.org/10.1186/s12915-016-0284-z.
19. https://doi.org/10.1038/nrmicro1341.
20. https://doi.org/10.1038/nrmicro.2017.171.
21. https://doi.org/10.1038/nrmicro1341,
22. https://doi.org/10.1038/s41467-023-43435-4,
23. https://doi.org/10.1186/s40168-023-01493-2,
24. https://doi.org/10.1186/s12915-024-02013-w,
25. https://doi.org/10.1093/femsec/fiad061,
26. https://doi.org/10.1186/s12915-016-0284-z,
27. https://doi.org/10.1371/journal.pone.0287947,
28. https://doi.org/10.1093/ismeco/ycae081,
29. https://doi.org/10.1038/s41564-023-01468-x,