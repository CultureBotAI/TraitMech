---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:28:35.600147'
end_time: '2026-06-17T20:47:10.006364'
duration_seconds: 1114.41
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: nitrogen-fixing symbiosis
  trait_identifier: traitmech:000044
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: nitrogen_fixing_symbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric\
    \ N2 for a host plant \u2014 classically rhizobia in legume root nodules \u2014\
    \ in exchange for photosynthate."
  parent_traits: traitmech:000041
  synonyms: nitrogen-fixing symbiont, root-nodule symbiosis
  evidence_summary: 'DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont
    transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd,
    "Speak, friend, and enter", supports the symbiotic signalling that establishes
    beneficial nitrogen-fixing plant-microbe associations.)'
  causal_graph_summary: 'rhizobia_legume_n2_fixation: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** nitrogen-fixing symbiosis
- **METPO identifier:** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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
- **Trait label:** nitrogen-fixing symbiosis
- **METPO identifier:** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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


## Microbial Trait Causal Graph Curation Report: nitrogen-fixing symbiosis (traitmech:000044)

### 0) Scope summary (TraitMech-curation view)
**Nitrogen-fixing symbiosis** in TraitMech (traitmech:000044) corresponds to **root-nodule symbiosis (RNS)**: an endosymbiosis where a diazotrophic bacterium is hosted inside a specialized plant organ (a **nodule**) and fixes atmospheric N2 via **nitrogenase** for the plant, while receiving host carbon (often as organic acids/photosynthate) and mineral nutrients. A defining mechanistic feature is that **nitrogen fixation occurs in nodules under microaerobic conditions** supported by plant structures (diffusion barrier) and oxygen-buffering proteins (leghemoglobin). (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7)

**Boundary cases / nearby traits**:
- **Actinorhizal nodulation** (Frankia–plant RNS) and rare non-legume nodulation (e.g., Parasponia) fall within RNS as a *plant phenotype class*, but specific mechanistic modules differ from legume–rhizobium nodulation. (sexauer2024rootnodulesymbiosis pages 24-27, lamoureux2024theeffectof pages 15-19)
- **Free-living diazotrophy** (nitrogenase in soil bacteria without nodules) is distinct because it lacks the host-built nodule organ, symbiosome compartmentation, and the canonical Nod-factor-based signalling program. (udvardi2024geneticsandgenomics pages 5-7, porter2024hostimposedcontrolmechanisms pages 1-3)
- **Associative/endophytic N fixation** in non-nodulating hosts is distinct from RNS (no nodule organogenesis and typically different signalling/compartmentalization).
- **Terminal bacteroid differentiation (TBD)** driven by NCR peptides is **lineage-restricted** (common in IRLC legumes, absent in soybean), so it should be modelled as an optional/conditional subgraph rather than core to all RNS. (zhang2023widelyconservedahl pages 1-2)

### 1) Key concepts and current mechanistic understanding (definitions + canonical pathway)
#### 1.1 Initiation: host–microbe signal exchange
Legumes secrete **flavonoids** that induce rhizobia to produce **Nod factors** (lipochitooligosaccharides). Nod factors are detected by host **LysM receptor-like kinases** (e.g., LjNFR1/LjNFR5 or Medicago orthologs), initiating symbiotic signalling that leads to root hair curling, infection thread formation, and nodule development. (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2, porter2024hostimposedcontrolmechanisms pages 1-3)

#### 1.2 Common symbiosis signalling (SYM pathway) and NIN as a hub
Nod-factor perception triggers hallmark **nuclear/perinuclear Ca2+ oscillations (“calcium spiking”)**, which are decoded by **CCaMK/DMI3**, leading to phosphorylation of **CYCLOPS/IPD3** and transcriptional activation of **NIN (NODULE INCEPTION)**. NIN is repeatedly identified as a master transcription factor controlling infection and organogenesis and coordinating the nitrogen-fixing state. (shen2024nin—attheheart pages 1-2, isidraarellano2024understandingthecrucial pages 1-2)

#### 1.3 Infection and organogenesis
Infection commonly proceeds through root hair curling and formation of a tubular **infection thread**, whose progression depends on cytoskeletal reorganization (including SCAR/WAVE complex components). NIN has cell-type-specific roles: epidermal NIN supports infection thread formation, whereas cytokinin-responsive cortical NIN promotes organogenesis and recruits lateral-root program genes. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30)

#### 1.4 Nodule physiology: oxygen protection + nitrogenase
Nitrogenase is oxygen-labile, so nodules establish a **microaerobic environment** using a **diffusion barrier** and high concentrations of **leghemoglobin**, which facilitates O2 transport to support respiration while keeping free O2 low enough to protect nitrogenase. (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7)

#### 1.5 Exchange economy (defining mutualism)
Hosts deliver carbon/reductant—often **organic acids**—to intracellular rhizobia/bacteroids; in return, bacteroids fix N2. A quantitative anchor is the energetic cost of nitrogenase: **~16 ATP per N2 reduced**. (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7)

### 2) Recent developments (prioritize 2023–2024)
#### 2.1 A mechanistic pathway for nitrate/inorganic-N inhibition via iron allocation (2024)
A major 2024 advance provides a direct mechanistic chain linking external inorganic N to suppression of SNF through **nodule iron homeostasis**: inorganic N induces **GmNIGT1a/b**, which represses **GmNRAMP2a/b** (tonoplast iron transporters), reducing Fe delivery to infected cells and inhibiting SNF. This establishes a clear causal edge from nutrient environment → transcriptional regulation → metal transport → fixation output. (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442)

