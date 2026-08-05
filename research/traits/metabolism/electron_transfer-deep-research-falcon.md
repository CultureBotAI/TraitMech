---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:07:43.980205'
end_time: '2026-08-04T06:25:15.012543'
duration_seconds: 1051.03
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Electron transfer
  trait_identifier: METPO:1000805
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: electron_transfer
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which electrons are transferred from an electron donor
    to an electron acceptor.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review
    supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93:
    c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer
    mechanisms.)'
  causal_graph_summary: 'electron_transfer_redox_carriers: 17 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Electron transfer
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 17 nodes, 13 edges

## Research Objective

Research the microbial trait **Electron transfer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/electron_transfer.yaml`.

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
- **Trait label:** Electron transfer
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 17 nodes, 13 edges

## Research Objective

Research the microbial trait **Electron transfer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/electron_transfer.yaml`.

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


# Curation-focused research report: microbial electron transfer

## Trait record and scope

- **Trait label:** Electron transfer
- **Trait identifier:** **“METPO:1000805”**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Definition:** “A metabolism in which electrons are transferred from an electron donor to an electron acceptor.”
- **Parent:** METPO:1000060

### Recommended interpretation

This trait should represent the **physiological capacity for organized donor-to-acceptor electron flow**, not every isolated oxidation–reduction reaction. Its central causal pattern is:

**electron-donor oxidation → reduced carrier(s) → redox enzyme/chain → electron acceptor reduction**, sometimes coupled to proton- or sodium-motive force and ATP synthesis. Multiheme cytochromes, quinones, flavins, iron–sulfur proteins, NAD(P)H, ferredoxin, and electrodes can serve as intermediate carriers or interfaces. Authoritative reviews describe respiratory electrons moving successively between redox centers, with released energy generating proton motive force and ultimately driving ATP synthase. (edwards2020roleofmultiheme pages 1-2)

**In scope:** aerobic and anaerobic respiratory electron-transfer chains; photosynthetic chains; extracellular electron transfer (EET) to or from minerals, humic substances, electrodes, or cells; direct interspecies electron transfer (DIET); and electron bifurcation when donor-to-two-acceptor flow is explicitly demonstrated.

**Not synonymous with the trait:** respiration, oxidative phosphorylation, EET, DIET, fermentation, metal reduction, or electricity production. These are narrower pathways, outcomes, or assays. Fermentation can include internal redox balancing without an external terminal acceptor. IET through diffusible H₂ or formate is not DIET. Electron bifurcation is a specialized energy-coupling mechanism in which a two-electron donor supplies high- and low-potential one-electron acceptors; flavin-based systems are chiefly found in strict anaerobes and can generate reduced ferredoxin/flavodoxin for difficult reductions or ion-gradient formation. (buckel2018flavinbasedelectronbifurcation pages 1-2)

### Assay interpretation

A positive phenotype may be observed as growth coupled to donor/acceptor pairs, acceptor reduction, donor oxidation, current production or consumption, cyclic voltammetry, redox spectroscopy, membrane-potential formation, or genetic dependence. Current alone is insufficient unless biological electron flow is separated from abiotic electrochemistry. Likewise, a redox-enzyme annotation alone should not establish the organism-level trait.

## Candidate graph architecture

A robust graph should use a conserved core and attach taxon-specific modules:

1. **Core intracellular module:** donor oxidation → NADH/NADPH, ferredoxin/flavodoxin, or electron-transfer flavoprotein → membrane quinone/quinol pool.
2. **Energy-conserving membrane module:** quinol/dehydrogenase or respiratory complex → proton or sodium motive force → ATP synthase.
3. **Terminal-acceptor module:** quinol/cytochrome/ferredoxin → terminal oxidase or reductase → O₂, fumarate, nitrate, sulfate-related intermediates, Fe(III), or another acceptor.
4. **Gram-negative EET module:** inner membrane quinone pool → CymA/CbcL/ImcH → periplasmic cytochromes → porin–cytochrome or nanowire pathway → mineral/electrode/cell.
5. **Mediator module:** intracellular chain → secreted flavin/phenazine or environmental humic shuttle → extracellular acceptor.
6. **DIET module:** donor organism → conductive protein/material interface → recipient organism → recipient terminal reduction.

## Candidate nodes grouped by type

### Trait and biological-process nodes

- Electron transfer — **“METPO:1000805”**
- Electron transport chain — **GO:0022900**
- Respiratory electron transport chain — **GO:0022904**
- Aerobic respiration — **GO:0009060**
- Anaerobic respiration — **GO:0009061**
- Oxidative phosphorylation — **GO:0006119**
- Proton motive force — label plus **GO:0015988** where represented as proton-coupled ATP synthesis
- Extracellular electron transfer — label-only candidate; verify an appropriate METPO/GO term before release
- Direct interspecies electron transfer — label-only candidate
- Flavin-based electron bifurcation — label-only candidate
- Biofilm formation — **GO:0042710**

