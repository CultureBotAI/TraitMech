---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:27:04.751124'
end_time: '2026-06-18T08:46:07.076151'
duration_seconds: 1142.33
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: magnetosome
  trait_identifier: traitmech:000071
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: magnetosome
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A membrane-bounded intracellular organelle containing a magnetic iron-mineral
    crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria
    to align with and navigate along geomagnetic field lines.
  parent_traits: traitmech:000066
  synonyms: magnetotactic
  evidence_summary: "DOI:10.1038/nrmicro.2016.99:  (Uebe & Sch\xFCler review magnetosome\
    \ biogenesis as the formation of membrane-bounded magnetic-mineral organelles\
    \ in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel,\
    \ \"Magnetosome formation in prokaryotes\", describe magnetosomes and the magnetotactic\
    \ lifestyle they enable.)"
  causal_graph_summary: 'magnetosome_magnetotaxis: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **METPO identifier:** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **METPO identifier:** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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


## Magnetosome (traitmech:000071) — Curation-Focused Research Report (2023–2024 emphasis)

### Scope summary (TraitMech curation view)
A **magnetosome** is a **membrane-bounded intracellular organelle** in magnetotactic bacteria (MTB) that encloses a magnetic iron-mineral crystal (most commonly **magnetite, Fe\_3O\_4**, or in some environments **greigite, Fe\_3S\_4**) and is typically organized into **chains** that function as a magnetic dipole to support **magnetoaerotaxis/magnetotaxis** in geomagnetic fields. Magnetosomes are encoded by **magnetosome gene clusters (MGCs)** / **magnetosome islands (MAIs)** (often **>30 magnetosome-associated proteins**) and develop via a canonical sequence of **membrane invagination → protein sorting → iron transport and biomineralization → chain assembly/positioning**. (dziuba2023silentgeneclusters pages 1-2, ferrara2024bacterialorganellesin pages 4-6)