#### 2.2 Nutrient allocation framing: nodules as high P/Fe sinks (2024)
A 2024 Plant & Cell Physiology mini-review emphasizes that nodules can receive **up to ~20–30% of total plant P and Fe**, and that P is tied to signalling/ATP supply while Fe is needed for leghemoglobin and nitrogenase assembly. This supports explicit environmental/nutrient nodes and edges for trait modelling. (isidraarellano2024understandingthecrucial pages 1-2)

#### 2.3 Host-imposed control and evolutionary/ecological framing (2024)
A 2024 Nature Microbiology synthesis reframes RNS as a controlled interaction where host plants regulate compatibility and resource allocation; it also provides quantitative cellular-scale descriptors (symbiosomes per cell; bacteroids per symbiosome) and re-emphasizes diffusion barrier + leghemoglobin as enabling nitrogenase. (porter2024hostimposedcontrolmechanisms pages 1-3)

#### 2.4 NCR/TBD regulation via conserved host TFs (2023)
A 2023 Nature Plants study shows NCR gene expression can be driven by conserved **AHL transcription factors**, and that NCR169 expressed under its own promoter in soybean roots can induce bacteroid changes consistent with TBD features. This is important for graph modularity: a lineage-restricted “NCR/TBD module” can be mechanistically grounded by AHL→NCR edges and NCR→TBD edges. (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3)

#### 2.5 Evolutionary reconstruction of ancestral RNS programs (2023)
Comparative phylotranscriptomics indicates that responses to bacterial signals, infection, organogenesis, and nitrogen fixation were already present in the most recent common ancestor of RNS-forming species (>90 MYA), while **symbiosome release** programs are associated with lineage-specific, derived small proteins. This supports separating “core ancestral modules” from “derived lineage-specific modules” during curation. (libourel2023comparativephylotranscriptomicsreveals pages 1-2)

### 3) Current applications and real-world implementations
- **Legume inoculants and strain selection**: The fundamental trait supports agricultural inoculation strategies to improve nodule occupancy and N fixation efficiency; this is implicit in the host-control framing and in the importance of compatibility (host responsiveness to molecular signals). (porter2024hostimposedcontrolmechanisms pages 1-3)
- **N management to protect SNF**: The 2024 NRAMP2/NIGT1 mechanism directly informs real-world fertilizer strategies: high inorganic N can inhibit SNF via iron allocation, implying that integrated N–Fe management could mitigate SNF suppression. (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442)
- **Prospects for engineering/synthetic symbioses**: Although not exhaustively evidenced in the retrieved full texts here, recent mechanistic work highlighting receptor specificity and conserved signalling modules underpins efforts to engineer nodulation-like pathways or optimize SNF via targeted genes (e.g., NIN-centred networks; nutrient transport control points). (udvardi2024geneticsandgenomics pages 7-10, shen2024nin—attheheart pages 1-2)

### 4) Expert opinions / authoritative synthesis (what experts emphasize)
- **Oxygen is the central constraint**: Authoritative reviews emphasize that nitrogenase is extremely O2-labile and that nodules maintain very low O2 (nanomolar range in infected cells) via diffusion barriers, respiration, and abundant leghemoglobin—framing oxygen homeostasis as a core causal bottleneck in RNS trait expression. (udvardi2024geneticsandgenomics pages 5-7)
- **Hosts actively control symbionts**: The Nature Microbiology synthesis stresses that hosts provide carbon (organic acids) and that fixation competes with rhizobial resource storage/reproduction, motivating host control mechanisms as a major explanatory lens for symbiosis stability. (porter2024hostimposedcontrolmechanisms pages 1-3)
- **NIN is a “hub” node**: Multiple 2024 syntheses position NIN at the heart of infection, organogenesis, and the nitrogen-fixing cell state, including regulation of leghemoglobin and other fixation-associated genes. (shen2024nin—attheheart pages 9-9, shen2024nin—attheheart pages 1-2)

### 5) Relevant statistics and data points (recent sources)
- **Energetics**: nitrogenase consumes **16 ATP per N2 reduced** (reaction-level benchmark). (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7)
- **Oxygen microenvironment**: infected cells can be at **nanomolar O2** vs ~250 µM equilibrium O2 in water (review synthesis). (udvardi2024geneticsandgenomics pages 5-7)
- **Nodule nutrient sinks**: nodules can receive **up to ~20–30% of total plant P and Fe**. (isidraarellano2024understandingthecrucial pages 1-2)
- **Cellular structure of infected cells**: an infected host cell can contain ~**10^3–10^4 symbiosomes**, and symbiosomes can contain **1–50 bacteroids** (review synthesis). (porter2024hostimposedcontrolmechanisms pages 1-3)

---

