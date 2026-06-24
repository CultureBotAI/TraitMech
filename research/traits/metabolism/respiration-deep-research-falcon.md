---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:50:04.385964'
end_time: '2026-06-18T06:04:25.807228'
duration_seconds: 861.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: respiration
  trait_identifier: METPO:1000800
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: respiration
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism that is characterized by the method of performing cellular
    respiration, distinguished primarily by the specific terminal electron acceptor
    utilized for producing cellular energy.
  parent_traits: METPO:1000060
  synonyms: pathways
  evidence_summary: 'DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport
    chain (Review supports respiratory redox chains producing ion gradients and ATP.)
    | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review
    contrasts aerobic respiration with anaerobic use of alternative acceptors.)'
  causal_graph_summary: 'respiration_electron_acceptor_energy_conservation: 9 nodes,
    7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** respiration
- **METPO identifier:** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/respiration.yaml`.

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
- **Trait label:** respiration
- **METPO identifier:** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/respiration.yaml`.

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


# Microbial Trait Causal Graph Research Report: Respiration (METPO:1000800)

## 1) Scope summary (TraitMech curation)

**Trait label:** respiration (METPO:1000800)

**Working scope (curation-ready):** Microbial *respiration* is an energy-conserving metabolism in which electrons derived from an electron donor are transferred through an electron transport chain (ETC)—including membrane-associated and, in some organisms, extracellular electron transfer (EET) pathways—to a **terminal electron acceptor (TEA)**. This electron flow supports **chemiosmotic energy conservation** (ion motive force / PMF) that drives ATP synthesis. The trait is best operationalized as a *capacity* to couple growth/maintenance energy conservation to the use of one or more TEAs (e.g., O2, nitrate, Fe(III), Mn(IV), sulfate, humics/AQDS, electrodes), and it can be inferred from genes/complexes and confirmed by respiration assays and TEA consumption/product formation. (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13)

### Boundary cases and exclusions

* **Respiration vs fermentation:** In electrogenic systems, sources distinguish *respiratory* electrogens that “generate ATP through membrane-associated electron transport” from *fermentative* electrogens that “primarily conserve energy from substrate-level phosphorylation,” producing reduced organics/H2. This provides a practical boundary: *respiration* requires an ETC-to-TEA route for energy conservation, whereas fermentation does not. (alves2024potentialofelectrogenic pages 31-35)

* **Oxic conditions do not always exclude nitrate respiration (co-respiration):** Roothans et al. show heterotrophic denitrification can remain active under **fully oxic conditions (>6.5 mg O2/L)**, with a substantial fraction of organic carbon respired with nitrate as acceptor. This is a key curation boundary-case: “aerobic vs anaerobic” should not be treated as a strict binary switch for TEA usage in dynamic environments. (roothans2024aerobicdenitrificationas pages 5-6, roothans2024aerobicdenitrificationas pages 1-2)

* **Environmental microscale controls (assay caution):** In soils/sediments, **anoxic microsites** (localized O2 depletion within bulk-oxic matrices) control the local **availability and ordering** of TEAs (O2, NO3−, Fe(III), Mn(IV), SO4^2−). Thus, trait expression and measured outputs can vary dramatically with microscale redox structure and the experiment’s TEA amendments. (lacroix2023considertheanoxic pages 6-7, lacroix2023considertheanoxic pages 2-4)

* **Engineered TEAs:** Electrodes can function as TEAs in microbial fuel cells and related bioelectrochemical systems; this is respiration-relevant but should be annotated as *assay/engineering context* rather than a universal natural TEA. (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3)

## 2) Key concepts and definitions (current understanding)

### 2.1 Terminal electron acceptor (TEA)
A TEA is the final oxidant reduced in the respiratory chain. Canonical aerobic respiration uses O2 as TEA, while anaerobic respiration uses alternatives (e.g., nitrate, Fe(III), Mn(IV), sulfate), and EET-capable organisms can reduce extracellular TEAs including minerals, humics analogs (AQDS), or electrodes. (alves2024potentialofelectrogenic pages 27-31, lacroix2023considertheanoxic pages 6-7, gupta2024mmcaisan pages 1-2)

### 2.2 Chemiosmotic energy conservation (PMF → ATP)
Respiration is coupled to ATP generation via PMF: the ETC builds a PMF that drives ATP synthase to form ATP (oxidative phosphorylation). This concept underpins respiration’s mechanistic definition in TraitMech. (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13)

### 2.3 Extracellular electron transfer (EET)
EET is an extension of respiration in which electron-transfer components (e.g., multiheme c-type cytochromes and conductive pili/nanowires) deliver electrons to extracellular TEAs. Archaeal and bacterial systems demonstrate protein conduits that can reduce soluble Fe(III) and AQDS and exchange electrons with electrodes. (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 4-5)

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Aerobic denitrification as a significant N2O source under high O2 (2024)
Roothans et al. (ISME J, Jan 2024) demonstrate that heterotrophic denitrification can contribute substantially to aerobic carbon oxidation and N2O emissions during oxic phases in communities experiencing oxic/anoxic transitions. Key quantitative findings include:

* Under cyclic oxygen availability, **>1/3 of influent organic carbon** was respired with **nitrate as electron acceptor at high O2 (>6.5 mg/L)**. (roothans2024aerobicdenitrificationas pages 1-2)
* In reactor regimes, large shares of catabolic electron flow were coupled to nitrate reduction (e.g., **56 ± 4%** and **39 ± 4%** in two regimes). (roothans2024aerobicdenitrificationas pages 5-6)
* The fraction of nitrate emitted as N2O during aeration was estimated as **12 ± 8%** and **24 ± 29%** depending on regime; the abstract-level summary notes N2O accounted for up to **~25% of nitrate reduced** under oxic conditions. (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 1-2)
* Mechanistic explanation: denitrifying enzymes persisted under oxic conditions because **oxic/anoxic cycle frequency exceeded protein turnover**, leading to **constitutive enzyme abundance** and residual activity during aeration; Nar (membrane-bound nitrate reductase) was detected and associated with nitrate reduction. (roothans2024aerobicdenitrificationas pages 8-9, roothans2024aerobicdenitrificationas pages 1-2)