**Boundary cases / nearby traits:**
- **Magnetotaxis behavior** is downstream of (and enabled by) magnetosome chain formation; it can be impaired even when some magnetosome structures exist (e.g., disorganized particles). (paulus2024mamflikeproteinsare pages 9-10, awal2023experimentalanalysisof pages 7-10)
- **Mineral type is environment-dependent:** magnetite is associated with oxygen-poor/low-sulfide conditions; greigite is associated with sulfide-rich habitats. This affects what “magnetosome” contains without changing the organelle definition (membrane enclosure + magnetic mineral). (ferrara2024bacterialorganellesin pages 2-4)
- **Dormant/foreign MGCs in non-MTB:** horizontally acquired magnetosome clusters can occur in non-magnetotactic bacteria but remain silent or unstable under negative selection, so “magnetosome trait” should be curated as **expressed organelle phenotype**, not merely presence of gene cluster. (dziuba2023silentgeneclusters pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### Conceptual decomposition into curatable sub-traits
1. **Magnetosome membrane/vesicle formation**: invagination from cytoplasmic membrane creates a compartment that becomes enriched in magnetosome proteins. (awal2023functionalexpressionof pages 1-2, ferrara2024bacterialorganellesin pages 4-6)
2. **Magnetosome protein sorting / organelle assembly**: magnetosome-associated proteins (MAPs) are recruited/retained at the magnetosome membrane (mechanism includes protein–protein interaction motifs; canonical sorting motifs remain unclear). (ferrara2024bacterialorganellesin pages 4-6)
3. **Iron uptake and intravesicular iron transport**: cytoplasmic iron import (e.g., Feo systems) and CDF-family transport into magnetosomes support mineral formation, with defined extracellular concentration regimes. (ferrara2024bacterialorganellesin pages 4-6)
4. **Biomineralization (nucleation → crystal growth → morphology control)**: nucleation near the membrane; specialized proteins regulate redox and crystal shape/size. (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32)
5. **Chain assembly, positioning, and inheritance**: cytoskeletal “magnetoskeleton” components align particles into chains that act as a compass; core is an actin-like filament (MamK) plus adaptors (MamJ or lineage-specific replacements). (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 1-2)

### Quantitative definitions (useful for trait curation)
- Magnetosome crystals in Magnetospirillum are reported as ~**45 nm** cubo‑octahedral magnetite (a common model system). (awal2023functionalexpressionof pages 1-2)
- Magnetosome gene islands typically span **~80–100 kb (~2% of genome)** and contain **>30 MAPs** across multiple operons; a conserved core set reported includes **mamABEKMOPQI** (and closely related “core” sets in genomic surveys). (ferrara2024bacterialorganellesin pages 2-4, xie2023linkingmineralsto pages 1-2)

---

## 2) Candidate causal graph entities (nodes) with ontology grounding

The following table is prepared for direct translation into `data/traits/morphology/magnetosome.yaml` node lists.

| Node label | Type | Suggested grounding | Evidence source IDs |
|---|---|---|---|
| mamB | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4, dziuba2023silentgeneclusters pages 1-2) |
| mamM | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4, awal2023functionalexpressionof pages 1-2) |
| mamE | gene/protein | GO:0008236 serine-type peptidase activity | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| mamO | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4, dziuba2023silentgeneclusters pages 1-2) |
| mamP | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| mamT | gene/protein | unmapped | (martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| mamA | gene/protein | GO:0005515 protein binding | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4) |
| mamI | gene/protein | unmapped | (dziuba2023silentgeneclusters pages 1-2, sun2024essentialmagnetosomeproteins pages 1-2, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| mamL | gene/protein | unmapped | (dziuba2023silentgeneclusters pages 1-2, sun2024essentialmagnetosomeproteins pages 1-2, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| mamQ | gene/protein | unmapped | (dziuba2023silentgeneclusters pages 1-2, ferrara2024bacterialorganellesin pages 2-4, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| mamK | gene/protein | GO:0003779 actin binding | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 10-12, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| mamJ | gene/protein | unmapped | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 10-12, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| mamY | gene/protein | unmapped | (awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| mcaA | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, xie2023linkingmineralsto pages 1-2) |
| mcaB | gene/protein | unmapped | (xie2023linkingmineralsto pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| mad28 | gene/protein | unmapped | (awal2023experimentalanalysisof pages 7-10, xie2023linkingmineralsto pages 1-2, awal2023experimentalanalysisof pages 10-12, russell2024madformagnetosomes pages 28-30) |
| mamF-like proteins (MamF/MmsF/MmxF family) | gene/protein | TIGRFAM/InterPro family candidate; unmapped | (paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 9-10) |
| mmsF | gene/protein | unmapped | (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 9-10, bickley2023thelocalizationof pages 7-10) |
| mms5 | gene/protein | unmapped | (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 6-8) |
| mms6 | gene/protein | unmapped | (bickley2023thelocalizationof pages 7-10, dziuba2023silentgeneclusters pages 1-2) |
| mamD | gene/protein | unmapped | (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 6-8, bickley2023thelocalizationof pages 7-10) |
| mamG | gene/protein | unmapped | (paulus2024mamflikeproteinsare pages 3-5, bickley2023thelocalizationof pages 7-10) |
| mamH | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| mamZ | gene/protein | unmapped | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4) |
| feoB1 | gene/protein | GO:0015691 iron ion transport | (ferrara2024bacterialorganellesin pages 4-6, ferrara2024bacterialorganellesin pages 2-4) |
| feoB2 | gene/protein | GO:0015691 iron ion transport | (ferrara2024bacterialorganellesin pages 4-6) |
| feoA/feoB system | pathway | KEGG module candidate; unmapped | (awal2023functionalexpressionof pages 1-2, dziuba2023silentgeneclusters pages 1-2) |
| mamAB operon | pathway | unmapped | (awal2023functionalexpressionof pages 1-2, ferrara2024bacterialorganellesin pages 2-4, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| mamGFDC operon | pathway | unmapped | (awal2023functionalexpressionof pages 1-2, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, bickley2023thelocalizationof pages 7-10) |
| mamXY operon | pathway | unmapped | (awal2023functionalexpressionof pages 1-2, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| mms6 operon | pathway | unmapped | (awal2023functionalexpressionof pages 1-2, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| magnetosome gene cluster / magnetosome island (MGC/MAI) | pathway | unmapped | (dziuba2023silentgeneclusters pages 1-2, ferrara2024bacterialorganellesin pages 2-4, sun2024essentialmagnetosomeproteins pages 1-2) |
| magnetosome membrane | cellular component | GO:0042582 azurosome? / unmapped preferred | (ferrara2024bacterialorganellesin pages 4-6, dziuba2023silentgeneclusters pages 1-2, sun2024essentialmagnetosomeproteins pages 1-2) |
| magnetosome chain | cellular component | unmapped | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| magnetosome organelle | cellular component | GO:1902494 magnetosome | (dziuba2023silentgeneclusters pages 1-2, ferrara2024bacterialorganellesin pages 4-6, paulus2024mamflikeproteinsare pages 1-2) |
| magnetite crystal | chemical | CHEBI:46662 magnetite | (awal2023functionalexpressionof pages 1-2, sun2024essentialmagnetosomeproteins pages 1-2, gubieda2024temporalandspatial pages 1-3) |
| greigite crystal | chemical | CHEBI:139278 greigite | (ferrara2024bacterialorganellesin pages 2-4, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) |
| Fe2+ | chemical | CHEBI:29033 ferrous iron(2+) | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) |
| Fe3+ | chemical | CHEBI:29034 ferric iron(3+) | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) |
| iron | chemical | CHEBI:18248 iron atom | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41, chades2024setupofa pages 9-11) |
| sulfide-rich habitat | environment | ENVO:00002044 sulfide? / unmapped | (ferrara2024bacterialorganellesin pages 2-4) |
| oxygen-poor environment | environment | ENVO:01000949 low oxygen? / unmapped | (ferrara2024bacterialorganellesin pages 2-4, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) |
| oxic-anoxic interface | environment | ENVO:01000314 oxic-anoxic interface | (martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturing pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| redox gradient | environment | unmapped | (awal2023functionalexpressionof pages 1-2, dziuba2023silentgeneclusters pages 1-2, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) |
| membrane invagination | process | GO:0010324 membrane invagination | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, sun2024essentialmagnetosomeproteins pages 1-2) |
| magnetosome protein sorting | process | GO:0008104 protein localization? / unmapped | (ferrara2024bacterialorganellesin pages 4-6, paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 5-6) |
| iron transport into magnetosome | process | GO:0034755 iron ion transmembrane transport | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| magnetite nucleation | process | GO:0030001 metal ion transport? / unmapped | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32) |
| biomineralization | process | GO:0031214 biomineral tissue development? / unmapped preferred | (awal2023functionalexpressionof pages 1-2, ferrara2024bacterialorganellesin pages 4-6, paulus2024mamflikeproteinsare pages 1-2) |
| chain assembly/positioning | process | unmapped | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) |
| magnetotaxis / magnetoaerotaxis | process | GO:0042330 taxis? / unmapped | (dziuba2023silentgeneclusters pages 1-2, ferrara2024bacterialorganellesin pages 2-4, paulus2024mamflikeproteinsare pages 9-10) |


*Table: This table lists candidate nodes for a TraitMech causal graph of the magnetosome trait, grouped across genes/proteins, pathways, chemicals, environments, cellular structures, and processes. It highlights the most curation-ready mechanistic entities and the evidence contexts supporting inclusion.*

---

## 3) Evidence-backed candidate causal edges (triples)

The following table provides subject–predicate–object candidates, each with supporting evidence, snippet, and curation notes.

| Subject node | Predicate | Object node | Evidence | Supporting snippet | Notes/uncertainty |
|---|---|---|---|---|---|
| mamAB operon | sufficient for | rudimentary biomineralization | (martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturing pages 29-32, ferrara2024bacterialorganellesin pages 2-4) | “the mamAB operon is sufficient for rudimentary biomineralization” | Well supported in Magnetospirillum-focused summaries; may not capture full diversity across all MTB lineages. |
| MamB | promotes | membrane invagination | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32) | “MamB… likely recruits MAPs and promotes membrane invagination” | Mechanistic wording in review is partly inferential from prior genetics/phenotypes; curate as likely/qualified. |
| MamB | recruits | magnetosome-associated proteins (MAPs) | (ferrara2024bacterialorganellesin pages 4-6) | “MamB… likely recruits MAPs” | Review-level synthesis; MAP recruitment mechanism still unresolved. |
| MamF-like proteins (MmsF/MmxF/MamF family) | enable targeting of | MamD and Mms5 to magnetosome membrane | (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 9-10) | “all three MFPs facilitate MM targeting of MamD and Mms5” | Strong 2024 evidence in M. gryphiswaldense; family-specific and taxon-tested mainly in alphaproteobacteria. |
| MamF-like proteins | required for | magnetosome chain formation | (paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 9-10) | “chain formation is disrupted in the absence of mmsF and mmxF” | Strong in deletion/complementation experiments; exact generality beyond tested strains uncertain. |
| MamF-like proteins | promote | magnetic navigation / magnetotaxis | (paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 9-10) | deletion caused “severe defects in organelle positioning, biomineralization, and magnetic navigation” | Downstream phenotype; may be represented via chain formation/crystal maturation rather than direct edge if graph stays mechanistic. |
| MamK | organizes | magnetosome chain assembly | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 10-12, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | “MTB align their magnetosome organelles into chains, which are organized by the actin-like MamK” | Strong and broadly conserved; one of the safest curation edges. |
| MamK | polymerizes into | actin-like filaments | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | “MamK polymerizes into long, actin-like filaments” | Structural/functional support strong; useful intermediate node if graph includes cytoskeletal filament entity. |
| MamJ | tethers | magnetosomes to MamK filaments | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | “MamJ acts as a connector attaching magnetosomes to MamK filaments” | Strong in Magnetospirillum; some MTB lack MamJ orthologs and use alternative adaptors. |
| MamJ-like adaptor (e.g., mg-1g50) | can substitute for | MamJ tethering function | (awal2023experimentalanalysisof pages 7-10, awal2023experimentalanalysisof pages 10-12) | “identified a novel… protein… that substitutes the function of the well-characterized MamJ protein” | Taxon-specific rescue evidence; curate as optional lineage-specific branch. |
| oxygen-poor / low-sulfide environment | favors | magnetite magnetosomes | (ferrara2024bacterialorganellesin pages 2-4) | “magnetite is more common in oxygen-poor, low-sulfide environments” | Environmental association rather than direct intracellular mechanism; useful ecological edge. |
| oxic-anoxic interface | enriches for | magnetotactic bacteria niche | (martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, martinez2024enhancingmagnetosomebiomanufacturing pages 29-32, martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32, dziuba2023silentgeneclusters pages 1-2) | MTB are “microaerophiles, anaerobes or facultative anaerobes” inhabiting the “oxic-anoxic interface” | Ecological niche statement; could be linked to magnetoaerotaxis rather than magnetosome organelle directly. |
| sulfide-rich habitat | favors | greigite magnetosomes | (ferrara2024bacterialorganellesin pages 2-4) | “greigite dominates in sulfide-rich habitats” | Strong environmental-mineralogy correlation; not universal at all sulfide levels. |
| extracellular iron 20–50 µM | saturates | iron uptake / biomineralization | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) | “uptake/biomineralization saturate at extracellular 20–50 μM” | Quantitative and curation-ready; likely strain/culture-condition dependent. |
| extracellular iron 200 µM | inhibits | MTB growth | (ferrara2024bacterialorganellesin pages 4-6, martinez2024enhancingmagnetosomebiomanufacturing pages 38-41) | “200 μM iron inhibits MTB growth” | Quantitative but culture-condition dependent; annotate as experimental/environmental factor. |
| magnetite in internalized magnetosomes | oxidizes to | maghemite in mammalian tumor cells over days | (gubieda2024temporalandspatial pages 7-9, gubieda2024temporalandspatial pages 5-7, gubieda2024temporalandspatial pages 1-3) | “by 8 days whole-map XANES showed ~25% maghemite” and “magnetite slowly oxidising to maghemite” | Application-context edge in mammalian cells, not native MTB biology; should not be merged into core microbial trait graph unless modeling downstream use/degradation. |
| pharmaceutical cell bank minimal-medium process | produces | magnetosomes with >99.9% Fe purity | (chades2024setupofa pages 9-11, chades2024setupofa pages 1-2, chades2024setupofa media 9965903f) | “highly pure magnetosomes composed of more than 99.9% of iron” | Bioprocess edge, not intrinsic natural mechanism; useful for applications/implementation section. |
| pharmaceutical cell bank minimal-medium process | preserves | stable magnetosome production over 100 generations / 16 months cryopreservation | (chades2024setupofa pages 9-11, chades2024setupofa pages 1-2, chades2024setupofa media 9965903f) | “genetic stability observed over 100 generations or under cryo-preservation for 16 months” | Strong manufacturing evidence; again downstream implementation rather than trait mechanism. |


