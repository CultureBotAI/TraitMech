---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:37:55.510091'
end_time: '2026-08-04T11:45:38.887027'
duration_seconds: 463.38
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: organotrophic
  trait_identifier: METPO:1000655
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: organotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from the oxidation
    of organic compounds.
  parent_traits: METPO:1000631
  synonyms: TT_organotroph, organotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound
    into biomass (Microbial metabolism reference supports assimilation and use of
    organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound
    electron transport chain (Review supports respiratory electron transport as an
    energy-conserving route.)'
  causal_graph_summary: 'organotrophic_organic_compound_oxidation: 11 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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
- **Trait label:** organotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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


# Curation report: organotrophic

## Trait record and scope

- **Trait:** organotrophic
- **Identifier:** **METPO:1000655**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000631
- **Definition supplied:** “A trophic type in which an organism obtains energy from the oxidation of organic compounds.”
- **Synonyms:** *TT_organotroph*, *organotroph*

### Recommended interpretation

Organotrophy is fundamentally an **electron-donor/energy-source classification**. An organism is organotrophic when an organic compound participates as the reduced substrate in an energy-conserving redox process. An authoritative formulation is “energy conservation from redox reactions involving at least one organic substrate”; examples include glucose oxidation with O₂ and isopropanol oxidation coupled to CO₂ reduction. This is broader than aerobic heterotrophic respiration and includes anaerobic respiration and fermentation. (schonheit2016ontheorigin pages 2-4)

The trait should not be treated as synonymous with **heterotrophy**. Heterotrophy concerns the source of biomass carbon, whereas organotrophy concerns the source of electrons/chemical energy. The two commonly coincide as chemoorganoheterotrophy, but organic compounds can supply electrons while carbon is obtained partly or principally by CO₂ fixation, and phototrophs may use organic electron donors. A 2024 review explicitly contrasts organotrophy—organic electron donors—with lithotrophy—inorganic electron donors—and separately distinguishes heterotrophic reduced-organic carbon from autotrophic oxidized carbon sources. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8)

Likewise, organotrophy is distinct from:

- **Lithotrophy:** energy/electrons are obtained from inorganic donors. An organism able to switch between organic and inorganic donors is metabolically versatile, not exclusively organotrophic.
- **Phototrophy:** light supplies energy. A photoheterotroph may assimilate organic carbon, but organotrophy additionally requires evidence that an organic compound acts in energy-yielding electron transfer.
- **Respiration:** one possible organotrophic energy-conservation mode, using an environmental terminal electron acceptor.
- **Fermentation:** another organotrophic mode. Here the substrate supplies both electron-donor and acceptor equivalents, and ATP can be conserved by substrate-level phosphorylation or ion-gradient mechanisms. (muller2012biochemistryandevolution pages 5-6, buckel2021energyconservationin pages 1-2)
- **Assimilation/growth on an organic compound:** supportive but not sufficient by itself. Incorporation into biomass demonstrates carbon use; it does not necessarily establish that oxidation of that compound supplies energy.

**Recommended graph scope:** represent a generic mechanistic core with explicit alternative branches for respiration and fermentation. Do not require O₂, a complete TCA cycle, a membrane electron-transport chain, or any single transporter/gene as universal defining features.

## Candidate nodes

Ontology grounding below is intentionally conservative. Broad or taxon-dependent entities are left label-only rather than assigned speculative identifiers.

### Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation comment |
|---|---|---|
| organotrophic | **METPO:1000655** | Target trait; quote CURIE verbatim in YAML. |
| organic-compound oxidation | GO:0016054, *organic acid catabolic process*, only for organic-acid-specific instances | No single GO term safely covers oxidation of every organic donor; retain a label-only generic node if necessary. |
| glycolytic process | GO:0006096 | Common carbohydrate-catabolism module, not universal. |
| tricarboxylic-acid cycle | GO:0006099 | Respiratory/catabolic module; incomplete or absent in some organotrophs. |
| cellular respiration | GO:0045333 | Parent process for respiratory branches. |
| aerobic respiration | GO:0009060 | Conditional branch requiring O₂. |
| anaerobic respiration | GO:0009061 | Conditional branch requiring a non-O₂ environmental acceptor. |
| fermentation | GO:0006113 | Alternative energy-conservation branch. |
| oxidative phosphorylation | GO:0006119 | Conditional on respiratory or other chemiosmotic machinery. |
| ATP synthesis coupled proton transport | GO:0015986 | Proton-driven ATP-synthase branch. |
| substrate-level phosphorylation | label-only candidate | Confirm a suitable ontology term before release. |
| organic-substrate transport | label-only parent | Instantiate substrate/transporter-specific children where evidence exists. |
| biomass assimilation | label-only candidate | Keep downstream of uptake and precursor generation, not as the defining energy edge. |

