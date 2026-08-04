---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:31:07.624617'
end_time: '2026-08-04T05:42:42.014439'
duration_seconds: 694.39
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
  causal_graph_summary: 'anaerobic_respiration_denitrification: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Anaerobic respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 14 nodes, 10 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000802
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which an organism uses electron acceptors other than oxygen for energy production.
- **Parent traits:** METPO:1000800
- **Synonyms:** Anoxic respiration, Dissimilatory respiration (non-O₂)
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997: N oxides as terminal electron acceptors (Denitrification review supports anaerobic respiration using non-oxygen terminal electron acceptors.)
- **Existing causal graph summary:** anaerobic_respiration_denitrification: 14 nodes, 10 edges

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


# TraitMech Curation Report: Anaerobic Respiration

## 1. Trait record and scope

- **Trait label:** Anaerobic respiration
- **Trait identifier:** **METPO:1000802**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** METPO:1000800
- **Synonyms:** anoxic respiration; dissimilatory respiration (non-O₂)

### Operational definition

Anaerobic respiration is an energy-conserving respiratory process in which electrons from an organic or inorganic donor pass through an electron-transport chain to a terminal electron acceptor other than molecular oxygen. Electron transfer generates a transmembrane electrochemical gradient that drives ATP synthesis. This mechanistic criterion—not merely growth without oxygen—is the recommended defining feature for TraitMech (little2024dietaryandhostderived pages 1-3, bueno2012bacterialadaptationof pages 1-2).

### Boundaries

1. **Versus aerobic respiration:** aerobic respiration terminates electron flow at O₂; anaerobic respiration uses a non-O₂ acceptor. Low oxygen commonly induces anaerobic systems in facultative bacteria, but strict anaerobes need not possess the FNR/Arc regulatory architecture of *Escherichia coli* (price2021bacterialapproachesto pages 11-12, price2021bacterialapproachesto pages 6-8).
2. **Versus fermentation:** fermentation does not require an external terminal acceptor or a respiratory electron-transport chain. In *Desulfovibrio vulgaris*, a recent analysis estimated approximately **1 mol ATP per mol lactate** from fermentation versus **2.5 mol ATP per mol lactate** during sulfate respiration, illustrating the energetic distinction; these yields are organism- and model-specific, not universal constants (marbehan2024combiningmetabolicflux pages 1-2).
3. **Versus anaerobic growth:** anaerobic growth is broader and includes fermentation, disproportionation, acetogenesis and methanogenesis. Do not infer this trait solely from growth under N₂ or low O₂.
4. **Versus denitrification:** denitrification is one subtype, normally reducing nitrate/nitrite through NO and N₂O toward N₂. Nitrate respiration can instead end in nitrite or ammonium (DNRA), so nitrate reduction alone does not establish denitrification (bueno2012bacterialadaptationof pages 1-2).
5. **Assimilatory versus dissimilatory reduction:** assimilatory nitrate or sulfate reduction supplies biomass precursors; respiratory/dissimilatory reduction supports energy conservation. The trait should represent the latter.
6. **Detoxification boundary:** cytosolic detoxification reductases such as ArsC should not automatically be equated with respiratory arsenate reductase Arr. Evidence of growth, membrane electron transport, ATP production or an established respiratory complex is needed.

## 2. Candidate nodes grouped by type

### Trait, processes and pathways

- Anaerobic respiration — **METPO:1000802**; GO candidate **GO:0009061**
- Anaerobic electron-transport chain — GO candidate **GO:0019646**; verify against the project’s GO release
- Ion-motive force/proton gradient; oxidative phosphorylation; ATP synthesis
- Nitrate respiration; denitrification; DNRA
- Fumarate, TMAO and DMSO respiration
- Dissimilatory sulfate/sulfite reduction
- Extracellular Fe(III)/Mn(IV) reduction
- Arsenate, selenate, chlorate/perchlorate and organohalide respiration
- Organic-metabolite respiration in the gut

### Environmental and experimental factors

- Oxygen limitation/anoxia; nitrate, nitrite or other acceptor availability
- Electron-donor availability and donor:acceptor ratio
- Redox potential; pH; salinity; temperature
- Anoxic culture or microcosm; acceptor-dependent growth; ATP assay
- Mutant/complementation assay; reductase activity assay
- Transcriptomics/proteomics; isotope tracing; electrochemical current
- Anaerobic/anoxic reactor stage; poised electrode