*Table: This table lists curation-ready and near-ready subject–predicate–object edges for the magnetosome trait, with direct supporting snippets and uncertainty notes. It is useful for translating recent literature into a TraitMech-style causal graph while separating core microbial mechanisms from environmental and application-specific edges.*

---

## 4) Mechanistic synthesis: a curation-ready causal narrative

### 4.1 Membrane formation and early organelle assembly
- **mamAB operon** is repeatedly highlighted as central; synthesis summaries state it can be **sufficient for rudimentary biomineralization**, with additional operons fine-tuning size/morphology/arrangement. (martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32, ferrara2024bacterialorganellesin pages 2-4)
- **MamB** (a CDF family member) is proposed to **promote membrane invagination and recruit MAPs** during organelle biogenesis, though mechanistic details remain partially inferential at review level. (ferrara2024bacterialorganellesin pages 4-6)
- **MamI and MamL** are “essential magnetosome genes” for vesicle formation; a 2024 heterologous study shows MamI and MamL **co-localize and physically interact** when expressed in mammalian cells, suggesting a robust protein–protein interaction module that may underpin early compartment assembly across cellular contexts. (sun2024essentialmagnetosomeproteins pages 1-2)

### 4.2 Protein targeting: a major 2024 conceptual advance (MamF-like/Tic20 link)
A 2024 Nature Communications study reframed **MamF-like proteins** (e.g., MmsF/MmxF/MamF family) as components of an **organelle-specific targeting/integration system**:
- Deleting mamF-like genes in *Magnetospirillum gryphiswaldense* caused “severe defects in organelle positioning, biomineralization, and magnetic navigation,” with **disrupted chain formation** and **mistargeting** of specific magnetosome proteins. (paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 5-6)
- The authors report that MFPs “facilitate magnetosome membrane targeting” of biomineralization proteins such as **MamD and Mms5**, and that decreased crystal sizes in MFP mutants are largely attributable to this mistargeting. (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5)
- Phylogenetic/structural analyses place MFPs as distant homologs of plastidial **Tic20**, supporting a model of “primitive organelle-specific” protein integration/translocation systems in bacteria. (paulus2024mamflikeproteinsare pages 3-5, paulus2024mamflikeproteinsare pages 9-10)