### Chemicals and energetic entities

| Candidate node | Suggested grounding | Role |
|---|---|---|
| organic compound / organic electron donor | label-only class, or substrate-specific CHEBI term | Defining input; examples include glucose, organic acids, amino acids, alcohols, hydrocarbons and methane. |
| glucose | CHEBI:17234 | Model organic donor for respiratory and fermentative examples. |
| pyruvate | CHEBI:15361 | Central catabolic intermediate and fermentation acceptor. |
| acetyl-CoA | CHEBI:15351 | Links substrate oxidation to TCA, biosynthesis and storage polymers. |
| NAD⁺ | CHEBI:15846 | Oxidized soluble redox carrier. |
| NADH | CHEBI:16908 | Reduced carrier generated by many catabolic pathways. |
| ATP | CHEBI:15422 | Conserved chemical-energy currency. |
| ADP | CHEBI:16761 | ATP-synthesis substrate. |
| oxygen | CHEBI:15379 | Aerobic terminal acceptor; not part of the trait definition. |
| nitrate | CHEBI:17632 | Example anaerobic acceptor; taxon/pathway-specific. |
| fumarate | CHEBI:18012 | Can serve as a metabolically generated fermentation acceptor or respiratory acceptor, depending on context. |
| acetate | CHEBI:30089 | Substrate, fermentation product, or assimilated carbon source depending on the system. |
| carbon dioxide | CHEBI:16526 | Oxidation product and/or separately fixed carbon source. |
| proton gradient / proton-motive force | label-only candidate | Energy-transducing intermediate. |
| sodium-motive force | label-only candidate | Important in Rnf- and decarboxylase-dependent anaerobes. |
| polyhydroxyalkanoate | label-only class | Taxon-specific carbon/energy-storage and biotechnology output. |

### Genes, proteins, complexes and functions

These should be represented as **optional mechanistic modules**, not necessary-and-sufficient markers of METPO:1000655:

- Substrate-specific permeases; proton/Na⁺ symporters; ABC transporters; phosphotransferase systems.
- Glycolytic enzymes, including hexokinase/glucokinase, phosphofructokinase, glyceraldehyde-3-phosphate dehydrogenase, phosphoglycerate kinase and pyruvate kinase.
- Entner–Doudoroff enzymes and substrate-specific dehydrogenases.
- Pyruvate dehydrogenase complex or anaerobic pyruvate:ferredoxin oxidoreductase.
- TCA-cycle enzymes.
- NADH dehydrogenase/respiratory complex I, quinones, cytochromes, terminal oxidases and anaerobic terminal reductases.
- Rnf complex and flavin-based electron-bifurcating complexes in particular anaerobes.
- F-type, A-type or V-type ATP synthase, grounded at the taxon/protein-complex level where possible.
- Fermentation enzymes and acetate kinase/phosphotransacetylase modules.
- PHA synthase and related storage-polymer enzymes only in an application-specific extension.

No universal “organotrophy gene” exists: substrate breadth and energy-conservation routes are distributed among many nonhomologous pathways.

## Candidate causal edges

The following table is a compact graph scaffold. The snippets are short evidence summaries derived from the cited passages; quotation marks identify wording reported directly or nearly directly in those passages.