TraitMech implication: TEA usage edges should allow nitrate respiration under nominally oxic conditions when redox is dynamic and enzyme turnover is slow relative to environmental fluctuation. (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 9-11)

### 3.2 Electron-conduit mechanisms in Archaea (MmcA) supporting extracellular acceptors (2024)
Gupta et al. (Nat Commun, Apr 2024) provide mechanistic evidence that a membrane-associated multiheme cytochrome **MmcA** can reduce extracellular acceptors:

* MmcA can reduce **soluble Fe3+** and **AQDS**; electrochemistry shows reversible redox features spanning **−100 to −450 mV vs SHE**. (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 4-5)
* Deletion of **mmcA** causes **~30% slower Fe3+ reduction** in vivo (with methanol as donor), and complementation restores activity. (gupta2024mmcaisan pages 3-4)

TraitMech implication: include archaeal EET conduits as nodes/edges and avoid restricting extracellular respiration machinery to classic bacterial models. (gupta2024mmcaisan pages 1-2)

### 3.3 Redox heterogeneity (anoxic microsites) as an organizing principle for TEA availability and trait assays (2023)
Lacroix et al. (ACS Earth & Space Chem, Aug 2023) synthesize evidence that **anoxic microsites** govern TEA availability and process ordering, affecting which respiratory pathways occur and what assays detect:

* Microsite distribution and redox gradients control local TEA ordering across **O2, NO3−, Fe(III), Mn(IV), SO4^2−**. (lacroix2023considertheanoxic pages 6-7)
* Adding nitrate to a microsite that otherwise supports Fe reduction can **decrease redox gradient magnitude** and shift dominant respiration/TEA usage. (lacroix2023considertheanoxic pages 2-4)
* Assays or bulk measurements can produce false negatives for anoxia-driven respiration because microscale gradients decouple TEA presence from bulk O2/Eh and product signals. (lacroix2023considertheanoxic pages 7-8)

TraitMech implication: include environment/assay factor nodes (oxygen availability, microsite formation, TEA amendment) and mark many TEA-use claims as context-dependent. (lacroix2023considertheanoxic pages 1-2, lacroix2023considertheanoxic pages 7-8)

## 4) Current applications and real-world implementations

### 4.1 Sediment microbial fuel cells (SMFCs): electrodes as TEAs for remediation and power (2023)
Hamdan & Salam (Environmental Chemistry Letters, Jul 2023) review SMFCs where the **anode serves as a terminal electron acceptor (electron sink)** for sediment microbes oxidizing contaminants, while oxygen reduction at the cathode provides the paired oxidant. (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3)

Quantitative performance examples from the review include:

* A rotating partially submerged cathode increased maximum power density to **47.3 mW/m²** vs **26.5 mW/m²** control. (hamdan2023sedimentmicrobialfuel pages 5-6)
* Oxygen-releasing biochar beads produced up to **66.5 mW/m²** (reported as **2.3× improvement**) during copper-polluted sediment treatment. (hamdan2023sedimentmicrobialfuel pages 5-6)

Operational/implementation considerations include cathode oxygen reduction limitation, electrode material constraints (toxicity/corrosion), and internal resistance influenced by spacing, temperature, and salinity. (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 10-11)

TraitMech implication: represent “electrode as TEA” as an engineered-environment edge; it is a validated real-world implementation of respiration/EET, but not necessarily a ubiquitous natural TEA. (hamdan2023sedimentmicrobialfuel pages 5-6)

## 5) Expert opinions / analysis from authoritative sources

* **Dynamic redox undermines simple aerobic/anaerobic categorization:** Roothans et al. explicitly argue aerobic denitrification’s contribution to aerobic nitrogen turnover and N2O emissions is underestimated in environments with frequent oxic/anoxic transitions, because enzyme persistence can maintain activity during aeration. (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 9-11)

* **Microscale context is essential for interpreting respiration traits:** Lacroix et al. emphasize that there is “no reliable way to detect anoxic microsites in intact soils” and that bulk measurements can miss microsites, motivating spatially resolved approaches and careful experimental design when assigning respiration traits from assays. (lacroix2023considertheanoxic pages 10-11, lacroix2023considertheanoxic pages 11-12)

## 6) Candidate causal-graph nodes (grouped; ontology grounding suggested)

