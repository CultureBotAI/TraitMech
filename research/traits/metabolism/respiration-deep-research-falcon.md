---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:56:35.843251'
end_time: '2026-08-04T07:07:26.010438'
duration_seconds: 650.17
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
  causal_graph_summary: 'respiration_electron_acceptor_energy_conservation: 13 nodes,
    11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 13 nodes, 11 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 13 nodes, 11 edges

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


# Curation-focused research report: microbial respiration

**Target trait:** `METPO:1000800`  
**Label:** respiration  
**Category:** METABOLISM  
**Parent:** `METPO:1000060`  
**Recommended interpretation:** a broad physiological capacity in which oxidation of an electron donor supplies electrons to a membrane-associated electron-transport chain, which terminates at an electron acceptor and ordinarily conserves energy as an electrochemical ion gradient used for ATP synthesis.

## 1. Scope and boundaries

### Core scope

The most defensible trait-level definition is: **electron-donor oxidation → electron transport chain → terminal electron-acceptor reduction → ion-gradient formation → ATP synthesis**. A 2024 Nature Microbiology study explicitly defines heterotrophic respiration as oxidation of an organic donor followed by passage of electrons through an electron-transport chain to a terminal acceptor; electron transfer creates an ion gradient that powers ATP synthase (little2024dietaryandhostderived pages 1-3). The foundational prokaryotic-bioenergetics review states that a membrane-bound chain transduces redox free energy into an electrochemical ion—usually proton—gradient that drives ATP synthesis (simon2008theorganisationof pages 1-3).

The supplied definition therefore captures an important discriminator—**the terminal electron acceptor**—but should not imply that acceptor identity alone is sufficient. The graph should retain electron donor, chain or conduit, energy-coupling membrane, ion gradient, and ATP synthase as core mechanistic entities.

### Included phenotypes

* **Aerobic respiration:** O₂ is reduced to water by a terminal oxidase.
* **Anaerobic respiration:** nitrate, nitrite, fumarate, sulfate/sulfite, DMSO and diverse organic compounds can serve as acceptors, depending on the organism.
* **Extracellular respiration/EET:** insoluble Fe(III) or Mn(IV) minerals and poised electrodes can be terminal extracellular acceptors in electroactive organisms.
* **Facultative respiratory switching:** a single organism may switch acceptors when oxygen availability changes; sulfate reduction and oxygen respiration are not necessarily mutually exclusive (dyksma2023oxygenrespirationand pages 1-2).
* **Ion coupling other than H⁺:** some prokaryotic chains use Na⁺-coupled modules. The graph should therefore use “electrochemical ion gradient” as the broad node and “proton-motive force” as its common specialization.

### Boundary cases

1. **Fermentation is adjacent but not equivalent.** Fermentation generally lacks an exogenous terminal acceptor and complete respiratory electron-transport chain; ATP may be made by substrate-level phosphorylation. Some organisms combine respiratory and fermentative branches, so pathway assignment must be made at the mechanism level rather than from an “anaerobic growth” label alone. In anoxic Methylococcales, recent data support both fermentation-based methanotrophy and denitrification (sina2024persistentactivityof pages 1-2).
2. **Photosynthetic electron transport is not respiration merely because it generates a proton gradient.** Light-driven charge separation belongs under phototrophy unless electrons subsequently enter a separately demonstrated respiratory branch.
3. **Assimilatory reduction and detoxification are not automatically respiration.** Nitrate, sulfate or metal reduction should be curated as respiratory only when linked to electron transport and energy conservation or growth.
4. **Methanogenesis is mechanistically unusual.** Some classifications treat CO₂ reduction by methanogenic archaea as anaerobic respiration, but its cofactors and terminal energy-conservation modules differ from canonical bacterial chains. It should be a taxon-qualified specialization, not part of the minimal generic graph.
5. **Dye reduction is not a definitive respiration assay.** Resazurin or tetrazolium reduction can report reducing metabolism without directly demonstrating O₂ consumption, terminal-acceptor use or oxidative phosphorylation. The retrieved assay review itself was mismatched during document extraction, reinforcing that this proposed assay warning should not be encoded as a positive causal edge without direct source verification.