**Curation implication:** This is a high-value mechanistic module suitable for nodes/edges in TraitMech because it converts “protein sorting” from an abstract step into a concrete candidate mechanism (MamF-like targeting system). (paulus2024mamflikeproteinsare pages 5-6, paulus2024mamflikeproteinsare pages 3-5)

### 4.3 Iron transport, thresholds, and toxicity (quantitative edges)
A 2024 review on bacterial iron organelles provides quantitative constraints that are directly curatable:
- In *M. gryphiswaldense*, cytoplasmic importers include **FeoB1/FeoB2**, while magnetosome transport includes CDF-family proteins with roles differentiated by valence (e.g., MamH/MamZ for Fe(III); MamM/MamB for Fe(II)). (ferrara2024bacterialorganellesin pages 4-6)
- Quantitative iron regimes: biomineralization detectable below **1 μM** iron (in vivo), saturation at extracellular **20–50 μM**, and growth inhibition at **~200 μM** iron. (ferrara2024bacterialorganellesin pages 4-6)
- A striking quantitative statement is that **>99.5% of intracellular iron** can be contained within magnetosomes in MTB under relevant conditions. (ferrara2024bacterialorganellesin pages 4-6)

### 4.4 Chain assembly and positioning (MamK-centered magnetoskeleton)
- A 2023 mBio experimental study tested diverse MamK orthologs and additional actin-like proteins; it supports MamK as a conserved, polymerizing actin homolog that **organizes magnetosome chains**, with chain continuity/compass function dependent on proper interactions. (awal2023experimentalanalysisof pages 7-10)
- The same work provides functional evidence for adaptor diversity: a novel protein from *Magnetovibrio blakemorei* can substitute for MamJ as “a molecular adaptor tethering magnetosomes to MamK filaments,” and Mad28 orthologs can partially complement mamK mutants, indicating lineage-specific chain-organization solutions. (awal2023experimentalanalysisof pages 7-10)

