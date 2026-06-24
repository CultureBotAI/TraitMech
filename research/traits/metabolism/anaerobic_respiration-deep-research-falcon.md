---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:59:27.624663'
end_time: '2026-06-18T04:20:41.162207'
duration_seconds: 1273.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Anaerobic respiration
  trait_identifier: METPO:1000802
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: anaerobic_respiration
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A respiration in which an organism uses electron acceptors other than
    oxygen for energy production.
  parent_traits: METPO:1000800
  synonyms: "Anoxic respiration, Dissimilatory respiration (non-O\u2082)"
  evidence_summary: 'DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron
    acceptors (Denitrification review supports anaerobic respiration using non-oxygen
    terminal electron acceptors.)'
  causal_graph_summary: 'anaerobic_respiration_denitrification: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Anaerobic respiration
- **METPO identifier:** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Anaerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_respiration.yaml`.

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
- **Trait label:** Anaerobic respiration
- **METPO identifier:** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Anaerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_respiration.yaml`.

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


## Anaerobic respiration (METPO:1000802) — curation-focused research report (2024-centered)

### 1) Scope summary (TraitMech curation semantics)

**Trait definition (operational):** Anaerobic respiration is the **capacity for respiratory energy conservation** under oxygen limitation by using a **terminal electron acceptor (TEA) other than O\₂** via an electron transport chain (ETC) and terminal reductase(s). This aligns with the METPO definition (“electron acceptors other than oxygen”).

**Boundary cases / exclusions (important for graph curation):**
- **Fermentation is excluded** (no external TEA; redox balance via internal electron sinks rather than terminal reductases). This is consistent with treating anaerobic respiration as ETC-mediated energy conservation.
- **Microaerobic respiration is excluded** because O\₂ remains the TEA.
- **Assimilatory nitrate reduction is excluded** because its purpose is biosynthesis rather than energy conservation; in contrast, DNRA/denitrification modules are respiratory.
- **“Aerobic denitrification”** should be treated as **anaerobic-respiration machinery operating under transient oxic conditions** (enzyme persistence and/or incomplete suppression), not a separate trait (roothans2024aerobicdenitrificationas pages 8-9, sennett2024determininghowoxygen pages 1-2).

### 2) Key concepts and current understanding (mechanistic entities)

Anaerobic respiration is best represented in a causal graph as **(environmental redox context + TEA availability) → (gene regulation) → (terminal reductase activity) → (electron flux / intermediates) → (growth/energy outcomes + byproducts)**.

**Canonical nitrogen-oxide respiratory module (denitrification):** sequential reduction steps mediated by functionally modular enzyme complexes, typically including nitrate reductases (Nar/Nap), nitrite reductases (NirK/NirS), nitric oxide reductases (Nor), and nitrous oxide reductase (NosZ). The 2024 oxygen-legacy study explicitly frames the core reductases and the strong role of O\₂ in regulating denitrification (sennett2024determininghowoxygen pages 1-2).

**DNRA (dissimilatory nitrate reduction to ammonium):** respiratory reduction of nitrate/nitrite to ammonium. A 2024 mSystems paper reports a **noncanonical DNRA mechanism** in an acidophilic sulfate-reducing bacterium that lacks recognized nitrite reductases, implicating alternative enzymes (AsrABC and/or a NirA-like protein) and highlighting mechanistic diversity within the trait (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 10-13).

**Sulfoxide/N-oxide respiration:** facultative anaerobes can use sulfoxides such as DMSO and even **methionine sulfoxide (MetSO)** as TEAs via molybdoenzyme terminal reductases. In 2024, *Salmonella* is shown to use **DmsABC** for anaerobic respiration with MetSO and DMSO (kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 10-11).

**Electron shuttles and coupling to respiration:** extracellular redox-active metabolites can couple to TEA reduction by feeding electrons into terminal reductase complexes. A 2024 bioRxiv preprint shows **phenazine-1-carboxylic acid (PCA) oxidation** coupled to anaerobic respiration with nitrate/fumarate/DMSO/TMAO, with terminal reductases genetically required in multiple cases (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 31-36, tsypin2024geneticallydissectingthe pages 21-26).

### 3) Candidate nodes for the causal graph (grouped by type)

The following node inventory is limited to entities directly supported by the retrieved 2024 evidence set.