| module | core causal chain | representative grounded nodes | evidence strength/qualification |
|---|---|---|---|
| Canonical chemiosmosis | electron donor oxidation → membrane electron transport chain → electrochemical ion gradient / proton motive force → ATP synthase-driven ATP production (simon2008theorganisationof pages 1-3, little2024dietaryandhostderived pages 1-3) | GO:0022900 electron transport chain; GO:0015992 proton transport; GO:0006754 ATP biosynthetic process; ATP synthase (label-only); NADH (CHEBI:16908); quinone/quinol pool (label-only) | Strong, broad trait-defining mechanism from foundational review and 2024 respiration definition; applies across many prokaryotes but exact ion/protein architecture varies by taxon (simon2008theorganisationof pages 1-3, little2024dietaryandhostderived pages 1-3) |
| Aerobic terminal oxidation | reduced carriers / cytochrome c or quinol → terminal oxidase → O2 reduction to H2O + proton translocation → pmf contribution (wikstrom2018oxygenactivationand pages 1-2, ford2024theelectrontransport pages 1-2) | oxygen (CHEBI:15379); water (CHEBI:15377); cytochrome c oxidase (label-only); GO:0004129 cytochrome-c oxidase activity | Strong for aerobic respiration; proton-pumping type A oxidases directly supported, but oxidase classes and efficiencies differ among bacteria (wikstrom2018oxygenactivationand pages 1-2) |
| Anaerobic soluble acceptors | organic or inorganic donor oxidation → quinone-linked / membrane-associated reductases → alternative terminal acceptor reduction under low O2 (little2024dietaryandhostderived pages 1-3, little2024dietaryandhostderived pages 3-4, sina2024persistentactivityof pages 1-2) | nitrate (CHEBI:17632); nitrite (CHEBI:16301); fumarate (CHEBI:18012); dimethyl sulfoxide (CHEBI:28262); formate (CHEBI:15740); fumarate reductase/UrdA/periplasmic reductases (label-only) | Strong that alternative acceptors support anaerobic respiration; specific reductase-substrate pairs can be taxon-specific, especially organic acceptors in gut lineages (little2024dietaryandhostderived pages 3-4, little2024dietaryandhostderived pages 1-3) |
| Sulfate respiration | sulfate uptake/activation → APS reduction → sulfite reduction via Dsr system → energy conservation during anaerobic sulfur respiration (diao2023globaldiversityand pages 1-2, dyksma2023oxygenrespirationand pages 1-2) | sulfate (CHEBI:16189); sulfite (CHEBI:18498); sulfide (CHEBI:16134); sat (label-only); aprAB (label-only); qmoABC (label-only); dsrAB/dsrC/dsrMKJOP (label-only) | Strong for sulfate/sulfite-respiring guilds; genomic prediction alone may not resolve reductive vs oxidative direction in some Dsr-containing taxa, so some edges need taxon/context qualification (diao2023globaldiversityand pages 1-2) |
| Extracellular electron transfer | intracellular donor oxidation → quinol pool → CymA/periplasmic carriers → outer-membrane conduit → extracellular acceptor reduction (minerals/electrode) (ford2024theelectrontransport pages 1-2, shaw2025independentlyevolvedextracellular pages 1-2, soares2025toolsforenhancing pages 5-8) | Fe(III) (label-only); Mn(IV) (label-only); electrode/anode (label-only); menaquinone (CHEBI:18009); ubiquinone (CHEBI:16389); MtrCAB (label-only); CymA (label-only); Omc/Pcc pathways (label-only) | Strong for electroactive taxa such as Shewanella/Geobacter relatives; not a universal respiration mechanism. Quantitative support includes measured single-cell/current outputs in BES literature, but transfer architectures are lineage-specific (ford2024theelectrontransport pages 1-2, soares2025toolsforenhancing pages 5-8) |
| Respiratory flexibility / switching | environmental O2 availability shift → transcriptional/metabolic switch between terminal acceptors (e.g., sulfate ↔ oxygen; denitrification/fermentation under anoxia) (dyksma2023oxygenrespirationand pages 1-2, sina2024persistentactivityof pages 1-2) | oxygen (CHEBI:15379); sulfate (CHEBI:16189); nitrate (CHEBI:17632); nitrite (CHEBI:16301); denitrification (GO:0019363) | Moderate-to-strong but context-dependent; directly shown in specific systems, so curate as facultative or taxon-scoped rather than universal for respiration trait (dyksma2023oxygenrespirationand pages 1-2, sina2024persistentactivityof pages 1-2) |
| Assay boundaries / non-defining proxies | resazurin/tetrazolium reduction or generic metabolic dye conversion ↛ direct evidence of O2 respiration or respiration trait state; methane oxidation under anoxia may involve fermentation or denitrification after O2-dependent activation step (braissant2020areviewof pages 1-2, sina2024persistentactivityof pages 1-2) | resazurin (CHEBI:50366); tetrazolium salts (label-only); oxygen consumption assay (label-only) | Strong caution: assay readouts can reflect metabolism without directly measuring respiration, and some pathways mix respiratory and non-respiratory energetics; avoid curating assay proxy as causal trait edge (braissant2020areviewof pages 1-2, sina2024persistentactivityof pages 1-2) |


*Table: This table summarizes major curation modules for microbial respiration (METPO:1000800), including core causal chains, grounded nodes, and evidence qualifications. It is useful for deciding which edges are broadly curatable versus taxon- or assay-limited.*

## 2. Candidate nodes grouped by type

Only identifiers that can be stated with high confidence are supplied. Label-only nodes are preferable to uncertain or invented CURIEs.