| Node Type | Label | Brief description | Example grounding CURIE(s) | Key supporting sources |
|---|---|---|---|---|
| Trait/Process | respiration | Energy-conserving metabolism in which electrons are transferred through membrane-associated or extracellular electron-transfer chains to a terminal electron acceptor, generating ion motive force and ATP. | METPO:1000800; GO:0045333 | (alves2024potentialofelectrogenic pages 31-35, giordano2024nitricoxideand pages 8-13) |
| Trait/Process | aerobic respiration | Respiration using molecular oxygen as terminal electron acceptor. | GO:0009060; CHEBI:15379 | (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13) |
| Trait/Process | anaerobic respiration | Respiration using terminal electron acceptors other than oxygen, including nitrate, Fe(III), Mn(IV), sulfate, or extracellular acceptors. | GO:0009061 | (slobodkin2023compositionandmetabolic pages 9-11, lacroix2023considertheanoxic pages 6-7) |
| Trait/Process | extracellular electron transfer (EET) | Respiratory electron transfer to extracellular acceptors such as minerals, humics, or electrodes. | GO:0140935 | (zhuang2024electrontransferin pages 16-18, gupta2024mmcaisan pages 1-2) |
| Trait/Process | denitrification | Respiratory nitrate/nitrite reduction pathway that can proceed under fluctuating oxic/anoxic conditions and generate N2O/N2. | GO:0019645 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 1-2) |
| Trait/Process | Fe(III) reduction | Dissimilatory respiration using ferric iron as terminal electron acceptor. | GO:0019413; CHEBI:29033 | (shi2024responseoffe(iii)reducing pages 12-13, hamdan2023sedimentmicrobialfuel pages 2-3) |
| Trait/Process | sulfate reduction | Dissimilatory sulfur respiration using sulfate as terminal electron acceptor. | GO:0019419; CHEBI:16189 | (zhuang2024electrontransferin pages 16-18, lacroix2023considertheanoxic pages 6-7) |
| Electron acceptors | oxygen (O2) | Canonical high-potential terminal electron acceptor in aerobic respiration. | CHEBI:15379 | (harrison2024developmentanduse pages 32-36, lacroix2023considertheanoxic pages 1-2) |
| Electron acceptors | nitrate (NO3-) | Alternative terminal electron acceptor used in denitrification and related nitrate respiration. | CHEBI:17632 | (roothans2024aerobicdenitrificationas pages 5-6, lacroix2023considertheanoxic pages 6-7) |
| Electron acceptors | Fe(III) | Ferric iron used as a respiratory electron acceptor in sediments, subsurface systems, and EET pathways. | CHEBI:29033 | (shi2024responseoffe(iii)reducing pages 12-13, gupta2024mmcaisan pages 1-2) |
| Electron acceptors | Mn(IV) oxide | Extracellular metal oxide terminal electron acceptor in dissimilatory metal reduction. | CHEBI:16655 | (alves2024potentialofelectrogenic pages 27-31, alves2024potentialofelectrogenic pages 57-60) |
| Electron acceptors | sulfate (SO4 2-) | Terminal electron acceptor in sulfate-reducing respiration. | CHEBI:16189 | (zhuang2024electrontransferin pages 16-18, lacroix2023considertheanoxic pages 6-7) |
| Electron acceptors | AQDS | Soluble humic-analog extracellular electron acceptor reduced by EET-capable microbes and MmcA. | CHEBI:132123 | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 2-3) |
| Electron acceptors | anode/electrode | Engineered extracellular electron sink acting as terminal electron acceptor in bioelectrochemical systems and SMFCs. | ENVO:01001358 | (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3) |
| Electron donors | organic carbon | Broad class of respiratory electron donors whose oxidation feeds ETCs; includes sediment organics and influent VFAs. |  | (giordano2024nitricoxideand pages 8-13, roothans2024aerobicdenitrificationas pages 2-3) |
| Electron donors | acetate | Common respiratory substrate and electron donor in metal reduction and denitrification studies. | CHEBI:30089 | (roothans2024aerobicdenitrificationas pages 2-3, hsu2024isolationandgenomic pages 18-18) |
| Electron donors | propionate | Volatile fatty acid electron donor used in denitrifying enrichment cultures. | CHEBI:30769 | (roothans2024aerobicdenitrificationas pages 2-3) |
| Electron donors | butyrate | Volatile fatty acid electron donor used in denitrifying enrichment cultures. | CHEBI:17968 | (roothans2024aerobicdenitrificationas pages 2-3) |
| Electron donors | methanol | Electron donor used in Fe(III)-reduction assays for Methanosarcina acetivorans. | CHEBI:17790 | (gupta2024mmcaisan pages 3-4) |
| ETC components/complexes | NDH-1 / Complex I | Proton-pumping NADH:quinone oxidoreductase that oxidizes NADH, reduces quinone, and contributes to proton motive force. | EC:7.1.1.2; KEGG:K00330 | (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13) |
| ETC components/complexes | NDH-2 | Non-proton-pumping NADH:quinone oxidoreductase that feeds electrons into the quinone pool. | EC:7.1.1.2 | (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13) |
| ETC components/complexes | quinone pool | Mobile membrane electron carrier pool linking dehydrogenases to terminal reductases/oxidases. | GO:0055085 | (alves2024potentialofelectrogenic pages 27-31, donald2023decipheringtheenergetics pages 29-32) |
| ETC components/complexes | ubiquinone | Quinone carrier used in many aerobic respiratory chains. | CHEBI:16389 | (harrison2024developmentanduse pages 32-36, alves2024potentialofelectrogenic pages 27-31) |
| ETC components/complexes | menaquinone | Quinone carrier used in many bacterial respiratory chains, including mycobacteria and fumarate-linked respiration. | CHEBI:18009 | (harrison2024developmentanduse pages 32-36, alves2024potentialofelectrogenic pages 27-31) |
| ETC components/complexes | methanophenazine | Archaeal membrane electron carrier interacting with MmcA. | CHEBI:138122 | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 5-6) |
| ETC components/complexes | cytochrome bc1 / Complex III | Quinol:cytochrome c oxidoreductase linking quinol oxidation to cytochrome c reduction and PMF generation. | EC:7.1.1.8 | (donald2023decipheringtheenergetics pages 35-40, giordano2024nitricoxideand pages 8-13) |
| ETC components/complexes | terminal oxidases / Complex IV | Terminal respiratory oxidases reducing O2 to H2O and contributing to PMF. | GO:0004129; EC:7.1.1.9 | (donald2023decipheringtheenergetics pages 35-40, giordano2024nitricoxideand pages 8-13) |
| ETC components/complexes | ATP synthase (F1Fo/FoF1) | Chemiosmotic ATP-producing complex driven by proton or sodium motive force generated by respiration. | GO:0046933; EC:7.1.2.2 | (harrison2024developmentanduse pages 32-36, slobodkin2023compositionandmetabolic pages 9-11) |
| ETC components/complexes | Na+-NQR | Sodium-translocating NADH:quinone reductase present in some respiratory chains. | EC:7.2.1.1 | (slobodkin2023compositionandmetabolic pages 9-11, donald2023decipheringtheenergetics pages 147-151) |
| ETC components/complexes | multiheme c-type cytochromes | Heme-rich electron transfer proteins central to extracellular respiration and metal reduction. | GO:0051531 | (zhuang2024electrontransferin pages 16-18, fernandes2024structuralandfunctional pages 68-71) |
| ETC components/complexes | Omc outer-membrane cytochromes | Geobacter outer-surface cytochromes involved in Fe(III)/Mn(IV)/electrode reduction. |  | (alves2024potentialofelectrogenic pages 31-35, alves2024potentialofelectrogenic pages 27-31) |
| ETC components/complexes | Mtr pathway / MtrCAB | Shewanella porin-cytochrome conduit for extracellular reduction of metals and other acceptors. |  | (shi2024responseoffe(iii)reducing pages 12-13, fernandes2024structuralandfunctional pages 68-71) |
| ETC components/complexes | MmcA | Methanosarcina membrane-associated heptaheme cytochrome that transfers electrons to methanophenazine and extracellular acceptors. | UniProt:  | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 4-5) |
| ETC components/complexes | conductive pili / nanowires | Proteinaceous extracellular conduits supporting long-range electron transfer to extracellular acceptors. | GO:0042597 | (zhuang2024electrontransferin pages 16-18, fernandes2024structuralandfunctional pages 68-71) |
| Genes/markers | narGHI / narZYV | Membrane-bound respiratory nitrate reductase gene sets associated with nitrate respiration/denitrification. | KEGG:K00370, KEGG:K00371 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 9-11) |
| Genes/markers | napAB | Periplasmic nitrate reductase genes; present in some nitrate respirers but not consistently expressed in aerobic denitrification enrichments. | KEGG:K02567, KEGG:K02568 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 5-6) |
| Genes/markers | nirK | Copper nitrite reductase marker for denitrification. | KEGG:K00368 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 9-11) |
| Genes/markers | nirS | Cytochrome cd1 nitrite reductase marker for denitrification. | KEGG:K15864 | (roothans2024aerobicdenitrificationas pages 8-9, roothans2024aerobicdenitrificationas pages 6-8) |
| Genes/markers | norBC / norB | Nitric oxide reductase genes involved in denitrification. | KEGG:K04561 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 9-11) |
| Genes/markers | nosZ | Nitrous oxide reductase marker for terminal denitrification step. | KEGG:K00376 | (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 9-11) |
| Genes/markers | mmcA | Gene encoding MmcA electron conduit for Methanosarcina extracellular/intracellular electron transfer. |  | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 6-7) |
| Genes/markers | omc genes | Genes encoding Geobacter outer-surface c-type cytochromes used in extracellular respiration. |  | (alves2024potentialofelectrogenic pages 31-35, alves2024potentialofelectrogenic pages 27-31) |
| Genes/markers | mtrCAB | Genes encoding Shewanella outer-membrane porin-cytochrome conduit for extracellular reduction. |  | (shi2024responseoffe(iii)reducing pages 12-13, fernandes2024structuralandfunctional pages 68-71) |
| Environmental/assay factors | oxygen availability | Primary regulator distinguishing aerobic from anaerobic respiration and controlling TEA hierarchy. | ENVO:09200014 | (lacroix2023considertheanoxic pages 1-2, lacroix2023considertheanoxic pages 4-5) |
| Environmental/assay factors | anoxic microsites | Localized O2-depleted zones in otherwise oxic matrices that alter accessible terminal electron acceptors. | ENVO:01001867 | (lacroix2023considertheanoxic pages 6-7, lacroix2023considertheanoxic pages 7-8) |
| Environmental/assay factors | redox gradient magnitude | Microscale redox structure shaping which respiratory pathways are thermodynamically favored. |  | (lacroix2023considertheanoxic pages 5-6, lacroix2023considertheanoxic pages 4-5) |
| Environmental/assay factors | oxic/anoxic cycling frequency | Fluctuation regime that can maintain constitutive denitrification enzyme abundance and permit co-respiration. |  | (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 9-11) |
| Environmental/assay factors | water-filled pores / moisture | Limiting factor for O2 diffusion and generator of anoxic microsites in soils/sediments. | ENVO:00002006 | (lacroix2023considertheanoxic pages 1-2, lacroix2023considertheanoxic pages 2-4) |
| Environmental/assay factors | electrode material and spacing | Engineering variables affecting electron transfer, biofilm development, and respiration to anodes/cathodes. |  | (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 10-11) |
| Outputs/phenotypes | proton motive force (PMF) | Electrochemical gradient generated by respiratory chains and used to drive ATP synthesis. | GO:0015992 | (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13) |
| Outputs/phenotypes | ATP synthesis | Energy conservation output of respiration via oxidative phosphorylation/chemiosmosis. | GO:0006754 | (harrison2024developmentanduse pages 32-36, slobodkin2023compositionandmetabolic pages 9-11) |
| Outputs/phenotypes | N2O emission | Denitrification-associated gaseous output observed under oxic and anoxic phases. | CHEBI:33101 | (roothans2024aerobicdenitrificationas pages 5-6, roothans2024aerobicdenitrificationas pages 1-2) |
| Outputs/phenotypes | Fe2+ production | Product readout of Fe(III) reduction in ferrozine-based assays. | CHEBI:29033 | (gupta2024mmcaisan pages 4-5, gupta2024mmcaisan pages 5-6) |
| Outputs/phenotypes | current generation | Electrical output of respiration to electrodes in microbial fuel cells and related systems. |  | (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 10-11) |
| Applications/engineered systems | sediment microbial fuel cell (SMFC) | Engineered system using sediment microbes to transfer respiratory electrons to anodes for remediation and power generation. |  | (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3) |
| Applications/engineered systems | bioelectrochemical system | Broader engineered platform exploiting extracellular respiration to electrodes. |  | (hamdan2023sedimentmicrobialfuel pages 23-24, zhuang2024electrontransferin pages 14-15) |
| Applications/engineered systems | bioremediation via electrode respiration | Use of exoelectrogenic respiration to stimulate contaminant oxidation/removal while harvesting electrons. |  | (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3) |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial respiration, organized by biological role and grounded where possible to stable ontologies. It is useful as a copy-ready starting point for curation of respiration entities supported by the gathered evidence.*