### Chemicals, donors, acceptors, and cofactors

- NADH — **CHEBI:16908**
- NAD⁺ — **CHEBI:15846**
- NADPH — **CHEBI:16474**
- Molecular oxygen — **CHEBI:15379**
- Water — **CHEBI:15377**
- Proton — **CHEBI:15378**
- Fumarate — **CHEBI:18012**
- Succinate — **CHEBI:30031**
- Acetate — **CHEBI:30089**
- Ethanol — **CHEBI:16236**
- Carbon dioxide — **CHEBI:16526**
- Methane — **CHEBI:16183**
- Ubiquinone / ubiquinol — **CHEBI:16389 / CHEBI:17976**
- Menaquinone — **CHEBI:16374**
- Flavin adenine dinucleotide — **CHEBI:16238**
- Flavin mononucleotide — **CHEBI:17621**
- Heme — **CHEBI:30413**
- Iron–sulfur cluster — label-only unless the exact cluster is specified
- Ferric iron — **CHEBI:29034**
- Ferrous iron — **CHEBI:29033**
- Ferrihydrite, Fe(III) oxide mineral, electrode, humic substance, biochar, graphene, and Fe₃O₄@biochar — retain as label-only/material nodes until the exact chemical or environment class is verified.

### Proteins, genes, and complexes

**General respiratory machinery:** NADH:quinone oxidoreductase/Complex I; Na⁺-pumping NADH:quinone oxidoreductase; succinate dehydrogenase/fumarate reductase; cytochrome bc₁; alternative complex III; cytochrome c oxidase; cytochrome bd; ATP synthase; Rnf; Ech; NfnAB; EtfAB-containing bifurcating complexes.

**Membrane EET entry/exit:** CymA, CbcL, MtrH/MtoC, and ImcH. A comparative genomic study identified these as multiheme c-type cytochrome families that recycle the membrane quinone/quinol pool; CbcL/MtrH/MtoC homologs occurred in 15 phyla and ImcH homologs in 12, whereas CymA was restricted largely to proteobacterial, especially *Shewanella*, genomes. These distribution-to-function relations remain genomic inference rather than universal biochemical proof. (zhong2018genomicanalysesof pages 1-2)

**Envelope and extracellular conduits:** MtrCAB, OmcA, PpcA–PpcE, OmaB/OmbB/OmcB, OmcS, OmcZ, OmcE, OmcT, PilA-N/PilA-C, and OzpA. Multiheme c-type cytochromes can store multiple electrons and form networks from the cytoplasmic membrane to extracellular acceptors. (edwards2020roleofmultiheme pages 1-2)

**Mediator-associated nodes:** riboflavin, flavin mononucleotide, phenazines, and putative quinol-like mediators; these require species-specific evidence.

### Cellular and environmental locations

- Cytoplasm — **GO:0005737**
- Plasma/cytoplasmic membrane — **GO:0005886**
- Periplasmic space — **GO:0042597**
- Cell outer membrane — **GO:0009279**
- Cell surface — **GO:0009986**
- Extracellular region — **GO:0005576**
- Biofilm matrix, biofilm–electrode interface, mineral surface, sediment, soil, anaerobic digester, and microbial electrochemical reactor — label-only candidates pending exact ENVO grounding.

### Taxon nodes

Use verified NCBITaxon accessions at strain level during YAML implementation. Principal labels are *Geobacter sulfurreducens*, *Geobacter metallireducens*, *Shewanella oneidensis* MR-1, *Pseudomonas aeruginosa*, *Listeria monocytogenes*, *Enterococcus faecalis*, and electroactive methanogenic/anaerobic communities. Do not generalize mechanisms observed in these models to “Bacteria” without broader evidence.

## Candidate causal edges

The following table is the compact high-confidence set. “Direct experimental” is preferred for curation; review-supported edges are suitable as conserved scaffold relations; genomic inference should be marked uncertain.