### Electron donors and intermediates

- NADH, formate, H₂, lactate, pyruvate, acetate, ethanol, sulfide and reduced organic carbon
- Quinone/quinol pools, including menaquinone and ubiquinone
- Periplasmic or membrane-associated formate dehydrogenases and hydrogenases

Sulfate-reducing microorganisms couple sulfate reduction to oxidation of lactate, pyruvate, formate, ethanol or H₂; in the absence of sulfate, some can instead ferment organic substrates (marbehan2024combiningmetabolicflux pages 1-2).

### Terminal acceptors and products

- Nitrate (**CHEBI:17632**) → nitrite → NO → N₂O → N₂, or nitrite → ammonium
- Fumarate → succinate
- TMAO → trimethylamine; DMSO → dimethyl sulfide
- Sulfate → APS → sulfite → sulfide
- Fe(III) and Mn(IV) minerals → reduced mineral products
- Arsenate → arsenite; selenate → reduced selenium species
- Chlorate/perchlorate → chloride through pathway-specific intermediates
- Urocanate → imidazole propionate; itaconate → 2-methylsuccinate
- Additional cinnamates, flavonoids, dicarboxylates, sulfoxides and amino-acid intermediates

Classical reviews document nitrate, Fe(III), fumarate, DMSO and TMAO as non-O₂ acceptors, and report arsenate respiration across at least 24 prokaryotic species known at that time (stolz2006arsenicandselenium pages 2-3). This taxon count is historical and should not be treated as a current census.

### Genes, proteins and complexes

- **Core energy conservation:** donor dehydrogenases, quinone pool, terminal reductase, proton-/ion-translocating complexes, F-type ATP synthase
- **Nitrate/denitrification:** narGHJI, nap, nir, nor, nos; nitrate/nitrite transporters such as NarK
- **Fumarate:** frdABCD
- **TMAO/DMSO:** torCAD, TorT–TorS–TorR; dmsABC
- **Sulfate:** sat, aprBA, qmoABC, dsrAB, dsrC and dsrMKJOP
- **Extracellular reduction:** multihaem c-type cytochromes, periplasmic and outer-membrane electron conduits
- **Arsenate:** arr respiratory reductase system; keep separate from ars detoxification genes
- **Regulation:** FNR, ArcBA, NarXL, NarQP and taxon-specific systems such as NreABC

Metagenome and metatranscriptome evidence from peatland Acidobacteria associates **sat–aprBA–qmoABC plus dsr genes** with sulfate-respiration potential and shows sulfur-metabolism-gene upregulation in anoxic microcosms. The authors nevertheless warn that the pathway might operate in reverse for sulfur oxidation or disproportionation (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2).

### Cellular locations

- Cytoplasmic/inner membrane
- Cytoplasm-facing and periplasm-facing catalytic sites
- Periplasm
- Outer membrane and cell surface
- Extracellular mineral or electrode interface

In Gram-negative extracellular reducers, c-type cytochromes transfer electrons across the periplasm and outer membrane; outer-membrane cytochromes catalyse the terminal step. This architecture is best established in *Shewanella* and *Geobacter* and must not be generalized to all anaerobic respirers (richter2012dissimilatoryreductionof pages 1-2).

## 3. Candidate causal edges

The table below provides the strongest directly supported edges. Label-only nodes are intentional where a stable identifier was not verified.