---

## 5) Recent developments and latest research (prioritize 2023–2024)

### 5.1 Gene cluster transfer and engineering of magnetosome formation (2023)
A 2023 mBio study provides proof-of-principle engineering advances:
- Magnetosome formation is governed by “~30 specific genes” in compact MGCs; the authors used **transformation-associated recombination (TAR) cloning** to assemble a “compact and portable” MGC and showed it could **restore magnetite biomineralization** in both donor deletion mutants and a surrogate host (*M. gryphiswaldense*). (awal2023functionalexpressionof pages 1-2)
- Co-expression of gene clusters from two MTB resulted in **“overproduction of magnetosomes,”** suggesting modular scaling via genetic design (though the excerpt does not quantify fold-change). (awal2023functionalexpressionof pages 1-2)

### 5.2 Horizontally inherited silent MGCs in non-magnetotactic bacteria (2023)
- A 2023 ISME Journal study reports a dormant, horizontally inherited magnetosome gene cluster region (~**27.5 kb**) in a non-magnetotactic phototroph, including “all genes thought to be essential for magnetosome biosynthesis (mamIELMOQB).” (dziuba2023silentgeneclusters pages 1-2)
- Laboratory transfer could endow magnetosome biosynthesis, but the trait could be rapidly lost due to negative selection, underscoring that ecological selection pressure is part of the causal context of the trait. (dziuba2023silentgeneclusters pages 1-2)

### 5.3 Protein-targeting discovery (MamF-like/Tic20) (2024)
- The 2024 Nature Communications paper provides a mechanistic leap from “unknown sorting” to a defined targeting module, with deletion phenotypes spanning chain organization, magnetite crystal size, and magnetotaxis. (paulus2024mamflikeproteinsare pages 1-2, paulus2024mamflikeproteinsare pages 5-6)

### 5.4 Biomanufacturing and real-world implementation: pharmaceutical cell banks (2024)
A 2024 Microbial Cell Factories paper demonstrates a pharmaceutical-style implementation:
- Establishment of a **pharmaceutical cell bank (PCB)** of *M. gryphiswaldense* MSR-1 grown in minimal medium “essentially devoid of other heavy metals than iron,” producing magnetosomes “composed of more than **99.9% iron**,” with genetic stability over **100 generations** and after **16 months** cryopreservation. (chades2024setupofa pages 1-2)
- Quantified yields and properties include volumetric yields **1.45–5.66 mg/L**, magnetosome masses **7.05–28.40 mg/run**, and increased fraction of intracellular iron in magnetosomes (e.g., **~9.26% → ~44.38%**). (chades2024setupofa pages 9-11)
- The same paper frames intended applications in nanomedicine (e.g., hyperthermia/MRI) and relates metal-impurity constraints to injectable iron doses (e.g., a calculated maximum ~**530 mg Fe/day** under specific impurity limits; typical proposed experimental dose **50 mg Fe**). (chades2024setupofa pages 9-11)

**Visual supporting evidence:** Tables/Figure from this work containing production and purity metrics were retrieved (chades2024setupofa media 9965903f, chades2024setupofa media 59998fe0, chades2024setupofa media 08ba31d8, chades2024setupofa media fbfc58cd).

### 5.5 Mammalian expression and imaging-oriented research (2024)
- A 2024 Scientific Reports study expresses **MamI and MamL in mammalian cells**, demonstrates co-localization and interaction, and argues magnetosomes are a model for genetically encoded nanoparticles. It provides an MRI sensitivity estimate if full programs could be replicated: detection at 3 Tesla of ~**3 cells** (small animals) and ~**1000 cells** (large animals/humans). (sun2024essentialmagnetosomeproteins pages 1-2)