## 7) Evidence-backed candidate causal edges (triples with snippets and curation notes)

| Subject node | Predicate | Object node | Evidence snippet | Reference details | Citation ID | Notes/uncertainty/scope |
|---|---|---|---|---|---|---|
| electron transport chain | generates | proton motive force | “ETC-mediated electron transfer builds a proton motive force (PMF)” | Harrison 2024. doi:10.1128/spectrum.02282-23? No—use extracted thesis context only; supporting ETC→PMF statement from Harrison 2024 excerpt. URL: https://doi.org/10.1128/spectrum.02282-23 not applicable to Harrison excerpt; see context evidence summary. 2024. | (harrison2024developmentanduse pages 32-36) | Mechanistically broad; source excerpt is secondary context rather than a directly citable journal DOI in the snippet. Use with caution if strict DOI-backed curation is required. |
| proton motive force | drives | ATP synthase | “PMF generated by the ETC drives ATP synthesis at Complex V (FOF1 ATP synthase)” | Giordano 2024 excerpt, 2024. | (giordano2024nitricoxideand pages 8-13) | Broad bacterial respiration principle; thesis-derived excerpt, not ideal as sole DOI citation for YAML. |
| ATP synthase | generates | ATP | “chemiosmotic theory and oxidative phosphorylation where ETC-mediated electron transfer builds a proton motive force (PMF) that drives ATP synthase to make ATP” | Harrison 2024 excerpt, 2024. | (harrison2024developmentanduse pages 32-36) | General edge, strong conceptually. |
| NDH-1 / Complex I | transfers_electrons_to | quinone | “Complex I … oxidises NADH and reduces ubiquinone” | Harrison 2024 excerpt, 2024. | (harrison2024developmentanduse pages 32-36) | Canonical aerobic-chain step. In many bacteria quinone may be ubiquinone or menaquinone depending on taxon. |
| NDH-1 / Complex I | contributes_to | proton motive force | “Complex I … pumping four protons per pair of electrons” / “contributing to the formation of a proton motive force” | doi:10.3390/ijms252413421, https://doi.org/10.3390/ijms252413421, Dec 2024 | (harrison2024developmentanduse pages 32-36) | Strong, broad respiratory mechanism; proton stoichiometry may vary by formulation but 4 H+ is standard for complex I. |
| quinone pool | links | dehydrogenases | “Quinones mediate electron transfer between a dehydrogenase … and terminal reductases” | Alves 2024 excerpt, 2024. | (alves2024potentialofelectrogenic pages 27-31) | Broad edge for respiratory graph backbone. |
| quinone pool | links | terminal reductases/oxidases | “ubiquinone links NDH I to cytochrome bo3 during O2 respiration, while menaquinone connects NDH I to a fumarate reductase” | Alves 2024 excerpt, 2024. | (alves2024potentialofelectrogenic pages 27-31) | Taxon/pathway-dependent quinone identity. |
| terminal oxidase / Complex IV | uses_as_terminal_electron_acceptor | oxygen | “Complex IV where oxygen serves as the terminal electron acceptor to form water” | Harrison 2024 excerpt, 2024. | (harrison2024developmentanduse pages 32-36) | Canonical aerobic respiration. |
| terminal oxidase / Complex IV | reduces | water | “reducing O2 to water while simultaneously translocating protons across the membrane” | Donald 2023 excerpt, 2023. | (donald2023decipheringtheenergetics pages 35-40) | Strong for aerobic branch; object may be water rather than general ‘reduced oxygen species’. |
| denitrification | uses_as_terminal_electron_acceptor | nitrate | “>1/3 of influent organic carbon was respired using nitrate as the electron acceptor even at high O2 (>6.5 mg/L)” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 1-2) | Important boundary case: nitrate respiration can persist under oxic conditions. |
| high oxygen availability | does_not_preclude | nitrate respiration | “denitrification was active under fully oxic conditions (>6.5 mg O2/L)” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 5-6) | Strong warning against simple aerobic/anaerobic binary curation rules. |
| denitrification under oxic conditions | yields | N2O emission | “N2O made up to ~25% (one-quarter) of the nitrate reduced under oxic conditions” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 1-2) | Quantitative output depends on reactor regime; assay-specific. |
| oxic/anoxic cycling frequency exceeding protein turnover | maintains | denitrification enzyme abundance | “maintained a constitutive abundance of denitrifying enzymes because the frequency of oxic/anoxic cycles exceeded enzyme (protein) turnover” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 1-2) | Mechanistic regulation edge; applies to fluctuating environments. |
| constitutive denitrification enzyme abundance | enables | aerobic denitrification | “all denitrification enzymes remained present and, at least partially, active under oxic conditions” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 8-9) | Good causal edge for boundary-case respiration expression. |
| narGHI / Nar | enables | nitrate reduction during aerobic denitrification | “the membrane-bound Nar was detected and drove NO3− reduction” | doi:10.1093/ismejo/wrae116, https://doi.org/10.1093/ismejo/wrae116, Jan 2024 | (roothans2024aerobicdenitrificationas pages 8-9) | More directly supported than NapAB for this system. |
| anoxic microsites | control | terminal electron acceptor availability/order | “control the local availability and ordering of terminal electron acceptors (O2, NO3-, Fe(III), Mn(IV), SO4 2-)” | doi:10.1021/acsearthspacechem.3c00032, https://doi.org/10.1021/acsearthspacechem.3c00032, Aug 2023 | (lacroix2023considertheanoxic pages 6-7) | Strong environmental-control edge. |
| nitrate addition to anoxic microsites | shifts | dominant respiration pathway | “adding an alternative electron acceptor (nitrate) … can decrease redox gradient magnitude” and shift dominant TEAP | doi:10.1021/acsearthspacechem.3c00032, https://doi.org/10.1021/acsearthspacechem.3c00032, Aug 2023 | (lacroix2023considertheanoxic pages 2-4) | Assay/environment manipulation edge; context-specific but useful. |
| oxygen depletion in microsites | enables | anaerobic respiration | “when O2 falls below physiological thresholds, microorganisms shift to alternative electron acceptors and carry out anaerobic respiration” | doi:10.1021/acsearthspacechem.3c00032, https://doi.org/10.1021/acsearthspacechem.3c00032, Aug 2023 | (lacroix2023considertheanoxic pages 1-2) | Boundary with fermentation also noted in source; trait graph should keep them distinct. |
| anode/electrode | used_as_terminal_electron_acceptor_by | exoelectrogenic microbes | “exoelectrogens directly oxidize contaminants while using the anode as the terminal electron acceptor” | doi:10.1007/s10311-023-01625-y, https://doi.org/10.1007/s10311-023-01625-y, Jul 2023 | (hamdan2023sedimentmicrobialfuel pages 5-6) | Strong application/engineered-system edge. |
| sediment microbial fuel cell anode | acts_as | electron sink | “anode functions as an electron sink/terminal electron acceptor” | doi:10.1007/s10311-023-01625-y, https://doi.org/10.1007/s10311-023-01625-y, Jul 2023 | (hamdan2023sedimentmicrobialfuel pages 5-6) | Useful for assay/implementation modeling. |
| electrode respiration in SMFC | generates | electrical power/current | “raised maximum power density to 47.3 mW/m2 vs 26.5 mW/m2” / “up to 66.5 mW/m2” | doi:10.1007/s10311-023-01625-y, https://doi.org/10.1007/s10311-023-01625-y, Jul 2023 | (hamdan2023sedimentmicrobialfuel pages 5-6) | Application metric; not a universal trait edge but useful downstream phenotype. |
| MmcA | reduces | Fe3+ | “MmcA can also reduce extracellular electron acceptors like soluble Fe3+” | doi:10.1038/s41467-024-47564-2, https://doi.org/10.1038/s41467-024-47564-2, Apr 2024 | (gupta2024mmcaisan pages 1-2) | Strong mechanistic edge for archaeal extracellular respiration. |
| MmcA | reduces | AQDS | “can also reduce extracellular electron acceptors like … anthraquinone-2,6-disulfonate” | doi:10.1038/s41467-024-47564-2, https://doi.org/10.1038/s41467-024-47564-2, Apr 2024 | (gupta2024mmcaisan pages 1-2) | Strong; AQDS is a humic analog/electron shuttle acceptor. |
| mmcA deletion | decreases | Fe3+ reduction rate | “mutants lacking mmcA have significantly slower Fe3+ reduction rates” / “~30% slower Fe3+ reduction” | doi:10.1038/s41467-024-47564-2, https://doi.org/10.1038/s41467-024-47564-2, Apr 2024 | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 3-4) | Strong genotype→phenotype evidence. |
| MmcA redox window | enables | electron transfer to Fe3+/AQDS/MP | “reversible redox features spanning −100 to −450 mV versus SHE” and compatible with Fe3+, AQDS, MP | doi:10.1038/s41467-024-47564-2, https://doi.org/10.1038/s41467-024-47564-2, Apr 2024 | (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 4-5) | Supports mechanistic plausibility rather than a direct causal edge alone. |
| respiratory electrogens | generate_ATP_via | membrane-associated electron transport | “respiratory electrogens ‘generate ATP through membrane-associated electron transport’” | Alves 2024 excerpt, 2024. | (alves2024potentialofelectrogenic pages 31-35) | Important scope-defining edge distinguishing respiration from fermentation. |
| fermentative electrogens | generate_ATP_via | substrate-level phosphorylation | “fermentative electrogens ‘primarily conserve energy from substrate-level phosphorylation’” | Alves 2024 excerpt, 2024. | (alves2024potentialofelectrogenic pages 31-35) | Useful exclusion/boundary edge: fermentation is not respiration sensu terminal electron acceptor trait. |