| subject | predicate | object | system/taxon | confidence | DOI |
|---|---|---|---|---|---|
| Catabolic electron donor oxidation / NADH | reduces | quinone pool | bacterial respiratory/EET chains | review-supported | 10.1146/annurev-biochem-052621-092202 (burton2025electrontransportacross pages 3-4) |
| Quinol dehydrogenase activity | contributes to generation of | proton gradient / proton motive force | bacterial inner membrane during EET | review-supported | 10.1146/annurev-biochem-052621-092202 (burton2025electrontransportacross pages 3-4) |
| Cytochrome bd | oxidizes | quinol and reduces O2 to H2O | diverse bacteria | review-supported | 10.1089/ars.2020.8039 (borisov2021bacterialoxidasesof pages 1-2) |
| Cytochrome bd activity | supports | proton motive force generation | bacterial respiratory chain | review-supported | 10.1089/ars.2020.8039 (borisov2021bacterialoxidasesof pages 1-2) |
| CymA family cytochromes | recycle | quinone/quinol pool during EET | Shewanella and other Proteobacteria | genomic/review inference | 10.3389/fmicb.2018.03029 (zhong2018genomicanalysesof pages 1-2) |
| CbcL/MtrH/MtoC family cytochromes | recycle | quinone/quinol pool during EET | Geobacter and diverse bacteria | genomic/review inference | 10.3389/fmicb.2018.03029 (zhong2018genomicanalysesof pages 1-2) |
| ImcH family cytochromes | oxidize | quinol pool during EET | Fe(III)-reducing bacteria | genomic/review inference | 10.3389/fmicb.2018.03029 (zhong2018genomicanalysesof pages 1-2) |
| MtrCAB complex | mediates electron transfer across | outer membrane to extracellular acceptors | Shewanella | review-supported | 10.1080/10643389.2020.1773728 (xie2021themechanismand pages 12-14), 10.1146/annurev-biochem-052621-092202 (burton2025electrontransportacross pages 3-4) |
| PpcA-E periplasmic cytochromes | inject electrons into | OmcS nanowires | Geobacter sulfurreducens | direct experimental | 10.1038/s41467-024-46192-0 (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9) |
| OzpA serine protease | cleaves | OmcZ50 to OmcZ30 | Geobacter sulfurreducens | direct experimental | 10.1038/s41564-022-01315-5 (gu2023structureofgeobacter pages 6-8) |
| OzpA-mediated OmcZ cleavage | enables assembly of | OmcZ nanowires | Geobacter sulfurreducens | direct experimental | 10.1038/s41564-022-01315-5 (gu2023structureofgeobacter pages 6-8) |
| Closely stacked OmcZ hemes | enable | high conductivity / long-range electron transport | Geobacter OmcZ nanowires | direct experimental | 10.1038/s41564-022-01315-5 (gu2023structureofgeobacter pages 1-2, gu2023structureofgeobacter pages 29-30) |
| omcZ deletion | impairs | anode reduction / current-producing biofilms | Geobacter sulfurreducens | direct experimental | 10.3389/fmicb.2023.1251346 (jiang2023thevariedroles pages 1-2, jiang2023thevariedroles pages 5-8) |
| pilA-N deletion | impairs | ferrihydrite reduction, anode reduction, and co-culture/DIET | Geobacter sulfurreducens | direct experimental | 10.3389/fmicb.2023.1251346 (jiang2023thevariedroles pages 1-2, jiang2023thevariedroles pages 5-8) |
| omcS deletion | diminishes | ferrihydrite reduction and early-stage anode reduction | Geobacter sulfurreducens | direct experimental | 10.3389/fmicb.2023.1251346 (jiang2023thevariedroles pages 1-2, jiang2023thevariedroles pages 5-8) |
| Triple deletion omcS omcT omcZ | abolishes | co-culture with G. metallireducens | Geobacter sulfurreducens | direct experimental | 10.3389/fmicb.2023.1251346 (jiang2023thevariedroles pages 1-2) |
| Biochar amendment (20 g/L) | increases | methane yield by 42.8% vs control | anaerobic digestion of pretreated sludge | direct experimental, application-specific | 10.3389/fceng.2024.1419770 (almegbl2024biogasenhancementin pages 1-2) |
| Graphene amendment (100 mg/L) | increases | methane yield by 24.8% vs control | anaerobic digestion of pretreated sludge | direct experimental, application-specific | 10.3389/fceng.2024.1419770 (almegbl2024biogasenhancementin pages 1-2) |
| Fe3O4@biochar amendment (200 mg/L) | promotes | DIET-associated methanogenesis and raises biogas production to 0.658 L/g VS at OLR 3.715 g(VS)/L·d | anaerobic digestion of vegetable waste | direct experimental, application-specific | 10.3390/fermentation10120656 (ma2024synergisticpromotionof pages 1-2) |


*Table: This table summarizes the strongest curation-ready causal triples for METPO:1000805, spanning core respiratory electron flow, extracellular electron transfer machinery, and application-specific DIET enhancements. It distinguishes direct experimental evidence from review- or genomics-based inference to support cautious TraitMech curation.*

### Evidence snippets and curation notes