## Candidate causal-graph nodes (grouped + grounded where possible)
| Node label | Node type | Suggested grounding (CURIE if known) | Notes |
|---|---|---|---|
| Flavonoids | metabolite/chemical | CHEBI:72544 | Plant root exudate signals that induce rhizobial nod genes and initiate symbiotic signalling; boundary note: specific flavonoids differ by host species. (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| Nod factor (lipochitooligosaccharide) | metabolite/chemical | CHEBI:24431 | Rhizobial signal perceived by host LysM receptors to trigger nodulation signalling, root hair curling, infection thread formation, and nodule development. (sexauer2024totheroots pages 27-30, porter2024hostimposedcontrolmechanisms pages 1-3, shen2024nin—attheheart pages 1-2) |
| LjNFR1 / NFR1 | gene/protein | label-only candidate | LysM receptor-like kinase for Nod-factor perception in Lotus; closely related host-specific orthologs exist (e.g., MtLYK3). (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| LjNFR5 / NFR5 | gene/protein | label-only candidate | LysM receptor-like kinase/co-receptor for Nod-factor perception; interacts with SYMRK in nodulation signalling. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30, shen2024nin—attheheart pages 1-2) |
| SYMRK / DMI2 | gene/protein | label-only candidate | Common symbiosis receptor kinase acting downstream of Nod-factor receptors to transmit the signal inward. (isidraarellano2024understandingthecrucial pages 1-2, sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| DMI1 / POLLUX / CASTOR | gene/protein | label-only candidate | Nuclear-envelope ion-channel components required for symbiotic calcium spiking after Nod-factor perception. (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| CNGC15 | gene/protein | label-only candidate | Cyclic nucleotide-gated channel contributing to nuclear/perinuclear Ca2+ oscillations in the common symbiosis pathway. (isidraarellano2024understandingthecrucial pages 1-2, shen2024nin—attheheart pages 1-2) |
| Calcium spiking | pathway/process | GO:0019722 | Hallmark nuclear/perinuclear Ca2+ oscillations that encode symbiotic signal information downstream of receptor activation. (isidraarellano2024understandingthecrucial pages 1-2, shen2024nin—attheheart pages 1-2) |
| CCaMK / DMI3 | gene/protein | label-only candidate | Ca2+/calmodulin-dependent kinase that decodes calcium spiking and activates downstream transcriptional regulators. (isidraarellano2024understandingthecrucial pages 1-2, sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| CYCLOPS / IPD3 | gene/protein | label-only candidate | Transcriptional regulator phosphorylated by CCaMK; activates NIN and other symbiosis genes. (isidraarellano2024understandingthecrucial pages 1-2, sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) |
| NSP1 | gene/protein | label-only candidate | GRAS-family transcription factor acting downstream of CYCLOPS/CCaMK in nodulation gene regulation. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| NIN (NODULE INCEPTION) | gene/protein | label-only candidate | Master transcription factor controlling infection, nodule organogenesis, oxygen-buffering gene expression, and nodule-number regulation. (shen2024nin—attheheart pages 13-13, shen2024nin—attheheart pages 9-9, shen2024nin—attheheart pages 1-2) |
| NF-Y transcription factors | gene/protein | label-only candidate | NIN target transcription factors implicated in nodule organogenesis and developmental reprogramming. (shen2024nin—attheheart pages 13-13, libourel2023comparativephylotranscriptomicsreveals pages 5-6) |
| Cytokinin | metabolite/chemical | CHEBI:24400 | Plant hormone promoting cortical nodule organogenesis; cytokinin-responsive NIN activity links signalling to nodule formation. (sexauer2024rootnodulesymbiosis pages 27-30, shen2024nin—attheheart pages 9-9) |
| Auxin | metabolite/chemical | CHEBI:30616 | Plant hormone implicated in nodulation and nodule zonation; interacts with cytokinin-linked developmental control. (sexauer2024rootnodulesymbiosis pages 27-30) |
| Infection thread | structure/location | GO:0043584 | Tubular plant-derived structure that guides rhizobia from curled root hairs into cortical tissue. (sexauer2024totheroots pages 27-30, porter2024hostimposedcontrolmechanisms pages 1-3, sexauer2024rootnodulesymbiosis pages 27-30) |
| Actin cytoskeleton | structure/location | GO:0015629 | Required for infection-thread progression and infection-site polarity; remodeled during rhizobial entry. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| SCAR/WAVE complex | gene/protein | GO:0031209 | Cytoskeletal regulatory complex required for normal infection-thread progression. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| NAP1 | gene/protein | label-only candidate | SCAR/WAVE-associated factor needed for proper epidermal/cortical infection-thread progression. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| PIR1 | gene/protein | label-only candidate | SCAR/WAVE-associated factor involved in infection-thread development. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| SCARN | gene/protein | label-only candidate | SCAR/WAVE-related component supporting infection-thread progression. (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) |
| Nodule organogenesis | pathway/process | GO:0009877 | Host developmental program that creates root nodules housing rhizobia; partly co-opted from lateral root development. (libourel2023comparativephylotranscriptomicsreveals pages 1-2, sexauer2024rootnodulesymbiosis pages 182-187, sexauer2024totheroots pages 182-187) |
| Autoregulation of nodulation (AON) | pathway/process | label-only candidate | Long-distance host control pathway that limits nodule number according to nitrogen/carbon status and systemic signalling. (shen2024nin—attheheart pages 13-13, lamoureux2024theeffectof pages 29-32) |
| miR172c/NNC1 module | pathway/process | label-only candidate | Label-only regulatory module reported as part of NIN-linked nodulation control and homeostasis. (shen2024nin—attheheart pages 13-13) |
| Symbiosome | structure/location | GO:0020005 | Plant-derived membrane compartment enclosing bacteroids; site of nutrient exchange and the immediate nitrogen-fixing unit. (zhou2024inorganicnitrogeninhibits pages 1-2, porter2024hostimposedcontrolmechanisms pages 1-3) |
| Bacteroid | structure/location | GO:0075348 | Differentiated intracellular rhizobial state specialized for nitrogen fixation inside nodules. (porter2024hostimposedcontrolmechanisms pages 1-3, zhang2023widelyconservedahl pages 1-2) |
| Nitrogenase complex | gene/protein | EC:1.18.6.1 | Oxygen-labile enzyme complex reducing N2 to NH3; central catalytic machinery of symbiotic nitrogen fixation. (porter2024hostimposedcontrolmechanisms pages 1-3, li2024metalnutritionand pages 5-6, udvardi2024geneticsandgenomics pages 5-7) |
| Leghemoglobin | gene/protein | label-only candidate | Highly abundant nodule oxygen-binding protein buffering free O2 and supporting microaerobic respiration compatible with nitrogenase. (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7, shen2024nin—attheheart pages 9-9) |
| Organic acids | metabolite/chemical | CHEBI:25696 | Main host-supplied carbon/reductant source for intracellular rhizobia to fuel ATP-intensive N2 fixation. (porter2024hostimposedcontrolmechanisms pages 1-3) |
| Diffusion barrier | structure/location | label-only candidate | Nodule anatomical barrier restricting oxygen influx into the infected zone to protect nitrogenase. (porter2024hostimposedcontrolmechanisms pages 1-3, lamoureux2024theeffectof pages 23-26) |
| Microaerobic environment | environmental factor | ENVO:01000823 | Low-oxygen nodule condition required for nitrogenase function and supported by diffusion barriers, respiration, and leghemoglobin. (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7, li2024metalnutritionand pages 5-6) |
| Iron (Fe2+) | metabolite/chemical | CHEBI:29033 | Essential cofactor for nitrogenase, leghemoglobin-related functions, and other symbiotic redox proteins; nodules can receive substantial plant Fe allocation. (isidraarellano2024understandingthecrucial pages 1-2, zhou2024inorganicnitrogeninhibits pages 1-2) |
| Phosphate | metabolite/chemical | CHEBI:43474 | Required for ATP supply and efficient nodulation/SNF; nodules can receive a large fraction of total plant P. (isidraarellano2024understandingthecrucial pages 1-2) |
| GmNRAMP2a / GmNRAMP2b | gene/protein | label-only candidate | Tonoplast Fe transporters in soybean nodules that move Fe toward infected cells and support SNF; repressed by inorganic N via NIGT1. (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442) |
| MtVTL8 | gene/protein | label-only candidate | Symbiosome-associated/vacuolar iron transporter-like protein essential for bacterial survival and SNF in Medicago nodules. (shen2024nin—attheheart pages 1-2) |
| GmNIGT1a / GmNIGT1b | gene/protein | label-only candidate | N-responsive GARP transcription factors that repress GmNRAMP2a/b, linking inorganic N sensing to reduced Fe delivery and lower SNF. (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442) |
| AHL1 / AHL2 | gene/protein | label-only candidate | AT-hook transcription factors required for NCR gene expression and normal nodule/bacteroid development; conserved beyond NCR-producing legumes. (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3) |
| NCR peptides | gene/protein | label-only candidate | Nodule-specific cysteine-rich host peptides that control terminal bacteroid differentiation in IRLC legumes. (zhang2023widelyconservedahl pages 1-2, patil2024identificationandcharacterization pages 14-18) |
| NCR169 | gene/protein | label-only candidate | Specific NCR required for full bacteroid differentiation and effective nitrogen-fixing nodule development in Medicago. (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3) |
| NCR247 | gene/protein | label-only candidate | Cationic NCR peptide that can enter bacteroids, alter gene expression, and induce terminal differentiation-related phenotypes. (patil2024identificationandcharacterization pages 18-22, patil2024identificationandcharacterization pages 35-41) |
| BacA | gene/protein | label-only candidate | Rhizobial peptide transporter/protective factor required for NCR-mediated bacteroid differentiation in compatible symbioses. (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3) |
| cbb3-type cytochrome oxidase | gene/protein | label-only candidate | High-affinity respiratory oxidase enabling bacteroid respiration under microaerobic nodule conditions. (li2024metalnutritionand pages 5-6) |
| Inorganic nitrogen / nitrate | environmental factor | CHEBI:17632 | External N source that suppresses nodulation/SNF; recent evidence links inhibition to host control of Fe allocation in nodules. (zhou2024inorganicnitrogeninhibits pages 1-2, udvardi2024geneticsandgenomics pages 5-7) |


*Table: This table lists candidate nodes for a TraitMech causal graph of nitrogen-fixing symbiosis, grouped by functional type and grounded where possible to standard ontologies. It is useful for curating mechanistic entities that link host signalling, infection, nodule function, oxygen control, nutrient exchange, and host regulation.*

## Evidence-backed candidate causal edges (triples + snippets + notes)
| Subject | Predicate | Object | Evidence snippet (quote or close paraphrase in quotes) | Source (DOI, year, URL) | Notes/uncertainty/grounding hints |
|---|---|---|---|---|---|
| Flavonoids | induce production of | Nod factor (lipochitooligosaccharide) | “Legumes secrete flavonoids that induce rhizobia to produce Nod factors” (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Host-root exudate signal; chemical node can be grounded as flavonoids/CHEBI and Nod factor as LCO. |
| Nod factor | activates | NFR1/NFR5 receptor system | “Nod factors… are perceived by NOD FACTOR RECEPTORs (e.g., Lotus NFR1/NFR5)” (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Taxon-specific receptor names vary: LjNFR1/LjNFR5, MtLYK3/MtNFP. |
| NFR5 | interacts_with | SYMRK/DMI2 | “NFR5 interacts with SYMRK” (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Specific to Lotus/Medicago ortholog systems; label-only grounding likely needed. |
| Nod factor perception | induces | nuclear/perinuclear calcium spiking | “Nod/Myc perception triggers nuclear calcium oscillations (‘spiking’)” (sexauer2024totheroots pages 27-30); “calcium spiking… is a central symbiotic signal” (isidraarellano2024understandingthecrucial pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Process node could map to calcium ion oscillation/signaling GO terms. |
| Calcium spiking | activates | CCaMK/DMI3 | “Calcium spiking activates CCaMK/DMI3” (sexauer2024totheroots pages 27-30, shen2024nin—attheheart pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Strongly supported across legumes. |
| CCaMK/DMI3 | phosphorylates | CYCLOPS/IPD3 | “CCaMK/DMI3 decodes calcium signals and phosphorylates CYCLOPS/IPD3” (isidraarellano2024understandingthecrucial pages 1-2, shen2024nin—attheheart pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Molecular-function edge; good curatable mechanism. |
| CYCLOPS/IPD3 | activates transcription of | NIN | “CCaMK… phosphorylates CYCLOPS/IPD3, which activates NIN by binding… the NIN promoter” (shen2024nin—attheheart pages 1-2) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Use “positively regulates expression of” if preferred ontology-wise. |
| NIN | promotes | infection thread formation | “NIN is essential for IT formation” (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Strong plant-host developmental control edge. |
| Cortical NIN (cytokinin-responsive) | induces | nodule organogenesis | “cortical NIN (cytokinin-responsive) induces nodule formation” (sexauer2024totheroots pages 27-30, sexauer2024rootnodulesymbiosis pages 27-30); “NIN… promotes… nodule organogenesis” (isidraarellano2024understandingthecrucial pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Cell-type-specific claim; retain note that epidermal and cortical NIN roles differ. |
| NIN | directly promotes expression of | leghemoglobin genes | “NIN (and NLP2) directly promote the expression of the leghemoglobins” (shen2024nin—attheheart pages 9-9) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Directness is explicitly stated in source summary; host-gene regulatory edge. |
| Leghemoglobin | buffers | oxygen concentration in nodules | “leghemoglobins… buffer the oxygen concentration within the nodules” (shen2024nin—attheheart pages 9-9) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Supports oxygen-homeostasis node in nodule infected zone. |
| Diffusion barrier | limits | oxygen flux into nodule interior | “a diffusion barrier of tightly packed cells… is thought to limit oxygen flux” (porter2024hostimposedcontrolmechanisms pages 1-3); “multilayered cortex… functions as an adaptable oxygen diffusion barrier” (lamoureux2024theeffectof pages 23-26) | 10.1038/s41564-024-01762-2, 2024, https://doi.org/10.1038/s41564-024-01762-2 | Structural/anatomical edge; some wording is review-level synthesis. |
| Microaerobic environment | enables | nitrogenase activity | “Symbiotic nitrogen fixation requires a low-oxygen environment for proper activity of nitrogenase” (shen2024nin—attheheart pages 9-9); nodules provide “microaerobic… requirements of the bacterial nitrogenase” (porter2024hostimposedcontrolmechanisms pages 1-3) | 10.3389/fpls.2023.1284720, 2024, https://doi.org/10.3389/fpls.2023.1284720 | Can represent as environmental condition positively regulating enzyme activity. |
| Plant host | supplies | organic acids to bacteroids | “the plant transfers reductant, typically in the form of organic acids, from plant cells to intracellular rhizobia” (porter2024hostimposedcontrolmechanisms pages 1-3) | 10.1038/s41564-024-01762-2, 2024, https://doi.org/10.1038/s41564-024-01762-2 | Exchange edge central to mutualism definition. |
| Nitrogenase complex | reduces | N2 to NH3 | “nitrogenase reaction indicates consumption of 16 ATP in the reduction of N2 to NH3” (udvardi2024geneticsandgenomics pages 5-7); “requiring 16 ATP per N2 molecule” (porter2024hostimposedcontrolmechanisms pages 1-3) | 10.1017/S1062798724000309, 2024, https://doi.org/10.1017/S1062798724000309 | Could split into two edges: reduces N2→NH3 and requires→16 ATP. |
| Nitrogenase complex | requires | 16 ATP per N2 reduced | “N2 fixation… requiring 16 ATP per N2 molecule” (porter2024hostimposedcontrolmechanisms pages 1-3, udvardi2024geneticsandgenomics pages 5-7) | 10.1038/s41564-024-01762-2, 2024, https://doi.org/10.1038/s41564-024-01762-2 | Quantitative mechanistic edge. |
| Iron availability | is required for | nitrogenase assembly and leghemoglobin function | “Fe is essential as a cofactor for leghemoglobin and for assembling the nitrogenase complex” (isidraarellano2024understandingthecrucial pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Strong nutrient-dependence edge; Fe2+/iron homeostasis may be separate nodes. |
| Phosphate availability | is required for | Nod-factor decoding and ATP supply for fixation | “P contributes to NF decoding and ATP supply for fixation” and “deficiencies in P… reduce nodule formation and nitrogen fixation” (isidraarellano2024understandingthecrucial pages 1-2) | 10.1093/pcp/pcae128, 2024, https://doi.org/10.1093/pcp/pcae128 | Best represented as positive regulation of signaling and energy metabolism. |
| Inorganic nitrogen | induces | GmNIGT1a/b | “high inorganic N levels induce the transcriptional repressors GmNIGT1a and 1b” (zhou2024inorganicnitrogeninhibits media 947c5442) | 10.1038/s41467-024-53325-y, 2024, https://doi.org/10.1038/s41467-024-53325-y | Soybean-specific host mechanism; mark taxon-specific if curating broadly. |
| GmNIGT1a/b | represses expression of | GmNRAMP2a/b | “These repressors then down-regulate the expression of the iron (Fe) transporters GmNRAMP2a and 2b” (zhou2024inorganicnitrogeninhibits media 947c5442, zhou2024inorganicnitrogeninhibits pages 1-2) | 10.1038/s41467-024-53325-y, 2024, https://doi.org/10.1038/s41467-024-53325-y | Strong mechanistic edge from 2024 primary study. |
| GmNRAMP2a/b | promotes | Fe delivery to infected nodule cells | “GmNRAMP2a&2b… are required for Fe transfer to infected cells and proper SNF” (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442) | 10.1038/s41467-024-53325-y, 2024, https://doi.org/10.1038/s41467-024-53325-y | Tonoplast-localized transporter in uninfected tissues; soybean-specific. |
| Reduced Fe delivery to infected cells | inhibits | symbiotic nitrogen fixation | “disruption of Fe homeostasis… leads to the inhibition of symbiotic nitrogen fixation” (zhou2024inorganicnitrogeninhibits media 947c5442, zhou2024inorganicnitrogeninhibits pages 1-2) | 10.1038/s41467-024-53325-y, 2024, https://doi.org/10.1038/s41467-024-53325-y | This can be chained from NIGT1/NRAMP2 to trait-level inhibition. |
| AHL transcription factors | induce | NCR gene expression | “AHL transcription factors… bound to AT-rich sequences in the NCR169 promoter inducing its expression” (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3) | 10.1038/s41477-022-01326-4, 2023, https://doi.org/10.1038/s41477-022-01326-4 | Good host-regulatory edge for IRLC legumes; not universal across all RNS. |
| NCR peptides | cause | terminal bacteroid differentiation | “NCR peptides drive terminal bacteroid differentiation” with “loss of bacterial cell division capacity, genome amplification, enlarged cell size” (zhang2023widelyconservedahl pages 1-2, patil2024identificationandcharacterization pages 14-18, patil2024identificationandcharacterization pages 18-22) | 10.1038/s41477-022-01326-4, 2023, https://doi.org/10.1038/s41477-022-01326-4 | Important but lineage-restricted to NCR-producing legumes; mark non-universal. |
| BacA | is required for | NCR-mediated bacteroid differentiation | “NCR-induced differentiation requires rhizobial peptide transporters (bacA/bclA dependence is discussed)” (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3) | 10.1038/s41477-022-01326-4, 2023, https://doi.org/10.1038/s41477-022-01326-4 | Bacterial-side determinant; could be “protects against/imports NCR peptides” depending curation granularity. |
| Ancestral root nodule symbiosis program | includes | signal response, infection, organogenesis, and nitrogen fixation modules | “response to bacterial signals, nodule infection, nodule organogenesis and nitrogen fixation… were ancestral” and present “more than 90 million years ago” (libourel2023comparativephylotranscriptomicsreveals pages 1-2, libourel2023comparativephylotranscriptomicsreveals pages 5-6) | 10.1038/s41477-023-01441-w, 2023, https://doi.org/10.1038/s41477-023-01441-w | Evolutionary edge; trait-level rather than within-organism mechanism. |
| Symbiosome release program | is associated with | lineage-specific small proteins | “symbiosome release… was associated with recently evolved genes encoding small proteins in each lineage” (libourel2023comparativephylotranscriptomicsreveals pages 1-2) | 10.1038/s41477-023-01441-w, 2023, https://doi.org/10.1038/s41477-023-01441-w | Derived/evolutionary claim; useful for boundary-setting, but not universal core edge. |


*Table: This table lists evidence-backed subject–predicate–object triples for a TraitMech causal graph of nitrogen-fixing symbiosis. It emphasizes mechanistic edges from signaling through oxygen control, nutrient exchange, nitrate inhibition, host control, and evolutionary context, with source details and curation notes.*

---

## Visual evidence (recent primary study)
Zhou et al. (Nature Communications, 2024) provide a mechanistic model figure linking **inorganic nitrogen** to **Fe allocation** and **SNF inhibition** through the **GmNIGT1–GmNRAMP2 module** (zhou2024inorganicnitrogeninhibits media 947c5442).

---

## DOI-first bibliography (with URLs and publication dates when available)
1. **Zhou M. et al.** *Inorganic nitrogen inhibits symbiotic nitrogen fixation through blocking NRAMP2-mediated iron delivery in soybean nodules.* **Nature Communications** (Oct 2024). DOI: **10.1038/s41467-024-53325-y**. URL: https://doi.org/10.1038/s41467-024-53325-y (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442)
2. **Porter S.S. et al.** *Host-imposed control mechanisms in legume-rhizobia symbiosis.* **Nature Microbiology** (Aug 2024). DOI: **10.1038/s41564-024-01762-2**. URL: https://doi.org/10.1038/s41564-024-01762-2 (porter2024hostimposedcontrolmechanisms pages 1-3)
3. **Isidra-Arellano M.C., Valdés-López O.** *Understanding the Crucial Role of Phosphate and Iron Availability in Regulating Root Nodule Symbiosis.* **Plant and Cell Physiology** (Oct 2024). DOI: **10.1093/pcp/pcae128**. URL: https://doi.org/10.1093/pcp/pcae128 (isidraarellano2024understandingthecrucial pages 1-2)
4. **Shen L., Feng J.** *NIN—at the heart of NItrogen-fixing Nodule symbiosis.* **Frontiers in Plant Science** (Jan 2024; article DOI indicates 2023). DOI: **10.3389/fpls.2023.1284720**. URL: https://doi.org/10.3389/fpls.2023.1284720 (shen2024nin—attheheart pages 1-2, shen2024nin—attheheart pages 9-9)
5. **Udvardi M., Mens C., Grundy E.** *Genetics and Genomics of Symbiotic Nitrogen Fixation in Legumes: Past, Present and Future.* **European Review** (Aug 2024). DOI: **10.1017/S1062798724000309**. URL: https://doi.org/10.1017/S1062798724000309 (udvardi2024geneticsandgenomics pages 5-7, udvardi2024geneticsandgenomics pages 7-10)
6. **Li Y. et al.** *Metal nutrition and transport in the process of symbiotic nitrogen fixation.* **Plant Communications** (Apr 2024). DOI: **10.1016/j.xplc.2024.100829**. URL: https://doi.org/10.1016/j.xplc.2024.100829 (li2024metalnutritionand pages 5-6)
7. **Zhang S. et al.** *Widely conserved AHL transcription factors are essential for NCR gene expression and nodule development in Medicago.* **Nature Plants** (Jan 2023). DOI: **10.1038/s41477-022-01326-4**. URL: https://doi.org/10.1038/s41477-022-01326-4 (zhang2023widelyconservedahl pages 1-2, zhang2023widelyconservedahl pages 2-3)
8. **Libourel C. et al.** *Comparative phylotranscriptomics reveals ancestral and derived root nodule symbiosis programmes.* **Nature Plants** (Jun 2023). DOI: **10.1038/s41477-023-01441-w**. URL: https://doi.org/10.1038/s41477-023-01441-w (libourel2023comparativephylotranscriptomicsreveals pages 1-2, libourel2023comparativephylotranscriptomicsreveals pages 5-6)

---

## Warnings / claims to treat as uncertain before curation
1. **Unknown-journal/grey literature texts** (e.g., “Sexauer 2024…”, “Lamoureux 2024…”, some theses/preprints) contain useful mechanistic descriptions but have uncertain publication status in the retrieved metadata; curate core edges preferentially from peer-reviewed sources when possible, using these as secondary support or for hypothesis generation. (sexauer2024totheroots pages 27-30, lamoureux2024theeffectof pages 19-23)
2. **Soybean-specific inorganic N→Fe mechanism** (NIGT1/NRAMP2) is strong but taxon-specific; represent as conditional (NCBITaxon:Glycine max) unless supported across legumes. (zhou2024inorganicnitrogeninhibits pages 1-2, zhou2024inorganicnitrogeninhibits media 947c5442)
3. **NCR/TBD module** is lineage-restricted (IRLC legumes) and should not be treated as universal RNS machinery. (zhang2023widelyconservedahl pages 1-2, patil2024identificationandcharacterization pages 14-18)
4. **Evolutionary edges** (ancestral vs derived modules) are valuable for scoping but may not map cleanly into within-organism causal graphs; consider storing these as metadata/notes rather than core mechanistic edges. (libourel2023comparativephylotranscriptomicsreveals pages 1-2)


References

1. (porter2024hostimposedcontrolmechanisms pages 1-3): Stephanie S. Porter, Simon E. Dupin, R. Ford Denison, E. Toby Kiers, and Joel L. Sachs. Host-imposed control mechanisms in legume-rhizobia symbiosis. Nature microbiology, 9:1929-1939, Aug 2024. URL: https://doi.org/10.1038/s41564-024-01762-2, doi:10.1038/s41564-024-01762-2. This article has 57 citations and is from a highest quality peer-reviewed journal.

2. (udvardi2024geneticsandgenomics pages 5-7): Michael Udvardi, Celine Mens, and Estelle Grundy. Genetics and genomics of symbiotic nitrogen fixation in legumes: past, present and future. European Review, 32:383-397, Aug 2024. URL: https://doi.org/10.1017/s1062798724000309, doi:10.1017/s1062798724000309. This article has 1 citations and is from a peer-reviewed journal.

3. (sexauer2024rootnodulesymbiosis pages 24-27): M Sexauer. Root nodule symbiosis adapted genes from am and lateral root. Unknown journal, 2024.

4. (lamoureux2024theeffectof pages 15-19): KE Lamoureux. The effect of copper-induced oxidative stress on symbiosis between model legume lotus japonicus and mesorhizobium loti. Unknown journal, 2024.

5. (zhang2023widelyconservedahl pages 1-2): Senlei Zhang, Ting Wang, Rui M. Lima, Aladár Pettkó-Szandtner, Attila Kereszt, J. Allan Downie, and Eva Kondorosi. Widely conserved ahl transcription factors are essential for ncr gene expression and nodule development in medicago. Nature Plants, 9:280-288, Jan 2023. URL: https://doi.org/10.1038/s41477-022-01326-4, doi:10.1038/s41477-022-01326-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

6. (sexauer2024totheroots pages 27-30): M Sexauer. To the roots of nodules: nodule organogenesis utilizes lateral root development processes. Unknown journal, 2024.

7. (shen2024nin—attheheart pages 1-2): Lisha Shen and Jian Feng. Nin—at the heart of nitrogen-fixing nodule symbiosis. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1284720, doi:10.3389/fpls.2023.1284720. This article has 39 citations.

8. (isidraarellano2024understandingthecrucial pages 1-2): Mariel C. Isidra-Arellano and Oswaldo Valdés-López. Understanding the crucial role of phosphate and iron availability in regulating root nodule symbiosis. Plant and Cell Physiology, 65:1925-1936, Oct 2024. URL: https://doi.org/10.1093/pcp/pcae128, doi:10.1093/pcp/pcae128. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (sexauer2024rootnodulesymbiosis pages 27-30): M Sexauer. Root nodule symbiosis adapted genes from am and lateral root. Unknown journal, 2024.

10. (zhou2024inorganicnitrogeninhibits pages 1-2): Min Zhou, Yuan Li, Xiao-Lei Yao, Jing Zhang, Sheng Liu, Hong-Rui Cao, Shuang Bai, Chun-Qu Chen, Dan-Xun Zhang, Ao Xu, Jia-Ning Lei, Qian-Zhuo Mao, Yu Zhou, De-Qiang Duanmu, Yue-Feng Guan, and Zhi-Chang Chen. Inorganic nitrogen inhibits symbiotic nitrogen fixation through blocking nramp2-mediated iron delivery in soybean nodules. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53325-y, doi:10.1038/s41467-024-53325-y. This article has 45 citations and is from a highest quality peer-reviewed journal.

11. (zhou2024inorganicnitrogeninhibits media 947c5442): Min Zhou, Yuan Li, Xiao-Lei Yao, Jing Zhang, Sheng Liu, Hong-Rui Cao, Shuang Bai, Chun-Qu Chen, Dan-Xun Zhang, Ao Xu, Jia-Ning Lei, Qian-Zhuo Mao, Yu Zhou, De-Qiang Duanmu, Yue-Feng Guan, and Zhi-Chang Chen. Inorganic nitrogen inhibits symbiotic nitrogen fixation through blocking nramp2-mediated iron delivery in soybean nodules. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53325-y, doi:10.1038/s41467-024-53325-y. This article has 45 citations and is from a highest quality peer-reviewed journal.

12. (zhang2023widelyconservedahl pages 2-3): Senlei Zhang, Ting Wang, Rui M. Lima, Aladár Pettkó-Szandtner, Attila Kereszt, J. Allan Downie, and Eva Kondorosi. Widely conserved ahl transcription factors are essential for ncr gene expression and nodule development in medicago. Nature Plants, 9:280-288, Jan 2023. URL: https://doi.org/10.1038/s41477-022-01326-4, doi:10.1038/s41477-022-01326-4. This article has 32 citations and is from a highest quality peer-reviewed journal.

13. (libourel2023comparativephylotranscriptomicsreveals pages 1-2): Cyril Libourel, Jean Keller, Lukas Brichet, Anne-Claire Cazalé, Sébastien Carrère, Tatiana Vernié, Jean-Malo Couzigou, Caroline Callot, Isabelle Dufau, Stéphane Cauet, William Marande, Tabatha Bulach, Amandine Suin, Catherine Masson-Boivin, Philippe Remigi, Pierre-Marc Delaux, and Delphine Capela. Comparative phylotranscriptomics reveals ancestral and derived root nodule symbiosis programmes. Nature Plants, 9:1067-1080, Jun 2023. URL: https://doi.org/10.1038/s41477-023-01441-w, doi:10.1038/s41477-023-01441-w. This article has 66 citations and is from a highest quality peer-reviewed journal.

14. (udvardi2024geneticsandgenomics pages 7-10): Michael Udvardi, Celine Mens, and Estelle Grundy. Genetics and genomics of symbiotic nitrogen fixation in legumes: past, present and future. European Review, 32:383-397, Aug 2024. URL: https://doi.org/10.1017/s1062798724000309, doi:10.1017/s1062798724000309. This article has 1 citations and is from a peer-reviewed journal.

15. (shen2024nin—attheheart pages 9-9): Lisha Shen and Jian Feng. Nin—at the heart of nitrogen-fixing nodule symbiosis. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1284720, doi:10.3389/fpls.2023.1284720. This article has 39 citations.

16. (shen2024nin—attheheart pages 13-13): Lisha Shen and Jian Feng. Nin—at the heart of nitrogen-fixing nodule symbiosis. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1284720, doi:10.3389/fpls.2023.1284720. This article has 39 citations.

17. (libourel2023comparativephylotranscriptomicsreveals pages 5-6): Cyril Libourel, Jean Keller, Lukas Brichet, Anne-Claire Cazalé, Sébastien Carrère, Tatiana Vernié, Jean-Malo Couzigou, Caroline Callot, Isabelle Dufau, Stéphane Cauet, William Marande, Tabatha Bulach, Amandine Suin, Catherine Masson-Boivin, Philippe Remigi, Pierre-Marc Delaux, and Delphine Capela. Comparative phylotranscriptomics reveals ancestral and derived root nodule symbiosis programmes. Nature Plants, 9:1067-1080, Jun 2023. URL: https://doi.org/10.1038/s41477-023-01441-w, doi:10.1038/s41477-023-01441-w. This article has 66 citations and is from a highest quality peer-reviewed journal.

18. (sexauer2024rootnodulesymbiosis pages 182-187): M Sexauer. Root nodule symbiosis adapted genes from am and lateral root. Unknown journal, 2024.

19. (sexauer2024totheroots pages 182-187): M Sexauer. To the roots of nodules: nodule organogenesis utilizes lateral root development processes. Unknown journal, 2024.

20. (lamoureux2024theeffectof pages 29-32): KE Lamoureux. The effect of copper-induced oxidative stress on symbiosis between model legume lotus japonicus and mesorhizobium loti. Unknown journal, 2024.

21. (li2024metalnutritionand pages 5-6): Yuan Li, Qian Liu, Dan-Xun Zhang, Zhuo-Yan Zhang, Ao Xu, Yuan-Long Jiang, and Zhi-Chang Chen. Metal nutrition and transport in the process of symbiotic nitrogen fixation. Apr 2024. URL: https://doi.org/10.1016/j.xplc.2024.100829, doi:10.1016/j.xplc.2024.100829. This article has 48 citations and is from a peer-reviewed journal.

22. (lamoureux2024theeffectof pages 23-26): KE Lamoureux. The effect of copper-induced oxidative stress on symbiosis between model legume lotus japonicus and mesorhizobium loti. Unknown journal, 2024.

23. (patil2024identificationandcharacterization pages 14-18): S Patil. Identification and characterization of genes responsible for the resistance of gram-negative bacteria towards nodule-specific cysteine rich peptides. Unknown journal, 2024.

24. (patil2024identificationandcharacterization pages 18-22): S Patil. Identification and characterization of genes responsible for the resistance of gram-negative bacteria towards nodule-specific cysteine rich peptides. Unknown journal, 2024.

25. (patil2024identificationandcharacterization pages 35-41): S Patil. Identification and characterization of genes responsible for the resistance of gram-negative bacteria towards nodule-specific cysteine rich peptides. Unknown journal, 2024.

26. (lamoureux2024theeffectof pages 19-23): KE Lamoureux. The effect of copper-induced oxidative stress on symbiosis between model legume lotus japonicus and mesorhizobium loti. Unknown journal, 2024.