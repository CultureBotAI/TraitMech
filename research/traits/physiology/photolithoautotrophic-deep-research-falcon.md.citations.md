# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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
**Generated:** 2026-08-04T12:00:51.906112

1. thiel2018diversityofchlorophototrophic pages 2-3
2. martin2018aphysiologicalperspective pages 2-3
3. kushkevych2021anoxygenicphotosynthesisin pages 3-5
4. gupta2021photoferrotrophyandphototrophic pages 1-2
5. kushkevych2024anoxygenicphotosynthesiswith pages 18-18
6. gupta2021photoferrotrophyandphototrophic pages 8-10
7. alarcon2024evidenceforautotrophic pages 1-2
8. alarcon2024evidenceforautotrophic pages 22-24
9. martin2018aphysiologicalperspective pages 21-21
10. martin2018aphysiologicalperspective pages 14-15
11. https://doi.org/10.1146/annurev-arplant-042817-040500
12. https://doi.org/10.1146/annurev-arplant-042817-040500;
13. https://doi.org/10.1093/femsre/fux056
14. https://doi.org/10.3390/antiox10060829
15. https://doi.org/10.3389/fmicb.2024.1417714
16. https://doi.org/10.1038/s41396-021-01015-8
17. https://doi.org/10.1128/aem.00863-24
18. https://doi.org/10.1128/aem.00863-24.
19. https://doi.org/10.3389/fmicb.2024.1417714.
20. https://doi.org/10.1038/s41396-021-01015-8.
21. https://doi.org/10.3390/antiox10060829.
22. https://doi.org/10.1146/annurev-arplant-042817-040500.
23. https://doi.org/10.1093/femsre/fux056.
24. https://doi.org/10.3389/fmicb.2011.00165.
25. https://doi.org/10.1128/AEM.02473-10.
26. https://doi.org/10.1146/annurev-arplant-042817-040500,
27. https://doi.org/10.1093/femsre/fux056,
28. https://doi.org/10.3390/antiox10060829,
29. https://doi.org/10.1038/s41396-021-01015-8,
30. https://doi.org/10.3389/fmicb.2024.1417714,
31. https://doi.org/10.1128/aem.00863-24,