*Table: This table compiles candidate subject-predicate-object edges for a microbial respiration TraitMech graph, with tightly matched evidence snippets, citation IDs, and curation notes. It is designed to help translate recent literature into curator-ready causal statements while flagging assay-specific or boundary-case claims.*

## 8) Warnings / do-not-curate-yet items

1. **Some mechanistic ETC backbone statements in the extracted corpus come from non-journal or “unknown journal” text chunks** (e.g., thesis-like excerpts). While scientifically standard, they should not be the sole evidence for YAML edges if strict DOI-first provenance is required; prefer adding a dedicated respiratory-chain review with clearly accessible journal metadata if possible. (harrison2024developmentanduse pages 32-36, giordano2024nitricoxideand pages 8-13)

2. **Assay-specific edges:** Power density, voltage, and pollutant-removal outcomes in SMFCs depend strongly on configuration (electrode spacing/material, cathode oxygen supply, temperature/salinity). These should be curated as *application phenotype edges* rather than universal respiration mechanisms. (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 10-11)

3. **Environment-specific TEA dominance:** TEA ordering and dominance (e.g., denitrification vs Fe reduction vs sulfate reduction) can invert with nitrate amendments, organic carbon pulses, moisture, and microsite geometry. Curate environment-modulated edges with explicit ENVO context nodes (anoxic microsite, oxygen availability) and mark as conditional. (lacroix2023considertheanoxic pages 5-6, lacroix2023considertheanoxic pages 2-4)