### Trait and processes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| respiration | `METPO:1000800` | Root trait node; quote identifier verbatim. |
| electron transport chain | `GO:0022900` | Broad process node. |
| proton transport | `GO:0015992` | Use beneath broader electrochemical-ion-gradient formation. |
| ATP biosynthetic process | `GO:0006754` | Productive energy-conservation output. |
| denitrification | `GO:0019363` | Anaerobic respiratory specialization. |
| extracellular electron transfer | label-only | Avoid treating as universal respiration. |
| dissimilatory sulfate reduction | label-only | Ground to a verified pathway ontology during implementation. |
| oxidative phosphorylation | label-only | Distinguish from substrate-level phosphorylation. |
| respiratory flexibility/acceptor switching | label-only | Environment-dependent phenotype. |

### Chemicals and environmental factors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| oxygen | `CHEBI:15379` | Aerobic terminal acceptor. |
| water | `CHEBI:15377` | Product of oxygen reduction. |
| nitrate | `CHEBI:17632` | Alternative acceptor. |
| nitrite | `CHEBI:16301` | Acceptor/intermediate in nitrogen respiration. |
| fumarate | `CHEBI:18012` | Organic terminal acceptor. |
| sulfate | `CHEBI:16189` | Sulfate-respiration acceptor/substrate. |
| sulfite | `CHEBI:18498` | Activated downstream acceptor in Dsr pathway. |
| sulfide | `CHEBI:16134` | Reduced sulfur product. |
| dimethyl sulfoxide | `CHEBI:28262` | Alternative acceptor. |
| NADH | `CHEBI:16908` | Soluble electron donor/carrier. |
| formate | `CHEBI:15740` | Respiratory electron donor in several systems. |
| menaquinone | `CHEBI:18009` | Membrane electron carrier. |
| ubiquinone | `CHEBI:16389` | Membrane electron carrier. |
| resazurin | `CHEBI:50366` | Assay reagent, not a defining trait node. |
| Fe(III) oxide; Mn(IV) oxide | label-only | Insoluble extracellular acceptors; ground the exact mineral rather than oxidation state alone. |
| anode; cathode; poised electrode | label-only | Experimental electron acceptor/donor. |
| low oxygen/anoxia; oxic–anoxic transition | preferably ENVO/PATO terms after verification | Regulatory context, not intrinsic trait state. |

### Proteins, complexes and genes

| Module | Candidate entities | Notes |
|---|---|---|
| Electron entry | complex I/NDH-1; `nuo` genes; NADH dehydrogenases; formate and lactate dehydrogenases | Complex I oxidizes NADH, reduces quinone and moves four H⁺ per reaction in the canonical enzyme (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). |
| Quinone hub | ubiquinone/ubiquinol pool; menaquinone/menaquinol pool | Connect donor dehydrogenases to terminal branches. |
| Aerobic terminal branch | cytochrome-c oxidase; quinol oxidases; heme–copper oxidases | `GO:0004129` may ground cytochrome-c oxidase activity. Type A CcO evidence is strongest; do not generalize identical proton-pumping stoichiometry to every oxidase (wikstrom2018oxygenactivationand pages 1-2). |
| Fumarate branch | fumarate reductase; FccA; UrdA | Some are soluble or extracytoplasmic and receive electrons from the membrane chain (little2024dietaryandhostderived pages 3-4). |
| Nitrogen branches | Nar, Nap, nitrite reductases, nitric-oxide and nitrous-oxide reductases | Keep individual branches separate; nitrate reduction can lead to denitrification or DNRA. |
| Sulfate branch | sulfate transporter; Sat; AprAB; QmoABC; DsrAB; DsrC; DsrMKJOP | Genomic presence alone may not establish pathway direction (diao2023globaldiversityand pages 1-2, dyksma2023oxygenrespirationand pages 1-2). |
| EET branch | CymA, CctA, FccA, MtrCAB, OmcA/OmcS/OmcZ, Pcc complexes, multiheme c-type cytochromes | Strongly taxon-specific. MtrCAB spans the outer membrane in *Shewanella* (ford2024theelectrontransport pages 1-2). |
| Energy output | F₀F₁ or A/V-type ATP synthase | Keep generic at trait root; enzyme family differs among bacteria and archaea. |

### Cellular locations

* Cytoplasmic/plasma membrane or archaeal membrane: coupling membrane and quinone pool.
* Cytoplasm: soluble donors and central catabolic pathways.
* Periplasm: electron carriers and many extracytoplasmic reductases in diderm bacteria.
* Outer membrane/cell surface: Mtr/Omc/Pcc conduits.
* Extracellular space, mineral surface or electrode–biofilm interface: terminal EET acceptor.

## 3. Candidate causal edges

Predicates below are curation-oriented labels; map them to the predicates already used by TraitMech rather than creating new relation identifiers.

