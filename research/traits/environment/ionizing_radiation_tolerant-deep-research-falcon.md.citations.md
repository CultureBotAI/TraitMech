# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ionizing radiation tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ionizing radiation (e.g. gamma rays), typically via efficient repair of DNA double-strand breaks and protection of the proteome from oxidative damage.
- **Parent traits:** traitmech:000007
- **Synonyms:** gamma radiation resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates gamma (ionizing) radiation D10 doses exceeding 12 kGy.) | DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Mechanism support — manganese-mediated oxidative-damage protection underlies survival of lethal ionizing-radiation doses.)
- **Existing causal graph summary:** ionizing_radiation_tolerance_dsb_repair: 6 nodes, 7 edges

## Research Objective

Research the microbial trait **ionizing radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ionizing_radiation_tolerant.yaml`.

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
**Generated:** 2026-08-04T01:15:24.996960

1. slade2011oxidativestressresistance pages 12-13
2. lu2024thedeinococcusprotease pages 4-5
3. munteanu2015recentprogressin pages 7-9
4. munteanu2015recentprogressin pages 5-7
5. pal2024unravelingradiationresistance pages 26-28
6. sweet2024tolradamodel pages 1-2
7. pal2024unravelingradiationresistance pages 2-4
8. slade2011oxidativestressresistance pages 4-5
9. pal2024unravelingradiationresistance pages 1-2
10. pal2024unravelingradiationresistance pages 34-35
11. slade2011oxidativestressresistance pages 45-47
12. munteanu2015recentprogressin pages 9-10
13. sweet2024tolradamodel pages 11-13
14. 10.1038/s41467-024-46208-9
15. 10.1371/journal.pone.0304810
16. 10.1128/spectrum.03838-23
17. 10.1128/MMBR.00015-10
18. 10.1007/s00792-015-0759-9
19. https://doi.org/10.1038/s41467-024-46208-9
20. https://doi.org/10.1371/journal.pone.0304810
21. https://doi.org/10.1128/spectrum.03838-23
22. https://doi.org/10.1128/MMBR.00015-10
23. https://doi.org/10.1007/s00792-015-0759-9
24. https://doi.org/10.1128/spectrum.03838-23,
25. https://doi.org/10.1128/mmbr.00015-10,
26. https://doi.org/10.1371/journal.pone.0304810,
27. https://doi.org/10.1038/s41467-024-46208-9,
28. https://doi.org/10.1007/s00792-015-0759-9,