| subject | predicate | object | grounding / CURIE | evidence snippet | DOI / date | qualifier |
|---|---|---|---|---|---|---|
| anaerobic electron transport chain | generates | proton gradient across membrane | subject: GO:0019646; object: label-only | "electrons from NADH donors are transferred through electron transport chains, with free energy used to drive proton translocation across membranes, generating electrochemical gradients for ATP synthesis" (bueno2012bacterialadaptationof pages 1-2) | 10.1089/ars.2011.4051 / 2012-04 | broad review; foundational, not trait-specific to one taxon |
| proton gradient across membrane | powers | ATP synthase-dependent ATP production | subject: label-only; object: label-only | "electron transfer creating ion gradients powering ATP synthesis via ATP synthase" (little2024dietaryandhostderived pages 1-3) | 10.1038/s41564-023-01560-2 / 2024-11 | broad definition from recent review/primary article intro |
| low oxygen / anoxia | activates via sensing by | FNR | subject: label-only; object: label-only | "FNR functions as a master regulator that detects low oxygen through iron-sulfur cluster oxidation ([4Fe-4S]2+ to [2Fe-2S]2+ conversion)" (price2021bacterialapproachesto pages 6-8) | 10.1111/mmi.14795 / 2021-08 | strongest for facultative bacteria such as E. coli; regulatory generalization |
| FNR | activates expression of | anaerobic respiration genes for nitrate, nitrite, and fumarate reduction | subject: label-only; object: label-only | "activates genes for nitrate, nitrite, and fumarate reduction under anaerobic conditions" (price2021bacterialapproachesto pages 6-8) | 10.1111/mmi.14795 / 2021-08 | taxon-weighted toward model facultative bacteria |
| nitrate | stimulates sensing by | NarX/NarL two-component system | subject: CHEBI:17632; object: label-only | "The Nar two-component system (NarXL and NarPQ) independently senses nitrate and nitrite... with NarX stimulated by nitrate and NarQ by both nitrate and nitrite" (price2021bacterialapproachesto pages 6-8) | 10.1111/mmi.14795 / 2021-08 | mostly E. coli / enteric paradigm |
| FNR and NarL | co-activate expression of | narGHJI nitrate reductase operon | subject: label-only; object: label-only | "The narGHJI operon encoding nitrate reductase requires both FNR and NarL functions for expression" (unden2021sensingofo2 pages 25-31) | 10.1111/1462-2920.15293 / 2021-11 | strong for nitrate respiration; gene-level edge |
| TMAO | activates | TorSR signaling system | subject: label-only; object: label-only | "TMAO binding to the periplasmic protein TorT stimulates TorS kinase activity and downstream phosphorylation of TorR, activating torCAD machinery" (price2021bacterialapproachesto pages 8-9) | 10.1111/mmi.14795 / 2021-08 | TMAO-specific; enteric-model evidence |
| torCAD machinery | enables | TMAO respiration | subject: label-only; object: label-only | "activating torCAD machinery" (price2021bacterialapproachesto pages 8-9) | 10.1111/mmi.14795 / 2021-08 | inferred mechanistic edge from regulatory activation |
| sulfate respiration pathway | includes | sat + aprBA + qmoABC + dsr genes | subject: label-only; object: label-only | "sulfate respiration (sat, aprBA, qmoABC plus dsr genes)" (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2) | 10.1038/s41396-018-0077-1 / 2018-02 | genome-predicted pathway in Acidobacteria; not direct biochemical proof alone |
| anoxic conditions | upregulates | sulfur-metabolism genes | subject: label-only; object: label-only | "Metatranscriptome analysis demonstrated expression of acidobacterial sulfur-metabolism genes in native peat soil and their upregulation in diverse anoxic microcosms" (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2) | 10.1038/s41396-018-0077-1 / 2018-02 | expression evidence in peat microcosms |
| DsrMKJOP complex | participates in | sulfate respiration bioenergetics | subject: label-only; object: label-only | "This study provided an overall view of the bioenergetic metabolism of sulfate respiration" and mentions "DsrMKJOP" among key complexes (marbehan2024combiningmetabolicflux pages 1-2) | 10.3389/fmicb.2024.1336360 / 2024-02 | organism-specific: Desulfovibrio vulgaris Hildenborough |
| c-type cytochromes | enable respiratory electron transfer to | extracellular Fe(III) / Mn oxides | subject: label-only; object: label-only | "c-type cytochromes as essential electron-transferring proteins that enable respiratory electron transfer from the cytoplasmic membrane through the periplasm and outer membrane in Gram-negative bacteria" (richter2012dissimilatoryreductionof pages 1-2) | 10.1128/AEM.06803-11 / 2012-02 | extracellular respiration; strongest in Shewanella/Geobacter |
| outer membrane cytochromes | catalyze final step of | extracellular anaerobic respiratory chain | subject: label-only; object: label-only | "Outer membrane cytochromes catalyze the final step of respiratory chains" (richter2012dissimilatoryreductionof pages 1-2) | 10.1128/AEM.06803-11 / 2012-02 | Gram-negative extracellular acceptor reducers |
| formate | serves as electron donor for | urocanate respiration | subject: label-only; object: label-only | "these bacteria use formate as an electron donor and urocanate as an organic respiratory electron acceptor" (little2024dietaryandhostderived pages 3-4) | 10.1038/s41564-023-01560-2 / 2024-11 | shown in E. lenta, S. wadsworthensis, H. filiformis |
| urocanate | serves as respiratory electron acceptor in | anaerobic respiration | subject: label-only; object: GO:0009061 | "use formate as an electron donor and urocanate as an organic respiratory electron acceptor" (little2024dietaryandhostderived pages 3-4) | 10.1038/s41564-023-01560-2 / 2024-11 | gut taxa-specific but experimentally demonstrated |
| formate + urocanate respiration | stimulates | ATP synthesis / production | subject: label-only; object: label-only | "urocanate reduction to imidazole propionate coupled to ATP synthesis" (little2024dietaryandhostderived pages 3-4) | 10.1038/s41564-023-01560-2 / 2024-11 | culture experiment in gut bacteria |
| high-reductase gut bacteria genomes | encode | >30 to 103 reductases per genome | subject: label-only; object: label-only | "three distinct clades... encoding >30 reductases per genome (up to 103)" (little2024dietaryandhostderived pages 3-4) | 10.1038/s41564-023-01560-2 / 2024-11 | comparative genomics; supports expanded anaerobic respiratory capacity |
| integrated anaerobic/anoxic/aerobic membrane bioreactor | achieves removal of | sulfate and nitrogen during wastewater treatment | subject: label-only; object: label-only | "the anaerobic reactor eliminated 44.9% of the raw WW sulfate" and the system showed "TN... removal efficiencies of 72.8 ± 5.6" (wimalaweera2024enhancingrubberindustry pages 1-2) | 10.3390/membranes14060130 / 2024-06 | engineered reactor application; mixed-community process, not a single trait edge |
| anaerobic/anoxic reactor conditions | associate with | active denitrification pathway | subject: label-only; object: label-only | "with evidence of an active denitrification pathway in anaerobic/anoxic conditions" (wimalaweera2024enhancingrubberindustry pages 1-2) | 10.3390/membranes14060130 / 2024-06 | engineered wastewater system; community-level inference |