| subject | predicate | object | confidence/scope | primary DOI |
|---|---|---|---|---|
| organic compound | acts_as_electron_donor_in | energy-conserving redox metabolism | high; core definition of organotrophy across microbes (schonheit2016ontheorigin pages 2-4, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8) | 10.1016/j.tim.2015.10.003 |
| organic substrate catabolism (e.g., glycolysis/ED/TCA-linked oxidation) | produces | reduced cofactors (NADH, sometimes reduced ferredoxin) | high for NADH; ferredoxin pathway-specific, especially anaerobic metabolism (muller2012biochemistryandevolution pages 5-6, buckel2021energyconservationin pages 1-2) | 10.1128/MMBR.05024-11 |
| reduced cofactors (e.g., NADH) | feed | respiratory electron transport chain | high for respiration-capable organisms under respiratory conditions (muller2012biochemistryandevolution pages 5-6) | 10.1128/MMBR.05024-11 |
| reduced cofactors generated during glycolysis/catabolism | require_reoxidation_by | respiration or fermentation | high; broad bioenergetic principle (muller2012biochemistryandevolution pages 5-6) | 10.1128/MMBR.05024-11 |
| respiratory electron transport | generates | ion motive force | high; broadly supported, especially in aerobic/anaerobic respiration (schonheit2016ontheorigin pages 2-4) | 10.1016/j.tim.2015.10.003 |
| ion motive force | drives | ATP synthesis via ATP synthase | high; universal chemiosmotic mechanism where ATP synthase is present (folch2021metabolicenergyconservation pages 3-4, buckel2021energyconservationin pages 1-2) | 10.1111/1751-7915.13746 |
| fermentation substrate | serves_as | electron donor and electron acceptor source | high for fermentation; not general to respiration (buckel2021energyconservationin pages 1-2) | 10.3389/fmicb.2021.703525 |
| metabolically generated organic intermediates/products (e.g., pyruvate, acetaldehyde, fumarate) | act_as_terminal_acceptors_in | fermentation | high; pathway-class statement (muller2012biochemistryandevolution pages 5-6) | 10.1128/MMBR.05024-11 |
| glycolysis and other kinase-catalyzed steps | produce_ATP_by | substrate-level phosphorylation | high; broad across many organotrophic pathways (folch2021metabolicenergyconservation pages 3-4, muller2012biochemistryandevolution pages 5-6) | 10.1111/1751-7915.13746 |
| organic substrate transport | enables | intracellular catabolism of organic substrates | medium-high; broad but transporter/mechanism-specific (folch2021metabolicenergyconservation pages 20-21) | 10.1111/1751-7915.13746 |
| proton/Na+ symport or ABC transport of organic substrates | consumes | ion motive force and/or ATP | high for those transporter classes; transporter-specific (folch2021metabolicenergyconservation pages 20-21) | 10.1111/1751-7915.13746 |
| organic carbon substrate | is_assimilated_into | biomass | medium-high; broad but assay-dependent and distinct from energy proof (schonheit2016ontheorigin pages 2-4) | 10.1016/j.tim.2015.10.003 |
| organic carbon substrate | is_assimilated_into | polyhydroxyalkanoate (PHA) storage polymer | high for PHA-producing taxa/conditions; not universal organotrophy (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 16-18, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8) | 10.3390/molecules29102293 |


*Table: This table summarizes compact, curation-ready causal edges for the organotrophic trait using only relationships supported by gathered evidence. It is useful as a starting scaffold for TraitMech graph curation while keeping scope and confidence conservative.*

### Expanded edge evidence and curation notes