| # | Subject — predicate — object | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | electron-donor oxidation — **supplies electrons to** — electron transport chain | Little et al., 2024, DOI [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2) | “oxidation of an organic electron donor and the passage of resulting electrons through an electron transport chain” | **Strong, generic** for heterotrophic respiration (little2024dietaryandhostderived pages 1-3). |
| 2 | electron transport chain — **transfers electrons to** — terminal electron acceptor | Same | “through an electron transport chain to a terminal electron acceptor” | **Strong, trait-defining** (little2024dietaryandhostderived pages 1-3). |
| 3 | membrane electron transport — **generates** — electrochemical ion gradient | Simon et al., 2008, DOI [10.1016/j.bbabio.2008.09.008](https://doi.org/10.1016/j.bbabio.2008.09.008) | “transduced via the generation of an electrochemical ion (usually proton) gradient” | **Strong, generic**, but individual redox reactions can be electrogenic, electroneutral or pmf-consuming (simon2008theorganisationof pages 1-3). |
| 4 | proton-motive force — **drives** — ATP synthesis | Same | gradient “drives ATP synthesis” | **Strong, generic** (simon2008theorganisationof pages 1-3). |
| 5 | proton pumping / quinone cycling / redox loop — **contributes to formation of** — proton-motive force | Same | “pmf can be built up by… proton pumping, quinone/quinol cycling or by a redox loop” | **Strong**, model these as alternative mechanisms, not a mandatory serial chain (simon2008theorganisationof pages 1-3). |
| 6 | complex I/NDH-1 — **oxidizes** — NADH | Grivennikova et al., published 14 Dec 2024, DOI [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421) | “catalyzes the oxidation of NADH by ubiquinone” | **Strong** for canonical proton-translocating complex I (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). |
| 7 | complex I/NDH-1 — **reduces** — ubiquinone to ubiquinol | Same | Reaction and text identify ubiquinone as oxidant and ubiquinol product | **Strong**; some prokaryotes use menaquinone or alternative complex-I-like substrates, so avoid universal ubiquinone specificity (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). |
| 8 | complex I/NDH-1 — **translocates** — four protons across coupling membrane | Same | “vectorial transmembrane transfer of four H⁺ ions” | **Strong for canonical complex I**; do not attach this stoichiometry to all NADH dehydrogenases (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). |
| 9 | complex-I proton translocation — **contributes to** — proton-motive force | Same | transfer of four protons causes “energy conservation… (proton motive force, pmf)” | **Strong** (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). |
| 10 | cytochrome-c oxidase — **reduces** — O₂ to H₂O | Wikström et al., published 19 Jan 2018, DOI [10.1021/acs.chemrev.7b00664](https://doi.org/10.1021/acs.chemrev.7b00664) | “catalyzes the respiratory reduction of dioxygen (O₂) to water” | **Strong for type A CcO** (wikstrom2018oxygenactivationand pages 1-2). |
| 11 | type A cytochrome-c oxidase — **translocates** — protons across membrane | Same | “couples the O₂ reduction chemistry to translocation of protons across the membrane” | **Strong but oxidase-class-specific**; type B/C efficiencies differ and NO reductases may not pump protons (wikstrom2018oxygenactivationand pages 1-2). |
| 12 | oxidase proton translocation — **contributes to** — electrochemical proton gradient → ATP synthesis | Same | gradient “is used to drive the synthesis of ATP… by the rotary ATP synthase” | **Strong** (wikstrom2018oxygenactivationand pages 1-2). |
| 13 | metabolite dehydrogenases — **reduce** — quinone pool | Ford & TerAvest, published online 20 Dec 2023; issue Jan 2024, DOI [10.1128/aem.01387-23](https://doi.org/10.1128/aem.01387-23) | “electrons are passed into the quinol pool… by dehydrogenases… [oxidizing] lactate, formate, and NADH” | **Strong but *Shewanella*-context evidence**; architecture is broadly plausible but curate with taxon scope (ford2024theelectrontransport pages 1-2). |
| 14 | reduced quinone pool — **donates electrons through** — CymA/periplasmic carriers | Same | “reduced quinones… are oxidized by… CymA,” which deposits electrons onto FccA and CctA | **Strong, *S. oneidensis*-specific** (ford2024theelectrontransport pages 1-2). |
| 15 | MtrCAB pathway — **transfers electrons to** — Fe(III)/Mn(IV) oxides or anode | Same | Mtr enables anaerobic respiration with “Fe(III) oxides, Mn(IV) oxides, and electrodes” | **Strong, taxon-specific EET edge** (ford2024theelectrontransport pages 1-2). |
| 16 | cathode-derived electrons — **flow through reversible Mtr/quinone/NADH-dehydrogenase system to generate** — NADH | Same | “Mtr pathway is reversible”; quinols can drive NAD⁺ reduction by reverse NADH dehydrogenases | **Strong but engineered, assay-specific**; place in an electrosynthesis extension, not the generic respiration root (ford2024theelectrontransport pages 1-2). |
| 17 | trace O₂ reduction by oxidases — **supports via proton translocation** — 2,3-butanediol electrosynthesis | Same | “translocation of protons… during O₂ reduction supports 2,3-BDO generation” | **Taxon- and reactor-specific**. High dissolved O₂ instead caused ROS and cell death, so the effect is non-monotonic (ford2024theelectrontransport pages 1-2). |
| 18 | sulfate availability + anoxia — **selects/activates** — sulfate-reduction pathway | Dyksma & Pester, published 10 Oct 2023, DOI [10.1038/s41467-023-42074-z](https://doi.org/10.1038/s41467-023-42074-z) | culture supplied “sulfate as an electron acceptor”; CO124 contained `sat`, `aprAB/qmoABC` and `dsr` genes | **Strong for MAG CO124 in the tested bioreactor**, not universal regulation (dyksma2023oxygenrespirationand pages 1-2). |
| 19 | shift from anoxic to oxic conditions — **causes switch from** — sulfate reduction to oxygen reduction | Same | “switch from sulfate to oxygen reduction when shifting from anoxic to oxic conditions” | **Strong primary evidence, taxon-specific** (dyksma2023oxygenrespirationand pages 1-2). |
| 20 | DsrAB/DsrC/DsrMKJOP — **supports** — sulfite reduction or sulfide oxidation | Same and Diao et al., 2023, DOI [10.1093/femsre/fuad058](https://doi.org/10.1093/femsre/fuad058) | Dsr pathway is performed by “DsrAB, DsrC, DsrMK and DsrJOP”; genome data alone can make direction difficult to predict | **Uncertain direction unless supported physiologically or by pathway context** (diao2023globaldiversityand pages 1-2, dyksma2023oxygenrespirationand pages 1-2). |
| 21 | Sat + AprAB + QmoABC + reductive Dsr system — **supports** — canonical sulfate reduction | Same | CO124 contained genes for sulfate activation, APS reduction and sulfite reduction | **Moderate-to-strong** when the complete module and appropriate physiology are present (dyksma2023oxygenrespirationand pages 1-2). |
| 22 | respiratory reductase — **reduces** — organic terminal acceptor | Little et al., 2024 | respiratory reductases let microbes use anaerobic molecules as “energy-generating respiratory electron acceptors” | **Strong but substrate-pair-specific** (little2024dietaryandhostderived pages 1-3). |
| 23 | formate oxidation + urocanate reduction — **increases** — respiratory growth and ATP synthesis | Same | “synergistic formate/urocanate-dependent growth enhancement”; “urocanate stimulated ATP synthesis” | **Strong for tested *E. lenta*, *S. wadsworthensis* and *H. filiformis* strains** (little2024dietaryandhostderived pages 3-4). |
| 24 | immune-derived H₂O₂/tetrathionate/nitrate — **fuels** — Enterobacteriaceae respiratory growth in inflamed gut | Same | “electron acceptors generated by immune cells… fuel respiratory growth” | **Strong literature synthesis but host-context-specific**; split by acceptor and organism before curation (little2024dietaryandhostderived pages 1-3). |
| 25 | nitrate/nitrite reduction — **supports** — methane oxidation under anoxia | Schorn et al., published Jun 2024, DOI [10.1038/s41467-024-49602-5](https://doi.org/10.1038/s41467-024-49602-5) | nitrate-/nitrite-linked AOM is described; study suggests denitrification and fermentation-based methanotrophy | **Uncertain/mixed mechanism for the Lake Zug Methylococcales** because O₂ remained necessary for initial methane activation (sina2024persistentactivityof pages 1-2). |

## 4. Recent developments and quantitative findings

### Diverse organic acceptors in the gut

Little et al. experimentally identified **22 dietary- or host-derived metabolites** used as respiratory acceptors across three bacterial families. In a survey of **1,533** gut genomes/MAGs, most encoded fewer than five candidate reductases, whereas a subset encoded over 30 and as many as **103**; related bacteria outside the gut reached more than **200 reductases per genome**. Urocanate reduction increased growth and ATP in representative strains, directly connecting acceptor reduction to energy conservation rather than merely detoxification (little2024dietaryandhostderived pages 3-4, little2024dietaryandhostderived pages 1-3).

### Sulfate-respirer diversity and flexibility

A 2023 FEMS review analyzed **950 primarily metagenome-derived `dsrAB` genomes**. It found uncharacterized sulfate/sulfite-reducing potential in **19 of 23 bacterial phyla** and **2 of 4 archaeal phyla**, while more than **60%** of family-level lineages in its updated database were taxonomically resolved but uncultured. These results make `dsrAB` a useful marker but reject a simple one-gene/one-phenotype rule because pathway direction depends on `dsrAB` type and accompanying genes (diao2023globaldiversityand pages 1-2).

The same review estimates that one-third of the **260 Tmol organic carbon per year** reaching the global seabed is mineralized through sulfate reduction; approximately **90%** of produced sulfide is reoxidized, representing roughly **25% of global sediment oxygen consumption**. In coastal sediments, sulfate reduction can account for **50%** of organic-carbon mineralization (diao2023globaldiversityand pages 1-2).

In a controlled 2023 study, an acidobacterial population switched from sulfate reduction under anoxia to oxygen respiration under oxic conditions. The bioreactor used **1 mM sulfate**, pH **4.5**, alternating one-week oxic periods at **50% air–O₂ saturation**, and operated for more than **200 days**. The focal MAG carried the complete `sat–aprAB/qmoABC–dsr` module and reached approximately **5.5 × 10⁴ cells ml⁻¹**, or **0.1% relative abundance** (dyksma2023oxygenrespirationand pages 1-2).

### Extracellular respiration and reversible electron transport

The 2024 *Shewanella* study showed that the Mtr pathway can operate outward for Fe(III), Mn(IV) or electrode respiration and inward from a cathode. Reverse electron flow reduces quinones and then NAD⁺, but requires ion-coupled NADH dehydrogenases to overcome the redox-energy barrier. Trace O₂ reduction maintained the gradient needed for electrosynthesis, whereas higher O₂ produced ROS and cell death (ford2024theelectrontransport pages 1-2).

Recent EET literature reports direct electron transfer of approximately **15–100 fA per cell**, planktonic-cell transfer of **0.05–2.8 fA per cell**, and an approximately **95% current decline in D₂O** in one proton-coupled flavocytochrome system. FMN binding was reported to accelerate MtrC-associated transfer by **10³–10⁵-fold**. These values are mechanism- and assay-specific and should annotate supporting experiments rather than become generic trait thresholds (soares2025toolsforenhancing pages 4-5, soares2025toolsforenhancing pages 2-4, soares2025toolsforenhancing pages 5-8).

A 2025 Desulfobacterota study—useful as a post-2024 update—reported simultaneous expression of Mtr, Omc and Pcc pathways in *Desulfuromonas acetexigens*, cytochromes with up to **86 heme-binding motifs**, and more than **40 Desulfobacterota species** encoding Omc and Mtr-related pathways. This challenges assumptions that individual EET architectures are confined to their classic model taxa, but does not make them universal (shaw2025independentlyevolvedextracellular pages 1-2).

### Anoxic activity of nominally aerobic methanotrophs

In Lake Zug, anaerobic methane oxidation reached up to **0.2 µM d⁻¹** and was linked by nanoSIMS, metagenomics and metatranscriptomics to Methylococcales. Methane assimilation was similar under hypoxic and anoxic conditions; however, the authors inferred a mixture of fermentation-based methanotrophy and denitrification, with molecular oxygen still needed for initial methane activation by methane monooxygenase (sina2024persistentactivityof pages 1-2). This is a prime warning against curating “anoxic methane oxidation” directly as “anaerobic respiration” without resolving the energy-conserving branch.

## 5. Applications and real-world implementations

* **Wastewater treatment and bioremediation:** EET couples organic-matter oxidation to anodes or mineral reduction and is exploited in microbial electrochemical technologies; current reviews identify wastewater treatment, contaminant remediation and electricity generation as major applications (soares2025toolsforenhancing pages 1-2).
* **Microbial fuel cells:** respiratory electron flow is diverted to an anode, turning donor oxidation into measurable current. Mtr/Omc/Pcc proteins, biofilm conductivity, electron shuttles and electrode materials are engineering targets (soares2025toolsforenhancing pages 5-8, soares2025toolsforenhancing pages 9-11).
* **Microbial electrosynthesis:** inward electron transfer from cathodes supplies reducing power for chemicals. The 2024 *Shewanella* implementation sustained cathode-driven 2,3-butanediol production and eliminated a prior need for phototrophic energy input (ford2024theelectrontransport pages 1-2).
* **Metal and radionuclide transformations:** Fe(III)/Mn(IV) respiration changes mineral solubility and speciation; this can immobilize or mobilize contaminants depending on geochemistry (burton2025electrontransportacross pages 18-19).
* **Sulfur-cycle engineering:** sulfate reducers support hydrocarbon degradation and heavy-metal removal in sulfate-containing groundwater and wastewater, but can also cause steel corrosion and oil souring (diao2023globaldiversityand pages 1-2).
* **Host-associated ecology:** inflammation-generated acceptors can promote Enterobacteriaceae expansion, while organic acceptor respiration links microbial ATP production to transformation of drugs, dietary compounds and host metabolites (little2024dietaryandhostderived pages 31-33, little2024dietaryandhostderived pages 1-3).
* **Methane mitigation:** recognizing respiratory and fermentative activity of methanotrophs in anoxic waters may improve estimates of lacustrine methane sinks (sina2024persistentactivityof pages 1-2).

## 6. Expert synthesis for `respiration.yaml`

The existing 13-node/11-edge graph appears directionally correct but probably too compressed. A robust TraitMech representation should have a **small universal spine** and **optional acceptor-specific branches**:

1. donor oxidation → reduced carrier;
2. reduced carrier → membrane quinone/electron-carrier pool;
3. carrier pool → terminal oxidoreductase or EET conduit;
4. terminal acceptor → reduced product;
5. one or more coupling reactions → electrochemical ion gradient;
6. gradient → ATP synthase → ATP.

Aerobic, nitrate, fumarate, sulfate and extracellular branches should be modular. This avoids asserting that every respiratory organism possesses complex I, cytochrome-c oxidase, quinones, a periplasm, or MtrCAB. In expert terms, **respiration is a systems-level energy-conservation architecture, not a single pathway or marker gene**. The latest studies reinforce that terminal-acceptor repertoires can be far broader and more condition-dependent than standard annotations imply (little2024dietaryandhostderived pages 3-4, diao2023globaldiversityand pages 1-2, dyksma2023oxygenrespirationand pages 1-2).

## 7. Warnings: claims not yet suitable for TraitMech curation

1. **Do not infer respiration from a terminal reductase homolog alone.** Reductase families include non-respiratory enzymes, and substrate specificity can diverge substantially (little2024dietaryandhostderived pages 3-4).
2. **Do not infer sulfate reduction from `dsrAB` alone.** Dsr proteins can function in reductive or oxidative sulfur metabolism; inspect `sat`, `aprAB`, `qmoABC`, `dsrD/dsrL`, gene context, expression and physiology (diao2023globaldiversityand pages 1-2, dyksma2023oxygenrespirationand pages 1-2).
3. **Do not curate Fe(III), Mn(IV), electrodes or MtrCAB as universal respiration nodes.** These belong to taxon-scoped EET modules (ford2024theelectrontransport pages 1-2).
4. **Do not apply the four-H⁺ stoichiometry to every NADH dehydrogenase.** It is supported for canonical proton-translocating complex I, while other dehydrogenases can be non-coupling or Na⁺-coupled (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, ford2024theelectrontransport pages 1-2).
5. **Do not apply type-A CcO proton-pumping behavior to every terminal oxidase.** Oxidase families differ in coupling efficiency (wikstrom2018oxygenactivationand pages 1-2).
6. **Do not equate anaerobic growth with anaerobic respiration.** Fermentation and respiration may coexist, as illustrated by anoxic methanotrophs (sina2024persistentactivityof pages 1-2).
7. **Do not curate resazurin/tetrazolium reduction as direct evidence of respiration without acceptor-consumption or energy-conservation data.** Treat it as an assay observation requiring validation.
8. **Do not encode high O₂ as uniformly beneficial.** In the 2024 cathodic *Shewanella* system, trace O₂ supported gradient formation but high O₂ caused ROS and death (ford2024theelectrontransport pages 1-2).
9. **Do not generalize reactor or host effects across taxa.** Oxic–anoxic switching, inflammation-derived acceptors and organic reductase repertoires are strongly organism- and environment-dependent (little2024dietaryandhostderived pages 31-33, little2024dietaryandhostderived pages 3-4, dyksma2023oxygenrespirationand pages 1-2).

## DOI-first bibliography

1. **Little AS et al.** “Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration.” *Nature Microbiology* 9, 55–69. **Published January 2024**. DOI: [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2) (little2024dietaryandhostderived pages 1-3).
2. **Ford KC, TerAvest MA.** “The electron transport chain of *Shewanella oneidensis* MR-1 can operate bidirectionally to enable microbial electrosynthesis.” *Applied and Environmental Microbiology* 90. **Published online 20 December 2023; January 2024 issue**. DOI: [10.1128/aem.01387-23](https://doi.org/10.1128/aem.01387-23) (ford2024theelectrontransport pages 1-2).
3. **Schorn S et al.** “Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility.” *Nature Communications* 15:5293. **Accepted 7 June 2024**. DOI: [10.1038/s41467-024-49602-5](https://doi.org/10.1038/s41467-024-49602-5) (sina2024persistentactivityof pages 1-2).
4. **Grivennikova VG et al.** “Proton-Translocating NADH–Ubiquinone Oxidoreductase: Interaction with Artificial Electron Acceptors, Inhibitors, and Potential Medicines.” *International Journal of Molecular Sciences* 25:13421. **Published 14 December 2024**. DOI: [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421) (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2).
5. **Diao M et al.** “Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction.” *FEMS Microbiology Reviews* 47. **Advance publication 5 October 2023**. DOI: [10.1093/femsre/fuad058](https://doi.org/10.1093/femsre/fuad058) (diao2023globaldiversityand pages 1-2).
6. **Dyksma S, Pester M.** “Oxygen respiration and polysaccharide degradation by a sulfate-reducing acidobacterium.” *Nature Communications* 14:6337. **Published 10 October 2023**. DOI: [10.1038/s41467-023-42074-z](https://doi.org/10.1038/s41467-023-42074-z) (dyksma2023oxygenrespirationand pages 1-2).
7. **Simon J, van Spanning RJM, Richardson DJ.** “The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems.” *Biochimica et Biophysica Acta* 1777, 1480–1490. **Available online 30 September 2008**. DOI: [10.1016/j.bbabio.2008.09.008](https://doi.org/10.1016/j.bbabio.2008.09.008) (simon2008theorganisationof pages 1-3).
8. **Wikström M, Krab K, Sharma V.** “Oxygen Activation and Energy Conservation by Cytochrome c Oxidase.” *Chemical Reviews* 118, 2469–2490. **Published 19 January 2018**. DOI: [10.1021/acs.chemrev.7b00664](https://doi.org/10.1021/acs.chemrev.7b00664) (wikstrom2018oxygenactivationand pages 1-2).
9. **Shaw DR et al.** “Independently evolved extracellular electron transfer pathways in ecologically diverse Desulfobacterota.” *The ISME Journal* 19. **2025**. DOI: [10.1093/ismejo/wraf097](https://doi.org/10.1093/ismejo/wraf097) (shaw2025independentlyevolvedextracellular pages 1-2).
10. **Soares KA et al.** “Tools for Enhancing Extracellular Electron Transfer in Bioelectrochemical Systems: A Review.” *Fermentation* 11:381. **June 2025**. DOI: [10.3390/fermentation11070381](https://doi.org/10.3390/fermentation11070381) (soares2025toolsforenhancing pages 1-2).

References

1. (little2024dietaryandhostderived pages 1-3): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (simon2008theorganisationof pages 1-3): Jörg Simon, Rob J.M. van Spanning, and David J. Richardson. The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems. Biochimica et biophysica acta, 1777 12:1480-90, Dec 2008. URL: https://doi.org/10.1016/j.bbabio.2008.09.008, doi:10.1016/j.bbabio.2008.09.008. This article has 233 citations.

3. (dyksma2023oxygenrespirationand pages 1-2): Stefan Dyksma and Michael Pester. Oxygen respiration and polysaccharide degradation by a sulfate-reducing acidobacterium. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42074-z, doi:10.1038/s41467-023-42074-z. This article has 68 citations and is from a highest quality peer-reviewed journal.

4. (sina2024persistentactivityof pages 1-2): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 69 citations and is from a highest quality peer-reviewed journal.

5. (wikstrom2018oxygenactivationand pages 1-2): Mårten Wikström, Klaas Krab, and Vivek Sharma. Oxygen activation and energy conservation by cytochrome c oxidase. Chemical Reviews, 118:2469-2490, Jan 2018. URL: https://doi.org/10.1021/acs.chemrev.7b00664, doi:10.1021/acs.chemrev.7b00664. This article has 509 citations and is from a highest quality peer-reviewed journal.

6. (ford2024theelectrontransport pages 1-2): Kathryne C. Ford and Michaela A. TerAvest. The electron transport chain of <i>shewanella oneidensis</i> mr-1 can operate bidirectionally to enable microbial electrosynthesis. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01387-23, doi:10.1128/aem.01387-23. This article has 36 citations and is from a peer-reviewed journal.

7. (little2024dietaryandhostderived pages 3-4): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

8. (diao2023globaldiversityand pages 1-2): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 88 citations and is from a domain leading peer-reviewed journal.

9. (shaw2025independentlyevolvedextracellular pages 1-2): Dario R Shaw, Krishna P Katuri, Veerraghavulu Sapireddy, Olga Douvropoulou, Jeffrey A Gralnick, and Pascal E Saikaly. Independently evolved extracellular electron transfer pathways in ecologically diverse desulfobacterota. The ISME Journal, Jan 2025. URL: https://doi.org/10.1093/ismejo/wraf097, doi:10.1093/ismejo/wraf097. This article has 18 citations.

10. (soares2025toolsforenhancing pages 5-8): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 24 citations.

11. (braissant2020areviewof pages 1-2): Olivier Braissant, Monika Astasov-Frauenhoffer, Tuomas Waltimo, and Gernot Bonkat. A review of methods to determine viability, vitality, and metabolic rates in microbiology. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.547458, doi:10.3389/fmicb.2020.547458. This article has 247 citations and is from a peer-reviewed journal.

12. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 10 citations.

13. (soares2025toolsforenhancing pages 4-5): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 24 citations.

14. (soares2025toolsforenhancing pages 2-4): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 24 citations.

15. (soares2025toolsforenhancing pages 1-2): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 24 citations.

16. (soares2025toolsforenhancing pages 9-11): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 24 citations.

17. (burton2025electrontransportacross pages 18-19): Joshua A.J. Burton, Marcus J. Edwards, David J. Richardson, and Thomas A. Clarke. Electron transport across bacterial cell envelopes. Annual Review of Biochemistry, 94:89-109, Jun 2025. URL: https://doi.org/10.1146/annurev-biochem-052621-092202, doi:10.1146/annurev-biochem-052621-092202. This article has 20 citations and is from a domain leading peer-reviewed journal.

18. (little2024dietaryandhostderived pages 31-33): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.