| Group | Preferred label | Type | Brief definition | Suggested grounding | Key supporting source context IDs |
|---|---|---|---|---|---|
| Biological processes/pathways | anaerobic respiration | biological process | Respiratory energy conservation using terminal electron acceptors other than O2 | METPO:1000802; GO:0009061 | (sennett2024determininghowoxygen pages 1-2, tsypin2024geneticallydissectingthe pages 1-6) |
| Biological processes/pathways | denitrification | biological process | Stepwise respiratory reduction of nitrate/nitrite to gaseous nitrogen oxides and N2 | GO:0019645 | (roothans2024aerobicdenitrificationas pages 8-9, sennett2024determininghowoxygen pages 1-2) |
| Biological processes/pathways | dissimilatory nitrate reduction to ammonium | biological process | Respiratory nitrate/nitrite reduction retaining nitrogen as ammonium | GO:0042128 | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5) |
| Biological processes/pathways | nitrate respiration | biological process | Anaerobic respiration using nitrate as terminal electron acceptor | GO:0009064 | (egas2024anovelmechanism pages 2-5, tsypin2024geneticallydissectingthe pages 21-26) |
| Biological processes/pathways | fumarate respiration | biological process | Anaerobic respiration using fumarate as terminal electron acceptor | GO:0009057 | (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 1-6) |
| Biological processes/pathways | DMSO respiration | biological process | Anaerobic respiration using dimethyl sulfoxide as terminal electron acceptor | label-only | (kim2024anaerobicrespirationof pages 8-10, tsypin2024geneticallydissectingthe pages 26-31) |
| Biological processes/pathways | methionine sulfoxide respiration | biological process | Anaerobic respiration using methionine sulfoxide as terminal electron acceptor | label-only | (kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 10-11) |
| Biological processes/pathways | PCA oxidation coupled to anaerobic respiration | biological process | Oxidation of reduced phenazine-1-carboxylic acid linked to terminal reductase activity during anaerobic respiration | label-only | (tsypin2024geneticallydissectingthe pages 1-6, tsypin2024geneticallydissectingthe pages 31-36) |
| Electron acceptors | nitrate | electron acceptor | Oxidized nitrogen oxyanion reduced during nitrate respiration, denitrification, or DNRA | CHEBI:17632 | (egas2024anovelmechanism pages 2-5, tsypin2024geneticallydissectingthe pages 21-26) |
| Electron acceptors | nitrite | electron acceptor/intermediate | Reduced product of nitrate reduction and substrate for denitrification or DNRA | CHEBI:16301 | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5) |
| Electron acceptors | nitric oxide | electron acceptor/intermediate | Gaseous denitrification intermediate reduced by nitric oxide reductases or Hcp-like systems | CHEBI:16480 | (egas2024anovelmechanism pages 9-10, roothans2024aerobicdenitrificationas pages 8-9) |
| Electron acceptors | nitrous oxide | electron acceptor/intermediate | Denitrification intermediate reduced to dinitrogen by NosZ | CHEBI:17045 | (egas2024anovelmechanism pages 9-10, roothans2024aerobicdenitrificationas pages 8-9) |
| Electron acceptors | fumarate | electron acceptor | Dicarboxylate terminal electron acceptor reduced during fumarate respiration | CHEBI:18012 | (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 6-9) |
| Electron acceptors | dimethyl sulfoxide | electron acceptor | Sulfoxide terminal electron acceptor used by DmsABC-family reductases | CHEBI:16385 | (kim2024anaerobicrespirationof pages 8-10, tsypin2024geneticallydissectingthe pages 26-31) |
| Electron acceptors | methionine sulfoxide | electron acceptor | Host- or environment-derived oxidized methionine used as respiratory terminal electron acceptor in Salmonella | label-only | (kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 10-11) |
| Electron acceptors | trimethylamine N-oxide | electron acceptor | N-oxide terminal electron acceptor in anaerobic respiration | CHEBI:15725 | (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 36-40) |
| Electron donors/shuttles | reduced PCA | electron donor/shuttle | Reduced phenazine-1-carboxylic acid that donates electrons into respiratory chains | label-only | (tsypin2024geneticallydissectingthe pages 1-6, tsypin2024geneticallydissectingthe pages 6-9) |
| Electron donors/shuttles | benzyl viologen | experimental electron donor | Artificial low-potential donor used to assay DmsABC sulfoxide reductase activity | CHEBI:29988 | (kim2024anaerobicrespirationof pages 31-36, kim2024anaerobicrespirationof pages 15-16) |
| Electron donors/shuttles | quinone pool | electron carrier | Membrane quinones transferring electrons from donors to terminal reductases | label-only | (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 9-16) |
| Enzymes/complexes/genes | narGHI | enzyme complex/gene set | Membrane-bound respiratory nitrate reductase complex reducing nitrate to nitrite | EC:1.7.5.1 | (egas2024anovelmechanism pages 2-5, tsypin2024geneticallydissectingthe pages 9-16) |
| Enzymes/complexes/genes | narG | gene/protein | Catalytic alpha subunit of membrane-bound nitrate reductase | label-only | (egas2024anovelmechanism pages 2-5, tsypin2024geneticallydissectingthe pages 21-26) |
| Enzymes/complexes/genes | narZ | gene/protein | Alternative catalytic nitrate reductase subunit contributing to nitrate-dependent PCA oxidation | label-only | (tsypin2024geneticallydissectingthe pages 36-40, tsypin2024geneticallydissectingthe pages 21-26) |
| Enzymes/complexes/genes | napA | gene/protein | Catalytic subunit of periplasmic nitrate reductase | label-only | (tsypin2024geneticallydissectingthe pages 36-40, tsypin2024geneticallydissectingthe pages 21-26) |
| Enzymes/complexes/genes | narK | transporter/gene | Nitrate/nitrite transporter upregulated during DNRA conditions | label-only | (egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 10-13) |
| Enzymes/complexes/genes | NirK | enzyme/gene | Copper-containing nitrite reductase producing NO from nitrite | EC:1.7.2.1 | (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 9-11) |
| Enzymes/complexes/genes | NirS | enzyme/gene | Cytochrome cd1 nitrite reductase producing NO from nitrite | EC:1.7.2.1 | (roothans2024aerobicdenitrificationas pages 8-9, sennett2024determininghowoxygen pages 1-2) |
| Enzymes/complexes/genes | NorB/C | enzyme complex/gene set | Nitric oxide reductase reducing NO to N2O | EC:1.7.2.5 | (schacksen2024unravelingthegenetic pages 9-11) |
| Enzymes/complexes/genes | NosZ | enzyme/gene | Nitrous oxide reductase reducing N2O to N2 | EC:1.7.2.4 | (egas2024anovelmechanism pages 9-10, schacksen2024unravelingthegenetic pages 1-2) |
| Enzymes/complexes/genes | nosZ clade I | gene class | Clade I nitrous oxide reductase lineage enriched in canonical denitrifiers | label-only | (schacksen2024unravelingthegenetic pages 11-13, sennett2024determininghowoxygen pages 1-2) |
| Enzymes/complexes/genes | nosZ clade II | gene class | Clade II nitrous oxide reductase lineage common in partial/non-denitrifiers | label-only | (schacksen2024unravelingthegenetic pages 11-13, sennett2024determininghowoxygen pages 1-2) |
| Enzymes/complexes/genes | AsrABC | enzyme complex/gene set | Anaerobic sulfite reductase complex proposed to reduce nitrite to ammonium in noncanonical DNRA | EC:1.8.1.2 (native sulfite reductase activity); DNRA role label-only | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5) |
| Enzymes/complexes/genes | DEACI_1836 (NirA-like) | enzyme/gene candidate | Putative ferredoxin-dependent NirA-like nitrite reductase candidate for nitrite-to-ammonium reduction | label-only | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 10-13) |
| Enzymes/complexes/genes | Hcp | enzyme/gene | Hybrid cluster protein functioning here as high-affinity nitric oxide reductase | label-only | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 10-13) |
| Enzymes/complexes/genes | DmsABC | enzyme complex/gene set | Membrane molybdoenzyme complex reducing DMSO and MetSO during anaerobic respiration | EC:1.8.5.3 | (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 11-13) |
| Enzymes/complexes/genes | dmsA | gene/protein | Catalytic subunit of DmsABC required for DMSO-driven PCA oxidation and sulfoxide respiration | label-only | (kim2024anaerobicrespirationof pages 6-8, tsypin2024geneticallydissectingthe pages 26-31) |
| Enzymes/complexes/genes | moaABCDE | biosynthetic gene set | Molybdopterin cofactor biosynthesis genes enabling function of nitrate/TMAO/DMSO reductases | KEGG:map00190 (supporting respiratory context); gene set label-only | (kim2024anaerobicrespirationof pages 5-6, kim2024anaerobicrespirationof pages 6-8) |
| Enzymes/complexes/genes | FrdA | enzyme/gene | Catalytic subunit of fumarate reductase required for fumarate-driven PCA oxidation | EC:1.3.5.4 | (tsypin2024geneticallydissectingthe pages 26-31) |
| Environmental/experimental factors | anoxia / oxygen limitation | environmental factor | Low-oxygen state permitting induction and activity of anaerobic respiratory pathways | ENVO:01001018 (hypoxic environment, approximate); label-only acceptable | (sennett2024determininghowoxygen pages 1-2, kim2024anaerobicrespirationof pages 6-8) |
| Environmental/experimental factors | oxic/anoxic cycling | environmental factor | Repeated oxygen transitions shaping denitrification enzyme persistence and activity | label-only | (roothans2024aerobicdenitrificationas pages 8-9, sennett2024determininghowoxygen pages 1-2) |
| Environmental/experimental factors | oxygen legacy | environmental factor | Prior O2 exposure regime influencing later denitrification rates and nosZ clade activity | label-only | (sennett2024determininghowoxygen pages 1-2) |
| Environmental/experimental factors | constant oxic legacy (Ox) | experimental condition | Soil treatment maintained oxic before final anoxic incubation | label-only | (sennett2024determininghowoxygen pages 9-10, sennett2024determininghowoxygen pages 1-2) |
| Environmental/experimental factors | short anoxic spells (SA) | experimental condition | Cycling regime with short anoxic and longer oxic periods | label-only | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 2-3) |
| Environmental/experimental factors | long anoxic spells (LA) | experimental condition | Cycling regime with long anoxic and shorter oxic periods | label-only | (sennett2024determininghowoxygen pages 9-10, sennett2024determininghowoxygen pages 1-2) |
| Environmental/experimental factors | nitrate availability | environmental factor | Presence/addition of nitrate supporting nitrate respiration and denitrification kinetics | CHEBI:17632 | (tsypin2024geneticallydissectingthe pages 31-36, sennett2024determininghowoxygen pages 2-3) |
| Environmental/experimental factors | terminal electron acceptor availability | environmental factor | Availability of respirable acceptors such as nitrate, fumarate, DMSO, TMAO stimulating anaerobic respiratory flux | label-only | (tsypin2024geneticallydissectingthe pages 1-6, tsypin2024geneticallydissectingthe pages 31-36) |
| Phenotypes/assays/outputs | anaerobic growth on DMSO | phenotype | Growth increase under anoxic conditions when DMSO is supplied as terminal electron acceptor | label-only | (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 31-36) |
| Phenotypes/assays/outputs | anaerobic growth on methionine sulfoxide | phenotype | Growth increase under anoxic conditions when MetSO is supplied as terminal electron acceptor | label-only | (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 10-11) |
| Phenotypes/assays/outputs | PCA oxidation | assay output | Measured oxidation of reduced phenazine-1-carboxylic acid during anaerobic respiration assays | label-only | (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 31-36) |
| Phenotypes/assays/outputs | nitrate-to-nitrite reduction | assay output | Respiratory conversion of nitrate to nitrite measured in cultures or electrochemical systems | label-only | (egas2024anovelmechanism pages 2-5, tsypin2024geneticallydissectingthe pages 31-36) |
| Phenotypes/assays/outputs | nitrite-to-ammonium reduction | assay output | DNRA-associated conversion of nitrite to ammonium | label-only | (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5) |
| Phenotypes/assays/outputs | N2O accumulation | phenotype/output | Build-up of nitrous oxide under incomplete or O2-perturbed denitrification | CHEBI:17045 | (roothans2024aerobicdenitrificationas pages 8-9, sennett2024determininghowoxygen pages 1-2) |
| Phenotypes/assays/outputs | N2O reduction rate | assay output | Rate of NosZ-dependent N2O-to-N2 reduction | label-only | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 2-3) |
| Phenotypes/assays/outputs | denitrification rate | assay output | Electron-flow or gas-production rate through denitrification pathway | label-only | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 2-3) |
| Phenotypes/assays/outputs | nitric oxide accumulation | phenotype/output | Measured NO intermediate accumulation under certain oxygen-legacies or pathway imbalance | CHEBI:16480 | (sennett2024determininghowoxygen pages 9-10, sennett2024determininghowoxygen pages 2-3) |
| Phenotypes/assays/outputs | membrane sulfoxide reductase activity | assay output | DMSO- or MetSO-dependent reductase activity measured in isolated membranes | label-only | (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 15-16) |