| # | Subject–predicate–object | Supporting snippet | Reference | Curation assessment |
|---:|---|---|---|---|
| 1 | organic compound — **acts as electron donor in** → energy-conserving redox reaction | Organotrophy is “energy conservation from redox reactions involving at least one organic substrate”; glucose oxidation with O₂ is an example. | Schönheit et al., 2016, DOI: [10.1016/j.tim.2015.10.003](https://doi.org/10.1016/j.tim.2015.10.003) | **Core, high confidence.** Best defining edge. “Oxidation” should permit partial oxidation and fermentation, not only complete conversion to CO₂. (schonheit2016ontheorigin pages 2-4) |
| 2 | organic substrate transport — **enables** → intracellular catabolism | Transport systems have distinct energy costs; proton/Na⁺ symport uses ion motive force, whereas ABC transport consumes ATP. | Folch et al., 2021, DOI: [10.1111/1751-7915.13746](https://doi.org/10.1111/1751-7915.13746) | **Conditional.** Applicable to extracellular substrates requiring uptake; omit for membrane-permeable substrates or extracellular oxidation. (folch2021metabolicenergyconservation pages 20-21) |
| 3 | proton/Na⁺ symporter — **consumes** → ion-motive force | Maltose transport in *Saccharomyces cerevisiae* was reported to cost approximately “1 ATP per maltose” in energetic equivalent. | Folch et al., 2021 | **Taxon/substrate-specific.** Do not generalize the numerical cost. (folch2021metabolicenergyconservation pages 20-21) |
| 4 | ABC transporter — **consumes** → ATP | Reported transport expenditure spans “1–50 ATP per substrate.” | Folch et al., 2021 | **Mechanism-specific; numerical range context-dependent.** Useful as an energetic-cost edge, not part of the defining core. (folch2021metabolicenergyconservation pages 20-21) |
| 5 | glycolysis/organic-substrate catabolism — **reduces** → NAD⁺ to NADH | Glycolysis produces reduced cofactors that “must be reoxidized through respiration or fermentation.” | Müller et al., 2012, DOI: [10.1128/MMBR.05024-11](https://doi.org/10.1128/MMBR.05024-11) | **Broad but not universal.** Some pathways use NADP⁺, ferredoxin or other carriers. (muller2012biochemistryandevolution pages 5-6) |
| 6 | oxidative decarboxylation of 2-oxoacids — **produces** → reduced ferredoxin | “Reduced ferredoxin is provided by oxidative decarboxylation of 2-oxoacids” and flavin-based electron bifurcation. | Buckel, 2021, DOI: [10.3389/fmicb.2021.703525](https://doi.org/10.3389/fmicb.2021.703525) | **Anaerobe/pathway-specific.** Appropriate for a fermentation subgraph, not the universal organotrophy graph. (buckel2021energyconservationin pages 1-2) |
| 7 | NADH — **donates electrons to** → respiratory electron-transport chain | Respiratory reoxidation of catabolically formed reduced cofactors supports electron transfer and energy conservation. | Müller et al., 2012 | **High confidence under respiratory conditions.** The exact entry complex varies. (muller2012biochemistryandevolution pages 5-6) |
| 8 | respiratory electron transport — **generates** → ion-motive force | Chemotrophic reactions conserve energy through generation of ion gradients or substrate-level phosphorylation. | Schönheit et al., 2016 | **High confidence but conditional.** Separate proton- and sodium-coupled implementations when known. (schonheit2016ontheorigin pages 2-4) |
| 9 | ion-motive force — **drives** → ATP synthase-mediated ATP synthesis | Fermentative organisms exhibit ion-motive forces of approximately −40 to −170 mV; IMF can support ATP synthesis. | Folch et al., 2021 | **High confidence where ATP synthase is present.** Direction may reverse during ATP-driven homeostasis. (folch2021metabolicenergyconservation pages 3-4) |
| 10 | glycolytic/kinase reaction — **produces ATP by** → substrate-level phosphorylation | Glycolysis provides O₂-independent ATP synthesis; kinase-catalysed reactions conserve metabolic energy by SLP. | Müller et al., 2012; Folch et al., 2021 | **Core alternative mechanism.** Instantiate reaction-specific enzymes where possible. (muller2012biochemistryandevolution pages 5-6, folch2021metabolicenergyconservation pages 3-4) |
| 11 | organic fermentation substrate — **supplies** → electron donor and acceptor equivalents | “The substrate of a fermentation has to serve as electron donor as well as acceptor.” | Buckel, 2021 | **High confidence for fermentation only.** The acceptor is normally a metabolically generated derivative, not necessarily the unchanged substrate molecule. (buckel2021energyconservationin pages 1-2) |
| 12 | pyruvate/acetaldehyde/fumarate — **acts as** → fermentation electron acceptor | Fermentation uses “metabolically-generated acceptors like pyruvate, acetaldehyde, fumarate.” | Müller et al., 2012 | **Pathway-specific.** Avoid asserting all three for every fermenter. (muller2012biochemistryandevolution pages 5-6) |
| 13 | Rnf complex — **generates** → Na⁺/H⁺ motive force | NAD:ferredoxin oxidoreductase Rnf and biotin-containing decarboxylases can generate Na⁺/H⁺ motive force. | Buckel, 2021 | **Taxon-specific/conditional.** Require genes plus physiological or biochemical support. (buckel2021energyconservationin pages 1-2) |
| 14 | organic substrate carbon — **is incorporated into** → biomass | Organic compounds can satisfy carbon, energy and, for amino acids or purines, nitrogen requirements. | Schönheit et al., 2016 | **Supportive, not defining.** Assimilation alone must not be used as conclusive evidence of organotrophic energy generation. (schonheit2016ontheorigin pages 8-10, schonheit2016ontheorigin pages 2-4) |
| 15 | organic substrate — **is converted into** → PHA storage polymer | A 2024 synthesis documents PHA production from wastewater, oils, molasses, starch, acetate, butyrate and propionate. | Fukala & Kučera, 2024, DOI: [10.3390/molecules29102293](https://doi.org/10.3390/molecules29102293) | **Application/taxon-specific.** Downstream consequence rather than defining trait mechanism. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 16-18) |

## Quantitative evidence and recent developments

### Bioenergetics

Fermentation and respiration differ dramatically in available free energy. A 2021 review reports approximately **−185 kJ mol⁻¹** for lactate fermentation versus **−2,872 kJ mol⁻¹** for aerobic glucose oxidation. It also gives an approximate aerobic yield of **38 mol ATP per mol glucose**, although actual microbial yields vary with respiratory-chain architecture, proton leakage, maintenance and growth conditions. These values support separate respiratory and fermentative branches rather than one fixed ATP-yield edge. (buckel2021energyconservationin pages 1-2)

For fermentative energy conservation, reported glucose-fermentation standard free energies span approximately **−187 to −266 kJ mol⁻¹**, and typical ion-motive forces are **−40 to −170 mV**. ATP hydrolysis was treated as approximately **44 kJ mol⁻¹** under the review’s assumptions. These are useful evidence annotations, but they should not be encoded as invariant node properties. (folch2021metabolicenergyconservation pages 3-4)

A concrete anaerobic example is *Clostridium acidiurici* purine fermentation: the reviewed pathway conserves energy through acetate kinase, formyl-H₄F synthetase, electron bifurcation and Rnf-dependent chemiosmotic coupling, with a reported yield of **1.25 mol ATP per mol uric acid**. This is a valuable taxon-specific extension, not a generic organotrophy mechanism. (schonheit2016ontheorigin pages 8-10)

### 2024 biotechnology

Recent work strongly emphasizes organotrophic carbon conversion for biodegradable polymers. A 2024 review reports PHA contents/yields of approximately **42–95%** across strain–substrate combinations and **94%** for *Halomonas bluephagenesis* grown on glucose plus acetate. Engineering substrate access and redox metabolism enabled reported PHA contents of **64% on glycerol**, **74% on sucrose**, **73% on xylose**, and **63% on raw starch;** glycerol-process duration decreased from **268 h to 72 h** in the cited engineering example. A two-organism system in which *Escherichia coli* converted xylose to acetate for *Pseudomonas putida* produced **1.30 g L⁻¹** PHA. These findings demonstrate real-world relevance of transport, cross-feeding and redox balancing, but they do not establish a universal PHA branch for organotrophs. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 16-18, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8)

### Environmental and engineering applications

1. **Wastewater treatment and resource recovery:** organotrophic communities oxidize dissolved and particulate organic matter, lowering chemical/biological oxygen demand; electron acceptor management selects aerobic respiration, denitrification or fermentation. Organic-rich waste streams can additionally be redirected into PHA, short-chain fatty acids, methane or other products.
2. **Bioremediation:** hydrocarbon- and aromatic-compound degraders couple donor oxidation to O₂, nitrate, sulfate, iron or other acceptors. A graph for a specific contaminant must add substrate activation and terminal-reductase modules.
3. **Industrial fermentation:** carbohydrate and organic-acid oxidation supplies ATP, reducing equivalents and precursors for fuels, solvents, organic acids, enzymes and polymers. Energy-efficient cell-factory design explicitly optimizes SLP, ion-gradient formation, cofactor recycling and transport costs. (folch2021metabolicenergyconservation pages 3-4, folch2021metabolicenergyconservation pages 20-21)
4. **Carbon cycling:** microbial oxidation and transformation of organic matter drives remineralization in soils, sediments, freshwater and oceans. However, ecological labels such as “heterotrophic bacteria” should not automatically be converted to METPO:1000655 unless the underlying evidence demonstrates organic-donor energy metabolism.
5. **Bioelectrochemical systems:** organic-donor oxidation can be coupled to extracellular electron transfer and electrode reduction. This requires an additional extracellular-electron-transfer subgraph and is not intrinsic to organotrophy.

## Expert synthesis for the TraitMech graph

The strongest generic graph is:

**available organic electron donor → uptake or extracellular oxidation → substrate-specific catabolism → reduced redox carriers and/or phosphorylated intermediates → {respiration → ion-motive force → ATP synthase; fermentation → redox balancing + SLP/ion-gradient conservation} → ATP/maintenance/growth.**

Assimilation should be represented as a parallel downstream branch:

**catabolic intermediates → biosynthetic precursors → biomass**, with optional **storage polymer** formation.

This structure improves on an overly respiration-centered graph because fermentation is unequivocally organotrophic and can conserve energy without a conventional terminal-acceptor respiratory chain. Conversely, a membrane-bound electron-transport chain remains a well-supported branch for respiratory organotrophy, consistent with the existing DOI:10.1016/j.bbabio.2008.09.008 evidence supplied by the user.

## Claims not yet safe to curate

- **Do not equate organic-carbon assimilation with organotrophy.** Isotope incorporation or biomass formation establishes assimilation, not necessarily energy generation from oxidation.
- **Do not equate heterotrophy with organotrophy.** Carbon source and electron/energy source are separate classification axes.
- **Do not require O₂.** Fermentation and anaerobic respiration are valid organotrophic mechanisms.
- **Do not require glycolysis, a complete TCA cycle, NADH dehydrogenase I or cytochrome oxidase.** Substrate and taxonomic diversity produce many alternative routes.
- **Do not curate transporter presence as proof of the phenotype.** Transporters can have broad or uncertain specificity, and genomic potential does not demonstrate expression or energy conservation.
- **Do not infer the trait from a single dehydrogenase annotation.** A complete, thermodynamically connected energy-conservation route and physiological context are needed.
- **Do not universalize Rnf, electron bifurcation, sodium gradients or PHA production.** These are valuable mechanistic extensions but are taxon- and condition-specific.
- **Treat mixotroph and facultative labels carefully.** Growth on a mixture of organic and inorganic donors does not quantify which donor supplied conserved energy without flux, isotope, inhibitor or electrochemical evidence.
- **Avoid fixed ATP yields.** Published stoichiometries depend on pathway, respiratory-chain composition, coupling efficiency and maintenance.
- **Inhibitor edges remain under-supported in the retrieved corpus.** Candidate probes such as respiratory-chain or ATP-synthase inhibitors should only be added with compound-, taxon- and assay-specific references; no generic inhibitor edge is recommended here.
- **The 2024 PHA figures are production phenotypes, not defining evidence for METPO:1000655.** Curate them only in application-specific extensions.

## DOI-first bibliography

1. Schönheit P, Buckel W, Martin WF. **On the Origin of Heterotrophy.** *Trends in Microbiology.* Published January 2016. DOI: [10.1016/j.tim.2015.10.003](https://doi.org/10.1016/j.tim.2015.10.003). Principal source for the organotrophy definition and trophic-axis distinctions. (schonheit2016ontheorigin pages 8-10, schonheit2016ontheorigin pages 2-4)
2. Fukala I, Kučera I. **Natural Polyhydroxyalkanoates—An Overview of Bacterial Production Methods.** *Molecules.* Published May 2024. DOI: [10.3390/molecules29102293](https://doi.org/10.3390/molecules29102293). Recent definition, substrate engineering and quantitative PHA applications. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 16-18, fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8)
3. Folch PL, Bisschops MMM, Weusthuis RA. **Metabolic Energy Conservation for Fermentative Product Formation.** *Microbial Biotechnology.* Published January 2021. DOI: [10.1111/1751-7915.13746](https://doi.org/10.1111/1751-7915.13746). SLP, ion-motive force, thermodynamics and transport costs. (folch2021metabolicenergyconservation pages 3-4, folch2021metabolicenergyconservation pages 20-21)
4. Buckel W. **Energy Conservation in Fermentations of Anaerobic Bacteria.** *Frontiers in Microbiology.* Published September 2021. DOI: [10.3389/fmicb.2021.703525](https://doi.org/10.3389/fmicb.2021.703525). Fermentation donor/acceptor logic, Rnf, electron bifurcation and quantitative energetics. (buckel2021energyconservationin pages 1-2)
5. Müller M et al. **Biochemistry and Evolution of Anaerobic Energy Metabolism in Eukaryotes.** *Microbiology and Molecular Biology Reviews.* Published June 2012. DOI: [10.1128/MMBR.05024-11](https://doi.org/10.1128/MMBR.05024-11). Respiration–fermentation distinction and cofactor reoxidation. (muller2012biochemistryandevolution pages 5-6)
6. Existing supplied reference: **Microbial metabolism chapter**, DOI: [10.1016/B978-012373944-5.00083-3](https://doi.org/10.1016/B978-012373944-5.00083-3). Supports organic-compound assimilation and growth, but should be used cautiously for the defining energy claim.
7. Existing supplied reference: **Bioenergetics review**, DOI: [10.1016/j.bbabio.2008.09.008](https://doi.org/10.1016/j.bbabio.2008.09.008). Supports membrane electron transport as one respiratory energy-conservation route, not as a universal requirement.

## Recommended curation decision

Retain **METPO:1000655** as a broad physiology class and curate a minimal core centered on **organic electron-donor oxidation and energy conservation**, with explicit alternative respiration and fermentation modules. Extend the existing 11-node/11-edge graph primarily by adding (i) transport as conditional, (ii) reduced-carrier generation and reoxidation, (iii) SLP as a coequal energy-conservation route, (iv) anaerobic/fermentative alternatives, and (v) assimilation as a downstream—not defining—branch. Taxon-specific complexes, acceptors, inhibitors and storage products should be placed in optional evidence-qualified subgraphs.

References

1. (schonheit2016ontheorigin pages 2-4): Peter Schönheit, Wolfgang Buckel, and William F. Martin. On the origin of heterotrophy. Trends in microbiology, 24 1:12-25, Jan 2016. URL: https://doi.org/10.1016/j.tim.2015.10.003, doi:10.1016/j.tim.2015.10.003. This article has 192 citations and is from a domain leading peer-reviewed journal.

2. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 6-8): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 31 citations.

3. (muller2012biochemistryandevolution pages 5-6): Miklós Müller, Marek Mentel, Jaap J. van Hellemond, Katrin Henze, Christian Woehle, Sven B. Gould, Re-Young Yu, Mark van der Giezen, Aloysius G. M. Tielens, and William F. Martin. Biochemistry and evolution of anaerobic energy metabolism in eukaryotes. Microbiology and Molecular Biology Reviews, 76:444-495, Jun 2012. URL: https://doi.org/10.1128/mmbr.05024-11, doi:10.1128/mmbr.05024-11. This article has 989 citations and is from a domain leading peer-reviewed journal.

4. (buckel2021energyconservationin pages 1-2): Wolfgang Buckel. Energy conservation in fermentations of anaerobic bacteria. Frontiers in Microbiology, Sep 2021. URL: https://doi.org/10.3389/fmicb.2021.703525, doi:10.3389/fmicb.2021.703525. This article has 139 citations and is from a peer-reviewed journal.

5. (folch2021metabolicenergyconservation pages 3-4): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

6. (folch2021metabolicenergyconservation pages 20-21): Pauline L. Folch, Markus M.M. Bisschops, and Ruud A. Weusthuis. Metabolic energy conservation for fermentative product formation. Microbial Biotechnology, 14:829-858, Jan 2021. URL: https://doi.org/10.1111/1751-7915.13746, doi:10.1111/1751-7915.13746. This article has 62 citations and is from a peer-reviewed journal.

7. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 16-18): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 31 citations.

8. (schonheit2016ontheorigin pages 8-10): Peter Schönheit, Wolfgang Buckel, and William F. Martin. On the origin of heterotrophy. Trends in microbiology, 24 1:12-25, Jan 2016. URL: https://doi.org/10.1016/j.tim.2015.10.003, doi:10.1016/j.tim.2015.10.003. This article has 192 citations and is from a domain leading peer-reviewed journal.