| Proposed triple | Supporting source snippet | Curation note |
|---|---|---|
| Catabolic electron oxidation **reduces** membrane quinones through NADH-linked transfer | “electrons from cytoplasmic catabolic reactions are transferred via electron shuttles like NADH to quinones in the cytoplasmic membrane” | Good core scaffold, but the exact donor/dehydrogenase varies by organism. Review evidence; do not assert NADH dependence universally. (burton2025electrontransportacross pages 3-4) |
| Quinol reoxidation **contributes to** proton-gradient generation | Quinol dehydrogenases “abstract both protons and electrons from the inner-membrane quinone pool into the periplasm, generating a proton gradient” | Curate as a qualified energy-coupling edge, not as a universal consequence of every electron-transfer reaction. (burton2025electrontransportacross pages 3-4) |
| Cytochrome bd **uses quinol to reduce** O₂ to H₂O | Cytochrome bd is a “ubiquinol:oxygen oxidoreductase” whose role couples O₂ reduction “to water with the generation of a proton motive force” | Strong respiratory example. Note that bd does not pump protons directly; scalar chemistry/charge separation produces PMF. (borisov2021bacterialoxidasesof pages 1-2) |
| CymA/CbcL/ImcH **recycle** the quinone/quinol pool during EET | These proteins are “quinol oxidases and/or quinone reductases…where they recycle the quinone/quinol pool” | Retain family and direction qualifiers. ImcH’s quinol-oxidase-only assignment was inferred from occurrence in Fe(III)-reducers. (zhong2018genomicanalysesof pages 1-2) |
| MtrCAB **transfers electrons across** the outer membrane | The Mtr pathway physically connects the membrane chain to extracellular acceptors; deletion of the *mtr* operon identified the *Shewanella* conduit | Strong for *Shewanella*; direction can reverse in some uptake contexts, so encode direction with assay conditions. (burton2025electrontransportacross pages 3-4, shaw2025independentlyevolvedextracellular pages 1-2) |
| PpcA–E **inject electrons into** OmcS nanowires | “PpcABCDE inject electrons directly into OmcS nanowires by binding transiently”; PpcC had the highest efficiency | High-priority 2024 edge. Direct spectroscopy/electrochemistry in *G. sulfurreducens*. (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9) |
| OmcS **transfers electrons to** extracellular Fe(III) oxide | The model states PpcA–E donate to OmcS nanowires, “transporting electrons to extracellular acceptors such as Fe(III) oxide” | Strong but specific to long-range *Geobacter* EET. OmcS midpoint was −130 mV versus SHE, 82 mV above an earlier value. (portela2024widespreadextracellularelectron pages 7-9) |
| OzpA cleavage of OmcZ50 **enables** OmcZ30 nanowire assembly | Purified OzpA cleaved OmcZ50 into OmcZ30, “which then self-assembled into nanowires” | Excellent biochemical causal edge. OzpA acts as a molecular assembly switch. (gu2023structureofgeobacter pages 6-8) |
| Closely stacked OmcZ hemes **enable** high-conductivity long-range EET | Cryo-EM revealed “linear and closely stacked haems that may account for conductivity”; conductivity exceeded 30 S cm⁻¹ and OmcZ supports transport beyond 10 μm | Curate “enables/supports,” not a precisely quantified elementary rate law. (gu2023structureofgeobacter pages 1-2) |
| *omcZ* deletion **impairs** anode reduction/current production | Deletion of *omcZ* impaired ferrihydrite and anode reduction and co-culture; prior results reported severely diminished electricity production | Strong but substrate- and strain-dependent. (jiang2023thevariedroles pages 5-8, jiang2023thevariedroles pages 1-2) |
| *omcS* deletion **diminishes** ferrihydrite and early anode reduction | The mutant showed diminished ferrihydrite reduction; anode voltage was trivial for the first 60 h but recovered and plateaued after about 85 h | Encode temporal/assay qualification; do not curate *omcS* as universally essential for anode respiration. (jiang2023thevariedroles pages 5-8, jiang2023thevariedroles pages 1-2) |
| *pilA-N* deletion **impairs** ferrihydrite reduction, anode reduction, and DIET | Single deletion impaired all three tested EET contexts; however, recent structures indicate PilA-N/PilA-C filaments are secretion-associated and nonconductive rather than the conductive nanowire itself | Curate PilA-N as required for secretion/assembly-dependent EET, not automatically as the electron-conducting filament. (jiang2023thevariedroles pages 1-2) |
| *omcS omcT omcZ* triple deletion **abolishes** syntrophic co-culture | Triple deletion abolished *G. sulfurreducens* co-culture with *G. metallireducens* | DIET interpretation requires controlling H₂ transfer. The paper explicitly warns that H₂-mediated transfer can mask cytochrome contributions. (jiang2023thevariedroles pages 5-8, jiang2023thevariedroles pages 1-2) |
| Conductive carbon amendment **increases** methane production in sludge digestion | At 20 g L⁻¹ biochar and 100 mg L⁻¹ graphene, methane yields were 183.6 and 153.8 mL gVS⁻¹—42.8% and 24.8% above control | Application edge only. Conductivity and community shifts support DIET, but methane increase does not independently prove DIET. (almegbl2024biogasenhancementin pages 1-2) |
| Fe₃O₄@biochar **promotes** methanogenic performance | At 200 mg L⁻¹ and OLR 3.715 g(VS) L⁻¹ d⁻¹, biogas production reached 0.658 L g(VS)⁻¹ with reduced VFA accumulation | Treat “promotes DIET” as uncertain unless direct electrical or partner-specific evidence is available; performance is firmly supported. (ma2024synergisticpromotionof pages 1-2) |

## Recent developments, 2023–2024