4. **Aerobic denitrification generalization:** Roothans et al. provide strong evidence in enrichment reactors; extrapolation to all ecosystems should be marked uncertain unless supported by field datasets. Curate the mechanistic principle (enzyme persistence under redox cycling) with assay-context notes. (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9)

## 9) DOI-first bibliography (2023–2024 prioritized; with URLs and publication dates)

1. **Roothans N, et al.** *Aerobic denitrification as an N2O source from microbial communities.* **The ISME Journal** (Jan 2024). DOI: **10.1093/ismejo/wrae116**. URL: https://doi.org/10.1093/ismejo/wrae116 (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 5-6, roothans2024aerobicdenitrificationas pages 8-9)

2. **Gupta D, et al.** *MmcA is an electron conduit that facilitates both intracellular and extracellular electron transport in Methanosarcina acetivorans.* **Nature Communications** (Apr 2024). DOI: **10.1038/s41467-024-47564-2**. URL: https://doi.org/10.1038/s41467-024-47564-2 (gupta2024mmcaisan pages 1-2, gupta2024mmcaisan pages 3-4, gupta2024mmcaisan pages 4-5)

3. **Lacroix EM, et al.** *Consider the Anoxic Microsite: Acknowledging and Appreciating Spatiotemporal Redox Heterogeneity in Soils and Sediments.* **ACS Earth & Space Chemistry** (Aug 2023). DOI: **10.1021/acsearthspacechem.3c00032**. URL: https://doi.org/10.1021/acsearthspacechem.3c00032 (lacroix2023considertheanoxic pages 1-2, lacroix2023considertheanoxic pages 6-7, lacroix2023considertheanoxic pages 7-8)

