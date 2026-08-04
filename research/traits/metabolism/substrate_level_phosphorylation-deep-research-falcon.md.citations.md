# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Substrate-level phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **Substrate-level phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/substrate_level_phosphorylation.yaml`.

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
**Generated:** 2026-08-04T07:08:27.184255

1. folch2021metabolicenergyconservation pages 4-6
2. folch2021metabolicenergyconservation pages 6-7
3. folch2021metabolicenergyconservation pages 8-10
4. baum2024theenergyconvertinghydrogenase pages 1-2
5. hackmann2024thevastlandscape pages 1-2
6. hackmann2024thevastlandscape pages 3-4
7. mackenzie2020bedaquilinereprogramscentral pages 1-2
8. zhang2024understandingenergyfluctuation pages 4-6
9. wolfe2005theacetateswitch pages 8-9
10. zhang2024understandingenergyfluctuation pages 1-2
11. zhang2024understandingenergyfluctuation pages 10-12
12. wolfe2005theacetateswitch pages 4-5
13. jong2024quantitativeproteomicsreveals pages 6-8
14. folch2021metabolicenergyconservation pages 7-8
15. wolfe2005theacetateswitch pages 3-4
16. jong2024quantitativeproteomicsreveals pages 1-2
17. mackenzie2020bedaquilinereprogramscentral pages 7-8
18. mackenzie2020bedaquilinereprogramscentral pages 9-10
19. hackmann2024thevastlandscape pages 14-15
20. reva2023functionaldiversityof pages 7-8
21. reva2023functionaldiversityof pages 9-10
22. PTA
23. ACK
24. acetyl-CoA(CoA):Pi acetyltransferase; EC 2.7.2.1
25. ATP:acetate phosphotransferase; EC 2.3.1.8
26. https://doi.org/10.1111/1751-7915.13746,
27. https://doi.org/10.1093/femsre/fuae016,
28. https://doi.org/10.1128/mmbr.69.1.12-50.2005,
29. https://doi.org/10.1038/s41467-020-19959-4,
30. https://doi.org/10.1128/spectrum.03380-23,
31. https://doi.org/10.1186/s12934-024-02572-1,
32. https://doi.org/10.3389/fmicb.2024.1468929,
33. https://doi.org/10.1186/s40168-023-01565-3,
34. https://doi.org/10.3389/fmicb.2023.1182464,