### 5.6 Fate and stability of magnetosomes in tumor-like environments (2024)
A 2024 Journal of Nanobiotechnology paper quantifies degradation/oxidation in 3D tumor spheroids:
- In A549 lung carcinoma spheroids, magnetosomes persist from **2 h to 36 days**; magnetite oxidizes to maghemite, with compositional fits showing ~**25% maghemite by day 8** and up to ~**36%** of cellular iron fraction by the end of monitoring. (gubieda2024temporalandspatial pages 7-9, gubieda2024temporalandspatial pages 5-7)
- Total cellular iron remained ~**22 pg/cell** over 36 days and magnetization declined only modestly (~**5%**), consistent with partial oxidation rather than wholesale loss. (gubieda2024temporalandspatial pages 5-7)

---

## 6) Current applications and real-world implementations

### 6.1 Nanomedicine manufacturing readiness
- The pharmaceutical cell bank approach provides concrete “implementation” evidence: standardized low-heavy-metal medium, cell bank stability, and high iron purity magnetosomes suitable for downstream biomedical use. (chades2024setupofa pages 1-2, chades2024setupofa pages 9-11)

### 6.2 “Living” or engineered magnetosome systems
- Gene cluster assembly/transfer (TAR cloning; transplantable MGCs) provides a platform for engineering magnetosome production and morphology, which is directly relevant to scalable manufacturing and application-specific particle properties. (awal2023functionalexpressionof pages 1-2)

### 6.3 Imaging and reporter gene concepts
- MamI/MamL interaction in mammalian cells is motivated as a step toward genetically encoded magnetic resonance reporters; the paper articulates theoretical detection thresholds at 3T. (sun2024essentialmagnetosomeproteins pages 1-2)

---

## 7) Expert opinions / authoritative analysis (2023–2024)
- Ferrara et al. (2024) synthesize that magnetosomes are one of three known iron-related bacterial organelles, emphasizing multi-stage biogenesis and unresolved mechanisms (e.g., no clear sorting signals, unclear iron chaperones/regulatory controls), which should temper over-specific mechanistic edges in TraitMech unless directly experimentally supported. (ferrara2024bacterialorganellesin pages 4-6)
- Paulus et al. (2024) argue that MamF-like proteins constitute an organelle-specific protein targeting system analogous (distantly) to Tic20, which reframes bacterial organelle assembly as potentially including dedicated translocase/integrase modules. (paulus2024mamflikeproteinsare pages 3-5)

---

## 8) Key statistics (recent, curation-relevant)
- Magnetosome islands: **~80–100 kb** (~2% of genome) and **>30 MAPs** in model MTB. (ferrara2024bacterialorganellesin pages 2-4)
- Intracellular iron localization: **>99.5%** of intracellular iron can be in magnetosomes (condition-dependent). (ferrara2024bacterialorganellesin pages 4-6)
- Iron concentration regimes: uptake/biomineralization saturation at **20–50 μM** extracellular iron; growth inhibition at **~200 μM**. (ferrara2024bacterialorganellesin pages 4-6)
- Pharmaceutical-grade production (2024): magnetosome purity **>99.9% Fe**; yields **1.45–5.66 mg/L**; stability over **100 generations** and **16 months** cryopreservation; high-cell load reported **~9×10^8 cells/mL**. (chades2024setupofa pages 1-2, chades2024setupofa pages 9-11)
- Tumor-spheroid fate (2024): ~**25% maghemite by day 8**, up to ~**36%** by end; iron ~**22 pg/cell** stable; magnetization decline ~**5%** over 36 days. (gubieda2024temporalandspatial pages 7-9, gubieda2024temporalandspatial pages 5-7)

---

## 9) Curation warnings (claims to treat cautiously)
1. **MamB “recruits MAPs/promotes invagination”** is phrased as “likely” in review synthesis; curate with qualifiers unless tied to a specific experimental paper in your evidence set. (ferrara2024bacterialorganellesin pages 4-6)
2. **Environmental mineral-type associations** (magnetite vs greigite) are broad ecological correlations; do not overinterpret as deterministic rules without specifying environment range and taxon. (ferrara2024bacterialorganellesin pages 2-4)
3. **Applications in mammalian imaging**: current work demonstrates interaction/localization of a subset of proteins (MamI/MamL), not full magnetosome biomineralization in mammalian cells; MRI sensitivity values are explicitly theoretical. (sun2024essentialmagnetosomeproteins pages 1-2)
4. **Manufacturing edges** (PCB → purity/yield) are implementation-specific and should be separated from the core microbial mechanism causal graph unless TraitMech intends to include “process” contexts. (chades2024setupofa pages 1-2, chades2024setupofa pages 9-11)

---