*Table: This table compiles the strongest curation-ready causal edges for METPO:1000802 from the retrieved evidence. It prioritizes mechanistic links, recent experimental findings, and clearly marked qualifiers for taxon specificity or reactor-level inference.*

### Additional candidate triples requiring pathway-specific evidence

These are appropriate as subtype-specific extensions, not universal properties of **METPO:1000802**:

- nitrate reductase — **reduces** → nitrate
- nitrite reductase — **reduces** → nitrite
- fumarate reductase FrdABCD — **reduces** → fumarate
- TorCAD — **reduces** → TMAO
- DmsABC — **reduces** → DMSO
- Sat — **activates** → sulfate to APS
- AprBA — **reduces** → APS to sulfite
- DsrAB/DsrC — **reduces** → sulfite-derived sulfur to sulfide
- ArrAB — **supports respiratory reduction of** → arsenate
- extracellular c-type cytochrome conduit — **transfers electrons to** → extracellular Fe(III)/Mn(IV) mineral

These biochemical triples should be added only with enzyme-specific primary references and taxon context. The retrieved broad reviews support acceptor diversity, but not every detailed enzyme–reaction edge at curation-grade resolution (little2024dietaryandhostderived pages 31-33, stolz2006arsenicandselenium pages 2-3).

## 4. Recent developments, 2023–2024

### Expansion of anaerobic respiration into the gut metabolome

Little and colleagues identified three phylogenetically distinct human-gut bacterial families—Burkholderiaceae, Eggerthellaceae and Erysipelotrichaceae—with unusually large respiratory-reductase inventories. Analysis of **1,533 genomes** found high-reductase organisms encoding more than 30 and as many as **103 reductases per genome**; by comparison, the study counted 22 molybdopterin/flavin reductases in *Shewanella oneidensis* (little2024dietaryandhostderived pages 8-9, little2024dietaryandhostderived pages 3-4).