*Table: This table lists curation-ready candidate nodes for an anaerobic respiration TraitMech graph, grouped by biological role and grounded where possible to stable ontologies. It is useful for selecting graph entities that are directly supported by the retrieved evidence set.*

### 4) Evidence-backed causal edges (triples) for TraitMech curation

The table below proposes candidate curation edges and includes direct evidence snippets and notes on uncertainty.

| Edge (S–P–O) | Evidence snippet (quote) | Reference (DOI + URL + year) | Notes/uncertainty | Suggested ontology grounding for S and O |
|---|---|---|---|---|
| oxygen limitation / anoxic transition — increases activity of — denitrification reductases | “early transcription of NAR (and sometimes NOS) at the cusp of anoxia” (sennett2024determininghowoxygen pages 1-2) | 10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024 | Supports environmental driver → enzyme activity in denitrification; broad to denitrifiers, not universal across all taxa. | S: label `anoxia / low O2` [candidate ENVO]; O: `narG/narH/narI`, `nosZ` [gene symbols], GO:0019645 denitrification |
| constant oxic legacy — selects for — nosZ clade II-carrying partial/non-denitrifiers | “LA selects for canonical denitrifiers carrying nosZ clade I, whereas Ox selects for nosZ clade II-carrying partial- or non-denitrifiers” (sennett2024determininghowoxygen pages 1-2) | 10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024 | Community-level ecological edge; not a single-organism mechanistic edge. Useful as environmental context node. | S: label `constant oxic legacy`; O: `nosZ clade II carriers` [label], gene `nosZ` |
| short anoxic spells / SA oxygen regime — increases — accumulation of denitrification intermediates | “SA showed the slowest denitrification progression and the highest accumulation of intermediates” (sennett2024determininghowoxygen pages 1-2) | 10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024 | Good environmental-driver edge; intermediates include NO2−, NO, N2O. | S: label `short anoxic spells`; O: CHEBI:17632 nitrite, CHEBI:16480 nitric oxide, CHEBI:17045 nitrous oxide |
| oxic/anoxic cycling faster than protein turnover — enables persistence of — denitrification enzyme activity under oxic conditions | “Denitrification enzymes remained at least partially active during oxic phases, likely because O2 cycling was faster than protein turnover” (roothans2024aerobicdenitrificationas pages 8-9) | 10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024 | Important boundary-case edge explaining aerobic denitrification via anaerobic-respiration machinery. | S: label `rapid oxic/anoxic cycling`; O: GO:0019645 denitrification / denitrification enzymes |
| membrane-bound nitrate reductase Nar — drives — NO3− reduction during aerobic denitrification | “NapAB … was not detected while membrane-bound Nar was present and drove NO3− reduction” (roothans2024aerobicdenitrificationas pages 8-9) | 10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024 | Assay/community-specific; supports Nar over Nap in this enrichment. | S: `narGHI` [gene symbols]; O: CHEBI:17632 nitrite / GO:0008940 nitrate reductase activity |
| NosZ oxygen sensitivity / slower recovery — increases — N2O accumulation | “N2O accumulation was consistently observed and is attributed to higher oxygen sensitivity and slower recovery of NosZ” (roothans2024aerobicdenitrificationas pages 8-9) | 10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024 | Mechanistic but community-contextual; links enzyme behavior to phenotype. | S: `nosZ`; O: CHEBI:17045 nitrous oxide accumulation |
| dmsABC — enables anaerobic respiration with — DMSO as terminal electron acceptor | “Salmonella can use DMSO … as terminal electron acceptors via the DmsABC molybdoenzyme” (kim2024anaerobicrespirationof pages 8-10) | 10.1016/j.chom.2024.01.004 · https://doi.org/10.1016/j.chom.2024.01.004 · 2024 | Strong genetic and biochemical evidence in Salmonella; taxon-specific but high-confidence. | S: `dmsABC`; O: CHEBI:16385 dimethyl sulfoxide |
| dmsABC — enables anaerobic respiration with — methionine sulfoxide as terminal electron acceptor | “DmsABC is a reductase that can use DMSO and methionine sulfoxide as terminal electron acceptors” (kim2024anaerobicrespirationof pages 11-13) | 10.1016/j.chom.2024.01.004 · https://doi.org/10.1016/j.chom.2024.01.004 · 2024 | Strong evidence in Salmonella; distinguishes respiratory use from repair-only Msr systems. | S: `dmsABC`; O: label `methionine sulfoxide (MetSO)` [CHEBI candidate, label-only if unresolved] |
| fnr — increases transcription of — dmsA | “dmsA transcription is strongly induced by anaerobiosis … and dmsABC is regulated by the O2-responsive FNR transcription factor (dmsA poorly transcribed in Δfnr)” (kim2024anaerobicrespirationof pages 6-8) | 10.1016/j.chom.2024.01.004 · https://doi.org/10.1016/j.chom.2024.01.004 · 2024 | Good environmental regulation edge; Salmonella-specific regulatory evidence. | S: `fnr`; O: `dmsA` |
| moaABCDE-mediated molybdenum cofactor biosynthesis — enables function of — DmsABC-dependent sulfoxide respiration | “The moaABCDE operon synthesizes molybdopterin, a cofactor for nitrate, TMAO, and DMSO reductases” (kim2024anaerobicrespirationof pages 5-6) | 10.1016/j.chom.2024.01.004 · https://doi.org/10.1016/j.chom.2024.01.004 · 2024 | Supports cofactor dependency rather than direct catalytic step; curate as enabling relation. | S: `moaABCDE`; O: `dmsABC` / GO:0051539 4Fe-4S cluster binding not exact; label `molybdenum cofactor biosynthesis` |
| narK — transports / supports uptake of — nitrate for DNRA | “a putative nitrate/nitrite transporter narK (sixfold upregulated)” (egas2024anovelmechanism pages 2-5) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Inferred transporter function from annotation + upregulation in DNRA conditions; moderate confidence. | S: `narK`; O: CHEBI:17632 nitrate |
| narGHI — catalyzes reduction of — nitrate to nitrite | “the narGHI nitrate reductase cluster (eightfold upregulated; NarGHI protein abundance increased 22-fold)” (egas2024anovelmechanism pages 2-5) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Strong expression evidence in A. acetoxydans DNRA conditions. | S: `narGHI`; O: CHEBI:17632 nitrite from CHEBI:17632 nitrate? use O label `nitrate reduction to nitrite` / GO:0008940 |
| AsrABC — likely reduces — nitrite to ammonium during DNRA | “Nitrite is likely reduced to ammonia by the previously undescribed nitrite reductase activity of the NADH-linked sulfite reductase AsrABC” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Novel mechanism and taxon-specific; curate as uncertain until wider validation. | S: `asrABC`; O: CHEBI:28938 ammonium |
| NirA-like DEACI_1836 — likely reduces — nitrite to ammonium | “or by a putatively ferredoxin-dependent homolog of the nitrite reductase NirA (DEACI_1836), or both” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Candidate enzyme, function not fully resolved; mark uncertain. | S: `DEACI_1836 (NirA-like)`; O: CHEBI:28938 ammonium |
| Hcp — reduces — nitric oxide to nitrous oxide | “Hcp—annotated as hydroxylamine reductase—is abundant and functions physiologically as a high-affinity nitric oxide reductase, converting NO to N2O” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Strong for this organism/system; unusual Hcp role should be flagged as context-specific. | S: `hcp`; O: CHEBI:17045 nitrous oxide from CHEBI:16480 nitric oxide |
| nosZ (+ nosDFY) — reduces — N2O to N2 | “NosZ reduces N2O to N2” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 · https://doi.org/10.1128/msystems.00967-23 · 2024 | Canonical denitrification edge; here also linked to DNRA hybrid physiology. | S: `nosZ`; O: CHEBI:17997 dinitrogen |
| presence of respirable terminal electron acceptor — stimulates — PCA oxidation | “any respirable terminal electron acceptor stimulates PCA oxidation” (tsypin2024geneticallydissectingthe pages 31-36) | 10.1101/2023.11.14.567096 · https://doi.org/10.1101/2023.11.14.567096 · 2024 | Broad mechanistic claim from bioRxiv; useful but preprint status. | S: label `respirable terminal electron acceptor`; O: label `PCA oxidation` |
| frdA — required for — fumarate-driven PCA oxidation | “frdA knockout abolishes fumarate-driven PCA oxidation” (tsypin2024geneticallydissectingthe pages 26-31) | 10.1101/2023.11.14.567096 · https://doi.org/10.1101/2023.11.14.567096 · 2024 | Strong genetic evidence, but preprint. | S: `frdA`; O: CHEBI:18012 fumarate respiration / label `PCA oxidation during fumarate respiration` |
| dmsA — required for — DMSO-driven PCA oxidation | “dmsA knockout abolishes DMSO-driven PCA oxidation” (tsypin2024geneticallydissectingthe pages 26-31) | 10.1101/2023.11.14.567096 · https://doi.org/10.1101/2023.11.14.567096 · 2024 | Strong genetic evidence, but preprint. | S: `dmsA`; O: CHEBI:16385 dimethyl sulfoxide respiration / label `PCA oxidation during DMSO respiration` |
| narG / napA / narZ nitrate reductases — are required for — nitrate-driven PCA oxidation | “eliminating both narG and narZ abolished PCA oxidation, and triple knockout of all three nitrate reductases fully abolished activity” (tsypin2024geneticallydissectingthe pages 21-26) | 10.1101/2023.11.14.567096 · https://doi.org/10.1101/2023.11.14.567096 · 2024 | Strong genetic evidence; condition dependence among nitrate reductases noted. | S: `narG`, `narZ`, `napA`; O: label `PCA oxidation during nitrate respiration` |
| nitrate availability — increases rate of — PCA oxidation / nitrate respiration | “Cells oxidized PCA when nitrate was present” and “the cells converted nitrate to nitrite faster than in the chamber without PCA” (tsypin2024geneticallydissectingthe pages 31-36) | 10.1101/2023.11.14.567096 · https://doi.org/10.1101/2023.11.14.567096 · 2024 | Links acceptor availability to respiration rate in electrochemical setting; preprint. | S: CHEBI:17632 nitrate; O: label `PCA oxidation coupled nitrate reduction` |
| nosZ gene presence — frequently co-occurs with — DNRA genes in WWTP MAGs | “HQ MAGs with genes for dissimilatory nitrate reduction to ammonium … frequently co-occurred with the nosZ gene” (schacksen2024unravelingthegenetic pages 1-2) | 10.1128/aem.02177-23 · https://doi.org/10.1128/aem.02177-23 · 2024 | Genomic co-occurrence, not direct activity; useful for graph expansion only with caution. | S: `nosZ`; O: `nrfA / DNRA pathway genes` |
| clade I nosZ MAGs — are more often associated with — complete denitrification than clade II nosZ MAGs | “39.4% of clade I vs 11.6% of clade II are complete denitrifiers” (schacksen2024unravelingthegenetic pages 11-13) | 10.1128/aem.02177-23 · https://doi.org/10.1128/aem.02177-23 · 2024 | Population-statistical association, not direct causal mechanism. | S: `nosZ clade I`; O: GO:0019645 denitrification |
| nitrate / carbon addition under repeated anoxic exposure — increases — denitrification electron-flow and N2O reduction rates | “initial denitrification electron-flow rates rising from 1.5 to 3.2 µmol e− vial−1 h−1” and “The initial VNOS … rose from 0.04 to 0.63 µmol N vial−1 h−1” (sennett2024determininghowoxygen pages 2-3) | 10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024 | Environmental-history edge from soil microcosms; multifactorial (nitrate + repeated anoxia + carbon). | S: label `repeated anoxic exposure with nitrate/carbon`; O: label `denitrification rate / N2O reduction rate` |