### OmcZ structure and regulated nanowire biogenesis — 2023

A 3.5 Å cryo-EM structure showed a linear, closely packed heme chain in OmcZ. OmcZ nanowires conduct at **>30 S cm⁻¹**, are required for high-current biofilms involving **>10 μm** transport, and occur near the biofilm–electrode interface. The same work established that OzpA cleavage converts soluble OmcZ50 into polymerizing OmcZ30. These findings replace a generic “conductive pili” model with a regulated cytochrome-filament mechanism for this system. Publication: February 2023; DOI URL: https://doi.org/10.1038/s41564-022-01315-5. (gu2023structureofgeobacter pages 6-8, gu2023structureofgeobacter pages 1-2)

### Substrate-specific redundancy in *Geobacter* EET — 2023

Systematic deletion of *pilA-N, omcE, omcS, omcT,* and *omcZ* demonstrated that no single label captures all EET contexts. *omcE* contributed strongly to ferrihydrite reduction but little to anode reduction or co-culture; *omcS* was important for ferrihydrite and early anode reduction; *omcT, omcZ,* and *pilA-N* affected ferrihydrite, anodes, and co-culture. Deleting all tested genes abolished ferrihydrite and anode reduction. Publication: 10 October 2023; DOI URL: https://doi.org/10.3389/fmicb.2023.1251346. (jiang2023thevariedroles pages 5-8, jiang2023thevariedroles pages 1-2)

### Direct charging of OmcS nanowires — 2024

Portela and colleagues showed that PpcA–E transiently bind OmcS and directly inject electrons. PpcC, although least abundant, was most efficient. The work reconciled whole-pathway fluxes above **10⁶ electrons s⁻¹** with slower periplasmic diffusion below **10⁵ s⁻¹**, reported ultrafast transfer below **200 fs**, and measured a physiological OmcS midpoint potential of **−130 mV versus SHE**, 82 mV more positive than previously reported. Publication: March 2024; DOI URL: https://doi.org/10.1038/s41467-024-46192-0. (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9)

### Engineering and applications — 2024

Current implementations include microbial fuel cells for wastewater-to-electricity conversion, microbial electrolysis cells for hydrogen production, microbial electrosynthesis for CO₂ conversion, biosensors, metal and contaminant bioremediation, corrosion studies, and conductive-protein bioelectronics. A 2024 review identified low microbe–electrode interfacial transfer as a major commercialization bottleneck and surveyed heteroatom-doped carbon, metals, oxides, sulfides, carbides, and nitrides. It retrieved **422 publications from 2010 to mid-2024**, indicating rapid growth but not equivalent technological maturity. Publication: 1 August 2024; DOI URL: https://doi.org/10.3390/app14156733. (wang2024electrocatalyticnanomaterialsimprove pages 1-2)

Recent digestion studies illustrate real-world promise but also evidential limits. Biochar increased methane yield by 42.8% and graphene by 24.8% in pretreated waste-sludge batch assays; the authors called for pilot-scale, life-cycle, and techno-economic evaluation. (almegbl2024biogasenhancementin pages 1-2) Fe₃O₄@biochar at 200 mg L⁻¹ supported 0.658 L biogas gVS⁻¹ in vegetable-waste reactors at the maximum tested loading, while changing community composition. (ma2024synergisticpromotionof pages 1-2)

## Expert analysis for TraitMech

1. **Use a modular graph, not one universal linear chain.** Bacterial respiratory architectures are branched, and EET components are functionally redundant. The same cytochrome can be essential for one acceptor and dispensable for another.
2. **Separate molecular function from organismal phenotype.** “Quinol oxidase activity” is a molecular edge; “growth by Fe(III) respiration” and “current production” are phenotype/assay outcomes.
3. **Represent direction explicitly.** CymA/Mtr-like systems can support outward electron disposal or inward electron uptake depending on donor, acceptor, and potential. Do not encode an irreversible generic direction from homology alone.
4. **Treat PilA cautiously.** In *G. sulfurreducens*, current evidence favors a secretion/assembly role for PilA-N/PilA-C in OmcS/OmcZ deployment rather than assuming the pilus itself is the conductive wire. (jiang2023thevariedroles pages 1-2)
5. **Keep DIET distinct from conductive-material enhancement.** Increased methane, abundance of *Geobacter*, or addition of conductive particles is suggestive but not direct proof of cell-to-cell electron transfer.
6. **Use negative and recovery phenotypes.** The delayed recovery of Δ*omcS* on anodes is evidence for alternative routes and should prevent an overstrong “necessary for all EET” edge. (jiang2023thevariedroles pages 5-8)

## Claims that should not yet be curated as general TraitMech edges