## DOI-first bibliography (with URLs and publication dates where available)
- Paulus A, et al. **MamF-like proteins are distant Tic20 homologs involved in organelle assembly in bacteria.** *Nature Communications* (Dec 2024). DOI: **10.1038/s41467-024-55121-0**. https://doi.org/10.1038/s41467-024-55121-0 (paulus2024mamflikeproteinsare pages 1-2)
- Ferrara KM, Gupta KR, Pi H. **Bacterial Organelles in Iron Physiology.** *Molecular Microbiology* 122:914–928 (Nov 2024). DOI: **10.1111/mmi.15330**. https://doi.org/10.1111/mmi.15330 (ferrara2024bacterialorganellesin pages 4-6)
- Sun Q, et al. **Essential magnetosome proteins MamI and MamL from magnetotactic bacteria interact in mammalian cells.** *Scientific Reports* (Nov 2024). DOI: **10.1038/s41598-024-77591-4**. https://doi.org/10.1038/s41598-024-77591-4 (sun2024essentialmagnetosomeproteins pages 1-2)
- Gubieda AG, et al. **Temporal and spatial resolution of magnetosome degradation at the subcellular level in a 3D lung carcinoma model.** *Journal of Nanobiotechnology* (Sep 2024). DOI: **10.1186/s12951-024-02788-8**. https://doi.org/10.1186/s12951-024-02788-8 (gubieda2024temporalandspatial pages 5-7)
- Chades T, et al. **Set-up of a pharmaceutical cell bank of Magnetospirillum gryphiswaldense MSR1 magnetotactic bacteria producing highly pure magnetosomes.** *Microbial Cell Factories* (Feb 2024). DOI: **10.1186/s12934-024-02313-4**. https://doi.org/10.1186/s12934-024-02313-4 (chades2024setupofa pages 1-2)
- Awal RP, Lefevre CT, Schüler D. **Functional expression of foreign magnetosome genes in the alphaproteobacterium Magnetospirillum gryphiswaldense.** *mBio* (Jun 2023). DOI: **10.1128/mbio.03282-22**. https://doi.org/10.1128/mbio.03282-22 (awal2023functionalexpressionof pages 1-2)
- Awal RP, et al. **Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in Magnetospirillum gryphiswaldense.** *mBio* (Oct 2023). DOI: **10.1128/mbio.01649-23**. https://doi.org/10.1128/mbio.01649-23 (awal2023experimentalanalysisof pages 7-10)
- Dziuba M, et al. **Silent gene clusters encode magnetic organelle biosynthesis in a non-magnetotactic phototrophic bacterium.** *The ISME Journal* (Dec 2023). DOI: **10.1038/s41396-022-01348-y**. https://doi.org/10.1038/s41396-022-01348-y (dziuba2023silentgeneclusters pages 1-2)
- Xie S. **Linking minerals to bacterial genes.** *National Science Review* (Nov 2023). DOI: **10.1093/nsr/nwac265**. https://doi.org/10.1093/nsr/nwac265 (xie2023linkingmineralsto pages 1-2)



References

1. (dziuba2023silentgeneclusters pages 1-2): M. Dziuba, A. Paulus, L. Schramm, R. P. Awal, M. Pósfai, C. Monteil, S. Fouteau, R. Uebe, and D. Schüler. Silent gene clusters encode magnetic organelle biosynthesis in a non-magnetotactic phototrophic bacterium. The ISME Journal, 17:326-339, Dec 2023. URL: https://doi.org/10.1038/s41396-022-01348-y, doi:10.1038/s41396-022-01348-y. This article has 21 citations.

2. (ferrara2024bacterialorganellesin pages 4-6): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (paulus2024mamflikeproteinsare pages 9-10): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

4. (awal2023experimentalanalysisof pages 7-10): Ram Prasad Awal, Frank D. Müller, Daniel Pfeiffer, Caroline L. Monteil, Guy Perrière, Christopher T. Lefèvre, and Dirk Schüler. Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in <i>magnetospirillum gryphiswaldense</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.01649-23, doi:10.1128/mbio.01649-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (ferrara2024bacterialorganellesin pages 2-4): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (awal2023functionalexpressionof pages 1-2): Ram Prasad Awal, Christopher T. Lefevre, and Dirk Schüler. Functional expression of foreign magnetosome genes in the alphaproteobacterium magnetospirillum gryphiswaldense. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03282-22, doi:10.1128/mbio.03282-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

7. (martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32): M Masó Martínez. Enhancing magnetosome biomanufacturing: understanding biomineralization and process development. Unknown journal, 2024.

8. (awal2023experimentalanalysisof pages 1-2): Ram Prasad Awal, Frank D. Müller, Daniel Pfeiffer, Caroline L. Monteil, Guy Perrière, Christopher T. Lefèvre, and Dirk Schüler. Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in <i>magnetospirillum gryphiswaldense</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.01649-23, doi:10.1128/mbio.01649-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (xie2023linkingmineralsto pages 1-2): Shucheng Xie. Linking minerals to bacterial genes. National Science Review, Nov 2023. URL: https://doi.org/10.1093/nsr/nwac265, doi:10.1093/nsr/nwac265. This article has 2 citations and is from a peer-reviewed journal.