*Table: This table compiles curation-ready subject–predicate–object edges for the anaerobic respiration trait from the provided evidence set. It covers environmental regulation, enzyme-catalyzed steps, acceptor-dependent respiration, and community-level genomic associations relevant to TraitMech graph construction.*

### 5) Recent developments (prioritizing 2023–2024 sources)

#### 5.1 Oxygen legacy and denitrifier functional coordination (soil; high-authority 2024)
A major 2024 advance is explicit experimental evidence that **oxygen history (“oxygen legacy”) changes later denitrification function** without requiring differences in total biomass or gene abundances. In a controlled soil system, “**denitriﬁcation and N2O reduction rates are three times greater in Ox than in LA and SA during a ﬁnal anoxic incubation**” (sennett2024determininghowoxygen pages 1-2). The same study links the oxygen legacy regimes to **nosZ clade composition/activity**, with “**LA selects for canonical denitrifiers carrying nosZ clade I, whereas Ox selects for nosZ clade II-carrying partial- or non-denitrifiers**” (sennett2024determininghowoxygen pages 1-2). Visual evidence for denitrification gene/transcript abundance and **nosZ clade proportions** is shown in figure panels extracted from the paper (sennett2024determininghowoxygen media f2b6b6e3, sennett2024determininghowoxygen media d66b6aa7).