- **“All microbes with *mtrCAB*, *omcZ*, or multiheme cytochrome homologs perform EET.”** Genomic presence does not prove expression, heme loading, localization, or phenotype.
- **“CymA/CbcL catalyzes both directions in every organism.”** Bidirectionality is partly inferred from taxonomic occurrence in Fe(III)-reducers and Fe(II)-oxidizers. (zhong2018genomicanalysesof pages 1-2)
- **“PilA is universally a conductive nanowire.”** Structural evidence in *G. sulfurreducens* instead supports secretion-associated, nonconductive PilA-N/PilA-C filaments. (jiang2023thevariedroles pages 1-2)
- **“OmcZ-like genes in methanogenic or methanotrophic archaea regulate methane flux.”** Homology, expression, and structural predictions are intriguing, but direct knockout or biochemical transfer evidence is lacking. (gu2023structureofgeobacter pages 6-8)
- **“Biochar, graphene, or magnetite increases methane specifically by DIET.”** Adsorption, buffering, trace-metal supply, altered community structure, and other mechanisms can confound the inference. (almegbl2024biogasenhancementin pages 1-2, ma2024synergisticpromotionof pages 1-2)
- **“A measured current proves microbial electron transfer.”** Abiotic electrochemistry, soluble metabolites, hydrogen cycling, and electrode reactions require controls.
- **“Electron transfer always conserves energy through PMF.”** Some redox reactions support detoxification, redox balancing, biosynthesis, or futile electron leakage; energy coupling must be demonstrated.
- **The 2025 Desulfobacterota expansion should not be treated as a 2023–2024 result.** It is useful prospective evidence: one organism co-expressed Mtr, Omc, and Pcc pathways, cytochromes with up to 86 heme motifs were reported, and more than 40 Desulfobacterota species encoded relevant pathways, but these are post-priority-period findings and some functional assignments remain expression/model based. (shaw2025independentlyevolvedextracellular pages 12-14, shaw2025independentlyevolvedextracellular pages 1-2, shaw2025independentlyevolvedextracellular pages 14-15)

## DOI-first bibliography

1. Portela PC et al. “Widespread extracellular electron transfer pathways for charging microbial cytochrome OmcS nanowires via periplasmic cytochromes PpcABCDE.” *Nature Communications* 15, 2434. **Published March 2024.** https://doi.org/10.1038/s41467-024-46192-0. (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9)
2. Jiang J et al. “The varied roles of pilA-N, omcE, omcS, omcT, and omcZ in extracellular electron transfer by *Geobacter sulfurreducens*.” *Frontiers in Microbiology* 14. **Published 10 October 2023.** https://doi.org/10.3389/fmicb.2023.1251346. (jiang2023thevariedroles pages 5-8, jiang2023thevariedroles pages 1-2)
3. Gu Y et al. “Structure of *Geobacter* cytochrome OmcZ identifies mechanism of nanowire assembly and conductivity.” *Nature Microbiology* 8:284–298. **Published February 2023.** https://doi.org/10.1038/s41564-022-01315-5. (gu2023structureofgeobacter pages 29-30, gu2023structureofgeobacter pages 6-8, gu2023structureofgeobacter pages 1-2)
4. Wang X, Li X, Zhu Q. “Electrocatalytic Nanomaterials Improve Microbial Extracellular Electron Transfer: A Review.” *Applied Sciences* 14:6733. **Published 1 August 2024.** https://doi.org/10.3390/app14156733. (wang2024electrocatalyticnanomaterialsimprove pages 1-2)
5. Almegbl AM, Munshi FMA, Khursheed A. “Biogas enhancement…by stimulating direct interspecies electron transfer by biochar and graphene.” *Frontiers in Chemical Engineering* 6. **Published 18 June 2024.** https://doi.org/10.3389/fceng.2024.1419770. (almegbl2024biogasenhancementin pages 1-2)
6. Ma H et al. “Synergistic Promotion of Direct Interspecies Electron Transfer by Biochar and Fe₃O₄ Nanoparticles…” *Fermentation* 10:656. **Published 18 December 2024.** https://doi.org/10.3390/fermentation10120656. (ma2024synergisticpromotionof pages 1-2)
7. Borisov VB et al. “Bacterial Oxidases of the Cytochrome bd Family.” *Antioxidants & Redox Signaling* 34:1280–1318. **Published 2021.** https://doi.org/10.1089/ars.2020.8039. (borisov2021bacterialoxidasesof pages 1-2)
8. Edwards MJ et al. “Role of multiheme cytochromes involved in extracellular anaerobic respiration in bacteria.” *Protein Science* 29:830–842. **Published 2020.** https://doi.org/10.1002/pro.3787. (edwards2020roleofmultiheme pages 1-2)
9. Zhong Y, Shi L. “Genomic Analyses of the Quinol Oxidases and/or Quinone Reductases Involved in Bacterial Extracellular Electron Transfer.” *Frontiers in Microbiology* 9:3029. **Published 10 December 2018.** https://doi.org/10.3389/fmicb.2018.03029. (zhong2018genomicanalysesof pages 1-2)
10. Buckel W, Thauer RK. “Flavin-Based Electron Bifurcation, A New Mechanism of Biological Energy Coupling.” *Chemical Reviews* 118:3862–3886. **Published 21 March 2018.** https://doi.org/10.1021/acs.chemrev.7b00707. (buckel2018flavinbasedelectronbifurcation pages 1-2)
11. Shi L et al. “Extracellular electron transfer mechanisms between microorganisms and minerals.” *Nature Reviews Microbiology* 14:651–662. **Published August 2016.** https://doi.org/10.1038/nrmicro.2016.93.
12. Xie Q et al. “The mechanism and application of bidirectional extracellular electron transport in the field of energy and environment.” *Critical Reviews in Environmental Science and Technology* 51:1924–1969. **Published 2021.** https://doi.org/10.1080/10643389.2020.1773728. (xie2021themechanismand pages 12-14)