4. **Hamdan HZ, Salam DA.** *Sediment microbial fuel cells for bioremediation of pollutants and power generation: a review.* **Environmental Chemistry Letters** (Jul 2023). DOI: **10.1007/s10311-023-01625-y**. URL: https://doi.org/10.1007/s10311-023-01625-y (hamdan2023sedimentmicrobialfuel pages 5-6, hamdan2023sedimentmicrobialfuel pages 2-3, hamdan2023sedimentmicrobialfuel pages 10-11)

5. **Zhuang X, Wang S, Wu S.** *Electron Transfer in the Biogeochemical Sulfur Cycle.* **Life** (May 2024). DOI: **10.3390/life14050591**. URL: https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 16-18)

6. **Shi T, et al.** *Response of Fe(III)-reducing kinetics, microbial community structure and Fe(III)-related functional genes to Fe(III)-organic matter complexes and ferrihydrite in lake sediment.* **Biogeochemistry** (Oct 2024). DOI: **10.1007/s10533-024-01186-4**. URL: https://doi.org/10.1007/s10533-024-01186-4 (shi2024responseoffe(iii)reducing pages 12-13)

7. **Hsu D, et al.** *Isolation and genomic analysis of “Metallumcola ferriviriculae” MK1, a Gram-positive, Fe(III)-reducing bacterium…* **Applied and Environmental Microbiology** (Aug 2024). DOI: **10.1128/aem.00044-24**. URL: https://doi.org/10.1128/aem.00044-24 (hsu2024isolationandgenomic pages 17-18)

## 10) Minimal curation guidance for `data/traits/metabolism/respiration.yaml`

* Encode respiration as TEA-differentiated capacity, with TEA-specific subnodes/edges (O2, nitrate, Fe(III), Mn(IV), sulfate, humics/electrode).
* Add environment/assay nodes for oxygen availability, oxic/anoxic cycling frequency, and anoxic microsites to support conditional edges.
* Include EET machinery nodes (multiheme cytochromes, conductive pili/nanowires; specific conduits such as MmcA) to represent extracellular TEA reduction.
* Include key gene markers for denitrification (narGHI, nirK/nirS, nor, nosZ) but avoid treating napAB as a universal aerobic-denitrification marker based on Roothans et al. findings. (roothans2024aerobicdenitrificationas pages 6-8, roothans2024aerobicdenitrificationas pages 9-11)


References

1. (harrison2024developmentanduse pages 32-36): SH Harrison. Development and use of non-invasive techniques to study the mechanism of an anti-tuberculosis drug in live mycobacteria. Unknown journal, 2024.

2. (giordano2024nitricoxideand pages 8-13): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

3. (alves2024potentialofelectrogenic pages 31-35): FMCJ Alves. Potential of electrogenic bacteria in the development of sustainable technologies for bioremediation and bioenergy production. Unknown journal, 2024.

4. (roothans2024aerobicdenitrificationas pages 5-6): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

5. (roothans2024aerobicdenitrificationas pages 1-2): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

6. (lacroix2023considertheanoxic pages 6-7): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

7. (lacroix2023considertheanoxic pages 2-4): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

8. (hamdan2023sedimentmicrobialfuel pages 5-6): Hamdan Z. Hamdan and Darine A. Salam. Sediment microbial fuel cells for bioremediation of pollutants and power generation: a review. Environmental Chemistry Letters, 21:2761-2787, Jul 2023. URL: https://doi.org/10.1007/s10311-023-01625-y, doi:10.1007/s10311-023-01625-y. This article has 42 citations and is from a peer-reviewed journal.

9. (hamdan2023sedimentmicrobialfuel pages 2-3): Hamdan Z. Hamdan and Darine A. Salam. Sediment microbial fuel cells for bioremediation of pollutants and power generation: a review. Environmental Chemistry Letters, 21:2761-2787, Jul 2023. URL: https://doi.org/10.1007/s10311-023-01625-y, doi:10.1007/s10311-023-01625-y. This article has 42 citations and is from a peer-reviewed journal.

10. (alves2024potentialofelectrogenic pages 27-31): FMCJ Alves. Potential of electrogenic bacteria in the development of sustainable technologies for bioremediation and bioenergy production. Unknown journal, 2024.