Mechanistically, the authors interpret these results as **community-level partnering/coordination** of denitrification steps under specific oxygen histories rather than a single-organism pathway change (sennett2024determininghowoxygen pages 1-2).

#### 5.2 “Aerobic denitrification” via enzyme persistence under rapid cycling (microbiomes; 2024)
A 2024 ISME Journal study shows denitrification can contribute substantially under oxic conditions in dynamic systems because denitrification enzymes can remain active when oxygen cycling is faster than protein turnover: “**Denitrification enzymes remained at least partially active during oxic phases, likely because O2 cycling was faster than protein turnover**” (roothans2024aerobicdenitrificationas pages 8-9). This work also provides molecular specificity in one enrichment context: “**NapAB … was not detected while membrane-bound Nar was present and drove NO3− reduction**” (roothans2024aerobicdenitrificationas pages 8-9), supporting a context-dependent Nar-over-Nap edge.

#### 5.3 Novel DNRA mechanism in acidophilic sulfate-reducing bacteria (2024)
Egas et al. (mSystems 2024) extends mechanistic space for DNRA by describing **DNRA in an organism encoding Nar-type nitrate reductase but lacking recognized nitrite reductase genes**, and proposes that “**Nitrite is likely reduced to ammonia by … AsrABC … or by a … homolog of the nitrite reductase NirA (DEACI_1836), or both**” (egas2024anovelmechanism pages 9-10). They also support an atypical role for Hcp: “**Hcp … functions physiologically as a high-affinity nitric oxide reductase, converting NO to N2O**” (egas2024anovelmechanism pages 9-10). This provides candidate entities/edges for trait graphs capturing mechanistic diversity, but should be curated with uncertainty flags (see warnings).