### Bottom-line curation recommendation

Expand the existing 17-node/13-edge graph first with the **high-confidence PpcA–E → OmcS**, **OzpA cleavage → OmcZ assembly**, **OmcZ stacked-heme → long-range EET**, and substrate-qualified deletion edges. Preserve the current redox-carrier core, but annotate taxon, compartment, donor, acceptor, electrode potential, and assay wherever possible. Add conductive-material/DIET application edges only in an explicitly experimental subgraph marked **assay-specific/uncertain mechanism**, rather than as universal determinants of **“METPO:1000805.”**

References

1. (edwards2020roleofmultiheme pages 1-2): Marcus J. Edwards, David J. Richardson, Catarina M. Paquete, and Thomas A. Clarke. Role of multiheme cytochromes involved in extracellular anaerobic respiration in bacteria. Protein Science, 29:830-842, Nov 2020. URL: https://doi.org/10.1002/pro.3787, doi:10.1002/pro.3787. This article has 110 citations and is from a peer-reviewed journal.

2. (buckel2018flavinbasedelectronbifurcation pages 1-2): Wolfgang Buckel and Rudolf K. Thauer. Flavin-based electron bifurcation, a new mechanism of biological energy coupling. Chemical reviews, 118 7:3862-3886, Mar 2018. URL: https://doi.org/10.1021/acs.chemrev.7b00707, doi:10.1021/acs.chemrev.7b00707. This article has 435 citations and is from a highest quality peer-reviewed journal.

3. (zhong2018genomicanalysesof pages 1-2): Yuhong Zhong and Liang Shi. Genomic analyses of the quinol oxidases and/or quinone reductases involved in bacterial extracellular electron transfer. Frontiers in Microbiology, Dec 2018. URL: https://doi.org/10.3389/fmicb.2018.03029, doi:10.3389/fmicb.2018.03029. This article has 48 citations and is from a peer-reviewed journal.

4. (burton2025electrontransportacross pages 3-4): Joshua A.J. Burton, Marcus J. Edwards, David J. Richardson, and Thomas A. Clarke. Electron transport across bacterial cell envelopes. Jun 2025. URL: https://doi.org/10.1146/annurev-biochem-052621-092202, doi:10.1146/annurev-biochem-052621-092202. This article has 20 citations and is from a domain leading peer-reviewed journal.

5. (borisov2021bacterialoxidasesof pages 1-2): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 149 citations and is from a domain leading peer-reviewed journal.

6. (xie2021themechanismand pages 12-14): Qingqing Xie, Yue Lu, Lin Tang, Guangming Zeng, Zhaohui Yang, Changzheng Fan, Jingjing Wang, and Siavash Atashgahi. The mechanism and application of bidirectional extracellular electron transport in the field of energy and environment. Critical Reviews in Environmental Science and Technology, 51:1924-1969, Jun 2021. URL: https://doi.org/10.1080/10643389.2020.1773728, doi:10.1080/10643389.2020.1773728. This article has 89 citations and is from a domain leading peer-reviewed journal.

7. (portela2024widespreadextracellularelectron pages 1-2): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 89 citations and is from a highest quality peer-reviewed journal.

8. (portela2024widespreadextracellularelectron pages 7-9): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 89 citations and is from a highest quality peer-reviewed journal.

9. (gu2023structureofgeobacter pages 6-8): Yangqi Gu, Matthew J. Guberman-Pfeffer, Vishok Srikanth, Cong Shen, Fabian Giska, Kallol Gupta, Yuri Londer, Fadel A. Samatey, Victor S. Batista, and Nikhil S. Malvankar. Structure of geobacter cytochrome omcz identifies mechanism of nanowire assembly and conductivity. Nature Microbiology, 8:284-298, Feb 2023. URL: https://doi.org/10.1038/s41564-022-01315-5, doi:10.1038/s41564-022-01315-5. This article has 148 citations and is from a highest quality peer-reviewed journal.