10. (martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32): M Masó Martínez. Enhancing magnetosome biomanufacturing: understanding biomineralization and process development. Unknown journal, 2024.

11. (sun2024essentialmagnetosomeproteins pages 1-2): Qin Sun, Liu Yu, Sarah C. Donnelly, Cécile Fradin, R. Terry Thompson, Frank S. Prato, and Donna E. Goldhawk. Essential magnetosome proteins mami and maml from magnetotactic bacteria interact in mammalian cells. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-77591-4, doi:10.1038/s41598-024-77591-4. This article has 4 citations and is from a peer-reviewed journal.

12. (awal2023experimentalanalysisof pages 10-12): Ram Prasad Awal, Frank D. Müller, Daniel Pfeiffer, Caroline L. Monteil, Guy Perrière, Christopher T. Lefèvre, and Dirk Schüler. Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in <i>magnetospirillum gryphiswaldense</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.01649-23, doi:10.1128/mbio.01649-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

13. (russell2024madformagnetosomes pages 28-30): VV Russell. Mad for magnetosomes: uncovering the mechanism for synthesizing and organizing tooth. Unknown journal, 2024.

14. (paulus2024mamflikeproteinsare pages 1-2): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

15. (paulus2024mamflikeproteinsare pages 5-6): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

16. (paulus2024mamflikeproteinsare pages 3-5): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

17. (bickley2023thelocalizationof pages 7-10): C Bickley. The localization of magnetite biogenesis proteins in magnetospirillum magneticum amb-1. Unknown journal, 2023.

18. (paulus2024mamflikeproteinsare pages 6-8): Anja Paulus, Frederik Ahrens, Annika Schraut, Hannah Hofmann, Tim Schiller, Thomas Sura, Dörte Becher, and René Uebe. Mamf-like proteins are distant tic20 homologs involved in organelle assembly in bacteria. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-55121-0, doi:10.1038/s41467-024-55121-0. This article has 6 citations and is from a highest quality peer-reviewed journal.

19. (gubieda2024temporalandspatial pages 1-3): Alicia G. Gubieda, Lucía Gandarias, Mihály Pósfai, Ajith Pattammattel, M. Luisa Fdez-Gubieda, Ana Abad-Díaz-de-Cerio, and Ana García-Prieto. Temporal and spatial resolution of magnetosome degradation at the subcellular level in a 3d lung carcinoma model. Journal of Nanobiotechnology, Sep 2024. URL: https://doi.org/10.1186/s12951-024-02788-8, doi:10.1186/s12951-024-02788-8. This article has 4 citations and is from a peer-reviewed journal.

20. (martinez2024enhancingmagnetosomebiomanufacturing pages 38-41): M Masó Martínez. Enhancing magnetosome biomanufacturing: understanding biomineralization and process development. Unknown journal, 2024.

21. (chades2024setupofa pages 9-11): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.

22. (martinez2024enhancingmagnetosomebiomanufacturing pages 29-32): M Masó Martínez. Enhancing magnetosome biomanufacturing: understanding biomineralization and process development. Unknown journal, 2024.

23. (gubieda2024temporalandspatial pages 7-9): Alicia G. Gubieda, Lucía Gandarias, Mihály Pósfai, Ajith Pattammattel, M. Luisa Fdez-Gubieda, Ana Abad-Díaz-de-Cerio, and Ana García-Prieto. Temporal and spatial resolution of magnetosome degradation at the subcellular level in a 3d lung carcinoma model. Journal of Nanobiotechnology, Sep 2024. URL: https://doi.org/10.1186/s12951-024-02788-8, doi:10.1186/s12951-024-02788-8. This article has 4 citations and is from a peer-reviewed journal.

24. (gubieda2024temporalandspatial pages 5-7): Alicia G. Gubieda, Lucía Gandarias, Mihály Pósfai, Ajith Pattammattel, M. Luisa Fdez-Gubieda, Ana Abad-Díaz-de-Cerio, and Ana García-Prieto. Temporal and spatial resolution of magnetosome degradation at the subcellular level in a 3d lung carcinoma model. Journal of Nanobiotechnology, Sep 2024. URL: https://doi.org/10.1186/s12951-024-02788-8, doi:10.1186/s12951-024-02788-8. This article has 4 citations and is from a peer-reviewed journal.

25. (chades2024setupofa pages 1-2): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.

26. (chades2024setupofa media 9965903f): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.

27. (chades2024setupofa media 59998fe0): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.

28. (chades2024setupofa media 08ba31d8): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.

29. (chades2024setupofa media fbfc58cd): Théo Chades, Raphaël Le Fèvre, Imène Chebbi, Karine Blondeau, François Guyot, and Edouard Alphandéry. Set-up of a pharmaceutical cell bank of magnetospirillum gryphiswaldense msr1 magnetotactic bacteria producing highly pure magnetosomes. Microbial Cell Factories, Feb 2024. URL: https://doi.org/10.1186/s12934-024-02313-4, doi:10.1186/s12934-024-02313-4. This article has 12 citations and is from a peer-reviewed journal.