#### 5.4 Host-derived MetSO as a terminal electron acceptor (infection biology; 2024)
Kim et al. (Cell Host & Microbe 2024) provides high-confidence evidence that *Salmonella* can use **methionine sulfoxide (MetSO)** as a TEA. The authors state: “**DmsABC is a reductase that can use DMSO and methionine sulfoxide as terminal electron acceptors**” (kim2024anaerobicrespirationof pages 11-13), and show anaerobic growth stimulation and membrane reductase activity dependent on dmsABC (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 31-36). This extends anaerobic respiration graphs into **host-relevant redox chemistry**.

### 6) Current applications and real-world implementations

#### 6.1 Wastewater treatment plants (WWTPs): N2O mitigation potential via nosZ-carrying populations
A 2024 Applied and Environmental Microbiology study analyzed **1,083 high-quality MAGs** from **23 full-scale WWTPs**, reporting that “**48.7% of the total 1,083 HQ MAGs harbored nosZ genes**” and that “**clade II [was] predominant, accounting for 93.7%**” of nosZ genes (schacksen2024unravelingthegenetic pages 1-2). More detailed counts include **27 clade I MAGs** and **401 clade II MAGs** (schacksen2024unravelingthegenetic pages 7-9). This provides actionable, system-level statistics suggesting that many WWTP communities contain a large reservoir of genetic potential for N\₂O reduction (though activity depends on expression and process conditions).

The same study reports functional-genomic stratification: “**39.4% of clade I vs 11.6% of clade II are complete denitrifiers**” (schacksen2024unravelingthegenetic pages 11-13), implying that clade II nosZ is frequently found in partial/non-denitrifying contexts.

#### 6.2 Engineered redox systems: coupling extracellular shuttles to TEA respiration
Tsypin et al. (bioRxiv 2024) show a mechanistically explicit coupling between extracellular PCA oxidation and multiple anaerobic respiratory TEAs, including evidence that terminal reductases are necessary. For nitrate respiration, “**eliminating both narG and narZ abolished PCA oxidation**” and a triple nitrate-reductase knockout “**fully abolished activity**” (tsypin2024geneticallydissectingthe pages 21-26). This supports causal-graph extensions that represent **electron shuttles** as modulating/feeding into anaerobic respiratory flux (with applicability to soils, bioelectrochemical systems, and redox-active metabolite ecology), while retaining a preprint-caution label.