Experiments with *Sutterella wadsworthensis*, *Eggerthella lenta* and *Holdemania filiformis* identified **22 metabolites** used as species-specific respiratory electron acceptors overall; 19 tested compounds supported growth with evidence including product formation and ATP stimulation. The substrates included dietary and host-derived cinnamates, flavonoids, dicarboxylates, sulfoxides, urocanate, resveratrol and itaconate (little2024dietaryandhostderived pages 1-3, little2024dietaryandhostderived pages 4-6). Formate served as donor for urocanate reduction to imidazole propionate, coupled to ATP production (little2024dietaryandhostderived pages 3-4).

This work materially broadens the trait beyond classical inorganic acceptors. However, it is based on three cultured species, and most predicted gut reductases remain functionally uncharacterized. Substrate assignments should therefore be curated at enzyme/species level only when experimentally validated (little2024dietaryandhostderived pages 9-11).

### Quantitative sulfate-respiration modeling

A 2024 proteomics-plus-flux-balance model for *D. vulgaris* achieved a reported correlation above **0.95** with experimental data and identified the sulfate:lactate consumption ratio as a pivotal bioenergetic variable. The study emphasizes that hydrogen/formate cycling remains mechanistically debated and may coexist with independent membrane electron-transfer routes (marbehan2024combiningmetabolicflux pages 1-2).

### Sulfur–nitrogen wastewater treatment

A 225-day laboratory integrated anaerobic/anoxic/oxic membrane-bioreactor study treating natural-rubber wastewater reported a six-day hydraulic retention time, greater than **98% COD reduction** (22,158 ± 2,859 to 118 ± 74 mg L⁻¹), **72.9 ± 5.7% NH₃-N**, **72.8 ± 5.6% total nitrogen**, and **71.3 ± 9.9% total-phosphorus removal**. The anaerobic reactor removed **44.9% of influent sulfate**, while community analysis indicated Desulfobacterota, sulfide-driven autotrophic denitrification and an active denitrification pathway under anaerobic/anoxic conditions (wimalaweera2024enhancingrubberindustry pages 1-2). These are reactor-level mixed-community results, not direct evidence that one organism or gene causes every removal outcome.

## 5. Current applications and implementations

1. **Wastewater nitrogen removal:** engineered anoxic zones exploit nitrate/nitrite respiration and denitrification. Performance depends on carbon/electron-donor supply, dissolved oxygen, pH, temperature, biomass retention and competition among guilds.
2. **Sulfate-rich industrial wastewater:** sulfate reducers convert sulfate to sulfide, which can facilitate sulfur-driven denitrification but also creates toxicity, odour and corrosion risks. The 2024 rubber-wastewater reactor illustrates combined N/S removal at laboratory scale (wimalaweera2024enhancingrubberindustry pages 1-2).
3. **Bioremediation:** respiratory reduction can transform Fe(III), Mn(IV), arsenate, selenate, chlorate/perchlorate and organohalides, changing solubility or toxicity. Arsenic is a cautionary example: reduction of relatively immobile As(V) to more mobile As(III) can worsen groundwater contamination, whereas nitrate-linked arsenite oxidation may promote immobilization under suitable geochemical conditions (hassan2024arseniccontaminationof pages 11-13).
4. **Microbial fuel cells and biosensors:** electroactive biofilms transfer electrons to external electrodes. Current applications include organic-waste-to-electricity systems, biochemical-oxygen-demand and toxicity sensors; several laboratory models have been commercialized, although electrode materials, mass transfer, biofilm stability and scale-up remain constraints (perchikov2024microbialbiofilmsfeatures pages 1-3).
5. **Host-associated metabolism:** gut respiratory reductases modify dietary compounds and immunometabolites. Itaconate reduction to 2-methylsuccinate and urocanate reduction to imidazole propionate link energy metabolism to host–microbiome chemistry, but clinical causality is not established (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 3-4).

## 6. Expert interpretation for graph design

A single graph containing every known acceptor would become an uninformative union of mutually exclusive pathways. The recommended TraitMech structure is a **shared core plus modular branches**:

1. **Environmental gate:** oxygen limitation and availability of a non-O₂ acceptor.
2. **Regulatory layer:** FNR/ArcBA and acceptor-specific sensors where supported.
3. **Donor oxidation:** donor dehydrogenase supplies electrons to a quinone or equivalent carrier pool.
4. **Terminal branch:** one verified reductase module—Nar, Frd, Tor/Dms, sulfate machinery, Arr, or extracellular cytochrome conduit.
5. **Energy-conservation output:** ion-motive force → ATP synthase → increased ATP/growth.
6. **Assay outputs:** acceptor depletion, reduced-product formation, donor-dependent growth, ATP increase, membrane potential or electrode current.

The existing denitrification graph should therefore be retained as one child/module rather than treated as synonymous with the parent trait.

## 7. Ontology-grounding recommendations

### High-confidence starting points

- Trait: **METPO:1000802**
- Anaerobic respiration: **GO:0009061**
- Anaerobic electron-transport chain: candidate **GO:0019646**, but verify release and exact label
- Nitrate: **CHEBI:17632**

### Ground only after database verification

Verify current ChEBI records for nitrite, fumarate, sulfate, sulfite, TMAO, DMSO, arsenate, selenate, chlorate, perchlorate, urocanate, itaconate, imidazole propionate and 2-methylsuccinate. Similarly, resolve EC/Rhea identifiers separately for Nar, Frd, Tor/Dms, Sat, Apr, Dsr and Arr reactions. Protein-level UniProt identifiers must be strain-specific; gene symbols alone are not globally unique.

For environmental nodes, candidate ENVO concepts include anoxic environment, sediment, wetland, intestinal environment, wastewater and electrode-associated biofilm, but exact CURIEs should be selected from the project’s pinned ENVO release.

## 8. Warnings—claims not yet suitable for curation

- Do not curate **anoxia → anaerobic respiration** as sufficient causation; an acceptor, donor and functional respiratory machinery are also required.
- Do not infer the trait from terminal-reductase homologs alone. Molybdopterin/flavin superfamilies include enzymes with non-respiratory roles.
- Do not infer direction from **dsrAB** or a sulfur-pathway gene set alone; reverse Dsr sulfur oxidation and sulfur disproportionation are important alternatives (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2).
- Do not equate **arsC** detoxification with **arr**-dependent arsenate respiration.
- Do not treat nitrate reduction as synonymous with complete denitrification; DNRA and truncated pathways are alternatives.
- Do not generalize FNR, ArcBA, NarXL/NarQP or TorSR to all taxa. They are strong model-system modules, especially in enteric bacteria (unden2021sensingofo2 pages 25-31, price2021bacterialapproachesto pages 6-8, price2021bacterialapproachesto pages 8-9).
- Do not generalize outer-membrane cytochrome architecture beyond taxa with direct evidence (richter2012dissimilatoryreductionof pages 1-2).
- Do not convert reactor-level associations into gene-level causal edges. The 2024 wastewater results arose from a mixed community in a laboratory reactor (wimalaweera2024enhancingrubberindustry pages 1-2).
- Treat predicted gut reductase substrates as uncertain unless supported by purified-enzyme activity, knockout/complementation, acceptor-dependent ATP or growth, and product identification. Most gut reductases remain uncharacterized (little2024dietaryandhostderived pages 9-11).
- Avoid universal ATP-yield values: the 1 versus 2.5 ATP per lactate comparison is specific to the *D. vulgaris* analysis (marbehan2024combiningmetabolicflux pages 1-2).

## 9. DOI-first bibliography