10. (gu2023structureofgeobacter pages 1-2): Yangqi Gu, Matthew J. Guberman-Pfeffer, Vishok Srikanth, Cong Shen, Fabian Giska, Kallol Gupta, Yuri Londer, Fadel A. Samatey, Victor S. Batista, and Nikhil S. Malvankar. Structure of geobacter cytochrome omcz identifies mechanism of nanowire assembly and conductivity. Nature Microbiology, 8:284-298, Feb 2023. URL: https://doi.org/10.1038/s41564-022-01315-5, doi:10.1038/s41564-022-01315-5. This article has 148 citations and is from a highest quality peer-reviewed journal.

11. (gu2023structureofgeobacter pages 29-30): Yangqi Gu, Matthew J. Guberman-Pfeffer, Vishok Srikanth, Cong Shen, Fabian Giska, Kallol Gupta, Yuri Londer, Fadel A. Samatey, Victor S. Batista, and Nikhil S. Malvankar. Structure of geobacter cytochrome omcz identifies mechanism of nanowire assembly and conductivity. Nature Microbiology, 8:284-298, Feb 2023. URL: https://doi.org/10.1038/s41564-022-01315-5, doi:10.1038/s41564-022-01315-5. This article has 148 citations and is from a highest quality peer-reviewed journal.

12. (jiang2023thevariedroles pages 1-2): Jie Jiang, Pengchen He, Ying Luo, Zhao-Kuai Peng, Yongguang Jiang, Yidan Hu, Lei Qi, Xiuzhu Dong, Yiran Dong, and Liang Shi. The varied roles of pila-n, omce, omcs, omct, and omcz in extracellular electron transfer by geobacter sulfurreducens. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1251346, doi:10.3389/fmicb.2023.1251346. This article has 41 citations and is from a peer-reviewed journal.

13. (jiang2023thevariedroles pages 5-8): Jie Jiang, Pengchen He, Ying Luo, Zhao-Kuai Peng, Yongguang Jiang, Yidan Hu, Lei Qi, Xiuzhu Dong, Yiran Dong, and Liang Shi. The varied roles of pila-n, omce, omcs, omct, and omcz in extracellular electron transfer by geobacter sulfurreducens. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1251346, doi:10.3389/fmicb.2023.1251346. This article has 41 citations and is from a peer-reviewed journal.

14. (almegbl2024biogasenhancementin pages 1-2): Abdulaziz Mohammed Almegbl, Faris Mohammad A. Munshi, and Anwar Khursheed. Biogas enhancement in the anaerobic digestion of thermo-chemically pretreated sludge by stimulating direct interspecies electron transfer by biochar and graphene. Frontiers in Chemical Engineering, Jun 2024. URL: https://doi.org/10.3389/fceng.2024.1419770, doi:10.3389/fceng.2024.1419770. This article has 8 citations.

15. (ma2024synergisticpromotionof pages 1-2): Hongruo Ma, Long Chen, Wei Guo, Lei Wang, Jian Zhang, and Dongting Zhang. Synergistic promotion of direct interspecies electron transfer by biochar and fe₃o₄ nanoparticles to enhance methanogenesis in anaerobic digestion of vegetable waste. Fermentation, 10:656, Dec 2024. URL: https://doi.org/10.3390/fermentation10120656, doi:10.3390/fermentation10120656. This article has 11 citations.

16. (shaw2025independentlyevolvedextracellular pages 1-2): Dario R Shaw, Krishna P Katuri, Veerraghavulu Sapireddy, Olga Douvropoulou, Jeffrey A Gralnick, and Pascal E Saikaly. Independently evolved extracellular electron transfer pathways in ecologically diverse desulfobacterota. The ISME Journal, Jan 2025. URL: https://doi.org/10.1093/ismejo/wraf097, doi:10.1093/ismejo/wraf097. This article has 18 citations.

17. (wang2024electrocatalyticnanomaterialsimprove pages 1-2): Xiaopin Wang, Xu Li, and Qisu Zhu. Electrocatalytic nanomaterials improve microbial extracellular electron transfer: a review. Applied Sciences, 14:6733, Aug 2024. URL: https://doi.org/10.3390/app14156733, doi:10.3390/app14156733. This article has 12 citations.

18. (shaw2025independentlyevolvedextracellular pages 12-14): Dario R Shaw, Krishna P Katuri, Veerraghavulu Sapireddy, Olga Douvropoulou, Jeffrey A Gralnick, and Pascal E Saikaly. Independently evolved extracellular electron transfer pathways in ecologically diverse desulfobacterota. The ISME Journal, Jan 2025. URL: https://doi.org/10.1093/ismejo/wraf097, doi:10.1093/ismejo/wraf097. This article has 18 citations.

19. (shaw2025independentlyevolvedextracellular pages 14-15): Dario R Shaw, Krishna P Katuri, Veerraghavulu Sapireddy, Olga Douvropoulou, Jeffrey A Gralnick, and Pascal E Saikaly. Independently evolved extracellular electron transfer pathways in ecologically diverse desulfobacterota. The ISME Journal, Jan 2025. URL: https://doi.org/10.1093/ismejo/wraf097, doi:10.1093/ismejo/wraf097. This article has 18 citations.