### 7) Expert synthesis / analysis (authoritative interpretations)

1. **Anaerobic respiration is modular and ecology-shaped.** The oxygen-legacy results highlight that the *trait phenotype* can emerge from **community-level partitioning of reduction steps**, not strictly from single-organism complete pathways (sennett2024determininghowoxygen pages 1-2).
2. **Oxygen dynamics control not just on/off switching but kinetics and byproduct profiles.** Rapid oxic/anoxic cycling can sustain denitrification enzyme activity during oxic phases (roothans2024aerobicdenitrificationas pages 8-9), while oxygen sensitivity of specific enzymes (e.g., NosZ recovery) can shift N\₂O outcomes (roothans2024aerobicdenitrificationas pages 8-9).
3. **Terminal electron acceptor scope is broader than classic nitrate/sulfate/metal narratives.** The identification of host-derived MetSO as a TEA underscores that trait graphs should include **organosulfur oxidants** where relevant to the ecological niche (infection, host-associated anaerobiosis) (kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 10-11).

### 8) Quantitative statistics and data points (recent)

- **Soil oxygen legacy effect:** denitrification and N\₂O reduction rates “**three times greater in Ox than in LA and SA**” (Nature Communications; Aug 2024) (sennett2024determininghowoxygen pages 1-2).
- **WWTP MAG prevalence:** “**48.7%** of 1,083 HQ MAGs harbored **nosZ**; **93.7%** of nosZ genes were **clade II** (AEM; Sep 2024) (schacksen2024unravelingthegenetic pages 1-2).
- **WWTP clade counts:** **27** clade I MAGs and **401** clade II MAGs; co-occurrence details (e.g., 167 MAGs with NO2−→NH4+ genes also containing nosZ) are reported (schacksen2024unravelingthegenetic pages 7-9).
- **Enzyme persistence concept:** denitrification enzymes remain active in oxic phases when cycling is faster than protein turnover (ISME J; Jan 2024) (roothans2024aerobicdenitrificationas pages 8-9).

### 9) Curation warnings (what should not be curated yet)

> **Curation warnings**
> - Treat PCA-coupled anaerobic-respiration edges from Tsypin et al. as provisional because the source is a 2024 bioRxiv preprint, not yet a peer-reviewed paper; useful for hypothesis generation, but weaker than curated primary literature for stable TraitMech edges. (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 1-6, tsypin2024geneticallydissectingthe pages 31-36, tsypin2024geneticallydissectingthe pages 21-26)
> - The proposed DNRA role of **AsrABC** and the **NirA-like DEACI_1836** in *Acididesulfobacillus acetoxydans* is explicitly a novel/noncanonical mechanism and should be marked taxon-specific and uncertain until validated in additional organisms. (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 10-13)
> - **Hcp as a high-affinity NO reductase** is supported in the same acidophilic DNRA system, but this is not yet evidence that Hcp generally substitutes for canonical Nor across anaerobically respiring microbes. (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 10-13)
> - WWTP MAG-based links involving **nosZ**, DNRA genes, and denitrification modules mostly show **genomic co-occurrence/potential**, not demonstrated in situ activity or flux; avoid curating these as direct causal enzymatic edges without expression or physiological confirmation. (schacksen2024unravelingthegenetic pages 9-11, schacksen2024unravelingthegenetic pages 11-13, schacksen2024unravelingthegenetic pages 1-2, schacksen2024unravelingthegenetic pages 7-9)
> - “Aerobic denitrification” evidence here should not be treated as a separate respiration trait; the 2024 ISME Journal study supports denitrification enzyme persistence during rapid oxic/anoxic cycling, meaning the phenotype is strongly **context-dependent** and reflects use of anaerobic-respiration machinery under transient oxic conditions. (roothans2024aerobicdenitrificationas pages 8-9, roothans2024aerobicdenitrificationas pages 12-13)
> - Oxygen-legacy effects on **nosZ clade I vs clade II** are robust at the community/transcript level, but these are ecological selection patterns rather than simple organism-level gene-to-trait rules; curate as environmental-context edges, not universal intrinsic trait logic. (sennett2024determininghowoxygen pages 9-10, sennett2024determininghowoxygen pages 8-9, sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen media f2b6b6e3)
> - **Methionine sulfoxide (MetSO)** is mechanistically well supported as a respiratory acceptor in *Salmonella*, but ontology grounding is currently less straightforward than nitrate, nitrite, DMSO, or TMAO; use a conservative label-only node unless a stable CHEBI identifier is verified during curation. (kim2024anaerobicrespirationof pages 8-10, kim2024anaerobicrespirationof pages 31-36, kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 10-11)
> - Some regulator-to-trait edges, such as **FNR → dmsA transcription** or **moaABCDE → DmsABC function**, are strong but remain partly system-specific; do not overgeneralize Salmonella infection-associated sulfoxide respiration to all facultative anaerobes. (kim2024anaerobicrespirationof pages 5-6, kim2024anaerobicrespirationof pages 6-8)
> - This evidence set is nitrogen- and sulfoxide-heavy and does **not** adequately cover several major anaerobic-respiration modes, including canonical sulfate reduction, Fe(III)/Mn(IV) respiration, and CO2-based anaerobic respiration/methanogenic systems; absence from the report should not be interpreted as absence from the trait scope. (tsypin2024geneticallydissectingthe pages 1-6, schacksen2024unravelingthegenetic pages 1-2)
> - Community statistics such as nosZ prevalence or clade frequencies are useful for contextual notes and application summaries, but they are generally too coarse to support direct mechanistic subject-predicate-object curation unless paired with experimentally resolved reductase function. (schacksen2024unravelingthegenetic pages 11-13, schacksen2024unravelingthegenetic pages 13-15, schacksen2024unravelingthegenetic pages 4-7, schacksen2024unravelingthegenetic pages 1-2)