1. Little AS et al. **Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration.** *Nature Microbiology* 9, 55–69. Published online 2023; volume record reported November 2024. DOI: [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2). (little2024dietaryandhostderived pages 1-3)
2. Marbehan X et al. **Combining metabolic flux analysis with proteomics to shed light on metabolic flexibility: the case of Desulfovibrio vulgaris Hildenborough.** *Frontiers in Microbiology* 15:1336360. Published 23 February 2024. DOI: [10.3389/fmicb.2024.1336360](https://doi.org/10.3389/fmicb.2024.1336360). (marbehan2024combiningmetabolicflux pages 1-2)
3. Wimalaweera IP et al. **Enhancing Rubber Industry Wastewater Treatment through an Integrated AnMBR and A/O MBR System.** *Membranes* 14:130. Published 5 June 2024. DOI: [10.3390/membranes14060130](https://doi.org/10.3390/membranes14060130). (wimalaweera2024enhancingrubberindustry pages 1-2)
4. Perchikov R et al. **Microbial Biofilms: Features of Formation and Potential for Use in Bioelectrochemical Devices.** *Biosensors* 14:302. Published 8 June 2024. DOI: [10.3390/bios14060302](https://doi.org/10.3390/bios14060302). (perchikov2024microbialbiofilmsfeatures pages 1-3)
5. Hassan Z, Westerhoff HV. **Arsenic Contamination of Groundwater Is Determined by Complex Interactions between Various Chemical and Biological Processes.** *Toxics* 12:89. Published January 2024. DOI: [10.3390/toxics12010089](https://doi.org/10.3390/toxics12010089). (hassan2024arseniccontaminationof pages 11-13)
6. Price EE, Román-Rodríguez F, Boyd JM. **Bacterial approaches to sensing and responding to respiration and respiration metabolites.** *Molecular Microbiology* 116:1009–1021. Published August 2021. DOI: [10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795). (price2021bacterialapproachesto pages 11-12)
7. Unden G, Klein R. **Sensing of O₂ and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration.** *Environmental Microbiology* 23:5–14. Published November 2021. DOI: [10.1111/1462-2920.15293](https://doi.org/10.1111/1462-2920.15293). (unden2021sensingofo2 pages 25-31)
8. Hausmann B et al. **Peatland Acidobacteria with a dissimilatory sulfur metabolism.** *ISME Journal* 12:1729–1742. Accepted 20 January 2018. DOI: [10.1038/s41396-018-0077-1](https://doi.org/10.1038/s41396-018-0077-1). (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2)
9. Richter K, Schicklberger M, Gescher J. **Dissimilatory Reduction of Extracellular Electron Acceptors in Anaerobic Respiration.** *Applied and Environmental Microbiology* 78:913–921. Published February 2012. DOI: [10.1128/AEM.06803-11](https://doi.org/10.1128/AEM.06803-11). (richter2012dissimilatoryreductionof pages 1-2)
10. Bueno E et al. **Bacterial adaptation of respiration from oxic to microoxic and anoxic conditions: redox control.** *Antioxidants & Redox Signaling* 16:819–852. Published April 2012. DOI: [10.1089/ars.2011.4051](https://doi.org/10.1089/ars.2011.4051). (bueno2012bacterialadaptationof pages 1-2)
11. Stolz JF et al. **Arsenic and Selenium in Microbial Metabolism.** *Annual Review of Microbiology* 60:107–130. Published October 2006. DOI: [10.1146/annurev.micro.60.080805.142053](https://doi.org/10.1146/annurev.micro.60.080805.142053). (stolz2006arsenicandselenium pages 2-3)

The supplied foundational denitrification review—DOI [10.1128/MMBR.61.4.533-616.1997](https://doi.org/10.1128/MMBR.61.4.533-616.1997)—remains appropriate evidence for the nitrogen-oxide branch, but it should support a denitrification subgraph rather than define the entire anaerobic-respiration trait.

References

1. (little2024dietaryandhostderived pages 1-3): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (bueno2012bacterialadaptationof pages 1-2): Emilio Bueno, Socorro Mesa, Eulogio J. Bedmar, David J. Richardson, and Maria J. Delgado. Bacterial adaptation of respiration from oxic to microoxic and anoxic conditions: redox control. Antioxidants & redox signaling, 16 8:819-52, Apr 2012. URL: https://doi.org/10.1089/ars.2011.4051, doi:10.1089/ars.2011.4051. This article has 252 citations and is from a domain leading peer-reviewed journal.

3. (price2021bacterialapproachesto pages 11-12): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

4. (price2021bacterialapproachesto pages 6-8): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

5. (marbehan2024combiningmetabolicflux pages 1-2): Xavier Marbehan, Magali Roger, Frantz Fournier, Pascale Infossi, Emmanuel Guedon, Louis Delecourt, Régine Lebrun, Marie-Thérèse Giudici-Orticoni, and Stéphane Delaunay. Combining metabolic flux analysis with proteomics to shed light on the metabolic flexibility: the case of desulfovibrio vulgaris hildenborough. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1336360, doi:10.3389/fmicb.2024.1336360. This article has 7 citations and is from a peer-reviewed journal.

6. (stolz2006arsenicandselenium pages 2-3): John F. Stolz, Partha Basu, Joanne M. Santini, and Ronald S. Oremland. Arsenic and selenium in microbial metabolism. Annual Review of Microbiology, 60(1):107-130, Oct 2006. URL: https://doi.org/10.1146/annurev.micro.60.080805.142053, doi:10.1146/annurev.micro.60.080805.142053. This article has 563 citations and is from a peer-reviewed journal.

7. (hausmann2018peatlandacidobacteriawithadissimilatory pages 1-2): Bela Hausmann, Claus Pelikan, Craig W Herbold, Stephan Köstlbacher, Mads Albertsen, Stephanie A Eichorst, Tijana Glavina del Rio, Martin Huemer, Per H Nielsen, Thomas Rattei, Ulrich Stingl, Susannah G Tringe, Daniela Trojan, Cecilia Wentrup, Dagmar Woebken, Michael Pester, and Alexander Loy. Peatland<i>acidobacteria</i>with a dissimilatory sulfur metabolism. The ISME Journal, 12:1729-1742, Feb 2018. URL: https://doi.org/10.1038/s41396-018-0077-1, doi:10.1038/s41396-018-0077-1. This article has 191 citations.

8. (richter2012dissimilatoryreductionof pages 1-2): Katrin Richter, Marcus Schicklberger, and Johannes Gescher. Dissimilatory reduction of extracellular electron acceptors in anaerobic respiration. Applied and Environmental Microbiology, 78:913-921, Feb 2012. URL: https://doi.org/10.1128/aem.06803-11, doi:10.1128/aem.06803-11. This article has 356 citations and is from a peer-reviewed journal.

9. (unden2021sensingofo2 pages 25-31): Gottfried Unden and Robin Klein. Sensing of <scp>o<sub>2</sub></scp> and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration by <scp>o<sub>2</sub></scp> and nitrate. Nov 2021. URL: https://doi.org/10.1111/1462-2920.15293, doi:10.1111/1462-2920.15293. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (price2021bacterialapproachesto pages 8-9): Erin E. Price, Franklin Román‐Rodríguez, and Jeffrey M. Boyd. Bacterial approaches to sensing and responding to respiration and respiration metabolites. Molecular Microbiology, 116:1009-1021, Aug 2021. URL: https://doi.org/10.1111/mmi.14795, doi:10.1111/mmi.14795. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (little2024dietaryandhostderived pages 3-4): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

12. (wimalaweera2024enhancingrubberindustry pages 1-2): Ishanka Prabhath Wimalaweera, Yuansong Wei, Fumin Zuo, Qihe Tang, Tharindu Ritigala, Yawei Wang, Hui Zhong, Rohan Weerasooriya, Shameen Jinadasa, and Sujithra Weragoda. Enhancing rubber industry wastewater treatment through an integrated anmbr and a/o mbr system: performance, membrane fouling analysis, and microbial community evolution. Membranes, 14:130, Jun 2024. URL: https://doi.org/10.3390/membranes14060130, doi:10.3390/membranes14060130. This article has 21 citations.

13. (little2024dietaryandhostderived pages 31-33): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

14. (little2024dietaryandhostderived pages 8-9): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

15. (little2024dietaryandhostderived pages 4-6): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

16. (little2024dietaryandhostderived pages 9-11): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

17. (hassan2024arseniccontaminationof pages 11-13): Zahid Hassan and Hans V. Westerhoff. Arsenic contamination of groundwater is determined by complex interactions between various chemical and biological processes. Toxics, 12:89, Jan 2024. URL: https://doi.org/10.3390/toxics12010089, doi:10.3390/toxics12010089. This article has 18 citations.

18. (perchikov2024microbialbiofilmsfeatures pages 1-3): Roman Perchikov, Maxim Cheliukanov, Yulia Plekhanova, Sergei Tarasov, Anna Kharkova, Denis Butusov, Vyacheslav Arlyapov, Hideaki Nakamura, and Anatoly Reshetilov. Microbial biofilms: features of formation and potential for use in bioelectrochemical devices. Biosensors, 14:302, Jun 2024. URL: https://doi.org/10.3390/bios14060302, doi:10.3390/bios14060302. This article has 51 citations.