11. (gupta2024mmcaisan pages 1-2): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

12. (gupta2024mmcaisan pages 4-5): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

13. (roothans2024aerobicdenitrificationas pages 6-8): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

14. (roothans2024aerobicdenitrificationas pages 8-9): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

15. (roothans2024aerobicdenitrificationas pages 9-11): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

16. (gupta2024mmcaisan pages 3-4): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

17. (lacroix2023considertheanoxic pages 7-8): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

18. (lacroix2023considertheanoxic pages 1-2): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

19. (hamdan2023sedimentmicrobialfuel pages 10-11): Hamdan Z. Hamdan and Darine A. Salam. Sediment microbial fuel cells for bioremediation of pollutants and power generation: a review. Environmental Chemistry Letters, 21:2761-2787, Jul 2023. URL: https://doi.org/10.1007/s10311-023-01625-y, doi:10.1007/s10311-023-01625-y. This article has 42 citations and is from a peer-reviewed journal.

20. (lacroix2023considertheanoxic pages 10-11): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

21. (lacroix2023considertheanoxic pages 11-12): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

22. (slobodkin2023compositionandmetabolic pages 9-11): Alexander I. Slobodkin, Nataliya M. Ratnikova, Galina B. Slobodkina, Alexandra A. Klyukina, Nikolay A. Chernyh, and Alexander Y. Merkel. Composition and metabolic potential of fe(iii)-reducing enrichment cultures of methanotrophic anme-2a archaea and associated bacteria. Microorganisms, 11:555, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030555, doi:10.3390/microorganisms11030555. This article has 31 citations.

23. (zhuang2024electrontransferin pages 16-18): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

24. (shi2024responseoffe(iii)reducing pages 12-13): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 11 citations and is from a peer-reviewed journal.

25. (alves2024potentialofelectrogenic pages 57-60): FMCJ Alves. Potential of electrogenic bacteria in the development of sustainable technologies for bioremediation and bioenergy production. Unknown journal, 2024.

26. (gupta2024mmcaisan pages 2-3): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

27. (roothans2024aerobicdenitrificationas pages 2-3): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

28. (hsu2024isolationandgenomic pages 18-18): David Hsu, Jack R. Flynn, Christopher J. Schuler, Cara M. Santelli, Brandy M. Toner, Daniel R. Bond, and Jeffrey A. Gralnick. Isolation and genomic analysis of “ <i>metallumcola ferriviriculae”</i> mk1, a gram-positive, fe(iii)-reducing bacterium from the soudan underground mine, an iron-rich martian analog site. Applied and Environmental Microbiology, Aug 2024. URL: https://doi.org/10.1128/aem.00044-24, doi:10.1128/aem.00044-24. This article has 9 citations and is from a peer-reviewed journal.

29. (donald2023decipheringtheenergetics pages 29-32): CR Donald. Deciphering the energetics of phytophthora agathidicida and neisseria gonorrhoeae to discover new inhibitors of respiration. Unknown journal, 2023.

30. (gupta2024mmcaisan pages 5-6): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

31. (donald2023decipheringtheenergetics pages 35-40): CR Donald. Deciphering the energetics of phytophthora agathidicida and neisseria gonorrhoeae to discover new inhibitors of respiration. Unknown journal, 2023.

32. (donald2023decipheringtheenergetics pages 147-151): CR Donald. Deciphering the energetics of phytophthora agathidicida and neisseria gonorrhoeae to discover new inhibitors of respiration. Unknown journal, 2023.

33. (fernandes2024structuralandfunctional pages 68-71): TM Fernandes. Structural and functional insights on the electrifying pathways of geobacter sulfurreducens. Unknown journal, 2024.

34. (gupta2024mmcaisan pages 6-7): Dinesh Gupta, Keying Chen, Sean J. Elliott, and Dipti D. Nayak. Mmca is an electron conduit that facilitates both intracellular and extracellular electron transport in methanosarcina acetivorans. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47564-2, doi:10.1038/s41467-024-47564-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

35. (lacroix2023considertheanoxic pages 4-5): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

36. (lacroix2023considertheanoxic pages 5-6): Emily M. Lacroix, Meret Aeppli, Kristin Boye, Eoin Brodie, Scott Fendorf, Marco Keiluweit, Hannah R. Naughton, Vincent Noël, and Debjani Sihi. Consider the anoxic microsite: acknowledging and appreciating spatiotemporal redox heterogeneity in soils and sediments. ACS Earth & Space Chemistry, 7:1592-1609, Aug 2023. URL: https://doi.org/10.1021/acsearthspacechem.3c00032, doi:10.1021/acsearthspacechem.3c00032. This article has 112 citations and is from a peer-reviewed journal.

37. (hamdan2023sedimentmicrobialfuel pages 23-24): Hamdan Z. Hamdan and Darine A. Salam. Sediment microbial fuel cells for bioremediation of pollutants and power generation: a review. Environmental Chemistry Letters, 21:2761-2787, Jul 2023. URL: https://doi.org/10.1007/s10311-023-01625-y, doi:10.1007/s10311-023-01625-y. This article has 42 citations and is from a peer-reviewed journal.

38. (zhuang2024electrontransferin pages 14-15): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

39. (hsu2024isolationandgenomic pages 17-18): David Hsu, Jack R. Flynn, Christopher J. Schuler, Cara M. Santelli, Brandy M. Toner, Daniel R. Bond, and Jeffrey A. Gralnick. Isolation and genomic analysis of “ <i>metallumcola ferriviriculae”</i> mk1, a gram-positive, fe(iii)-reducing bacterium from the soudan underground mine, an iron-rich martian analog site. Applied and Environmental Microbiology, Aug 2024. URL: https://doi.org/10.1128/aem.00044-24, doi:10.1128/aem.00044-24. This article has 9 citations and is from a peer-reviewed journal.