*Blockquote: This blockquote lists key limitations and caveats for curating anaerobic respiration causal edges from the current evidence set. It highlights which findings are provisional, taxon-specific, or ecological rather than direct mechanistic evidence.*

### 10) DOI-first bibliography (with dates and URLs)

- **Sennett LB, et al.** Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and N2O emissions. *Nature Communications* (Aug 2024). DOI: **10.1038/s41467-024-51688-w**. URL: https://doi.org/10.1038/s41467-024-51688-w (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 2-3, sennett2024determininghowoxygen media f2b6b6e3, sennett2024determininghowoxygen media d66b6aa7)
- **Roothans N, et al.** Aerobic denitrification as an N2O source from microbial communities. *The ISME Journal* (Jan 2024). DOI: **10.1093/ismejo/wrae116**. URL: https://doi.org/10.1093/ismejo/wrae116 (roothans2024aerobicdenitrificationas pages 8-9)
- **Egas RA, et al.** A novel mechanism for dissimilatory nitrate reduction to ammonium in *Acididesulfobacillus acetoxydans*. *mSystems* (Mar 2024). DOI: **10.1128/msystems.00967-23**. URL: https://doi.org/10.1128/msystems.00967-23 (egas2024anovelmechanism pages 9-10, egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 10-13)
- **Kim J-S, et al.** Anaerobic respiration of host-derived methionine sulfoxide protects intracellular Salmonella from the phagocyte NADPH oxidase. *Cell Host & Microbe* (Mar 2024). DOI: **10.1016/j.chom.2024.01.004**. URL: https://doi.org/10.1016/j.chom.2024.01.004 (kim2024anaerobicrespirationof pages 11-13, kim2024anaerobicrespirationof pages 6-8, kim2024anaerobicrespirationof pages 10-11)
- **Schacksen PS, Nielsen JL.** Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. *Applied and Environmental Microbiology* (Sep 2024). DOI: **10.1128/aem.02177-23**. URL: https://doi.org/10.1128/aem.02177-23 (schacksen2024unravelingthegenetic pages 1-2, schacksen2024unravelingthegenetic pages 7-9)
- **Tsypin LMZ, et al.** Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. *bioRxiv* (posted Nov 2023; indexed 2024). DOI: **10.1101/2023.11.14.567096**. URL: https://doi.org/10.1101/2023.11.14.567096 (tsypin2024geneticallydissectingthe pages 26-31, tsypin2024geneticallydissectingthe pages 31-36, tsypin2024geneticallydissectingthe pages 21-26)


References

1. (roothans2024aerobicdenitrificationas pages 8-9): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

2. (sennett2024determininghowoxygen pages 1-2): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

3. (egas2024anovelmechanism pages 9-10): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

4. (egas2024anovelmechanism pages 2-5): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

5. (egas2024anovelmechanism pages 10-13): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

6. (kim2024anaerobicrespirationof pages 11-13): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

7. (kim2024anaerobicrespirationof pages 10-11): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (tsypin2024geneticallydissectingthe pages 26-31): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

9. (tsypin2024geneticallydissectingthe pages 31-36): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

10. (tsypin2024geneticallydissectingthe pages 21-26): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

11. (tsypin2024geneticallydissectingthe pages 1-6): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

12. (kim2024anaerobicrespirationof pages 8-10): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (tsypin2024geneticallydissectingthe pages 6-9): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

14. (tsypin2024geneticallydissectingthe pages 36-40): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

15. (kim2024anaerobicrespirationof pages 31-36): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

16. (kim2024anaerobicrespirationof pages 15-16): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

17. (tsypin2024geneticallydissectingthe pages 9-16): Lev M.Z. Tsypin, Scott H. Saunders, Allen W. Chen, and Dianne K. Newman. Genetically dissecting the electron transport chain of a soil bacterium reveals a generalizable mechanism for biological phenazine-1-carboxylic acid oxidation. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.14.567096, doi:10.1101/2023.11.14.567096. This article has 1 citations.

18. (schacksen2024unravelingthegenetic pages 9-11): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

19. (schacksen2024unravelingthegenetic pages 1-2): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

20. (schacksen2024unravelingthegenetic pages 11-13): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

21. (kim2024anaerobicrespirationof pages 6-8): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

22. (kim2024anaerobicrespirationof pages 5-6): Ju-Sim Kim, Lin Liu, Sashi Kant, David J. Orlicky, Siva Uppalapati, Alyssa Margolis, Bennett J. Davenport, Thomas E. Morrison, Jennifer Matsuda, Michael McClelland, Jessica Jones-Carson, and Andres Vazquez-Torres. Anaerobic respiration of host-derived methionine sulfoxide protects intracellular salmonella from the phagocyte nadph oxidase. Cell Host &amp; Microbe, 32:411-424.e10, Mar 2024. URL: https://doi.org/10.1016/j.chom.2024.01.004, doi:10.1016/j.chom.2024.01.004. This article has 16 citations and is from a highest quality peer-reviewed journal.

23. (sennett2024determininghowoxygen pages 9-10): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

24. (sennett2024determininghowoxygen pages 2-3): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

25. (sennett2024determininghowoxygen media f2b6b6e3): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

26. (sennett2024determininghowoxygen media d66b6aa7): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

27. (schacksen2024unravelingthegenetic pages 7-9): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

28. (roothans2024aerobicdenitrificationas pages 12-13): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

29. (sennett2024determininghowoxygen pages 8-9): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

30. (schacksen2024unravelingthegenetic pages 13-15): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

31. (schacksen2024unravelingthegenetic pages 4-7): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.